'use client';

import React from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { BarChart2, BookOpen, Cpu, ShieldCheck, Sparkles, UserCheck } from 'lucide-react';

export default function Navigation() {
  const pathname = usePathname();

  const navItems = [
    { name: 'Dashboard', href: '/', icon: BarChart2 },
    { name: 'Analytics & Graphs', href: '/analytics', icon: Cpu },
    { name: 'Question Generator', href: '/generator', icon: Sparkles },
    { name: 'Student Module', href: '/student', icon: UserCheck },
    { name: 'Explainability & SHAP', href: '/explainability', icon: BookOpen },
    { name: 'Admin & MLOps', href: '/admin', icon: ShieldCheck },
  ];

  return (
    <nav className="w-full bg-[#0E1322] border-b border-gray-800 sticky top-0 z-50 shadow-xl backdrop-blur-md bg-opacity-90">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 flex items-center justify-between h-16">
        <div className="flex items-center space-x-3">
          <Link href="/" className="flex items-center space-x-2">
            <div className="w-9 h-9 rounded-xl bg-gradient-to-tr from-indigo-600 via-sky-500 to-indigo-400 flex items-center justify-center text-white font-extrabold text-lg shadow-lg shadow-indigo-500/25">
              EO
            </div>
            <span className="text-xl font-extrabold tracking-tight bg-clip-text text-transparent bg-gradient-to-r from-white via-gray-200 to-indigo-200">
              Exam Oracle AI
            </span>
          </Link>
          <span className="hidden md:inline-block px-2.5 py-0.5 text-[10px] font-bold rounded-full bg-indigo-500/10 text-indigo-400 border border-indigo-500/30 uppercase tracking-widest">
            Universal Exam Engine
          </span>
        </div>

        <div className="flex space-x-1 md:space-x-4">
          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = pathname === item.href;
            return (
              <Link
                key={item.href}
                href={item.href}
                className={`flex items-center space-x-2 px-3 py-2 rounded-xl text-xs font-semibold transition-all duration-200 ${
                  isActive
                    ? 'bg-indigo-600/20 text-indigo-400 border border-indigo-500/30 shadow-inner'
                    : 'text-gray-400 hover:text-gray-200 hover:bg-gray-800/50'
                }`}
              >
                <Icon className="w-4 h-4" />
                <span className="hidden lg:inline">{item.name}</span>
              </Link>
            );
          })}
        </div>
      </div>
    </nav>
  );
}
