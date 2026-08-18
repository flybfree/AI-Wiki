---
title: A Declarative-Procedural Perspective on Expert Routing in Bilingual Mixture-of-Experts Language Models
url: http://arxiv.org/abs/2608.15102v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_07-53-12Z_ADeclarative_ProceduralPerspectiveonExpertRoutingi.md
generated_at: 2026-08-17 21:38
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether MoE language models develop structured expert routing during bilingual acquisition using a Declarative‑Procedural framework. It finds that curriculum training yields peak mutual information at layer 5 indicating category‑dependent specialization, while the no‑curriculum baseline shows stronger aggregate specialisation but less stable results across seeds.

## Key Takeaways
- Curriculum‑trained model reaches peak mutual information of 0.1148 at layer 5 showing category‑dependent routing differences.
- No‑curriculum baseline achieves higher mutual information 0.2599 indicating stronger overall specialisation.
- Seed‑dependent single‑language dominance appears in no‑curriculum, whereas curriculum yields stable balanced routing.

## Context
Mixture‑of‑experts models aim to balance capacity and efficiency yet their internal routing remains opaque. Understanding how linguistic exposure shapes expert utilisation offers insight into emergent language structure and informs more interpretable AI systems.

## Implications
Interpretable routing can guide model design for multilingual tasks, reducing bias towards dominant languages. Practitioners may use curriculum strategies to achieve balanced expertise, improving fairness and performance across diverse datasets.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15102v1)
