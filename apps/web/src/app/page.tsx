'use client';

import React from 'react';
import Link from 'next/link';
import DisclaimerBanner from '@/components/DisclaimerBanner';
import { Activity, BookOpen, Cpu, ShieldCheck, Sparkles, UserCheck, ArrowRight, CheckCircle2 } from 'lucide-react';

export default function HomePage() {
  return (
    <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 space-y-12">
      {/* Hero Section */}
      <section className="text-center space-y-6 max-w-4xl mx-auto py-6">
        <div className="inline-flex items-center space-x-2 px-3.5 py-1.5 rounded-full bg-indigo-500/10 border border-indigo-500/30 text-indigo-400 text-xs font-semibold uppercase tracking-widest shadow-inner">
          <Sparkles className="w-3.5 h-3.5" />
          <span>Universal Examination Intelligence Engine</span>
        </div>

        <h1 className="text-4xl sm:text-5xl lg:text-6xl font-extrabold tracking-tight text-white leading-tight">
          Probabilistic Examination Analysis & <span className="bg-clip-text text-transparent bg-gradient-to-r from-indigo-400 via-sky-400 to-indigo-200">Practice Synthesizer</span>
        </h1>

        <p className="text-base sm:text-lg text-gray-400 max-w-2xl mx-auto leading-relaxed font-normal">
          Empirical Bayesian distribution modeling, multi-LLM classification, knowledge graph centralities, and calibrated practice question synthesis for NEET, GATE, UPSC, CAT, GRE, SAT, and JEE.
        </p>

        <div className="flex flex-wrap justify-center gap-4 pt-4">
          <Link
            href="/analytics"
            className="px-6 py-3.5 rounded-xl bg-gradient-to-r from-indigo-600 to-sky-500 hover:from-indigo-500 hover:to-sky-400 text-white font-bold text-sm tracking-wide shadow-lg shadow-indigo-500/25 flex items-center space-x-2 transition-all duration-200"
          >
            <Activity className="w-4 h-4" />
            <span>Explore Analytics & Graphs</span>
            <ArrowRight className="w-4 h-4" />
          </Link>
          <Link
            href="/generator"
            className="px-6 py-3.5 rounded-xl bg-gray-900 hover:bg-gray-800 border border-gray-800 text-gray-200 font-semibold text-sm tracking-wide flex items-center space-x-2 transition-all duration-200"
          >
            <Sparkles className="w-4 h-4 text-sky-400" />
            <span>Question Synthesizer</span>
          </Link>
        </div>
      </section>

      <DisclaimerBanner />

      {/* Core Features Grid */}
      <section className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <div className="p-6 rounded-2xl bg-gray-900/60 border border-gray-800 backdrop-blur-md space-y-3 hover:border-indigo-500/40 transition-all duration-300 shadow-xl group">
          <div className="w-12 h-12 rounded-xl bg-indigo-600/10 border border-indigo-500/30 flex items-center justify-center text-indigo-400 group-hover:scale-110 transition-transform">
            <Cpu className="w-6 h-6" />
          </div>
          <h3 className="text-lg font-bold text-gray-100">Bayesian Topic Estimator</h3>
          <p className="text-xs text-gray-400 leading-relaxed">
            Kernel Density Estimation (KDE) and Dirichlet distribution priors modeling historical topic occurrence probabilities P(Topic) bounded by 95% confidence intervals.
          </p>
        </div>

        <div className="p-6 rounded-2xl bg-gray-900/60 border border-gray-800 backdrop-blur-md space-y-3 hover:border-sky-500/40 transition-all duration-300 shadow-xl group">
          <div className="w-12 h-12 rounded-xl bg-sky-600/10 border border-sky-500/30 flex items-center justify-center text-sky-400 group-hover:scale-110 transition-transform">
            <BookOpen className="w-6 h-6" />
          </div>
          <h3 className="text-lg font-bold text-gray-100">PageRank Knowledge Graph</h3>
          <p className="text-xs text-gray-400 leading-relaxed">
            NetworkX / Neo4j Graph Neural Networks computing Node2Vec graph embeddings, Louvain community detection, and PageRank concept centralities.
          </p>
        </div>

        <div className="p-6 rounded-2xl bg-gray-900/60 border border-gray-800 backdrop-blur-md space-y-3 hover:border-indigo-500/40 transition-all duration-300 shadow-xl group">
          <div className="w-12 h-12 rounded-xl bg-indigo-600/10 border border-indigo-500/30 flex items-center justify-center text-indigo-400 group-hover:scale-110 transition-transform">
            <Sparkles className="w-6 h-6" />
          </div>
          <h3 className="text-lg font-bold text-gray-100">Original Practice Synthesizer</h3>
          <p className="text-xs text-gray-400 leading-relaxed">
            Generates novel, statistically equivalent practice questions (MCQ, Numerical, Integer, Assertion-Reason) with rubrics and vector cosine similarity scoring.
          </p>
        </div>
      </section>

      {/* Navigation Modules Quick Access Cards */}
      <section className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4">
        {[
          { title: 'Student Revision Module', desc: 'Mock score tracking & personalized 7-day study plan.', href: '/student', icon: UserCheck },
          { title: 'Explainability & SHAP', desc: 'SHAP / LIME attribution & historical evidence rationale.', href: '/explainability', icon: CheckCircle2 },
          { title: 'Admin Control Panel', desc: 'User RBAC, paper uploads, & MLflow registry.', href: '/admin', icon: ShieldCheck },
          { title: 'Analytics & Heatmaps', desc: 'Topic probability curves & correlation matrices.', href: '/analytics', icon: Activity },
        ].map((mod, idx) => {
          const Icon = mod.icon;
          return (
            <Link
              key={idx}
              href={mod.href}
              className="p-5 rounded-2xl bg-gray-900/40 hover:bg-gray-900/80 border border-gray-800 hover:border-indigo-500/40 transition-all duration-200 space-y-2 block group shadow-lg"
            >
              <Icon className="w-5 h-5 text-indigo-400 group-hover:text-sky-400 transition-colors" />
              <h4 className="font-bold text-sm text-gray-200 group-hover:text-white">{mod.title}</h4>
              <p className="text-xs text-gray-400">{mod.desc}</p>
            </Link>
          );
        })}
      </section>
    </main>
  );
}
