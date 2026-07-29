import React from 'react';

export default function HomePage() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-12">
      <header className="w-full max-w-6xl flex justify-between items-center pb-8 border-b border-gray-800">
        <div className="flex items-center space-x-3">
          <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-indigo-600 to-sky-400 flex items-center justify-center font-bold text-xl shadow-lg shadow-indigo-500/20">
            EO
          </div>
          <span className="text-2xl font-extrabold tracking-tight bg-clip-text text-transparent bg-gradient-to-r from-white via-gray-200 to-gray-400">
            Exam Oracle AI
          </span>
        </div>
        <span className="px-3 py-1 text-xs font-semibold rounded-full bg-indigo-500/10 text-indigo-400 border border-indigo-500/30">
          Enterprise v1.0 Architecture Ready
        </span>
      </header>

      {/* Non-predictive Disclaimer Alert Banner */}
      <div className="w-full max-w-6xl my-8 p-4 rounded-xl bg-amber-500/10 border border-amber-500/30 text-amber-300 flex items-start space-x-4 shadow-xl">
        <div className="text-2xl">⚠️</div>
        <div>
          <h4 className="font-bold text-amber-200 text-sm tracking-wide uppercase">
            Scientific & Ethical Non-Predictive Disclaimer
          </h4>
          <p className="text-xs text-amber-300/90 mt-1 leading-relaxed">
            Exam Oracle AI uses Bayesian probability distributions, natural language processing, and stochastic frequency analysis on historical exam sample data.
            <strong> It does NOT predict exact future exam papers or questions.</strong> All outputs are probability estimates accompanied by confidence bounds and empirical reasoning.
          </p>
        </div>
      </div>

      <div className="w-full max-w-6xl grid grid-cols-1 md:grid-cols-3 gap-6 my-6">
        <div className="p-6 rounded-2xl bg-gray-900/60 border border-gray-800 backdrop-blur-md">
          <h3 className="text-lg font-semibold text-gray-200 mb-2">📊 Bayesian Topic Estimator</h3>
          <p className="text-sm text-gray-400">
            Kernel Density Estimation & Dirichlet distributions to model topic weights over multi-year sample periods.
          </p>
        </div>
        <div className="p-6 rounded-2xl bg-gray-900/60 border border-gray-800 backdrop-blur-md">
          <h3 className="text-lg font-semibold text-gray-200 mb-2">🧠 NLP Bloom's Taxonomy Classifier</h3>
          <p className="text-sm text-gray-400">
            Deep syntactic & semantic vector analysis mapping cognitive complexity across previous examination items.
          </p>
        </div>
        <div className="p-6 rounded-2xl bg-gray-900/60 border border-gray-800 backdrop-blur-md">
          <h3 className="text-lg font-semibold text-gray-200 mb-2">⚡ Practice Question Synthesizer</h3>
          <p className="text-sm text-gray-400">
            Generates original, statistically equivalent practice questions with rubric solutions and cosine similarity scoring.
          </p>
        </div>
      </div>

      <footer className="w-full max-w-6xl pt-8 border-t border-gray-800 text-center text-xs text-gray-500">
        © 2026 Exam Oracle AI Enterprise Architecture. Built with Next.js, NestJS, FastAPI, Qdrant, PostgreSQL, MinIO & RabbitMQ.
      </footer>
    </main>
  );
}
