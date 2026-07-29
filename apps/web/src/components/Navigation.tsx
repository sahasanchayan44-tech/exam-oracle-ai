'use client';

import React from 'react';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import { BarChart2, BookOpen, Cpu, ShieldCheck, Sparkles, UserCheck } from 'lucide-react';

export default function Navigation() {
  const pathname = usePathname();

  const navItems = [
    { name: 'Dashboard', href: '/', icon: BarChart2 },
    { name: 'Analytics', href: '/analytics', icon: Cpu },
    { name: 'Generator', href: '/generator', icon: Sparkles },
    { name: 'Student Plan', href: '/student', icon: UserCheck },
    { name: 'Explainability', href: '/explainability', icon: BookOpen },
    { name: 'Admin Panel', href: '/admin', icon: ShieldCheck },
  ];

  return (
    <header className="sticky top-0 z-50 w-full border-b border-[#222E28] bg-[#0C0F0E]/90 backdrop-blur-xl shadow-lg">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 h-16 flex items-center justify-between">
        <Link href="/" className="flex items-center space-x-3 group">
          <div className="w-10 h-10 rounded-xl bg-gradient-to-tr from-emerald-600 to-amber-500 flex items-center justify-center text-white font-extrabold text-sm shadow-md shadow-emerald-500/20 group-hover:scale-105 transition-transform">
            EO
          </div>
          <div className="flex flex-col">
            <span className="text-lg font-extrabold text-white tracking-tight leading-none">
              Exam Oracle <span className="text-amber-400 font-semibold">AI</span>
            </span>
            <span className="text-[11px] text-emerald-400/90 font-medium tracking-wide">
              Emerald & Onyx Intelligence
            </span>
          </div>
        </Link>

        <nav className="flex items-center space-x-1 sm:space-x-2">
          {navItems.map((item) => {
            const Icon = item.icon;
            const isActive = pathname === item.href;
            return (
              <Link
                key={item.href}
                href={item.href}
                className={`flex items-center space-x-2 px-3.5 py-2 rounded-xl text-sm font-semibold transition-all duration-200 ${
                  isActive
                    ? 'bg-emerald-500/15 text-emerald-300 border border-emerald-500/30 shadow-inner'
                    : 'text-slate-300 hover:text-white hover:bg-[#141A17]'
                }`}
              >
                <Icon className="w-4 h-4" />
                <span className="hidden md:inline">{item.name}</span>
              </Link>
            );
          })}
        </nav>
      </div>
    </header>
  );
}
