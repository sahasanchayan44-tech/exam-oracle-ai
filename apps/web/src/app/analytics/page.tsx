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
    <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-10 space-y-8">
      <div className="flex flex-col sm:flex-row sm:items-center justify-between gap-4 pb-6 border-b border-[#222E28]">
        <div>
          <h1 className="text-2xl sm:text-3xl font-extrabold text-white flex items-center gap-3">
            <Activity className="w-7 h-7 text-emerald-400" />
            Statistical Intelligence & Analytics
          </h1>
          <p className="text-sm text-slate-400 mt-1">
            Multivariate probability distributions, heatmaps, PageRank centrality, & correlation matrices.
          </p>
        </div>

        <div className="flex items-center space-x-3">
          <label className="text-xs sm:text-sm font-semibold text-slate-300">Exam Suite:</label>
          <select
            value={selectedExam}
            onChange={(e) => setSelectedExam(e.target.value)}
            className="px-4 py-2 rounded-xl bg-[#0C0F0E] border border-[#222E28] text-amber-400 text-sm font-bold focus:outline-none"
          >
            <option value="JEE_MAIN">JEE Main (2015-2026)</option>
            <option value="GATE_CS">GATE Computer Science</option>
            <option value="NEET">NEET Physics & Chemistry</option>
            <option value="UPSC_GS">UPSC General Studies</option>
            <option value="CAT_QUANT">CAT Quantitative</option>
          </select>
        </div>
      </div>

      <DisclaimerBanner />

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Topic Probability Curves */}
        <div className="p-6 rounded-3xl bg-[#141A17]/80 border border-[#222E28] space-y-5 shadow-xl">
          <div className="flex justify-between items-center">
            <h3 className="text-sm sm:text-base font-bold text-slate-200 uppercase tracking-wider flex items-center gap-2">
              <TrendingUp className="w-5 h-5 text-emerald-400" />
              Bayesian Topic Probability Distributions P(Topic)
            </h3>
            <span className="text-xs text-slate-400 font-semibold">95% Confidence Bounds</span>
          </div>

          <div className="space-y-4">
            {topicProbabilities.map((t, idx) => (
              <div key={idx} className="space-y-1.5 text-xs sm:text-sm">
                <div className="flex justify-between text-slate-200 font-medium">
                  <span>{t.topic}</span>
                  <span className="text-emerald-400 font-bold">
                    {(t.prob * 100).toFixed(1)}% <span className="text-slate-400 font-normal text-xs">[{ (t.lower*100).toFixed(0) }% - { (t.upper*100).toFixed(0) }%]</span>
                  </span>
                </div>
                <div className="w-full h-3 rounded-full bg-[#0C0F0E] overflow-hidden">
                  <div
                    className="h-full rounded-full bg-gradient-to-r from-emerald-500 via-amber-400 to-emerald-300"
                    style={{ width: `${t.prob * 100}%` }}
                  />
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* Heatmap Matrix */}
        <div className="p-6 rounded-3xl bg-[#141A17]/80 border border-[#222E28] space-y-5 shadow-xl">
          <h3 className="text-sm sm:text-base font-bold text-slate-200 uppercase tracking-wider flex items-center gap-2">
            <Layers className="w-5 h-5 text-amber-400" />
            Topic Occurrence Heatmap Matrix
          </h3>
          <div className="grid grid-cols-5 gap-2.5 text-center text-xs sm:text-sm">
            <div className="font-bold text-slate-400">Year / Topic</div>
            <div className="font-bold text-slate-300">2023</div>
            <div className="font-bold text-slate-300">2024</div>
            <div className="font-bold text-slate-300">2025</div>
            <div className="font-bold text-slate-300">2026</div>

            <div className="font-semibold text-left text-slate-200">Trees & Graphs</div>
            <div className="p-2.5 rounded-xl bg-emerald-600/40 text-emerald-100 font-bold">12m</div>
            <div className="p-2.5 rounded-xl bg-emerald-600/80 text-white font-bold">18m</div>
            <div className="p-2.5 rounded-xl bg-emerald-600/60 text-emerald-100 font-bold">15m</div>
            <div className="p-2.5 rounded-xl bg-emerald-600/90 text-white font-bold">20m</div>

            <div className="font-semibold text-left text-slate-200">Dynamic Prog.</div>
            <div className="p-2.5 rounded-xl bg-emerald-600/60 text-emerald-100 font-bold">14m</div>
            <div className="p-2.5 rounded-xl bg-emerald-600/30 text-emerald-200 font-bold">8m</div>
            <div className="p-2.5 rounded-xl bg-emerald-600/70 text-emerald-100 font-bold">16m</div>
            <div className="p-2.5 rounded-xl bg-emerald-600/50 text-emerald-200 font-bold">10m</div>

            <div className="font-semibold text-left text-slate-200">OS Scheduling</div>
            <div className="p-2.5 rounded-xl bg-emerald-600/30 text-emerald-200 font-bold">6m</div>
            <div className="p-2.5 rounded-xl bg-emerald-600/50 text-emerald-200 font-bold">10m</div>
            <div className="p-2.5 rounded-xl bg-emerald-600/40 text-emerald-200 font-bold">8m</div>
            <div className="p-2.5 rounded-xl bg-emerald-600/70 text-emerald-100 font-bold">14m</div>
          </div>
        </div>
      </div>

      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {/* Knowledge Graph Network */}
        <div className="p-6 rounded-3xl bg-[#141A17]/80 border border-[#222E28] space-y-4 shadow-xl">
          <h3 className="text-sm sm:text-base font-bold text-slate-200 uppercase tracking-wider flex items-center gap-2">
            <Network className="w-5 h-5 text-emerald-400" />
            PageRank Concept Knowledge Graph Network
          </h3>

          <div className="space-y-3">
            {knowledgeGraphNodes.map((n, idx) => (
              <div key={idx} className="p-4 rounded-2xl bg-[#0C0F0E]/60 border border-[#222E28] flex justify-between items-center text-xs sm:text-sm">
                <div>
                  <span className="font-bold text-slate-100 block">{n.id}</span>
                  <span className="text-slate-400 text-xs">{n.type} Node</span>
                </div>
                <span className="px-3 py-1 rounded-full bg-emerald-500/10 text-emerald-300 font-bold border border-emerald-500/20 text-xs">
                  PageRank: {n.rank}
                </span>
              </div>
            ))}
          </div>
        </div>

        {/* Correlation Matrix */}
        <div className="p-6 rounded-3xl bg-[#141A17]/80 border border-[#222E28] space-y-4 shadow-xl">
          <h3 className="text-sm sm:text-base font-bold text-slate-200 uppercase tracking-wider flex items-center gap-2">
            <PieChart className="w-5 h-5 text-amber-400" />
            Pearson Correlation Matrix
          </h3>

          <div className="grid grid-cols-5 gap-2.5 text-center text-xs sm:text-sm">
            <div></div>
            {matrixLabels.map((lbl, i) => <div key={i} className="font-bold text-slate-300">{lbl}</div>)}
            {matrixLabels.map((rowLbl, rowIdx) => (
              <React.Fragment key={rowIdx}>
                <div className="font-bold text-left text-slate-300 self-center">{rowLbl}</div>
                {correlationMatrix[rowIdx].map((val, colIdx) => (
                  <div
                    key={colIdx}
                    className="p-3 rounded-xl font-bold text-white shadow-md text-xs sm:text-sm"
                    style={{ backgroundColor: `rgba(16, 185, 129, ${val})` }}
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
