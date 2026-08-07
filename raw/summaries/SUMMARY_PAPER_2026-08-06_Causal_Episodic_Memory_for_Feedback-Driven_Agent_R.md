---
title: Causal Episodic Memory for Feedback-Driven Agent Repair
url: http://arxiv.org/abs/2608.05906v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_11-34-03Z_CausalEpisodicMemoryforFeedback_DrivenAgentRepair.md
generated_at: 2026-08-06 20:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MERIT, a training-free agent that stores oracle-verified corrections to improve later Text-to-SQL tasks without updating model parameters. Experiments on Spider and BIRD show modest gains in execution accuracy compared to stateless repair methods. The results suggest that causal episodic memory can be beneficial under certain conditions.

## Key Takeaways
- MERIT maintains an online dual-polarity memory of oracle-verified corrections and unsuccessful directions, allowing retrieval only from earlier finalized episodes during oracle-assisted benchmark feedback.
- A deterministic classifier assigns a coarse failure type that conditions a hybrid lexical-dense retriever before the frozen model generates each revision, enabling dataset-specific memory usage.
- Ablations indicate negative memory contributes modestly while schema-local experience provides the most consistent benefit, and broader memory representations are less reliable than typed episodic recall.

## Context
Causal episodic memory aims to let agents reuse successful outcomes across queries without retraining, addressing inefficiencies in iterative repair. This work extends that idea to Text-to-SQL agents where each query is independent yet benefits from prior fixes, highlighting a niche where memory can reduce parameter overhead.

## Implications
For practitioners, MERIT offers a lightweight way to boost SQL accuracy on benchmark datasets by leveraging stored corrections rather than costly model updates. The findings guide future research toward targeted memory strategies that respect query independence and schema constraints in large language models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05906v1)
