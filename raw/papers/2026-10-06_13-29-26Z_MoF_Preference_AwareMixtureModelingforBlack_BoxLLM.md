---
title: MoF: Preference-Aware Mixture Modeling for Black-Box LLM Personalization
published: 2026-10-06T13:29:26Z
authors: Hun Park
url: http://arxiv.org/abs/2610.08330v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MoF: Preference-Aware Mixture Modeling for Black-Box LLM Personalization

## Abstract
Proprietary Large Language Models (LLMs) have demonstrated remarkable capabilities across a wide range of tasks, yet aligning their outputs with diverse user preferences remains challenging. Existing personalization approaches for black-box LLMs often rely on user-specific scoring heads, causing the number of personalized parameters to grow linearly with the number of users and requiring additional adaptation for unseen users. To address these limitations, we propose Mixture-of-Facets (MoF), a scalable personalization framework for black-box LLMs that models user preferences as compositions of shared latent preference facets rather than dedicated user-specific parameters. MoF performs personalization through history-conditioned routing over shared facet heads, enabling personalization for users unseen during training without additional parameter updates. Across diverse personalization tasks, MoF delivers stronger personalization performance while maintaining a more scalable and parameter-efficient design than prior approaches. Additional analysis indicates strong generalization to unseen users.

## Metadata
- **Published**: 2026-10-06T13:29:26Z
- **Authors**: Hun Park
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.08330v1)