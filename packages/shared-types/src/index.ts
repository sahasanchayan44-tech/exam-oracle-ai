// =============================================================================
// EXAM ORACLE AI - ENTERPRISE DOMAIN TYPES & API CONTRACTS
// =============================================================================

export enum UserRole {
  SUPER_ADMIN = 'SUPER_ADMIN',
  PROFESSOR = 'PROFESSOR',
  STUDENT = 'STUDENT',
  ANALYST = 'ANALYST',
}

export interface UserProfile {
  id: string;
  email: string;
  fullName: string;
  role: UserRole;
  avatarUrl?: string;
  isActive: boolean;
  createdAt: string;
}

export enum ProcessingStatus {
  PENDING = 'PENDING',
  PARSING = 'PARSING',
  EXTRACTED = 'EXTRACTED',
  PROCESSED = 'PROCESSED',
  FAILED = 'FAILED',
}

export enum BloomsTaxonomyLevel {
  REMEMBER = 'REMEMBER',
  UNDERSTAND = 'UNDERSTAND',
  APPLY = 'APPLY',
  ANALYZE = 'ANALYZE',
  EVALUATE = 'EVALUATE',
  CREATE = 'CREATE',
}

export interface ExamPaperMetadata {
  id: string;
  subjectCode: string;
  title: string;
  year: number;
  term?: string;
  totalMarks: number;
  durationMinutes?: number;
  filePath: string;
  fileHash: string;
  status: ProcessingStatus;
  createdAt: string;
}

export interface QuestionExtract {
  id: string;
  examPaperId: string;
  topicId?: string;
  questionNumber: number;
  subQuestionLabel?: string;
  content: string;
  marks: number;
  bloomsLevel: BloomsTaxonomyLevel;
  difficultyScore: number; // 0.0 - 1.0
  qdrantVectorId?: string;
}

export interface StatisticalRationale {
  historicalFrequency: number;
  variance: number;
  sampleCount: number;
  temporalDecayWeight: number;
  bayesFactor: number;
  explanationText: string;
}

export interface TopicProbabilityEstimate {
  topicId: string;
  topicName: string;
  estimatedProbability: number; // P(Topic) in range [0.0, 1.0]
  expectedMarksWeight: number;
  confidenceLowerBound: number;
  confidenceUpperBound: number;
  confidenceScore: number; // Statistical reliability metric [0.0, 1.0]
  rationale: StatisticalRationale;
}

export interface ProbabilityAnalysisResponse {
  runId: string;
  subjectCode: string;
  algorithmName: string;
  executedAt: string;
  disclaimer: string; // Explicit non-predictive statistical disclaimer
  estimates: TopicProbabilityEstimate[];
}

export interface SynthesizedQuestion {
  id: string;
  topicId: string;
  questionText: string;
  suggestedSolution: string;
  rubric: Record<string, any>;
  marks: number;
  similarityToOriginal: number;
  confidenceScore: number;
}
