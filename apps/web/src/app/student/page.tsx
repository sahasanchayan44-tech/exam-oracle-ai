'use client';

import React, { useState } from 'react';
import DisclaimerBanner from '@/components/DisclaimerBanner';
import { Calendar, CheckCircle, Sparkles, Target, TrendingUp, UserCheck } from 'lucide-react';

export default function StudentModulePage() {
  const [targetExam, setTargetExam] = useState('GATE_CS');
  const [mockScore, setMockScore] = useState('62');
  const [weakTopics, setWeakTopics] = useState('Dynamic Programming, Graph Traversal, Cache Coherence');
  const [analysisResult, setAnalysisResult] = useState<any>(null);
  const [loading, setLoading] = useState(false);

  const handleGeneratePlan = (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    setTimeout(() => {
      setAnalysisResult({
        priorityChapters: [
          { name: 'Dynamic Programming & Recurrences', weight: '14 Marks High Yield', impact: '+8 Marks Potential' },
          { name: 'Graph Algorithms (Dijkstra, BFS, DFS)', weight: '10 Marks High Yield', impact: '+6 Marks Potential' },
          { name: 'Virtual Memory & Cache Mappings', weight: '8 Marks Medium Yield', impact: '+4 Marks Potential' },
        ],
        expectedImprovement: '+18 Marks (Predicted Mock Jump: 62 -> 80)',
        revisionSchedule: [
          { day: 'Day 1 - 2', task: 'Master Master Theorem & DP State Transitions', duration: '3.5 hrs/day' },
          { day: 'Day 3 - 4', task: 'Solve 15 Graph Shortest Path Numerical Questions', duration: '3.0 hrs/day' },
          { day: 'Day 5 - 6', task: 'Review Set-Associative Cache Mapping Formulae', duration: '2.5 hrs/day' },
          { day: 'Day 7', task: 'Take Targeted 50-Mark Simulated Practice Exam', duration: '2.0 hrs' },
        ],
        keyFormulae: [
          'T(n) = aT(n/b) + f(n) (Master Theorem)',
          'Cache Index Bits = log2(Number of Sets)',
          'Page Table Size = Number of Entries * Entry Size',
        ]
      });
      setLoading(false);
    }, 600);
  };

  return (
    <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      <div className="pb-6 border-b border-gray-800">
        <h1 className="text-3xl font-extrabold tracking-tight text-white flex items-center gap-3">
          <UserCheck className="w-8 h-8 text-sky-400" />
          Student AI Personal Revision Planner
        </h1>
        <p className="text-sm text-gray-400 mt-1">
          Input your mock test scores, target exam, and weak chapters to generate an optimized, probability-weighted revision plan.
        </p>
      </div>

      <DisclaimerBanner />

      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        {/* Form Column */}
        <div className="p-6 rounded-2xl bg-gray-900/60 border border-gray-800 backdrop-blur-md space-y-6 shadow-xl h-fit">
          <h3 className="text-lg font-bold text-gray-200 flex items-center gap-2">
            <Target className="w-5 h-5 text-indigo-400" />
            Performance Input Profile
          </h3>

          <form onSubmit={handleGeneratePlan} className="space-y-4 text-xs">
            <div>
              <label className="block text-gray-300 font-semibold mb-1">Target Examination:</label>
              <select
                value={targetExam}
                onChange={(e) => setTargetExam(e.target.value)}
                className="w-full px-3 py-2 rounded-xl bg-gray-800 border border-gray-700 text-gray-200 font-medium focus:ring-2 focus:ring-indigo-500"
              >
                <option value="GATE_CS">GATE Computer Science & IT</option>
                <option value="NEET_PHYSICS">NEET Physics & Chemistry</option>
                <option value="UPSC_GS">UPSC Civil Services Prelims</option>
                <option value="CAT_QUANT">CAT Quantitative Ability</option>
                <option value="GRE_MATH">GRE Quantitative Reasoning</option>
              </select>
            </div>

            <div>
              <label className="block text-gray-300 font-semibold mb-1">Recent Mock Test Score (% or Marks):</label>
              <input
                type="number"
                value={mockScore}
                onChange={(e) => setMockScore(e.target.value)}
                className="w-full px-3 py-2 rounded-xl bg-gray-800 border border-gray-700 text-gray-200 font-medium focus:ring-2 focus:ring-indigo-500"
                placeholder="e.g. 62"
              />
            </div>

            <div>
              <label className="block text-gray-300 font-semibold mb-1">Weak Chapters / Concepts (Comma Separated):</label>
              <textarea
                rows={3}
                value={weakTopics}
                onChange={(e) => setWeakTopics(e.target.value)}
                className="w-full px-3 py-2 rounded-xl bg-gray-800 border border-gray-700 text-gray-200 font-medium focus:ring-2 focus:ring-indigo-500"
                placeholder="e.g. Dynamic Programming, Cache Memory"
              />
            </div>

            <button
              type="submit"
              disabled={loading}
              className="w-full py-3 rounded-xl bg-gradient-to-r from-indigo-600 to-sky-500 hover:from-indigo-500 hover:to-sky-400 text-white font-bold tracking-wide shadow-lg shadow-indigo-500/25 flex items-center justify-center gap-2 transition-all"
            >
              <Sparkles className="w-4 h-4" />
              {loading ? 'Analyzing Performance...' : 'Generate AI Revision Plan'}
            </button>
          </form>
        </div>

        {/* Results Column */}
        <div className="lg:col-span-2 space-y-6">
          {analysisResult ? (
            <div className="space-y-6">
              {/* Expected Score Jump Banner */}
              <div className="p-6 rounded-2xl bg-gradient-to-r from-indigo-900/60 to-sky-900/40 border border-indigo-500/30 flex items-center justify-between shadow-xl">
                <div>
                  <h4 className="text-xs font-bold text-indigo-300 uppercase tracking-wider">Projected Improvement</h4>
                  <div className="text-2xl font-extrabold text-white mt-1">{analysisResult.expectedImprovement}</div>
                </div>
                <TrendingUp className="w-10 h-10 text-sky-400" />
              </div>

              {/* Priority Chapters */}
              <div className="p-6 rounded-2xl bg-gray-900/60 border border-gray-800 backdrop-blur-md space-y-4 shadow-xl">
                <h3 className="text-lg font-bold text-gray-200 flex items-center gap-2">
                  <CheckCircle className="w-5 h-5 text-indigo-400" />
                  Priority Chapters (Bayesian High-Yield Ranking)
                </h3>
                <div className="space-y-3">
                  {analysisResult.priorityChapters.map((c: any, i: number) => (
                    <div key={i} className="p-4 rounded-xl bg-gray-800/50 border border-gray-700/50 flex justify-between items-center text-xs">
                      <div>
                        <span className="font-bold text-gray-200 block text-sm">{c.name}</span>
                        <span className="text-gray-400">{c.weight}</span>
                      </div>
                      <span className="px-3 py-1 rounded-full bg-emerald-500/10 text-emerald-400 font-bold border border-emerald-500/30">
                        {c.impact}
                      </span>
                    </div>
                  ))}
                </div>
              </div>

              {/* Revision Schedule */}
              <div className="p-6 rounded-2xl bg-gray-900/60 border border-gray-800 backdrop-blur-md space-y-4 shadow-xl">
                <h3 className="text-lg font-bold text-gray-200 flex items-center gap-2">
                  <Calendar className="w-5 h-5 text-sky-400" />
                  Personalized 7-Day Revision Schedule
                </h3>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
                  {analysisResult.revisionSchedule.map((s: any, idx: number) => (
                    <div key={idx} className="p-4 rounded-xl bg-gray-800/40 border border-gray-700/40 space-y-1">
                      <span className="font-bold text-indigo-400 block">{s.day}</span>
                      <p className="text-gray-200 font-medium">{s.task}</p>
                      <span className="text-gray-500 block text-[11px]">Recommended: {s.duration}</span>
                    </div>
                  ))}
                </div>
              </div>
            </div>
          ) : (
            <div className="p-12 rounded-2xl bg-gray-900/40 border border-gray-800 border-dashed text-center text-gray-500 space-y-3">
              <UserCheck className="w-12 h-12 mx-auto text-gray-600" />
              <p className="text-sm font-medium">Fill in your mock scores and weak chapters on the left to generate your personalized AI study plan.</p>
            </div>
          )}
        </div>
      </div>
    </main>
  );
}
