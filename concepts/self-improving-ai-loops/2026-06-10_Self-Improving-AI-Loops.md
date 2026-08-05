---
title: Self-Improving AI Loops
created: 2026-06-10
tags: [agent-architecture, feedback-loops, harness-engineering, open-source, self-hosted]
---

## Summary

Placeholder summary — please add a concise summary.


# Self-Improving AI Loops



**Source**: [Original Article](http://localhost:11434)
A paradigm shift in AI engineering where agents improve over time through automated feedback loops rather than static prompting. The core insight: **the harness matters more than the model**.

## Semantic links
- [[concepts/self-improving-ai-loops/2026-06-10_Lesson1_ParadigmShift.md|Lesson 1 — The Paradigm Shift: From Prompting to Loops]] — 1 title term overlap, shared tags: feedbackloops, harnessengineering, 6 topic terms overlap
- [[concepts/self-improving-ai-loops/2026-06-10_Lesson2_InferenceLayer.md|Lesson 2 — Inference Layer: Self-Hosted LLMs]] — 1 title term overlap, shared tags: selfhosted, 6 topic terms overlap
- [[concepts/ornith-1-0.md|Ornith 1.0: Self-Scaffolding Agentic Coding Models]] — 1 title term overlap, shared tags: opensource, 2 topic terms overlap

## Core Concepts

### The Hierarchy of Leverage

1. **Prompt engineering** — How you phrase the request. Models are now good enough to infer intent from vague prompts.
2. **Context engineering** — Giving the model the right information (docs, files, schemas). Gets you further than prompts alone.
3. **Feedback loop engineering** — Building tools so agents verify their own work. Separates working code from getting lucky.
4. **Harness engineering** — The frame around everything: what the agent can call, what it can touch, when it stops. (Birgitta Böckeler's "Agent = Model + Harness")

## LangChain anchor articles

Use these as the clean external references for this lesson set:

- [The Anatomy of an Agent Harness](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness) — the best plain-language definition of harness scope: prompts, tools, skills, filesystem state, sandboxes, orchestration, memory, compaction, hooks, and verification.
- [The Art of Loop Engineering](https://www.langchain.com/blog/the-art-of-loop-engineering) — the clearest breakdown of stacked loops: agent loop, verification loop, event-driven loop, and hill-climbing loop.
- [[2026-07-26_LangChain_Harness_and_Loop_Engineering_References]] — compact source note tying the two articles into one lesson-friendly reference.

These are especially useful when the lesson needs a tighter model-vs-harness distinction or a more explicit stack of loops.

### Three Failure Modes of Prompt-First Approaches

- **Context rot** — Long conversations become a junk drawer. Failed attempts pile up until the sliding window drops the original spec. Model slides into a "dumb zone" where it hallucinates and forgets goals.
- **Premature exit** — Agents declare victory too early. Anthropic research: agents look around, see progress, and call it done. Standard ReAct loops inherit this.
- **Single-pass fragility** — One prompt, one context, one shot. When it fails, the failure is chaotic.

### Ralph Loops

Named after Ralph Wiggum (tries the same thing over and over until it works). The simplest self-improving pattern:

```bash
while true; do
  claude "implement the next ticket from doc/tickets using TDD"
done
```

**Mechanics:** Wipes conversation each iteration (fresh context, no confirmation bias). Uses filesystem + git as persistent memory. Objective verification (tests passing, lint clean) is the only exit gate.

**Why it works:** Models are stochastic. First iteration produces good but flawed output. Second pass spots what was missed. Third handles cleanup. Geoffrey Huntley delivered an MVP quoted at $50,000 for 297 tokens using a single Ralph loop — 170x cost reduction.

OpenAI's Codex shipped **1M lines of code across 1,500 PRs with zero human-written code** using a "Ralph Wiggum Loop."

### Inner Loop / Outer Loop

From Mozilla AI's `cq` and Daniel Demmel's analysis:

- **Inner loop** (seconds): Agent runs code → reads result → feeds it back → iterates. Tighten this loop and output quality improves immediately.
- **Outer loop** (hours/days): At session end, distill lessons → write into shared knowledge (skills, CLAUDE.md, knowledge base) → next session starts with that knowledge pre-loaded.

> "Today's distilled lesson becomes tomorrow's guide — feedforward, in harness terms — so the outer loop quietly improves the inner one over time."

### Self-Learning Spectrum

Raj Shukla (Symphony AI CTO) described three levels:

1. **In-context learning** — Dynamic few-shot examples selected by feedback. Simplest loop.
2. **Intelligent memory layer** — Growing middle ground. Feedback updates memory stored in file systems/markdown. Memory pulled in at right context.
3. **True RL** — Reinforcement learning with verifiable feedback (RLVR, GRPO). Hardest to implement, only "true" learning.

## Implementation: Self-Hosted LLMs & Open Source Stack

### Inference Layer

| Tool | Best For | Self-Hosted | Notes |
|------|----------|-------------|-------|
| **Ollama** | Quick local dev, 7B-70B models | Yes | `ollama run llama3.3`, simple API, growing model library |
| **vLLM** | High-throughput serving, production | Yes | PagedAttention, tensor parallelism, OpenAI-compatible API |
| **LM Studio** | Desktop dev, GUI-first | Yes | Local-first, supports GGUF models, built-in API server |
| **TGI** (Hugging Face) | Production inference, quantized models | Yes | Docker-based, handles batching, supports speculative decoding |

**Model recommendations for agentic work (2026):**
- **Llama 4 Scout** (256B) — Best reasoning, needs 8x A100/H100 or cloud
- **Gemma 4** (12B-27B) — Strong coding, fits on single GPU with quantization
- **Mistral Small 3.1** (24B) — Balanced reasoning/cost, good for local
- **Phi-4 Mini** (3.8B) — Edge/local, surprisingly capable for tool calling
- **DeepSeek-R1 distilled** — Open reasoning model, strong for Ralph loops

### Abstraction Layer

**LiteLLM** — Proxy server that normalizes 100+ LLM providers (including local) to OpenAI-compatible API. Swap models without changing code:

```yaml
# litellm config.yaml
model_list:
  - model_name: my-agent
    litellm_params:
      model: ollama/llama3.3
      api_base: http://localhost:11434
```

Switch from local Ollama to cloud Claude without changing agent code.

### Agent Frameworks

| Framework | Pattern | Self-Hosted | Best For |
|-----------|---------|-------------|----------|
| **SmolAgents** (Hugging Face) | CodeAgent writes actions as code | Yes | Minimalist agents, ~1K lines of code, first-class code execution |
| **LangGraph** | State machine graphs with cycles | Yes | Self-correcting loops, `langgraph-reflection` package for judge nodes |
| **OpenDevin/OpenHands** | Autonomous coding agent | Yes | Full-stack dev, browser automation, test-driven execution |
| **Aider** | CLI pair programming | Yes | Local LLM coding, skill-based self-improvement, git-aware context |
| **Agno** (formerly Phoenix) | Multi-agent orchestration | Yes | Complex workflows, memory layers, tool integration |

### Knowledge & Memory

| Tool | Type | Self-Hosted | Notes |
|------|------|-------------|-------|
| **Mozilla cq** | Shared knowledge units | Yes (self-host) | "Stack Overflow for agents." Agents persist, share, query collective knowledge. Three tiers: local, org, global commons. |
| **Qdrant** | Vector database | Yes | Rust-based, high-performance, Python/Go/TS clients |
| **Chroma** | Embedding database | Yes | Lightweight, Python-first, good for prototyping |
| **LanceDB** | Embedded vector DB | Yes | No server needed, SQL-like queries, integrates with PyArrow |
| **SQLite** | Structured knowledge | Yes | Mozilla cq KUs can live locally in SQLite |

### Evaluation & Verification

| Tool | Purpose | Self-Hosted | Notes |
|------|---------|-------------|-------|
| **DeepEval** | LLM-as-judge evaluation | Yes | Python testing workflow, custom metrics, hallucination detection |
| **Arize Phoenix** | Observability + evals | Yes | Track output distributions, semantic drift, latency, error rates |
| **Promptfoo** | CI pipeline evals | Yes | Run evals in CI, security checks, prompt versioning, A/B testing |
| **MLflow** | Experiment tracking | Yes | Track prompt experiments, model versions, evaluation scores |

### Orchestration & UI

| Tool | Type | Self-Hosted | Notes |
|------|------|-------------|-------|
| **Dify** | Visual workflow builder | Yes | RAG pipelines, multi-agent orchestration, MCP support, team collaboration |
| **Flowise** | LangChain-native visual flows | Yes | Drag-and-drop agent workflows, open-source alternative to LangChain UI |
| **Open WebUI** | Chat interface | Yes | Modern chat UI for local LLMs, extensible, works with any OpenAI-compatible backend |

## Sample DIY Architecture

```
┌─────────────────────────────────────────────────────┐
│                    Orchestration                     │
│               Dify / Flowise / LangGraph             │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│                  Agent Layer                         │
│         SmolAgents / OpenDevin / Aider              │
│         (CodeAgent writes actions as code)           │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│              Abstraction Layer                       │
│                   LiteLLM Proxy                      │
│         (Swap ollama/llama3.3 ↔ cloud Claude)        │
└──────────────────────┬──────────────────────────────┘
                       │
┌──────────────────────▼──────────────────────────────┐
│                 Inference Layer                      │
│    Ollama (dev) / vLLM (prod) / LM Studio (desktop)  │
│         Llama 4 Scout / Gemma 4 / Mistral S3.1       │
└─────────────────────────────────────────────────────┘

Feedback Loop:
┌─────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
│ DeepEval │───▶│ Arize    │───▶│ Mozilla  │───▶│ Skill/   │
│ (eval)   │    │ Phoenix  │    │ cq       │    │ CLAUDE.  │
│          │◀───│ (drift)  │    │ (memory) │    │ md)      │
└─────────┘    └──────────┘    └──────────┘    └──────────┘
```

### Minimal Ralph Loop with Local Models

```bash
#!/bin/bash
# Ralph loop using Aider + local LLM via LiteLLM
export LITELLM_PROXY=http://localhost:4000/v1

while true; do
  # Aider reads doc/tickets/001.md, implements it, runs tests
  aider --model openai/my-agent \
    --file doc/tickets/$(ls doc/tickets/ | head -1) \
    --yes-always \
    --no-auto-commit \
    --commit-message "implement ticket"
  
  # Verify: if tests pass, move to next ticket
  if pytest tests/ -q; then
    mv doc/tickets/$(ls doc/tickets/ | head -1) doc/tickets/done/
    echo "✓ Ticket done"
  else
    echo "✗ Tests failed, retrying..."
    sleep 5
  fi
done
```

## Pitfalls & Risks

- **Drift is the #1 failure mode** — Analysis of 4M+ production agent calls shows drift (compliance, length, semantic, regression) is most common. Track output distributions, not just error rates.
- **Feedback-to-node routing** — Task-level feedback ("this is wrong") is useless without node-level routing. Tracing "this invoice amount is wrong" back to resume parser vs scoring model vs formatting layer is hard.
- **Cold start** — Agents need production feedback to improve but need to be good enough to generate useful feedback. Staged deployment on narrow scope → expand as accuracy improves.
- **Model version brittleness** — Enterprise systems break when foundation model APIs update. Every model upgrade requires prompt changes and investigation. Local models reduce this risk.
- **Verification gap** — "Does it compile?" ≠ "Does it actually work?" Need browser automation, database queries, log access, OTel traces, real API keys — not mocks.
- **Safety** — Ralph loops are safe when repo-contained with toolchain as judge. Dangerous with irreversible side effects (e.g., terraform destroy). Review every plan manually.

## Related Concepts

- [[Feedback Loop Engineering]]
- [[Harness Engineering]]
- [[Context Engineering]]
- [[Ralph Loops]]
- [[Self-Learning AI Agents]]
- [[Open-Source LLM Stack]]
- [[Mozilla cq]]
- [[Agent Washing]]
