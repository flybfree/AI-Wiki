---
title: Averaging Bias: Human Faithfulness Annotations are not Locally Faithful
url: http://arxiv.org/abs/2608.00205v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-07-31_18-39-28Z_AveragingBias_HumanFaithfulnessAnnotationsarenotLo.md
generated_at: 2026-08-03 20:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether human‑rated faithfulness labels on summarization benchmarks follow the strict conjunctive rule that every sentence must be supported by the source. It finds that global human labels correlate more closely with an average of per‑sentence LLM judgments than with the rule, indicating a systematic bias.

## Key Takeaways
- Human annotators often label a summary as faithful even when it contains unsupported sentences because they focus on the overall impression rather than checking each sentence individually.  
- The global label aligns better with an average of per‑sentence LLM judgments than with the strict conjunctive rule that requires all sentences to be supported.  
- Manual reviews reveal many summaries marked faithful contain genuine local factual errors, confirming the presence of averaging bias.

## Context
This work addresses a longstanding issue in evaluating model outputs: most faithfulness benchmarks rely on single global annotations rather than detailed sentence‑level verification. The mismatch between human judgment and strict logical consistency has been overlooked, limiting trustworthy benchmark design.

## Implications
For practitioners designing evaluation protocols, the paper calls for structured annotation schemes that capture per‑sentence support to avoid misleading performance metrics. This shift is essential for ensuring that AI systems are truly faithful and reliable in real‑world applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00205v1)
