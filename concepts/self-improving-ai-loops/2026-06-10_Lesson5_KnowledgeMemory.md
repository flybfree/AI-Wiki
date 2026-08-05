---
title: "Lesson 5 — Knowledge & Memory: The Outer Loop"
created: 2026-06-10
module: Self Improving AI Loops
lesson: 5
tags: [knowledge-management, memory, mozilla-cq, vector-dbs, cold-start]
---

## Summary

Placeholder summary — please add a concise summary.


# Lesson 5: Knowledge & Memory — The Outer Loop



**Source**: [Original Article](http://localhost:8080/knowledge?query=)

## Semantic links
- [[concepts/self-improving-ai-loops/2026-06-10_Lesson4_AgentFrameworks.md|Lesson 4 — Agent Frameworks: The Loop Engine]] — 3 title terms overlap, 8 topic terms overlap, same area: home
- [[concepts/self-improving-ai-loops/2026-06-10_Lesson6_Evaluation.md|Lesson 6 — Evaluation & Verification: The Judge Node]] — 2 title terms overlap, 7 topic terms overlap, same area: home
- [[concepts/self-improving-ai-loops/2026-06-10_Lesson1_ParadigmShift.md|Lesson 1 — The Paradigm Shift: From Prompting to Loops]] — 2 title terms overlap, 7 topic terms overlap, same area: home

## Core Idea

The **outer loop** turns one session's hard-won lesson into something every future session starts with. It separates solving from learning: agents store discoveries as structured Knowledge Units and query the store before retrying a failure, so they stop rediscovering the same dead ends.

## Inner Loop vs. Outer Loop

| | Inner Loop | Outer Loop |
|---|-----------|-----------|
| **Time scale** | Seconds | Hours / days |
| **What it does** | Agent runs code → reads result → iterates | Distills lessons → writes to shared knowledge → next session starts smarter |
| **Where knowledge lives** | Context window (ephemeral) | File system / database (persistent) |
| **Goal** | Fix the current task | Improve all future tasks |

> "Today's distilled lesson becomes tomorrow's guide — feedforward, in harness terms — so the outer loop quietly improves the inner one over time."

## Mozilla cq: Shared Knowledge Units

**Definition:** An open standard for shared agent learning. Agents persist, share, and query collective knowledge so they stop rediscovering the same failures independently.

**Three tiers:**
1. **Local** — Agent's own knowledge store (SQLite)
2. **Organizational** — Team/organization-wide knowledge
3. **Global commons** — Community knowledge (via cq.exchange)

**How it works:**
- Agents store discoveries as structured **Knowledge Units** (KUs): undocumented API quirks, workarounds, fixes
- Before tackling unfamiliar work, agent queries the store
- If another agent has already learned something, your agent knows before writing code
- When your agent discovers something novel, it proposes that knowledge back
- Low-confidence units gain trust through confirmations by other agents and humans

**Self-hosting:**
```bash
# Run your own cq server
docker run -p 8080:8080 mozilla/cq:latest

# Agent queries before retrying
curl http://localhost:8080/knowledge?query="stripe rate limit error body"
```

**Why it matters:** Peter Wilson (Mozilla AI) describes it as "Stack Overflow for agents." It addresses repeated issues that waste agent time rediscovering the same dead ends.

## Vector Databases for Self-Hosted

### Qdrant
**Best for:** High-performance production, Rust-based
**Self-hosted:** Yes, Docker

```bash
docker run -p 6333:6333 qdrant/qdrant
```

**Pros:**
- Rust-based, extremely fast
- High-performance vector similarity search
- Python/Go/TypeScript clients
- Production-ready

**Cons:**
- More complex setup than Chroma
- Overkill for small projects

### Chroma
**Best for:** Prototyping, Python-first projects
**Self-hosted:** Yes, pip install

```bash
pip install chromadb
```

**Pros:**
- Python-first, simple API
- Lightweight, no server needed
- Good for prototyping
- Built-in embedding models

**Cons:**
- Not designed for high-concurrency production
- Limited scalability

### LanceDB
**Best for:** Embedded vector search, no server needed
**Self-hosted:** Yes, pip install

```bash
pip install lancedb
```

**Pros:**
- Embedded — no server, no Docker
- SQL-like queries
- Integrates with PyArrow
- Great for local-first agents

**Cons:**
- Smaller community than Qdrant/Chroma
- Less mature than the others

### SQLite for Structured Knowledge
Mozilla cq's Knowledge Units can live locally in SQLite. For structured data (not embeddings), SQLite is often better than vector DBs:

```python
import sqlite3

conn = sqlite3.connect("agent_knowledge.db")
conn.execute("""
  CREATE TABLE IF NOT EXISTS knowledge_units (
    id INTEGER PRIMARY KEY,
    topic TEXT,
    content TEXT,
    confidence REAL DEFAULT 0.0,
    confirmed_by INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
  )
""")
```

## The Cold Start Problem

**Definition:** Self-learning requires data. New agents have none. The agent needs production feedback to improve, but it needs to be to be good enough in production to generate useful feedback.

### Strategies:

1. **Pre-train on synthetic data** — Gets you to a baseline, but synthetic data has a ceiling. Real production environments have edge cases that synthetic data cannot anticipate.

2. **Staged deployment** — Start the agent on a narrow scope where existing data covers most cases, collect feedback on the edges, expand scope as accuracy improves.

3. **Human-in-the-loop bootstrapping** — Have a human provide initial feedback, then let the agent learn from that.

**Best approach:** Staged deployment. Start narrow, expand as accuracy improves. Requires infrastructure that supports dynamic scope boundaries and gradual rollout.

## Knowledge Architecture Pattern

```
┌─────────────────────────────────────┐
│         Agent Session               │
│                                     │
│  ┌───────────┐    ┌──────────────┐ │
│  │ Inner Loop│───▶│ Mozilla cq   │ │
│  │ (seconds) │    │ (query)      │ │
│  └───────────┘    └──────────────┘ │
│         │                           │
│  ┌───────────┐    ┌──────────────┐ │
│  │  Writes   │◀───│  Stores as   │ │
│  │ KUs       │    │ Knowledge    │ │
│  └───────────┘    └──────────────┘ │
└─────────────────────────────────────┘
         │
         ▼
┌─────────────────────────────────────┐
│    Next Session (starts with KUs)   │
│    Agent queries before retrying    │
│    "Has anyone seen this error?"    │
└─────────────────────────────────────┘
```

## Key Takeaway

The outer loop is where self-improvement actually happens. Without it, every session starts from scratch. Mozilla cq gives you a standard for shared knowledge. Start with SQLite for structured data, add a vector DB when you need semantic search. Solve the cold start with staged deployment.

## Related Concepts
- [[2026-06-10_Self-Improving-AI-Loops.md]]
- [[2026-07-26_LangChain_Harness_and_Loop_Engineering_References.md]]
- [[2026-06-10_Self-Improving-AI-Loops.md]]
- [[2026-06-10_Lesson1_ParadigmShift.md]]
