---
title: DVBench: Benchmarking MLLMs for Understanding Dynamic Charts and Narratives in Data Videos
url: http://arxiv.org/abs/2608.29711v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_10-38-29Z_DVBench_BenchmarkingMLLMsforUnderstandingDynamicCh.md
generated_at: 2026-08-31 21:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces DVBench, a benchmark designed to evaluate multimodal language models on data videos that combine dynamic charts with structured narratives. The study demonstrates that Gemini‑3.1‑Pro leads overall performance while Kimi‑k2.5 excels among open‑source models, and it uncovers two unexpected phenomena: non‑linear scaling of open‑source model size and the independence between narrative proficiency and visual understanding.

## Key Takeaways
- The benchmark includes 300 real‑world data videos and 1,000 human‑verified QA pairs gathered via a semi‑automated pipeline, providing a comprehensive test set for temporal structured visual information.  
- Gemini‑3.1‑Pro achieves the highest aggregate score across all dimensions, indicating that closed‑source models still hold an advantage despite open‑source progress.  
- Open‑source model performance does not increase strictly with parameter count and narrative proficiency does not guarantee strong visual comprehension.

## Context
Current MLLM evaluations often treat chart understanding and video comprehension as isolated tasks, missing the interaction between them in real data videos. This gap limits reliable assessments of models that must integrate both modalities for tasks like automated reporting or decision support.

## Implications
For researchers, DVBench offers a standardized framework to probe how models handle evolving visual narratives, guiding more holistic model design. For industry practitioners, it highlights opportunities to improve open‑source MLLMs without solely chasing larger parameter counts and underscores the need for better integration of narrative and visual cues in deployed systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29711v1)
