# 🔮 Exam Oracle AI (Enterprise Monorepo)

> **Enterprise AI, NLP & Statistical Examination Analysis & Practice Set Generation Engine**

[![CI/CD Pipeline](https://github.com/exam-oracle/exam-oracle-ai/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/exam-oracle/exam-oracle-ai/actions)
[![Security Scan](https://github.com/exam-oracle/exam-oracle-ai/actions/workflows/security-scan.yml/badge.svg)](https://github.com/exam-oracle/exam-oracle-ai/actions)
[![Architecture](https://img.shields.io/badge/Architecture-Microservices-indigo.svg)](./ARCHITECTURAL_BLUEPRINT.md)
[![License](https://img.shields.io/badge/License-UNLICENSED-red.svg)]()

---

## ⚠️ SCIENTIFIC & ETHICAL DISCLAIMER

**Exam Oracle AI NEVER claims to predict exact future examination papers or questions.** 
Exam papers are stochastic outcomes influenced by human test creators, changing curricula, and institutional policies.

This platform operates strictly as a **probabilistic analysis engine**:
- It computes historical topic occurrence probabilities $P(\text{Topic } T)$ using Bayesian Kernel Density Estimation (KDE) and Markov chain transition models.
- Every probability output is bounded by statistical confidence intervals ($95\% \text{ CI}$) and explainable attribution metrics.
- Synthesized practice questions are generated for pedagogical review and revision, with cosine similarity scoring relative to historical question vectors.

---

## 🏗️ Technology Stack

| Domain | Technology | Purpose |
| :--- | :--- | :--- |
| **Frontend** | Next.js 14 (App Router), React 18, TypeScript, TailwindCSS, ShadCN UI | Responsive Dashboard, Visualizations & Interactive Practice Tests |
| **Data Viz** | D3.js & Plotly.js | Interactive Probability Density Curves, Topic Radar Charts, Knowledge Graphs |
| **API Gateway** | NestJS (TypeScript) | API Gateway, OAuth2/JWT Authentication, RBAC Guard, Rate Limiting, OpenAPI |
| **AI / NLP Microservice** | Python 3.11, FastAPI, PyTorch, Transformers, SciPy, Statsmodels | NLP Feature Extraction, Bayesian Probability Distributions, Question Synthesis |
| **Relational Database** | PostgreSQL 16 | User Accounts, Exam Metadata, RBAC, Statistical Runs, Audit Logging |
| **In-Memory Cache** | Redis 7 | Distributed Caching, Session Store, Rate-Limiting Tokens |
| **Vector Database** | Qdrant | Semantic Question Embeddings, Clustering, Cosine Similarity Scoring |
| **Object Storage** | MinIO (S3-Compatible) | Exam PDF Storage, Extracted Diagrams, Rendered Assets |
| **Message Queue** | RabbitMQ | Asynchronous Event-Driven Microservice Pipeline |
| **Containerization** | Docker, Docker Compose, Kubernetes | Production Deployment & Orchestration |

---

## 📂 Repository Hierarchy

```
exam-oracle-ai/
├── .github/                     # GitHub Actions Workflows & PR Templates
│   ├── workflows/
│   │   ├── ci-cd.yml
│   │   ├── security-scan.yml
│   │   └── docker-build.yml
│   └── PULL_REQUEST_TEMPLATE.md
├── apps/                        # Microservices & Web Applications
│   ├── web/                     # Next.js 14 Frontend App
│   ├── api-gateway/             # NestJS API Gateway Service
│   └── ai-engine/               # Python FastAPI AI / NLP Service
├── packages/                    # Shared Libraries & Modules
│   ├── shared-types/            # Shared TypeScript Interfaces & DTOs
│   ├── config-eslint/           # Shared ESLint Rules
│   ├── config-typescript/       # Shared TSConfig Rules
│   └── ui-components/           # Shared Component Library
├── infrastructure/              # Infrastructure as Code
│   ├── docker/                  # Init SQL, RabbitMQ Topology, Qdrant Config
│   │   ├── postgres/init.sql
│   │   ├── rabbitmq/definitions.json
│   │   └── qdrant/config.yaml
│   └── k8s/                     # Kubernetes Base & Overlay Manifests
│       └── base/deployment.yaml
├── docker-compose.yml           # Production Orchestration
├── docker-compose.override.yml  # Development Override
├── .env.example                 # Environment Variable Template
├── pnpm-workspace.yaml          # Monorepo Workspace Definitions
├── turbo.json                   # Turborepo Build Cache Config
└── README.md
```

---

## 🚀 Quickstart Development Setup

### 1. Prerequisites
- **Node.js**: `v20.0.0+`
- **pnpm**: `v8.15.4+`
- **Python**: `v3.11+`
- **Docker & Docker Compose**

### 2. Clone & Environment Setup
```bash
cp .env.example .env
```

### 3. Launch Full Local Infrastructure Stack via Docker
```bash
docker-compose up -d
```

This starts:
- **PostgreSQL**: `localhost:5432`
- **Redis**: `localhost:6379`
- **Qdrant Vector DB**: `localhost:6333` (UI: `http://localhost:6333/dashboard`)
- **MinIO S3**: `localhost:9000` (Console: `http://localhost:9001`)
- **RabbitMQ**: `localhost:5672` (Management UI: `http://localhost:15672`)
- **Python AI Engine**: `localhost:8000` (Swagger: `http://localhost:8000/api/v1/docs`)
- **NestJS API Gateway**: `localhost:4000` (Swagger: `http://localhost:4000/api/v1/docs`)
- **Next.js Web**: `localhost:3000`

---

## 🧪 Testing & Verification

```bash
# Run all tests across monorepo via Turborepo
pnpm run test

# Run API Gateway NestJS unit tests
pnpm --filter api-gateway test

# Run AI Engine Python PyTest suite
cd apps/ai-engine && pytest
```

---

## 🔐 Security & RBAC Matrix

| Role | Paper Ingestion | View Statistics | Run Probability Models | Generate Practice Sets | System Admin |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **SUPER_ADMIN** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **PROFESSOR** | ✅ | ✅ | ✅ | ✅ | ❌ |
| **ANALYST** | ❌ | ✅ | ✅ | ❌ | ❌ |
| **STUDENT** | ❌ | ✅ | ❌ | ✅ | ❌ |

---

## 📄 License & Governance

Proprietary Enterprise Software. All rights reserved.
