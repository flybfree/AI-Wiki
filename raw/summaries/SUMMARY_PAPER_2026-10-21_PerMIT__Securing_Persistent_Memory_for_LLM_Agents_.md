---
title: PerMIT: Securing Persistent Memory for LLM Agents via Machine-Checked Integrity Theorems and Scalable Community Trust
url: http://arxiv.org/abs/2610.28987v1
type: paper-summary
date: 2026-10-21
source_paper: 2026-10-20_23-31-06Z_PerMIT_SecuringPersistentMemoryforLLMAgentsviaMach.md
generated_at: 2026-10-21 20:53
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
PerMIT introduces a memory architecture for LLM agents that provides provable integrity guarantees against injection and poisoning attacks on persistent memory, under an explicit trust assumption that only user-typed inputs and gate-confirmed values are trusted. The paper formalizes two integrity theorems machine-checked in Lean 4, demonstrating that environment-derived memory can only influence agent behavior through a single auditable gate decision, and shows zero observed attack success on the Trojan Hippo benchmark. Additionally, PerMIT enables a community trust mechanism where accumulated endorsements across users reduce per-user verification effort while lowering risks of promoting poisoned knowledge or evicting benign knowledge as communities scale.

## Key Takeaways
- PerMIT mediates all untrusted environment-derived values through a finite memory interface, proving two integrity theorems in Lean 4 that guarantee environment-derived memory reaches a sensitive action only if confirmed at a gate, and influences agent behavior only through what the gate displays. This reduces every attack in the threat model to a single auditable decision verifiable by a human, an LLM verifier, or both.
- On the Trojan Hippo benchmark, PerMIT records zero observed attack success when using self-verification and lightweight verifiers, demonstrating that the formal guarantees translate into practical defense against memory poisoning and injection attacks that currently plague persistent memory systems for agents.
- The community trust mechanism allows endorsements to accumulate across users, with sufficiently endorsed items becoming community-confirmed without further verification. The authors prove and corroborate in simulation a co-scaling property: as the community grows, the risks of promoting poison and wrongly evicting benign knowledge fall while per-user verification effort does not rise. On τ²-bench, communities of up to 90 autonomous agents build shared knowledge bases with no direct memory injection promoted, and the resulting knowledge significantly improves new agents on held-out tasks.

## Context
Persistent memory has emerged as a critical capability for LLM agents, enabling multi-turn planning, tool use, and knowledge accumulation across sessions. However, this same capability creates a largely undefended attack surface where adversarial content injected into memory can poison agent behavior or corrupt shared knowledge bases. Existing defenses rely on heuristic filtering without formal guarantees, and the risk of contamination severely limits the ability of agents to safely share memory with one another. PerMIT addresses this gap by combining formal verification with practical community-based trust, bridging the divide between theoretical security guarantees and deployable agent systems.

## Implications
For practitioners building multi-agent systems, PerMIT offers a path toward safe self-improvement at test time, where agents can collectively build and share knowledge bases without fear of adversarial contamination, potentially enabling autonomous agent communities that improve over time without human intervention for every memory update. For the broader AI safety field, the use of machine-checked theorems in Lean 4 to verify memory integrity properties sets a precedent for applying formal methods to practical LLM agent architectures, moving beyond empirical benchmarks toward provable security guarantees. Industry deployments of agent systems in healthcare, finance, and legal domains could benefit from the auditable single-decision gate model, which simplifies compliance and oversight requirements while scaling verification effort sublinearly with community size.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.28987v1)
