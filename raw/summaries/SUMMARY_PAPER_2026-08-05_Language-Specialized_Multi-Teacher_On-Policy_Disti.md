---
title: Language-Specialized Multi-Teacher On-Policy Distillation for Multilingual LLM-Based ASR
url: http://arxiv.org/abs/2608.03610v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_13-02-47Z_Language_SpecializedMulti_TeacherOn_PolicyDistilla.md
generated_at: 2026-08-05 01:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Language-Specialized Multi-Teacher On-Policy Distillation to improve multilingual ASR by separating language-specific teacher optimization from joint modeling, reducing conflicts. Experiments on Mandarin, subdialects, Cantonese, and English show LS-MOPD outperforms RL baselines and exceeds the best RL teachers' performance envelope.

## Key Takeaways
- Language-specialized teachers are optimized independently via reinforcement learning, allowing each language to acquire its own expertise without cross-lingual interference.
- The student integrates these teacher insights through language routing and token-level multi-teacher distillation, enabling a generalist multilingual model.
- Both static and dynamic acoustic prefixes were tested, with results indicating that prefix consistency enhances the effectiveness of on-policy distillation.

## Context
Current ASR research emphasizes multilingual LLMs that share knowledge across languages, but this approach often leads to suboptimal performance due to conflicting optimization signals. This work addresses a key limitation by decoupling language-specific learning from global model training.

## Implications
The method offers a scalable framework for deploying high-quality multilingual ASR systems where each language benefits uniquely. Practitioners can adopt LS-MOPD to fine-tune teacher models per language, improving overall system robustness and efficiency without retraining the entire multilingual student.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03610v1)
