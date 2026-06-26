---
title: When are likely answers right? On Sequence Probability and Correctness in LLMs
url: http://arxiv.org/abs/2606.27359v1
type: paper-summary
date: 2026-06-25
source_paper: 2026-06-25_17-58-02Z_Whenarelikelyanswersright_OnSequenceProbabilityand.md
generated_at: 2026-06-25 22:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how sequence probability, defined as the conditional likelihood of a continuation given a prompt, correlates with answer correctness across various decoding strategies and hyperparameter settings. The authors find that within a fixed dataset higher sequence probability often predicts correct answers, yet this predictive power does not persist when decoding methods or parameters are altered.

## Key Takeaways
- Higher sequence probability is frequently linked to correct responses for specific prompt‑answer pairs in a given benchmark.  
- Changing hyperparameters or switching decoding methods to increase sequence probability rarely leads to improved accuracy on the same prompts.  
- Sequence probability does not remain consistent across repeated generations of the identical prompt, indicating it is not a reliable metric for self‑consistency.

## Context
Understanding the disconnect between model confidence and factual correctness is crucial as language models become more widely used in automated reasoning tasks. This work contributes to the broader effort to align decoding practices with real‑world performance by empirically mapping where probability estimates are trustworthy.

## Implications
For practitioners, the findings suggest that relying solely on high sequence probabilities can mislead optimization efforts; instead, they should focus on methods that maintain consistency across repeated answers and validate outputs against external criteria.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.27359v1)
