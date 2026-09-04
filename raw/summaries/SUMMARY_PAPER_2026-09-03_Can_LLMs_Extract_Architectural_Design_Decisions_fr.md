---
title: Can LLMs Extract Architectural Design Decisions from Source Code Commits? - A Preliminary Exploratory Study
url: http://arxiv.org/abs/2609.03721v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-03_11-54-27Z_CanLLMsExtractArchitecturalDesignDecisionsfromSour.md
generated_at: 2026-09-03 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary  
This paper explores whether large language models can uncover architectural design decisions hidden in source‑code commit messages. Using four LLMs with zeroshot and fewshot prompts on thirty documented ADDs, the authors report BERT‑F1 scores above 0.81 for all models, with fewshot prompting raising Gemini’s score to 0.847. The results show that while LLMs can generate plausible ADDs, their outputs are often overly verbose, implementation‑centric, and miss the underlying rationale.

## Key Takeaways  
- All tested LLMs achieve a BERT‑F1 above 0.81, indicating strong alignment with the reference ADDs despite the task’s implicit nature.  
- Fewshot prompting improves Gemini’s performance, raising its BERT‑F1 from 0.828 to 0.847, suggesting that providing examples guides the model toward more accurate design explanations.  
- The generated ADDs frequently become excessively long and focus on implementation details rather than the strategic reasoning behind the architectural choice.

## Context  
Understanding Architectural Design Decisions is central to Architectural Knowledge Management, yet such knowledge is rarely captured in explicit documentation. Large language models have demonstrated impressive code comprehension abilities, opening a pathway for automated extraction of hidden design rationale from commit histories.

## Implications  
These findings suggest that architecture‑aware LLMs could automate the capture and preservation of ADDs, supporting better system evolution tracking and reducing reliance on manual review. Practitioners may leverage this research to build systems that surface design intentions directly from source code repositories.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03721v1)
