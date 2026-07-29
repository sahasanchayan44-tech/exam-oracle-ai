-- =============================================================================
-- EXAM ORACLE AI - ENTERPRISE POSTGRESQL DDL INITIALIZATION SCHEMA
-- =============================================================================

CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- -----------------------------------------------------------------------------
-- 1. USERS & RBAC AUTHENTICATION SCHEMA
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS roles (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    name VARCHAR(50) UNIQUE NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO roles (name, description) VALUES
('SUPER_ADMIN', 'Platform System Administrator with unrestricted access'),
('PROFESSOR', 'Academic Institution Administrator & Exam Creator'),
('STUDENT', 'Standard End-User for Exam Analytics & Practice Practice Sets'),
('ANALYST', 'Read-only Statistical Analytics Auditor')
ON CONFLICT (name) DO NOTHING;

CREATE TABLE IF NOT EXISTS users (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255),
    full_name VARCHAR(100) NOT NULL,
    avatar_url TEXT,
    provider VARCHAR(20) DEFAULT 'local', -- local, google, github
    provider_id VARCHAR(255),
    role_id UUID NOT NULL REFERENCES roles(id) ON DELETE RESTRICT,
    is_active BOOLEAN DEFAULT TRUE,
    is_verified BOOLEAN DEFAULT FALSE,
    last_login_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS permissions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    resource VARCHAR(100) NOT NULL, -- e.g., 'papers', 'analytics', 'questions'
    action VARCHAR(50) NOT NULL,     -- e.g., 'read', 'write', 'delete', 'execute'
    UNIQUE(resource, action)
);

CREATE TABLE IF NOT EXISTS role_permissions (
    role_id UUID REFERENCES roles(id) ON DELETE CASCADE,
    permission_id UUID REFERENCES permissions(id) ON DELETE CASCADE,
    PRIMARY KEY (role_id, permission_id)
);

-- -----------------------------------------------------------------------------
-- 2. ACADEMIC DOMAINS & EXAM PAPERS SCHEMA
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS subjects (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    code VARCHAR(50) UNIQUE NOT NULL, -- e.g. CS101, MATH301
    name VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS topics (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    subject_id UUID NOT NULL REFERENCES subjects(id) ON DELETE CASCADE,
    parent_id UUID REFERENCES topics(id) ON DELETE SET NULL,
    name VARCHAR(255) NOT NULL,
    code VARCHAR(50),
    description TEXT,
    weight_default NUMERIC(5,4) DEFAULT 1.0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS exam_papers (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    subject_id UUID NOT NULL REFERENCES subjects(id) ON DELETE RESTRICT,
    title VARCHAR(255) NOT NULL,
    year INT NOT NULL,
    term VARCHAR(50), -- Fall, Spring, Annual
    total_marks INT NOT NULL,
    duration_minutes INT,
    file_path TEXT NOT NULL, -- MinIO S3 object key
    file_hash VARCHAR(64) UNIQUE NOT NULL, -- SHA-256 integrity check
    processing_status VARCHAR(50) DEFAULT 'PENDING', -- PENDING, PARSING, EXTRACTED, PROCESSED, FAILED
    metadata JSONB DEFAULT '{}'::jsonb,
    uploaded_by UUID REFERENCES users(id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- 3. QUESTION BANK & NLP FEATURE EXTRACTS
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS raw_questions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    exam_paper_id UUID NOT NULL REFERENCES exam_papers(id) ON DELETE CASCADE,
    topic_id UUID REFERENCES topics(id) ON DELETE SET NULL,
    question_number INT NOT NULL,
    sub_question_label VARCHAR(10),
    content TEXT NOT NULL,
    marks INT NOT NULL,
    blooms_taxonomy_level VARCHAR(50), -- REMEMBER, UNDERSTAND, APPLY, ANALYZE, EVALUATE, CREATE
    difficulty_score NUMERIC(3,2), -- 0.00 to 1.00
    qdrant_vector_id VARCHAR(255), -- Reference to Qdrant vector embedding
    nlp_features JSONB DEFAULT '{}'::jsonb, -- keywords, syntactic complexity, entity types
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- 4. PROBABILISTIC MODELS & STATISTICAL ESTIMATIONS
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS probability_runs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    subject_id UUID NOT NULL REFERENCES subjects(id) ON DELETE CASCADE,
    algorithm_name VARCHAR(100) NOT NULL, -- e.g. BayesianKDE, MarkovTopicModel, DirichletPrior
    model_version VARCHAR(20) NOT NULL,
    confidence_interval_alpha NUMERIC(4,3) DEFAULT 0.950,
    parameters JSONB NOT NULL,
    executed_by UUID REFERENCES users(id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS topic_probability_estimates (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    run_id UUID NOT NULL REFERENCES probability_runs(id) ON DELETE CASCADE,
    topic_id UUID NOT NULL REFERENCES topics(id) ON DELETE CASCADE,
    estimated_probability NUMERIC(5,4) NOT NULL, -- Probability estimation P(Topic) [0.0 - 1.0]
    expected_marks_weight NUMERIC(5,2) NOT NULL,
    confidence_lower_bound NUMERIC(5,4) NOT NULL,
    confidence_upper_bound NUMERIC(5,4) NOT NULL,
    confidence_score NUMERIC(3,2) NOT NULL, -- Overall statistical confidence (0.00 - 1.00)
    statistical_explanation JSONB NOT NULL, -- Attribution, variance, historical frequency rationale
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- 5. SYNTHESIZED ORIGINAL PRACTICE QUESTIONS
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS practice_test_sets (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    subject_id UUID NOT NULL REFERENCES subjects(id) ON DELETE CASCADE,
    created_by UUID REFERENCES users(id) ON DELETE SET NULL,
    title VARCHAR(255) NOT NULL,
    target_marks INT NOT NULL,
    generation_seed VARCHAR(100),
    probability_run_id UUID REFERENCES probability_runs(id) ON DELETE SET NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS synthesized_questions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    practice_test_id UUID NOT NULL REFERENCES practice_test_sets(id) ON DELETE CASCADE,
    topic_id UUID NOT NULL REFERENCES topics(id) ON DELETE RESTRICT,
    reference_question_id UUID REFERENCES raw_questions(id) ON DELETE SET NULL,
    question_text TEXT NOT NULL,
    suggested_solution TEXT,
    rubric JSONB,
    marks INT NOT NULL,
    similarity_score_to_original NUMERIC(4,3),
    confidence_score NUMERIC(3,2) NOT NULL,
    qdrant_vector_id VARCHAR(255),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- -----------------------------------------------------------------------------
-- 6. SYSTEM AUDIT & SECURITY LOGS
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS audit_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    user_id UUID REFERENCES users(id) ON DELETE SET NULL,
    action VARCHAR(100) NOT NULL,
    resource VARCHAR(100) NOT NULL,
    ip_address VARCHAR(45),
    user_agent TEXT,
    payload JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Indexes for performance optimization
CREATE INDEX idx_exam_papers_subject ON exam_papers(subject_id);
CREATE INDEX idx_raw_questions_paper ON raw_questions(exam_paper_id);
CREATE INDEX idx_raw_questions_topic ON raw_questions(topic_id);
CREATE INDEX idx_estimates_run ON topic_probability_estimates(run_id);
CREATE INDEX idx_synthesized_questions_test ON synthesized_questions(practice_test_id);
CREATE INDEX idx_audit_user ON audit_logs(user_id);
