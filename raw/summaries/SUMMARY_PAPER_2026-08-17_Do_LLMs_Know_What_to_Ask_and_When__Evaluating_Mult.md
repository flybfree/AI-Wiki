---
title: Do LLMs Know What to Ask and When? Evaluating Multi-Turn Information Seeking
url: http://arxiv.org/abs/2608.14808v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-14_18-23-32Z_DoLLMsKnowWhattoAskandWhen_EvaluatingMulti_TurnInf.md
generated_at: 2026-08-17 21:43
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how large language models handle underspecified user queries by prompting them to seek additional information in a multi‑turn dialogue. The authors formalize the problem as a constraint satisfaction task and evaluate 5,251 problems across multiple domains, showing that model performance deteriorates as missing variables increase.

## Key Takeaways
- Models often underestimate how many pieces of information are needed, especially in logical tasks where at k=2 they predict missing info four times more than it actually is.  
- They rarely identify the smallest set of queries sufficient to resolve a problem and only improve marginally when given the true k value.  
- Incorrect query ordering can lower final accuracy even if all required information is eventually gathered.

## Context
Current LLM evaluations focus on single‑turn answer generation, which does not capture the ability to iteratively request missing data. This gap limits understanding of how models manage incomplete user intent and hampers benchmarking of multi‑turn reasoning capabilities.

## Implications
Recognizing that information seeking is a distinct skill from answer generation could drive new evaluation metrics and design strategies for chatbots that must adaptively gather context, ultimately improving real‑world interaction quality.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14808v1)
