---
title: LexAgentHallu: A Hierarchical Benchmark for Profiling Hallucinations in Legal Agents
url: http://arxiv.org/abs/2609.09754v1
type: paper-summary
date: 2026-09-09
source_paper: 2026-09-09_05-52-53Z_LexAgentHallu_AHierarchicalBenchmarkforProfilingHa.md
generated_at: 2026-09-09 20:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
LexAgentHallu is a new benchmark that evaluates legal language models for hallucinations across multi-step agentic workflows, moving beyond single‑turn QA to capture how errors propagate along an execution path. The study finds that hallucination subclasses cluster rather than scatter, revealing systematic patterns tied to specific legal tasks and categories.

## Key Takeaways
- LexAgentHallu provides a dual‑layer taxonomy of 7 high‑level and 27 fine‑grained hallucination subclasses, enabling detailed diagnosis of substantive errors versus procedural failures.  
- The benchmark’s fine‑grained metrics quantify both the extent and localization of hallucinations within an agent’s trajectory.  
- Evaluation across 18 agents uncovers a “right‑answer‑wrong‑reason” effect, showing that agents often produce correct answers with incorrect justifications.

## Context
Legal AI tools increasingly rely on autonomous reasoning to assist practitioners, yet current benchmarks ignore the nuanced ways hallucinations manifest over multiple steps. LexAgentHallu fills this gap by creating a legally grounded dataset that mirrors real‑world agent workflows and diagnostic needs.

## Implications
Practitioners can now assess model reliability beyond pass/fail outcomes, informing design choices to mitigate cascading errors. The benchmark’s clustering insights guide the development of specialized safeguards for high‑risk legal tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.09754v1)
