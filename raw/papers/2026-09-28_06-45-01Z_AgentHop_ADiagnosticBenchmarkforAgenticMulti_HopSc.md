---
title: AgentHop: A Diagnostic Benchmark for Agentic Multi-Hop Scientific Question Answering
published: 2026-09-28T06:45:01Z
authors: Chanhee Park, Jeongho Yoon, Sungbin Han, Hyeonseok Moon, Heuiseok Lim
url: http://arxiv.org/abs/2609.34428v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AgentHop: A Diagnostic Benchmark for Agentic Multi-Hop Scientific Question Answering

## Abstract
Agentic tasks require a large language model to interact with the world, navigating information and gathering evidence across multiple steps with restricted resources. Due to this complexity, agentic task failures arise from various sources, and pinpointing these failure causes is essential to diagnose and improve agentic systems. Existing benchmarks, however, tend to focus on a single leaderboard score, leaving the underlying failure modes opaque. To fill this gap, we introduce AgentHop, a diagnostic benchmark of 1,011 multiple-choice questions paired with a controlled seven-tool sandbox under fixed token, turn, and tool-call constraints. AgentHop reveals model vulnerabilities by dissecting a single accuracy score along four axes of agent operation: retrieval, synthesis, tool-call, and resource management. Across 19 models, we find that behavior clusters by model family, with tool-call signatures revealing distinct family fingerprints: GPT models commit early, Anthropic and GLM checkpoints verify before committing, DeepSeek and Kimi over-search, and Gemini-3 Pro stays balanced. Decomposed axes further expose within-family structure: Claude Opus 4.6 and Sonnet 4.6 land within one accuracy point yet diverge on retrieval-versus-synthesis emphasis, with Opus retrieving more and Sonnet synthesizing better. We release the full benchmark set and the harness to support diagnostic agent benchmarking.

## Metadata
- **Published**: 2026-09-28T06:45:01Z
- **Authors**: Chanhee Park, Jeongho Yoon, Sungbin Han, Hyeonseok Moon, Heuiseok Lim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34428v1)