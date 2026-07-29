'use client';

import React from 'react';
import { Info } from 'lucide-react';

export default function DisclaimerBanner() {
  return (
    <div className="w-full max-w-7xl mx-auto px-4 py-2.5 rounded-xl bg-slate-900/50 border border-slate-800/80 text-slate-400 flex items-center justify-between text-xs gap-3">
      <div className="flex items-center space-x-2">
        <Info className="w-4 h-4 text-indigo-400 flex-shrink-0" />
        <span>
          <strong className="text-slate-300 font-semibold">Probabilistic Model:</strong> Estimates topic distributions with 95% confidence bounds. Does not predict exact exam papers.
        </span>
      </div>
      <span className="text-[10px] font-mono text-slate-500 uppercase tracking-widest hidden md:inline-block">ISO-Calibrated</span>
    </div>
  );
}
