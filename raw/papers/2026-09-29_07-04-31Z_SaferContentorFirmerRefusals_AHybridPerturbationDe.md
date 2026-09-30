---
title: Safer Content or Firmer Refusals? A Hybrid Perturbation Defense for Alignment under Harmful Fine-tuning
published: 2026-09-29T07:04:31Z
authors: Muhammad Zeeshan Akram, Mufid Kamel Marican, Anvesh Reddy Yenugu, Ali Zain Kaimkhani, Minghong Fang
url: http://arxiv.org/abs/2609.36862v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Safer Content or Firmer Refusals? A Hybrid Perturbation Defense for Alignment under Harmful Fine-tuning

## Abstract
Fine-tuning-as-a-service lets users adapt a safety-aligned language model to their own data, but it also creates a harmful fine-tuning attack surface: a small amount of harmful data mixed into an otherwise benign fine-tuning set can degrade the model's alignment. Two recent alignment-stage defenses address this problem at different levels of the model. Vaccine improves the robustness of hidden embeddings to the representation shifts induced by harmful fine-tuning, whereas Booster simulates harmful weight updates and attenuates their effect during alignment. We investigate whether these mechanisms are complementary and propose VaccineBooster, a single alignment procedure that combines embedding perturbation and weight-level gradient attenuation within each training step. On Llama-2-7B aligned with BeaverTails and then attacked through poisoned fine-tuning, VaccineBooster achieves the lowest OpenAI moderation score among the compared defenses, 0.315, while a Booster-Only variant retains the highest post-attack refusal rate, 50%. Together with ablations over the embedding-perturbation and gradient-attenuation strengths, these results indicate a trade-off: embedding perturbation primarily reduces flagged harmful content, whereas gradient attenuation primarily preserves explicit refusal behavior. Because our evaluation uses ten prompts and a single unseeded run per configuration, we report this trade-off as an observed pattern rather than a statistically resolved effect. These results provide practical guidance for prioritizing content safety or refusal retention when aligned models are exposed to untrusted fine-tuning.

## Metadata
- **Published**: 2026-09-29T07:04:31Z
- **Authors**: Muhammad Zeeshan Akram, Mufid Kamel Marican, Anvesh Reddy Yenugu, Ali Zain Kaimkhani, Minghong Fang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.36862v1)