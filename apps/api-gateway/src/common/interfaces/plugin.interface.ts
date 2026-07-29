/**
 * Modular Plugin Architecture Interface Definitions for NestJS Gateway
 */

export interface IAnalyticsEnginePlugin {
  readonly id: string;
  readonly name: string;
  readonly version: string;

  calculateTopicProbabilities(
    subjectId: string,
    historicalPaperIds: string[],
    parameters: Record<string, any>,
  ): Promise<{
    estimates: Array<{
      topicId: string;
      probability: number;
      confidence: number;
      rationale: string;
    }>;
  }>;
}

export interface IQuestionGeneratorPlugin {
  readonly id: string;
  readonly name: string;
  readonly version: string;

  generatePracticeQuestion(
    topicId: string,
    referenceQuestionId: string,
    difficulty: number,
  ): Promise<{
    questionText: string;
    suggestedSolution: string;
    rubric: Record<string, any>;
    similarityScore: number;
  }>;
}
