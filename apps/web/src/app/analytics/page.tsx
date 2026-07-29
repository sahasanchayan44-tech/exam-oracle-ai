'use client';

import React, { useState } from 'react';
import DisclaimerBanner from '@/components/DisclaimerBanner';
import { Activity, BarChart, Layers, Network, PieChart, TrendingUp } from 'lucide-react';

export default function AnalyticsPage() {
  const [selectedExam, setSelectedExam] = useState('GATE_CS');

  const topicProbabilities = [
    { topic: 'Binary Search Trees & AVL', prob: 0.82, lower: 0.74, upper: 0.90, confidence: '94%' },
    { topic: 'Graph Traversal (BFS / DFS)', prob: 0.78, lower: 0.70, upper: 0.86, confidence: '92%' },
    { topic: 'Dynamic Programming', prob: 0.65, lower: 0.55, upper: 0.75, confidence: '88%' },
    { topic: 'Process Scheduling & Threads', prob: 0.58, lower: 0.48, upper: 0.68, confidence: '85%' },
    { topic: 'Virtual Memory & Paging', prob: 0.52, lower: 0.42, upper: 0.62, confidence: '82%' },
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
    <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      {/* Header & Exam Selector */}
      <div className="flex flex-col md:flex-row md:items-center justify-between gap-4 pb-6 border-b border-gray-800">
        <div>
          <h1 className="text-3xl font-extrabold tracking-tight text-white flex items-center gap-3">
            <Activity className="w-8 h-8 text-indigo-400" />
            Statistical Intelligence & Analytics
          </h1>
          <p className="text-sm text-gray-400 mt-1">
            Multivariate probability distributions, heatmaps, PageRank centrality knowledge graphs, & correlation metrics.
          </p>
        </div>

        <div className="flex items-center space-x-3">
          <label className="text-xs font-semibold text-gray-400 uppercase tracking-wider">Exam Suite:</label>
          <select
            value={selectedExam}
            onChange={(e) => setSelectedExam(e.target.value)}
            className="px-4 py-2 rounded-xl bg-gray-900 border border-gray-800 text-sm font-semibold text-indigo-300 focus:outline-none focus:ring-2 focus:ring-indigo-500"
          >
            <option value="GATE_CS">GATE Computer Science</option>
            <option value="NEET_PHYSICS">NEET Physics</option>
            <option value="UPSC_GS">UPSC General Studies</option>
            <option value="CAT_QUANT">CAT Quantitative Ability</option>
            <option value="GRE_MATH">GRE General Mathematics</option>
            <option value="SAT_REASONING">SAT Math & Reading</option>
          </select>
        </div>
      </div>

      <DisclaimerBanner />

      {/* Grid Row 1: Probability Curves & Topic Distribution */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Topic Probability Curves */}
        <div className="p-6 rounded-2xl bg-gray-900/60 border border-gray-800 backdrop-blur-md space-y-4 shadow-xl">
          <div className="flex justify-between items-center">
            <h3 className="text-lg font-bold text-gray-200 flex items-center gap-2">
              <TrendingUp className="w-5 h-5 text-indigo-400" />
              Bayesian Topic Probability Distributions P(Topic)
            </h3>
            <span className="text-xs font-semibold text-gray-400">95% Confidence Bounds</span>
          </div>

          <div className="space-y-4">
            {topicProbabilities.map((t, idx) => (
              <div key={idx} className="space-y-1">
                <div className="flex justify-between text-xs font-semibold">
                  <span className="text-gray-300">{t.topic}</span>
                  <span className="text-indigo-400">{(t.prob * 100).toFixed(1)}% <span className="text-gray-500 font-normal">[{ (t.lower*100).toFixed(0) }% - { (t.upper*100).toFixed(0) }%]</span></span>
                </div>
                <div className="w-full h-3 rounded-full bg-gray-800 overflow-hidden relative">
                  <div
                    className="h-full rounded-full bg-gradient-to-r from-indigo-600 via-sky-400 to-indigo-300 transition-all duration-500"
                    style={{ width: `${t.prob * 100}%` }}
                  />
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Heatmap Matrix: Year x Topic Frequency */}
        <div className="p-6 rounded-2xl bg-gray-900/60 border border-gray-800 backdrop-blur-md space-y-4 shadow-xl">
          <h3 className="text-lg font-bold text-gray-200 flex items-center gap-2">
            <Layers className="w-5 h-5 text-sky-400" />
            Topic Occurrence Heatmap Matrix (Historical Sample Years)
          </h3>
          <div className="grid grid-cols-5 gap-2 text-center text-xs">
            <div className="font-bold text-gray-500">Year / Topic</div>
            <div className="font-bold text-gray-400">2023</div>
            <div className="font-bold text-gray-400">2024</div>
            <div className="font-bold text-gray-400">2025</div>
            <div className="font-bold text-gray-400">2026</div>

            <div className="font-semibold text-left text-gray-300">Trees & Graphs</div>
            <div className="p-2 rounded bg-indigo-600/40 text-indigo-200 font-bold">12m</div>
            <div className="p-2 rounded bg-indigo-600/80 text-white font-bold">18m</div>
            <div className="p-2 rounded bg-indigo-600/60 text-indigo-100 font-bold">15m</div>
            <div className="p-2 rounded bg-indigo-600/90 text-white font-bold">20m</div>

            <div className="font-semibold text-left text-gray-300">Dynamic Prog.</div>
            <div className="p-2 rounded bg-indigo-600/60 text-indigo-100 font-bold">14m</div>
            <div className="p-2 rounded bg-indigo-600/30 text-indigo-300 font-bold">8m</div>
            <div className="p-2 rounded bg-indigo-600/70 text-indigo-100 font-bold">16m</div>
            <div className="p-2 rounded bg-indigo-600/50 text-indigo-200 font-bold">10m</div>

            <div className="font-semibold text-left text-gray-300">OS Scheduling</div>
            <div className="p-2 rounded bg-indigo-600/30 text-indigo-300 font-bold">6m</div>
            <div className="p-2 rounded bg-indigo-600/50 text-indigo-200 font-bold">10m</div>
            <div className="p-2 rounded bg-indigo-600/40 text-indigo-200 font-bold">8m</div>
            <div className="p-2 rounded bg-indigo-600/70 text-indigo-100 font-bold">14m</div>
          </div>
        </div>
      </div>

      {/* Grid Row 2: Knowledge Graph Visualization & Correlation Matrix */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Knowledge Graph Network */}
        <div className="p-6 rounded-2xl bg-gray-900/60 border border-gray-800 backdrop-blur-md space-y-4 shadow-xl">
          <h3 className="text-lg font-bold text-gray-200 flex items-center gap-2">
            <Network className="w-5 h-5 text-indigo-400" />
            PageRank Concept Knowledge Graph Network
          </h3>

          <div className="space-y-3">
            {knowledgeGraphNodes.map((n, idx) => (
              <div key={idx} className="p-3 rounded-xl bg-gray-800/50 border border-gray-700/50 flex justify-between items-center text-xs">
                <div>
                  <span className="font-bold text-gray-200 block">{n.id}</span>
                  <span className="text-gray-500">{n.type} Node</span>
                </div>
                <span className="px-3 py-1 rounded-full bg-indigo-500/10 text-indigo-400 font-semibold border border-indigo-500/30">
                  PageRank Score: {n.rank}
                </span>
              </div>
            ))}
          </div>
        </div>

        {/* Correlation Matrix Heatmap */}
        <div className="p-6 rounded-2xl bg-gray-900/60 border border-gray-800 backdrop-blur-md space-y-4 shadow-xl">
          <h3 className="text-lg font-bold text-gray-200 flex items-center gap-2">
            <PieChart className="w-5 h-5 text-sky-400" />
            Pearson Correlation Matrix ($r$)
          </h3>

          <div className="grid grid-cols-5 gap-2 text-center text-xs">
            <div></div>
            {matrixLabels.map((lbl, i) => <div key={i} className="font-bold text-gray-400">{lbl}</div>)}
            {matrixLabels.map((rowLbl, rowIdx) => (
              <React.Fragment key={rowIdx}>
                <div className="font-bold text-left text-gray-400 self-center">{rowLbl}</div>
                {correlationMatrix[rowIdx].map((val, colIdx) => (
                  <div
                    key={colIdx}
                    className="p-3 rounded font-bold text-white shadow"
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
