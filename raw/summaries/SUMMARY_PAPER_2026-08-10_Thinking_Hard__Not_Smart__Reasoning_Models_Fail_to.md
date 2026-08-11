---
title: Thinking Hard, Not Smart: Reasoning Models Fail to Ration Test-Time Compute Across Questions
url: http://arxiv.org/abs/2608.07968v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_07-04-28Z_ThinkingHard_NotSmart_ReasoningModelsFailtoRationT.md
generated_at: 2026-08-10 22:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how reasoning language models allocate a shared token budget across multiple test questions when the overall inference cost is limited. The authors introduce an exam‑style evaluation where models must distribute compute among questions of varying difficulty and point values to maximize total score, revealing that current models allocate resources inefficiently.

## Key Takeaways
- Models treat each question sequentially, front‑loading effort on early items regardless of difficulty or value, which reduces overall performance when a shared budget is imposed.  
- Greedy sequential solvers ignore the strategic trade‑off between point value and computational cost, leading to suboptimal total scores across multi‑question exams.  
- Explicit planning prompts spread compute more evenly but still fail to produce value‑ or difficulty‑aware prioritization, indicating a deeper limitation in budget allocation.

## Context
The paper addresses a gap in AI evaluation that focuses on per‑question performance while ignoring the cumulative resource constraints faced by real‑world reasoning tasks. As models become capable of handling complex multi‑step problems, understanding how they manage shared compute becomes essential for realistic benchmarking and model deployment.

## Implications
For researchers, this work calls for new evaluation protocols that capture end‑to‑end cost management rather than isolated question scores. Practitioners should consider budget‑aware training objectives to improve models’ ability to allocate inference resources efficiently in production settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07968v1)
