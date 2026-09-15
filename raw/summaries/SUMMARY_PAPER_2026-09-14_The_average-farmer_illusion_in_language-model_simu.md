---
title: The average-farmer illusion in language-model simulations of agricultural decisions
url: http://arxiv.org/abs/2609.15038v1
type: paper-summary
date: 2026-09-14
source_paper: 2026-09-14_04-54-51Z_Theaverage_farmerillusioninlanguage_modelsimulatio.md
generated_at: 2026-09-14 22:22
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
This paper investigates the reliability of using large language models as synthetic agents in agricultural decision-making simulations. By evaluating Claude, Codex, and Kimi against real-world farmer data from China and four African nations, the authors demonstrate that while LLMs can replicate population-level averages and adoption rates, they consistently fail to capture individual-level behavioral variation and policy-relevant extremes. The study introduces the "average-farmer illusion," highlighting that distributional similarity alone is insufficient for validating synthetic populations, and proposes a structured validation framework alongside modular prompts to improve experimental transparency.

## Key Takeaways
- LLM configurations can reproduce observed population means and adoption rates, yet their individual-level predictions remain weak, with decisions heavily clustering around typical values while missing critical policy-relevant extremes.
- A simple statistical generator trained only on marginal distributions outperformed every tested language-model configuration in achieving distributional similarity, underscoring the limitations of LLMs in capturing complex behavioral heterogeneity.
- Prompt modifications yield conditional rather than universal improvements, with performance varying significantly across models, outcomes, populations, and validation targets, necessitating a claim-matched validation framework and aud

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.15038v1)
