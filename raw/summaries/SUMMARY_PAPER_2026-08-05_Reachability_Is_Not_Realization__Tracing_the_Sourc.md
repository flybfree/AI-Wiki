---
title: Reachability Is Not Realization: Tracing the Sources of LLM Benchmark Gains
url: http://arxiv.org/abs/2608.03219v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_06-52-27Z_ReachabilityIsNotRealization_TracingtheSourcesofLL.md
generated_at: 2026-08-05 01:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper argues that benchmark gains do not always reflect genuine improvements in large language model capability, as they can arise from different mechanisms such as expanding reachable answers versus increasing realized performance. It introduces a question‑level audit that distinguishes between “reachability,” where an answer is found within a fixed inference budget, and “realization,” where the default deployment actually outputs the correct answer. Experiments show that structured search can boost reachability without improving deployed scores.

## Key Takeaways
- A model may already be able to produce correct answers; the benchmark gain could simply reflect reaching those pre‑existing answers rather than a true capability increase.  
- Random routing matches or exceeds structured search in all 43 model and task settings, yet answer‑blind procedures lose most of this benefit because they require access to the correct answer.  
- Silencing one identified MLP block repairs 68 to 92 percent of a predefined failure set, indicating that reachable answers sometimes fail due to specific architectural weaknesses.

## Context
In AI research, benchmark scores are often used as proxies for model capability, but this paper highlights the risk of conflating superficial score improvements with actual functional gains. The distinction between reachability and realization matters because it reveals whether a model’s performance is limited by inference constraints or by genuine knowledge gaps.

## Implications
For practitioners and industry stakeholders, reporting both realized performance and reachable ceiling under matched evaluation conditions is essential to avoid misleading claims of capability expansion. This clarification can guide more honest benchmarking practices and better resource allocation in LLM development.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03219v1)
