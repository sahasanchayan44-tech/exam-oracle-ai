'use client';

import React from 'react';
import { ShieldAlert } from 'lucide-react';

export default function DisclaimerBanner() {
  return (
    <div className="w-full max-w-7xl mx-auto px-5 py-3.5 rounded-2xl bg-[#141A17]/80 border border-[#222E28] text-slate-300 flex items-start sm:items-center justify-between text-xs sm:text-sm gap-3 shadow-md backdrop-blur-md">
      <div className="flex items-center space-x-3">
        <ShieldAlert className="w-5 h-5 text-amber-400 flex-shrink-0" />
        <span className="leading-relaxed">
          <strong className="text-white font-semibold mr-1">Probabilistic Model:</strong> Exam Oracle AI estimates topic occurrence distributions with 95% confidence intervals based on historical paper analysis. It does not predict exact future exam papers.
        </span>
      </div>
      <span className="px-2.5 py-1 rounded-full bg-amber-500/10 text-amber-400 font-semibold border border-amber-500/20 text-xs whitespace-nowrap hidden lg:inline-block">
        Calibrated ISO Model
      </span>
    </div>
  );
}
