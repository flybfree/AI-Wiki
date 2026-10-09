---
title: Has LLM Screening Performance Stalled in Software Engineering Systematic Reviews?
url: http://arxiv.org/abs/2610.10633v1
type: paper-summary
date: 2026-10-08
source_paper: 2026-10-07_13-25-54Z_HasLLMScreeningPerformanceStalledinSoftwareEnginee.md
generated_at: 2026-10-08 23:38
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether the screening performance of large language models in software engineering systematic reviews has plateaued by benchmarking eight newer LLMs against seven previously evaluated models using the SESR-Eval dataset and a newly power-sampled smaller variant called SESR-Eval-Mini. The authors find that newer, more expensive LLMs deliver only marginal gains in screening accuracy, with average Matthews Correlation Coefficient rising from 0.347 to 0.365, suggesting that LLMs remain insufficiently reliable to replace human screeners in systematic review workflows.

## Key Takeaways
- Newer LLMs show only a marginal improvement over older models in screening performance (average MCC increased from 0.347 to 0.365), and the variation in performance across different secondary studies is substantially larger than the variation across different LLMs, indicating that the inherent difficulty of the screening task dominates over model capability.
- LLMs demonstrate high inter-model agreement on screening decisions (mean Gwet's AC1 of 0.830), yet certain inclusion and exclusion criteria produce notably larger disagreement than others, and deriving overall screening decisions from criterion-level judgments only slightly degrades performance, suggesting that structured criterion-by-criterion evaluation is a viable but not transformative approach.
- Refining inclusion and exclusion criteria produced only modest improvements in recall and decision-making ease for some models, while the practical advantages of adopting newer, more costly LLMs appear very limited, leading the authors to conclude that agent-based approaches, prompt engineering, and further criteria refinement represent the most promising future research directions rather than simply upgrading model versions.

## Context
Systematic reviews are a cornerstone of evidence-based software engineering research, and their screening phase—where thousands of candidate papers are triaged against inclusion and exclusion criteria—is labor-intensive and time-consuming. Prior studies have proposed LLMs as a partial automation solution, but because the LLM landscape evolves rapidly, earlier performance benchmarks risk becoming outdated. This paper addresses that gap by re-evaluating screening performance with current-generation models, providing the community with an updated and more rigorous assessment of where LLM-assisted screening actually stands relative to human performance.

## Implications
For software engineering researchers and practitioners who rely on systematic reviews, this work signals that simply adopting the latest commercial LLM will not meaningfully reduce screening workload or improve accuracy, and that investment in agent-based architectures, carefully engineered prompts, and iteratively refined screening criteria is likely to yield greater practical gains than model upgrades alone. For the broader AI research community, the finding that task difficulty across studies outweighs model differences underscores the need for benchmark design that isolates genuine model capability from dataset-specific challenges, and it cautions against overclaiming automation readiness in high-stakes academic workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.10633v1)
