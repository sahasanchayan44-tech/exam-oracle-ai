'use client';

import React from 'react';
import { AlertTriangle } from 'lucide-react';

export default function DisclaimerBanner() {
  return (
    <div className="w-full max-w-7xl mx-auto my-4 p-4 rounded-2xl bg-gradient-to-r from-amber-500/10 via-amber-500/5 to-transparent border border-amber-500/30 text-amber-300 flex items-start space-x-3 shadow-xl backdrop-blur-md">
      <AlertTriangle className="w-5 h-5 text-amber-400 mt-0.5 flex-shrink-0" />
      <div className="text-xs leading-relaxed">
        <span className="font-bold text-amber-200 uppercase tracking-wide mr-2">
          Non-Predictive Disclaimer:
        </span>
        Exam Oracle AI provides probabilistic estimations based on historical sample distributions.
        <strong> It DOES NOT predict exact future exam papers or questions.</strong> All probability outputs include 95% confidence intervals and historical attribution evidence.
      </div>
    </div>
  );
}
