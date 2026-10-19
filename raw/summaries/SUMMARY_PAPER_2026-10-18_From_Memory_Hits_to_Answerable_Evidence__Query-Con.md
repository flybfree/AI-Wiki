---
title: From Memory Hits to Answerable Evidence: Query-Conditioned Memory Compilation for Long-Term Agent Memory
url: http://arxiv.org/abs/2610.23313v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-16_11-15-29Z_FromMemoryHitstoAnswerableEvidence_Query_Condition.md
generated_at: 2026-10-18 20:46
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces MemCompile, a query-conditioned evidence compilation framework designed to improve long-term conversational agent memory by separating memory addressing from evidence presentation. Rather than passing raw retrieved units directly to a reader model, MemCompile compiles heterogeneous retrieval hits into stable, answer-ready contexts through a two-plane architecture. The framework achieves 80.52% Judge Accuracy on the LoCoMo benchmark and demonstrates generalization across additional long-term memory benchmarks such as LongMemEval-S.

## Key Takeaways
- MemCompile decouples memory addressing from evidence presentation by introducing a normalization boundary that resolves heterogeneous retrieval hits into stable SourcePacket identities, preventing the redundancy and incompleteness that arise when expanded retrieval units are passed directly to a reader. This architectural separation is the core innovation distinguishing MemCompile from existing structured-memory and adaptive-retrieval systems.
- The framework operates through two coordinated planes: the Address Plane uses compact source-linked descriptors and capacity-aware Cells to locate relevant support, while the Evidence Plane allocates a bounded evidence budget across complementary packets, admits limited additional support, and renders retained claims into an answer-ready context. This bounded-budget approach controls cost while maintaining answer quality.
- Empirically, MemCompile extends the quality-cost Pareto frontier to a higher-quality regime on LoCoMo (80.52% Judge Accuracy) and shows strong transfer to LongMemEval-S, suggesting that query-conditioned compilation is a generalizable strategy rather than a benchmark-specific optimization.

## Context
Long-term agent memory is a critical bottleneck for conversational AI systems that must recall and synthesize information dispersed across many turns and sessions. Current approaches increasingly rely on structured memory stores and adaptive retrieval pipelines, but they typically treat retrieval as the final step before generation, leaving the model to handle noisy, redundant, or incomplete context. This gap between retrieval and answerability has become a recognized weakness in agent architectures, and MemCompile addresses it by inserting a compilation stage that transforms raw memory hits into curated, query-aligned evidence packets.

## Implications
For practitioners building long-term conversational agents, MemCompile offers a modular compilation layer that can be integrated into existing memory pipelines to reduce context bloat and improve answer fidelity without proportionally increasing inference cost. The bounded evidence budget and SourcePacket normalization strategy provide a practical template for production systems where token budgets and latency constraints are hard requirements. For the broader research community, the demonstrated generalization across multiple benchmarks suggests that query-conditioned evidence compilation is a transferable design principle that could inform next-generation agent memory architectures beyond conversational settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.23313v1)
