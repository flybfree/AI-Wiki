---
title: Forget or Fine-tune? A Comparative Study of Machine Unlearning Strategies for Noisy Label Correction
url: http://arxiv.org/abs/2608.30046v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_21-16-29Z_ForgetorFine_tune_AComparativeStudyofMachineUnlear.md
generated_at: 2026-08-31 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates five machine unlearning strategies for correcting noisy labels in deep neural networks, comparing them on multiple datasets and noise types. It finds that the best strategy depends on whether noise is symmetric, asymmetric, instance‑dependent, or open‑set, with simple fine‑tuning being a strong baseline but random labeling and SalUn offering robust performance at low cost.

## Key Takeaways
- Simple fine‑tuning (FT) remains a strong baseline across most closed‑set noise scenarios, achieving high accuracy while keeping computational overhead modest. 
- Random labeling (RL) and SalUn are the most consistently robust methods and can approach retraining accuracy when noise is instance‑dependent, using far less training time than full retraining. 
- MUNBa shows advantages only under extreme symmetric noise, whereas open‑set noise makes retraining on a cleaned subset degrade accuracy, so approximating the retrained model is not suitable.

## Context
Machine unlearning offers an alternative to costly full retraining when datasets contain noisy labels, which are common in real‑world scenarios. Understanding which unlearning method works best for different noise structures helps practitioners maintain model performance without sacrificing compute resources.

## Implications
For industry and researchers, the study provides clear guidelines: use FT or RL/SalUn depending on whether noise is closed‑set or instance‑dependent, avoid retraining when open‑set noise is present, and leverage MUNBa only for symmetric noise. This can reduce training time by an order of magnitude while preserving accuracy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30046v1)
