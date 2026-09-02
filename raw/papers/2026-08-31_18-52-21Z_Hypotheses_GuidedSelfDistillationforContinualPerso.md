---
title: Hypotheses-Guided Self Distillation for Continual Personalization
published: 2026-08-31T18:52:21Z
authors: EunJeong Hwang, Kushan Mitra, Dan Zhang, Hannah Kim, Estevam Hruschka
url: http://arxiv.org/abs/2609.00251v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hypotheses-Guided Self Distillation for Continual Personalization

## Abstract
As people increasingly interact with LLM assistants in daily life, continually adapting to individual preferences has become essential for effective long-term interactions. However, user preferences are rarely stated in full, and instead emerge through heterogeneous, latent, and noisy signals, with existing methods relying on raw interaction histories or costly reward-based optimization to manage personalization. We introduce HypReflect, a reliable, scalable framework for continual personalization that infers explicit, uncertainty-aware preference hypotheses from diverse user signals, reflectively refines them as new evidence accumulates, and incorporates the resulting user model through hypotheses-guided self-distillation. Experiments across three personalization settings: online personalization, multi-session interactions, and implicit behavioral signals, show that HypReflect outperforms a range of baselines, including raw-history and incremental-update methods. We further demonstrate strong generalization to unseen users and cross-domain settings, along with stability across context budgets, reusable hypotheses, and more focused personalization. These results suggest a step towards reliable and scalable continual personalization through explicit, revisable user preference hypotheses.

## Metadata
- **Published**: 2026-08-31T18:52:21Z
- **Authors**: EunJeong Hwang, Kushan Mitra, Dan Zhang, Hannah Kim, Estevam Hruschka
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00251v1)