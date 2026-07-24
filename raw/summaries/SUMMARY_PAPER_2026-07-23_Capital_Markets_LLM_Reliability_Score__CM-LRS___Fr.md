---
title: Capital Markets LLM Reliability Score (CM-LRS): From Plausible to Bankable
url: http://arxiv.org/abs/2607.21340v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_14-10-58Z_CapitalMarketsLLMReliabilityScore_CM_LRS__FromPlau.md
generated_at: 2026-07-23 22:59
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CM-LRS, a Capital Markets LLM Reliability Score that evaluates language model outputs at the workflow level across seven dimensions such as factual accuracy and evidence traceability. It scores four frontier models against four judges, finding closed‑source models outperform open‑weights baselines by up to 0.22 points on average. The study shows retrieval and synthesis are the weakest areas while decision usefulness exhibits high inter‑judge variance.

## Key Takeaways
- Frontier closed‑source models cluster within 0.22 points on four‑judge averaged CM-LRS, scoring higher than Llama 3.3 70B which ranks last.
- The performance gap is concentrated in retrieval (2.23) and synthesis (2.15), with extraction showing minimal difference (0.84).
- Decision Usefulness shows the widest cross‑model dispersion of any dimension, reaching 4.0 points on issuer profiling.

## Context
This work addresses a critical gap in AI reliability for regulated financial workflows where surface fluency is insufficient; it provides a quantitative rubric that mirrors reviewer expectations rather than benchmark question‑answer accuracy. The methodology bridges open‑domain QA and finance‑specific benchmarks by focusing on the actual documents practitioners defend.

## Implications
CM-LRS offers regulators and firms a concrete metric to assess LLM usefulness in capital markets, moving trust from speculative drafts to bankable outputs. Its emphasis on workflow completeness and auditability can shape model selection policies and drive more responsible AI deployment in finance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21340v1)
