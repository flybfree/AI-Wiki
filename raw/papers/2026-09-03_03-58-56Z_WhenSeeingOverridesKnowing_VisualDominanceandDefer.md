---
title: When Seeing Overrides Knowing: Visual Dominance and Deferral-Based Method for Personalized Safety in VLMs
published: 2026-09-03T03:58:56Z
authors: Edward Sun, Yuchen Wu, Zixian Ma, Eric Hanchen Jiang, Yijia Xiao, Xiaoyuan Yi, Ranjay Krishna, Wei Wang, Jindong Wang, Aylin Caliskan
url: http://arxiv.org/abs/2609.04281v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Seeing Overrides Knowing: Visual Dominance and Deferral-Based Method for Personalized Safety in VLMs

## Abstract
Vision-language models (VLMs) are increasingly deployed in high-stakes settings, where a response that is reasonable in general may still be unsafe for a particular user whose medical, emotional, or situational context is unknown to the model. We study this problem of personalized safety in multimodal systems and introduce MPS-Bench, a benchmark of 5,181 scenarios from 584 real-world images across 12 high-risk domains, each paired with a hidden user profile. Evaluating eight frontier VLMs, we find that they almost always respond directly (86-99%) rather than seek missing context, and none exceeds 2.6/5 on personalized safety. To understand why these failures arise, we analyze multimodal interactions and identify visual dominance: visual information enters text representations early and suppresses textual risk signals during multimodal fusion. Causal interventions reveal a two-stage mechanism in which visual affect is first transferred into the text stream in early layers and then shapes the final decision through this altered text representation, making late-stage internal remediation unreliable. Motivated by this mechanism, we propose PRISM, a lightweight input monitor that uses bidirectional cross-modal modulation to predict when a query is likely to require deferral. PRISM achieves 0.978 AUC and strictly dominates the safety-utility Pareto frontier across all tested models.

## Metadata
- **Published**: 2026-09-03T03:58:56Z
- **Authors**: Edward Sun, Yuchen Wu, Zixian Ma, Eric Hanchen Jiang, Yijia Xiao, Xiaoyuan Yi, Ranjay Krishna, Wei Wang, Jindong Wang, Aylin Caliskan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04281v1)