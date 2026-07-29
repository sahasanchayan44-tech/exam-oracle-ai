'use client';

import React, { useState } from 'react';
import DisclaimerBanner from '@/components/DisclaimerBanner';
import { Activity, Layers, Network, PieChart, TrendingUp } from 'lucide-react';

export default function AnalyticsPage() {
  const [selectedExam, setSelectedExam] = useState('JEE_MAIN');

  const topicProbabilities = [
    { topic: 'Binary Search Trees & AVL', prob: 0.82, lower: 0.74, upper: 0.90 },
    { topic: 'Graph Traversal (BFS / DFS)', prob: 0.78, lower: 0.70, upper: 0.86 },
    { topic: 'Dynamic Programming', prob: 0.65, lower: 0.55, upper: 0.75 },
    { topic: 'Process Scheduling & Threads', prob: 0.58, lower: 0.48, upper: 0.68 },
    { topic: 'Virtual Memory & Paging', prob: 0.52, lower: 0.42, upper: 0.62 },
  ];

  const correlationMatrix = [
    [1.00, 0.74, 0.42, 0.15],
    [0.74, 1.00, 0.58, 0.22],
    [0.42, 0.58, 1.00, 0.65],
    [0.15, 0.22, 0.65, 1.00],
  ];
  const matrixLabels = ['Trees', 'Graphs', 'DP', 'Memory'];

  const knowledgeGraphNodes = [
    { id: 'Data Structures', rank: '0.24 (High)', type: 'Chapter' },
    { id: 'Trees & Recursion', rank: '0.18', type: 'Concept' },
    { id: 'Graph Algorithms', rank: '0.16', type: 'Concept' },
    { id: 'Time Complexity', rank: '0.12', type: 'Tag' },
  ];

  return (
    <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-6">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-4 border-b border-slate-800/80">
        <div>
          <h1 className="text-xl sm:text-2xl font-bold text-white flex items-center gap-2">
            <Activity className="w-5 h-5 text-indigo-400" />
            Statistical Intelligence & Analytics
          </h1>
          <p className="text-xs text-slate-400 mt-1">
            Multivariate probability distributions, heatmaps, PageRank centrality, & correlation matrices.
          </p>
        </div>

        <div className="flex items-center space-x-2">
          <span className="text-xs text-slate-400 font-medium">Exam Suite:</span>
          <select
            value={selectedExam}
            onChange={(e) => setSelectedExam(e.target.value)}
            className="px-3 py-1.5 rounded-lg bg-slate-800 border border-slate-700 text-indigo-300 text-xs font-semibold focus:outline-none"
          >
            <option value="JEE_MAIN">JEE Main (2015-2026)</option>
            <option value="GATE_CS">GATE Computer Science</option>
            <option value="NEET">NEET Physics</option>
            <option value="UPSC_GS">UPSC General Studies</option>
            <option value="CAT_QUANT">CAT Quantitative</option>
          </select>
        </div>
      </div>

      <DisclaimerBanner />

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Topic Probability Curves */}
        <div className="p-5 rounded-2xl bg-slate-900/40 border border-slate-800/80 space-y-4">
          <div className="flex justify-between items-center">
            <h3 className="text-xs font-bold text-slate-300 uppercase tracking-wider flex items-center gap-2">
              <TrendingUp className="w-4 h-4 text-indigo-400" />
              Bayesian Topic Probability Distributions P(Topic)
            </h3>
            <span className="text-[11px] text-slate-400 font-medium">95% Confidence Bounds</span>
          </div>

          <div className="space-y-3">
            {topicProbabilities.map((t, idx) => (
              <div key={idx} className="space-y-1 text-xs">
                <div className="flex justify-between text-slate-300 font-medium">
                  <span>{t.topic}</span>
                  <span className="text-indigo-400 font-semibold">
                    {(t.prob * 100).toFixed(1)}% <span className="text-slate-500 font-normal text-[10px]">[{ (t.lower*100).toFixed(0) }% - { (t.upper*100).toFixed(0) }%]</span>
                  </span>
                </div>
                <div className="w-full h-2 rounded-full bg-slate-950 overflow-hidden">
                  <div
                    className="h-full rounded-full bg-gradient-to-r from-indigo-500 to-sky-400"
                    style={{ width: `${t.prob * 100}%` }}
                  />
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Heatmap Matrix */}
        <div className="p-5 rounded-2xl bg-slate-900/40 border border-slate-800/80 space-y-4">
          <h3 className="text-xs font-bold text-slate-300 uppercase tracking-wider flex items-center gap-2">
            <Layers className="w-4 h-4 text-sky-400" />
            Topic Occurrence Heatmap Matrix
          </h3>
          <div className="grid grid-cols-5 gap-2 text-center text-xs">
            <div className="font-semibold text-slate-500">Year / Topic</div>
            <div className="font-semibold text-slate-400">2023</div>
            <div className="font-semibold text-slate-400">2024</div>
            <div className="font-semibold text-slate-400">2025</div>
            <div className="font-semibold text-slate-400">2026</div>

            <div className="font-medium text-left text-slate-300">Trees & Graphs</div>
            <div className="p-2 rounded bg-indigo-600/30 text-indigo-200 font-semibold">12m</div>
            <div className="p-2 rounded bg-indigo-600/70 text-white font-semibold">18m</div>
            <div className="p-2 rounded bg-indigo-600/50 text-indigo-100 font-semibold">15m</div>
            <div className="p-2 rounded bg-indigo-600/80 text-white font-semibold">20m</div>

            <div className="font-medium text-left text-slate-300">Dynamic Prog.</div>
            <div className="p-2 rounded bg-indigo-600/50 text-indigo-100 font-semibold">14m</div>
            <div className="p-2 rounded bg-indigo-600/20 text-indigo-300 font-semibold">8m</div>
            <div className="p-2 rounded bg-indigo-600/60 text-indigo-100 font-semibold">16m</div>
            <div className="p-2 rounded bg-indigo-600/40 text-indigo-200 font-semibold">10m</div>

            <div className="font-medium text-left text-slate-300">OS Scheduling</div>
            <div className="p-2 rounded bg-indigo-600/20 text-indigo-300 font-semibold">6m</div>
            <div className="p-2 rounded bg-indigo-600/40 text-indigo-200 font-semibold">10m</div>
            <div className="p-2 rounded bg-indigo-600/30 text-indigo-200 font-semibold">8m</div>
            <div className="p-2 rounded bg-indigo-600/60 text-indigo-100 font-semibold">14m</div>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Knowledge Graph Network */}
        <div className="p-5 rounded-2xl bg-slate-900/40 border border-slate-800/80 space-y-3">
          <h3 className="text-xs font-bold text-slate-300 uppercase tracking-wider flex items-center gap-2">
            <Network className="w-4 h-4 text-indigo-400" />
            PageRank Concept Knowledge Graph Network
          </h3>

          <div className="space-y-2">
            {knowledgeGraphNodes.map((n, idx) => (
              <div key={idx} className="p-3 rounded-xl bg-slate-800/30 border border-slate-800/60 flex justify-between items-center text-xs">
                <div>
                  <span className="font-semibold text-slate-200 block">{n.id}</span>
                  <span className="text-slate-500 text-[11px]">{n.type} Node</span>
                </div>
                <span className="px-2.5 py-0.5 rounded-full bg-indigo-500/10 text-indigo-400 font-medium border border-indigo-500/20 text-[11px]">
                  PageRank: {n.rank}
                </span>
              </div>
            ))}
          </div>
        </div>

        {/* Correlation Matrix */}
        <div className="p-5 rounded-2xl bg-slate-900/40 border border-slate-800/80 space-y-3">
          <h3 className="text-xs font-bold text-slate-300 uppercase tracking-wider flex items-center gap-2">
            <PieChart className="w-4 h-4 text-sky-400" />
            Pearson Correlation Matrix
          </h3>

          <div className="grid grid-cols-5 gap-2 text-center text-xs">
            <div></div>
            {matrixLabels.map((lbl, i) => <div key={i} className="font-semibold text-slate-400">{lbl}</div>)}
            {matrixLabels.map((rowLbl, rowIdx) => (
              <React.Fragment key={rowIdx}>
                <div className="font-semibold text-left text-slate-400 self-center">{rowLbl}</div>
                {correlationMatrix[rowIdx].map((val, colIdx) => (
                  <div
                    key={colIdx}
                    className="p-2.5 rounded font-semibold text-white text-xs"
                    style={{ backgroundColor: `rgba(99, 102, 241, ${val})` }}
                  >
                    {val.toFixed(2)}
                  </div>
                ))}
              </React.Fragment>
            ))}
          </div>
        </div>
      </div>
    </main>
  );
}
