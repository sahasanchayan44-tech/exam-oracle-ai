'use client';

import React, { useState } from 'react';
import DisclaimerBanner from '@/components/DisclaimerBanner';
import { Activity, Database, FileText, Server, ShieldCheck, Users } from 'lucide-react';

export default function AdminPage() {
  const [activeTab, setActiveTab] = useState('users');

  const users = [
    { id: '1', name: 'Dr. Robert Vance', email: 'vance@university.edu', role: 'PROFESSOR', status: 'Active' },
    { id: '2', name: 'Sarah Jenkins', email: 'sarah@student.org', role: 'STUDENT', status: 'Active' },
    { id: '3', name: 'Audit Team', email: 'audit@oracle.ai', role: 'ANALYST', status: 'Active' },
  ];

  const mlModels = [
    { name: 'BayesianKDE_v1.4', version: 'v1.4.2', accuracy: '94.2%', status: 'Production Registry' },
    { name: 'XGBoost_Topic_Classifier', version: 'v2.1.0', accuracy: '91.8%', status: 'Staging' },
    { name: 'SentenceTransformer_MPNet', version: 'v1.0.0', accuracy: '768-d Vector', status: 'Production Registry' },
  ];

  return (
    <main className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 space-y-8">
      <div className="pb-6 border-b border-gray-800">
        <h1 className="text-3xl font-extrabold tracking-tight text-white flex items-center gap-3">
          <ShieldCheck className="w-8 h-8 text-sky-400" />
          Admin & MLOps Control Center
        </h1>
        <p className="text-sm text-gray-400 mt-1">
          RBAC User Management, Paper Uploads, MLflow Model Registry, Experiment Tracking, & Container Health Monitoring.
        </p>
      </div>

      <DisclaimerBanner />

      {/* Tabs */}
      <div className="flex space-x-2 border-b border-gray-800 pb-2 text-xs font-semibold">
        {[
          { id: 'users', label: 'User RBAC Management', icon: Users },
          { id: 'models', label: 'MLflow Model Registry', icon: Database },
          { id: 'papers', label: 'Paper Ingestion', icon: FileText },
          { id: 'system', label: 'System & Container Health', icon: Server },
        ].map((t) => {
          const Icon = t.icon;
          return (
            <button
              key={t.id}
              onClick={() => setActiveTab(t.id)}
              className={`flex items-center space-x-2 px-4 py-2 rounded-xl transition-all ${
                activeTab === t.id
                  ? 'bg-indigo-600/20 text-indigo-400 border border-indigo-500/30'
                  : 'text-gray-400 hover:bg-gray-800'
              }`}
            >
              <Icon className="w-4 h-4" />
              <span>{t.label}</span>
            </button>
          );
        })}
      </div>

      {/* Users Tab */}
      {activeTab === 'users' && (
        <div className="p-6 rounded-2xl bg-gray-900/60 border border-gray-800 space-y-4 shadow-xl text-xs">
          <h3 className="text-lg font-bold text-gray-200">Registered Users & Role-Based Access Control</h3>
          <div className="overflow-x-auto">
            <table className="w-full text-left">
              <thead>
                <tr className="border-b border-gray-800 text-gray-400 font-bold uppercase">
                  <th className="py-2">User Name</th>
                  <th className="py-2">Email</th>
                  <th className="py-2">RBAC Role</th>
                  <th className="py-2">Status</th>
                </tr>
              </thead>
              <tbody className="divide-y divide-gray-800">
                {users.map((u) => (
                  <tr key={u.id} className="text-gray-300">
                    <td className="py-3 font-semibold text-white">{u.name}</td>
                    <td className="py-3">{u.email}</td>
                    <td className="py-3 font-bold text-indigo-400">{u.role}</td>
                    <td className="py-3 text-emerald-400 font-semibold">{u.status}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      )}

      {/* Models Tab */}
      {activeTab === 'models' && (
        <div className="p-6 rounded-2xl bg-gray-900/60 border border-gray-800 space-y-4 shadow-xl text-xs">
          <h3 className="text-lg font-bold text-gray-200">MLflow Model Registry & Experiment Tracking</h3>
          <div className="space-y-3">
            {mlModels.map((m, idx) => (
              <div key={idx} className="p-4 rounded-xl bg-gray-800/40 border border-gray-700/40 flex justify-between items-center">
                <div>
                  <span className="font-bold text-gray-200 text-sm block">{m.name}</span>
                  <span className="text-gray-500">Version: {m.version}</span>
                </div>
                <div className="text-right">
                  <span className="px-3 py-1 rounded-full bg-emerald-500/10 text-emerald-400 font-bold border border-emerald-500/30 block mb-1">
                    {m.status}
                  </span>
                  <span className="text-gray-400 text-[11px]">Validation Metric: {m.accuracy}</span>
                </div>
              </div>
            ))}
          </div>
        </div>
      )}

      {/* System Health Tab */}
      {activeTab === 'system' && (
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 text-xs">
          <div className="p-6 rounded-2xl bg-gray-900/60 border border-gray-800 space-y-2">
            <span className="text-gray-400 font-semibold block">PostgreSQL 16 DB</span>
            <span className="text-emerald-400 font-bold text-lg block">HEALTHY</span>
            <span className="text-gray-500">Connections: 12 / 20</span>
          </div>
          <div className="p-6 rounded-2xl bg-gray-900/60 border border-gray-800 space-y-2">
            <span className="text-gray-400 font-semibold block">Qdrant Vector DB</span>
            <span className="text-emerald-400 font-bold text-lg block">HEALTHY</span>
            <span className="text-gray-500">Indexed Points: 14,250</span>
          </div>
          <div className="p-6 rounded-2xl bg-gray-900/60 border border-gray-800 space-y-2">
            <span className="text-gray-400 font-semibold block">RabbitMQ Broker</span>
            <span className="text-emerald-400 font-bold text-lg block">HEALTHY</span>
            <span className="text-gray-500">Queued Messages: 0</span>
          </div>
        </div>
      )}
    </main>
  );
}
