---
title: Can you make models believe false facts in the prompt?
url: http://arxiv.org/abs/2611.23938v1
type: paper-summary
date: 2026-11-20
source_paper: 2026-11-18_06-26-12Z_Canyoumakemodelsbelievefalsefactsintheprompt.md
generated_at: 2026-11-20 21:59
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether a single fine-tuned model can be made to believe arbitrary false facts injected into its prompt via a <facts> tag, eliminating the need to train a separate model for each set of false beliefs. The authors explore prompt-conditioned Synthetic Document Finetuning (SDF), training one model on synthetic documents covering thousands of facts, and find that belief depth on unseen facts scales roughly log-linearly with the number of training facts. However, preliminary alignment audit experiments on small models showed negative results, and reinforcement learning techniques applied on top of prompt-conditioned SDF showed mixed outcomes, including a concerning tradeoff where training against a belief-depth metric made those evaluations less trustworthy.

## Key Takeaways
- Prompt-conditioned SDF enables a single model to believe any fact placed in a <facts> tag in the prompt, scaling belief depth log-linearly with the number of training facts. This makes it a cheap and promising avenue for large-scale alignment evaluations that require models to hold many different false beliefs simultaneously, removing the per-fact-set fine-tuning bottleneck of prior SDF approaches.
- Applying this technique to alignment audits on small models produced negative results because those small models already behaved as though they believed facts provided in regular honeypot system prompts, meaning the added <facts> tag provided no meaningful behavioral change and the technique's value was masked by baseline model behavior.
- Using reinforcement learning to reduce the rate at which models verbalize adherence to a false fact in the prompt, layered on top of prompt-conditioned SDF, generalized to held-out evaluations and nearly matched full SDF performance on some metrics. However, training directly against one of the authors' belief-depth metrics made it harder to trust those same evaluations, raising a methodological concern about metric gaming.

## Context
Synthetic Document Finetuning has emerged as a key tool in AI alignment research for constructing "model organisms" that hold specific false beliefs, enabling researchers to probe how models reason when their factual priors are deliberately corrupted. Prior SDF methods required training a distinct model for every new set of injected beliefs, creating a scalability bottleneck that limited the breadth of alignment evaluations. This paper addresses that bottleneck by proposing a single-model approach conditioned on prompt-injected facts, which is directly relevant to the growing need for scalable, reproducible alignment auditing pipelines across many model families and belief sets.

## Implications
For alignment researchers and safety practitioners, this work suggests a practical path toward large-scale belief-injection evaluations without the computational cost of training separate models per fact set, potentially enabling broader audits of model reasoning under counterfactual premises. However, the negative results on small models and the metric-trustworthiness tradeoff introduced by RL fine-tuning highlight that current evaluation tools may not yet reliably distinguish genuine belief from surface-level compliance, urging caution before deploying these techniques in high-stakes alignment audits. Practitioners building model organisms for safety evaluation should carefully validate that their belief-depth metrics remain independent of the training objective to avoid circular evaluation artifacts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.23938v1)
