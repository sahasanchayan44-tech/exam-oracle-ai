import type { Metadata } from 'next';
import '../styles/globals.css';

export const metadata: Metadata = {
  title: 'Exam Oracle AI - Enterprise Statistical Exam Analysis & Practice Platform',
  description: 'AI & NLP powered probability distribution estimation and original practice question synthesizer.',
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en" className="dark">
      <body className="font-sans antialiased">{children}</body>
    </html>
  );
}
