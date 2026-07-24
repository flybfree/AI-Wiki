---
title: REFACT: Adaptive Fact Restatement for Compact and Faithful Chain-of-Thought Reasoning
url: http://arxiv.org/abs/2607.20833v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_01-41-17Z_REFACT_AdaptiveFactRestatementforCompactandFaithfu.md
generated_at: 2026-07-23 23:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper REFACT introduces an adaptive fact-restatement citation framework that helps large language models ground reasoning steps with appropriate source facts while keeping the trace compact and faithful. Experiments on LongBench LV-Eval ConFiQA demonstrate improved long-context QA performance, higher counterfactual faithfulness, and a significant reduction in token usage. The method balances evidence density with conciseness by restating only necessary facts.

## Key Takeaways
- REFACT trains models to decide when each reasoning step requires contextual grounding and at what granularity source facts should be restated, preventing unsupported inference or unnecessary copying.
- The two-stage SFT-to-RL pipeline uses a citation‑utility reward that ensures cited facts are well‑formed, traceable, and sufficient for the final answer.
- Results show REFACT reduces token consumption while preserving more answer‑bearing evidence with fewer restated facts, yielding denser reasoning traces.

## Context
Long‑form reasoning is essential for complex LLM tasks but often suffers from drifting traces that lack reliable grounding. Current citation strategies either append references after generation or embed retrieval inside the trace without guaranteeing factual sufficiency. REFACT addresses this gap by integrating fact restatement directly into the reasoning pipeline, offering a more systematic approach to evidence management.

## Implications
For practitioners, REFACT provides a practical tool to produce concise yet trustworthy outputs, reducing hallucinations and token waste in production systems. The framework’s emphasis on answer‑sufficient citations could become standard practice as LLM applications demand higher reliability and efficiency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20833v1)
