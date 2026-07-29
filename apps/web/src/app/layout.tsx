import type { Metadata } from 'next';
import '../styles/globals.css';
import Navigation from '@/components/Navigation';

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
      <body className="font-sans antialiased bg-[#0B0F19] text-gray-100 min-h-screen">
        <Navigation />
        {children}
      </body>
    </html>
  );
}
