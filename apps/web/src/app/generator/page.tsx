'use client';

import React, { useState } from 'react';
import DisclaimerBanner from '@/components/DisclaimerBanner';
import { HelpCircle, RefreshCw, Sparkles } from 'lucide-react';

export default function QuestionGeneratorPage() {
  const [topic, setTopic] = useState('Binary Search Tree & Recursion');
  const [qType, setQType] = useState('MCQ');
  const [difficulty, setDifficulty] = useState('Medium');
  const [marks, setMarks] = useState(5);
  const [generatedQuestion, setGeneratedQuestion] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const handleGenerate = (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    setTimeout(() => {
      if (qType === 'MCQ') {
        setGeneratedQuestion({
          type: 'MCQ',
          text: 'Consider an initially empty Binary Search Tree (BST). Keys [15, 10, 20, 8, 12, 18, 25] are inserted sequentially. What is the height of the resulting BST (number of edges on the longest root-to-leaf path)?',
          options: [
            { label: 'A', text: '2' },
            { label: 'B', text: '3' },
            { label: 'C', text: '4' },
            { label: 'D', text: '5' },
          ],
          solution: 'Inserting elements sequentially: Root=15. Left=10, Right=20. Left-Left=8, Left-Right=12. Right-Left=18, Right-Right=25. Path 15->10->8 has 2 edges, 15->10->12 has 2 edges, 15->20->25 has 2 edges. Height = 2 edges.',
          rubric: { 'Correct Tree Diagram': 2, 'Correct Edge Count Calculation': 3 },
          similarity: '0.89 (High Structural Equivalence)',
        });
      } else if (qType === 'ASSERTION_REASON') {
        setGeneratedQuestion({
          type: 'ASSERTION_REASON',
          text: 'Assertion (A): Searching in a balanced AVL tree takes O(log N) worst-case time.\nReason (R): The height difference (balance factor) between left and right subtrees for every node in an AVL tree is at most 1.',
          options: [
            { label: 'A', text: 'Both (A) and (R) are true and (R) is the correct explanation of (A).' },
            { label: 'B', text: 'Both (A) and (R) are true but (R) is NOT the correct explanation of (A).' },
            { label: 'C', text: '(A) is true but (R) is false.' },
            { label: 'D', text: '(A) is false but (R) is true.' },
          ],
          solution: 'Since balance factor is strictly maintained <= 1, tree height H is bounded by 1.44 log2 N = O(log N). Thus (R) correctly explains (A).',
          rubric: { 'Assertion Evaluation': 2, 'Reason Rationale': 3 },
          similarity: '0.92',
        });
      } else {
        setGeneratedQuestion({
          type: 'NUMERICAL',
          text: 'In a 4-way set-associative cache memory with 64 KB total size and line size of 64 bytes, calculate the total number of index bits required for address decoding.',
          options: [],
          solution: 'Cache lines = 64 KB / 64 B = 1024 lines. Sets = 1024 / 4 = 256 sets. Index bits = log2(256) = 8 bits.',
          rubric: { 'Set Count Formula': 2, 'Logarithm Calculation': 3 },
          similarity: '0.88',
        });
      }
      setLoading(false);
    }, 600);
  };

  return (
    <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      <div className="pb-6 border-b border-gray-800">
        <h1 className="text-3xl font-extrabold tracking-tight text-white flex items-center gap-3">
          <Sparkles className="w-8 h-8 text-indigo-400" />
          AI Practice Question Synthesizer
        </h1>
        <p className="text-sm text-gray-400 mt-1">
          Synthesize original, statistically similar examination-style questions (MCQ, Numerical, Integer, Assertion-Reason) with rubrics and similarity scoring.
        </p>
      </div>

      <DisclaimerBanner />

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Controls Column */}
        <div className="p-6 rounded-2xl bg-gray-900/60 border border-gray-800 backdrop-blur-md space-y-6 shadow-xl h-fit">
          <h3 className="text-lg font-bold text-gray-200 flex items-center gap-2">
            <HelpCircle className="w-5 h-5 text-sky-400" />
            Generation Parameters
          </h3>

          <form onSubmit={handleGenerate} className="space-y-4 text-xs">
            <div>
              <label className="block text-gray-300 font-semibold mb-1">Target Topic / Concept:</label>
              <input
                type="text"
                value={topic}
                onChange={(e) => setTopic(e.target.value)}
                className="w-full px-3 py-2 rounded-xl bg-gray-800 border border-gray-700 text-gray-200 font-medium focus:ring-2 focus:ring-indigo-500"
              />
            </div>

            <div>
              <label className="block text-gray-300 font-semibold mb-1">Question Format / Type:</label>
              <select
                value={qType}
                onChange={(e) => setQType(e.target.value)}
                className="w-full px-3 py-2 rounded-xl bg-gray-800 border border-gray-700 text-gray-200 font-medium focus:ring-2 focus:ring-indigo-500"
              >
                <option value="MCQ">Multiple Choice Question (MCQ)</option>
                <option value="NUMERICAL">Numerical Answer Type (NAT)</option>
                <option value="INTEGER">Integer Answer Type</option>
                <option value="ASSERTION_REASON">Assertion & Reason</option>
              </select>
            </div>

            <div>
              <label className="block text-gray-300 font-semibold mb-1">Difficulty Level:</label>
              <div className="grid grid-cols-3 gap-2">
                {['Easy', 'Medium', 'Hard'].map((lvl) => (
                  <button
                    key={lvl}
                    type="button"
                    onClick={() => setDifficulty(lvl)}
                    className={`py-2 rounded-xl font-bold text-xs border transition-all ${
                      difficulty === lvl
                        ? 'bg-indigo-600 border-indigo-500 text-white shadow-lg'
                        : 'bg-gray-800 border-gray-700 text-gray-400 hover:bg-gray-700'
                    }`}
                  >
                    {lvl}
                  </button>
                ))}
              </div>
            </div>

            <div>
              <label className="block text-gray-300 font-semibold mb-1">Target Marks Weight:</label>
              <input
                type="number"
                value={marks}
                onChange={(e) => setMarks(Number(e.target.value))}
                className="w-full px-3 py-2 rounded-xl bg-gray-800 border border-gray-700 text-gray-200 font-medium focus:ring-2 focus:ring-indigo-500"
              />
            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full py-3 rounded-xl bg-gradient-to-r from-indigo-600 to-sky-500 hover:from-indigo-500 hover:to-sky-400 text-white font-bold tracking-wide shadow-lg shadow-indigo-500/25 flex items-center justify-center gap-2 transition-all"
            >
              <RefreshCw className={`w-4 h-4 ${loading ? 'animate-spin' : ''}`} />
              {loading ? 'Synthesizing...' : 'Synthesize Original Question'}
            </button>
          </form>
        </div>

        {/* Question Display Column */}
        <div className="lg:col-span-2">
          {generatedQuestion ? (
            <div className="p-8 rounded-2xl bg-gray-900/70 border border-gray-800 space-y-6 shadow-2xl backdrop-blur-md">
              <div className="flex justify-between items-center pb-4 border-b border-gray-800 text-xs">
                <span className="px-3 py-1 rounded-full bg-indigo-500/10 text-indigo-400 font-bold border border-indigo-500/30">
                  Format: {generatedQuestion.type} ({difficulty} - {marks} Marks)
                </span>
                <span className="text-gray-400">Cosine Similarity: {generatedQuestion.similarity}</span>
              </div>

              <div className="space-y-4">
                <h3 className="text-lg font-semibold text-gray-100 leading-relaxed">
                  {generatedQuestion.text}
                </h3>

                {generatedQuestion.options.length > 0 && (
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
                    {generatedQuestion.options.map((opt: any, i: number) => (
                      <div key={i} className="p-3 rounded-xl bg-gray-800/40 border border-gray-700/50 flex items-center space-x-3">
                        <span className="w-6 h-6 rounded-lg bg-indigo-600/30 text-indigo-300 font-bold flex items-center justify-center">
                          {opt.label}
                        </span>
                        <span className="text-gray-300">{opt.text}</span>
                      </div>
                    ))}
                  </div>
                )}
              </div>

              <div className="pt-6 border-t border-gray-800 space-y-3 text-xs">
                <h4 className="font-bold text-sky-400 uppercase tracking-wider">Suggested Solution Derivation:</h4>
                <div className="p-4 rounded-xl bg-gray-800/30 border border-gray-700/30 text-gray-300 font-mono whitespace-pre-line leading-relaxed">
                  {generatedQuestion.solution}
                </div>
              </div>
            </div>
          ) : (
            <div className="p-12 rounded-2xl bg-gray-900/40 border border-gray-800 border-dashed text-center text-gray-500 space-y-3">
              <Sparkles className="w-12 h-12 mx-auto text-gray-600" />
              <p className="text-sm font-medium">Select parameters on the left and click 'Synthesize Original Question' to generate practice questions.</p>
            </div>
          )}
        </div>
      </div>
    </main>
  );
}
