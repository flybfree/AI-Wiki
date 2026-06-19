---
title: "2026 06 05 17 59 42Z Howreliablearellmswhenitcomestoplayingdice Summary"
date: 2026-06-05
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-06-05_17-59-42Z_HowreliableareLLMswhenitcomestoplayingdice.md


**Source**: [Original Paper](https://example.com/placeholder)
Saved: 2026-06-07 22:01
Source: 2026-06-05_17-59-42Z_HowreliableareLLMswhenitcomestoplayingdice.md
Model: None

---


## Summary  
This paper investigates how large language models (LLMs) perform on discrete probability tasks, specifically dice‑rolling exercises designed to test both straightforward and counterintuitive reasoning. The authors benchmark eight state‑of‑the‑art LLMs with and without chain‑of‑thought prompting, revealing that while the models excel at standard problems, their probabilistic intuition falters dramatically on more subtle cases. Moreover, they demonstrate that small changes in phrasing or hidden cues can cause large drops in accuracy, indicating a reliance on surface patterns rather than genuine probability understanding. The study concludes that current LLMs are not yet reliable probabilistic reasoners.

## Key Contributions  
- [Finding 1] Models achieve an average accuracy of 0.96 on standard dice‑rolling problems but only 0.59 on counterintuitive ones, highlighting a sharp drop in performance when reasoning becomes non‑obvious.  
- [Finding 2] Performance drops by over 20% when canonical formulations are replaced with disguised variants, showing sensitivity to wording rather than true probabilistic knowledge.  
- [Finding 3] Embedding misleading suggestions into the prompt reduces accuracy up to 34%, and no model is immune to such manipulation.

## Methodology  
The authors constructed two datasets: a set of standard dice‑rolling exercises and a set of counterintuitive variants that require heuristic reasoning. They evaluated eight leading LLMs, each run twice—once with chain‑of‑thought prompting and once without—to capture the effect of structured reasoning steps. Accuracy was measured as the proportion of correct outcomes across all trials.

## Results  
The baseline accuracy for standard problems averaged 0.96 (i.e., 96 % correct). Counterintuitive tasks suffered a significant decline to an average of 0.59. When prompts were altered to hide or mislead the model, token‑level bias caused additional declines: over 20 % loss for reformulated problems and up to 34 % loss when deceptive cues were embedded. No model achieved >80 % accuracy on counterintuitive tasks even with chain‑of‑thought prompting.

## Significance  
These findings reveal a critical gap between LLMs’ apparent competence in advanced mathematics and their genuine probabilistic reasoning abilities, especially for simple stochastic events like dice rolls. The results caution against overestimating model reliability when subtle or deceptive prompts are used, underscoring the need for more robust evaluation of reasoning under adversarial conditions.

## Related Concepts  
- Large language models (LLMs)  
- Chain‑of‑thought prompting  
- Heuristic reasoning  
- Probabilistic inference  
- Token bias / formulation sensitivity  
- Embedding manipulation in prompts

[[How reliable are LLMs when it comes to playing dice?]]