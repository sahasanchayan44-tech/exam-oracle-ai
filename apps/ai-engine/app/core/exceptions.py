class ExamOracleException(Exception):
    """Base exception for Exam Oracle AI Engine"""
    def __init__(self, message: str, code: str = "INTERNAL_ERROR"):
        self.message = message
        self.code = code
        super().__init__(self.message)

class PaperParsingException(ExamOracleException):
    """Raised when PDF/OCR paper extraction fails"""
    def __init__(self, message: str):
        super().__init__(message, code="PAPER_PARSING_FAILED")

class StatisticalComputationException(ExamOracleException):
    """Raised when probability distribution algorithm encounters invalid bounds or insufficient data"""
    def __init__(self, message: str):
        super().__init__(message, code="STATISTICAL_COMPUTATION_FAILED")

class PluginExecutionException(ExamOracleException):
    """Raised when a dynamic algorithm plugin execution fails"""
    def __init__(self, message: str):
        super().__init__(message, code="PLUGIN_EXECUTION_FAILED")
