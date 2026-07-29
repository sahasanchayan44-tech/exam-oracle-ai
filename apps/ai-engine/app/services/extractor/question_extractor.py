import re
from typing import List
from app.services.extractor.schema import ExtractedQuestion
import structlog

logger = structlog.get_logger(__name__)

class QuestionExtractorService:
    """Robust regex & layout parsing to segment raw paper text into question items preserving equations, tables, images & options"""

    # Regex Patterns
    Q_HEADER_PATTERN = re.compile(
        r'(?:Q(?:uestion)?\.?\s*(\d+)|\b(\d+)\.\s+|\[Q(\d+)\])', re.IGNORECASE
    )
    OPTION_PATTERN = re.compile(
        r'(?:(?:\(([A-Da-d])\)|([A-Da-d])\.\s+)\s*([^(\n]+))'
    )
    LATEX_PATTERN = re.compile(
        r'(\$\$[\s\S]*?\$\$|\$[^$\n]+\$|\\begin\{equation\}[\s\S]*?\\end\{equation\}|\\\[[\s\S]*?\\\])'
    )
    IMAGE_REF_PATTERN = re.compile(
        r'(!\[.*?\]\(.*?\)|\[IMAGE_REF:\s*([^\]]+)\]|<img[^>]+src=["\']([^"\']+)["\'][^>]*>)', re.IGNORECASE
    )
    TABLE_PATTERN = re.compile(
        r'(\|(?:[^\n]+\|\r?\n)+)'
    )
    NUMERICAL_UNIT_PATTERN = re.compile(
        r'\b(\d+(?:\.\d+)?)\s*(m/s\^2|m/s|kg|N|J|Pa|Hz|V|A|Ω|W|mol|K|m|cm|mm|g)\b', re.IGNORECASE
    )
    MARKS_PATTERN = re.compile(
        r'\[(\d+)\s*(?:marks?|pts?)\]|\((\d+)\s*(?:marks?|pts?)\)', re.IGNORECASE
    )

    async def extract_questions(self, raw_text: str) -> List[ExtractedQuestion]:
        extracted: List[ExtractedQuestion] = []
        lines = raw_text.split('\n')

        current_q_num = 1
        current_text_buf = []
        current_marks = 5

        for line in lines:
            line_str = line.strip()
            match = self.Q_HEADER_PATTERN.match(line_str)

            if match and len(current_text_buf) > 0:
                # Flush previous question
                full_content = "\n".join(current_text_buf)
                if full_content.strip():
                    extracted.append(self._parse_single_question(current_q_num, full_content, current_marks))
                    current_q_num += 1
                current_text_buf = [line_str]
            else:
                if line_str:
                    current_text_buf.append(line_str)

        if current_text_buf:
            full_content = "\n".join(current_text_buf)
            if full_content.strip():
                extracted.append(self._parse_single_question(current_q_num, full_content, current_marks))

        # Fallback if no explicit headers found
        if not extracted and raw_text.strip():
            extracted.append(self._parse_single_question(1, raw_text, 10))

        logger.info("question_extraction_completed", extracted_count=len(extracted))
        return extracted

    def _parse_single_question(self, q_num: int, content: str, default_marks: int) -> ExtractedQuestion:
        # Extract Marks
        marks_match = self.MARKS_PATTERN.search(content)
        marks = default_marks
        if marks_match:
            marks = int(marks_match.group(1) or marks_match.group(2))

        # Extract Options (MCQ)
        options = []
        for opt_match in self.OPTION_PATTERN.finditer(content):
            label = opt_match.group(1) or opt_match.group(2)
            opt_text = opt_match.group(3).strip()
            if label and opt_text:
                options.append({"label": label.upper(), "text": opt_text})

        # Extract Equations
        equations = self.LATEX_PATTERN.findall(content)

        # Extract Image Refs
        images = []
        for img_match in self.IMAGE_REF_PATTERN.finditer(content):
            ref = img_match.group(2) or img_match.group(3) or img_match.group(1)
            images.append({"reference": ref})

        # Extract Tables
        tables = []
        for tbl_match in self.TABLE_PATTERN.finditer(content):
            tables.append({"raw_markdown": tbl_match.group(1)})

        # Numerical detection
        numerical_units = self.NUMERICAL_UNIT_PATTERN.findall(content)
        is_num = len(numerical_units) > 0 or "calculate" in content.lower() or "solve" in content.lower()

        return ExtractedQuestion(
            question_number=q_num,
            content=content,
            marks=marks,
            options=options,
            equations=[eq for eq in equations if isinstance(eq, str)],
            images=images,
            tables=tables,
            is_numerical=is_num,
            numerical_units=[f"{val} {unit}" for val, unit in numerical_units],
            sub_questions=[],
            raw_snippet=content[:200]
        )
