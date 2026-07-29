import type { Metadata } from 'next';
import '../styles/globals.css';
import Navigation from '@/components/Navigation';
import InteractiveNeuralBackground from '@/components/InteractiveNeuralBackground';

export const metadata: Metadata = {
  title: 'Exam Oracle AI - Universal Examination Analytics & Practice Platform',
  description: 'AI & Statistical Examination Analysis & Practice Generation Engine for NEET, GATE, UPSC, CAT, GRE, SAT, JEE & Global Exams.',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="dark">
      <body className="font-sans antialiased bg-[#0C0F0E] text-slate-100 min-h-screen relative selection:bg-emerald-500 selection:text-white">
        <InteractiveNeuralBackground />
        <div className="relative z-10">
          <Navigation />
          {children}
        </div>
      </body>
    </html>
  );
}
