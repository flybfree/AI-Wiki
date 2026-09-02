---
title: Towards reliable multimodal disaster severity assessment through preference optimization and explainable vision-language reasoning
published: 2026-09-01T08:11:09Z
authors: Yuanjun Zhang, Fuzel Ahamed Shaik, Suvojit Acharjee, Fahad Khalid, Mourad Oussalah
url: http://arxiv.org/abs/2609.00879v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards reliable multimodal disaster severity assessment through preference optimization and explainable vision-language reasoning

## Abstract
Reliable disaster damage assessment requires models that provide both accurate predictions and transparent explanations. However, existing multimodal approaches are limited by scarce annotated data and insufficient evaluation of reasoning quality. This study proposes a two-stage training framework that integrates Supervised Fine-Tuning (SFT) and Direct Preference Optimization (DPO) within a unified data construction pipeline. From a single Human-in-the-Loop (HITL) annotation workflow, two complementary datasets are derived, namely ReasoningSet, which contains validated rationales for SFT, and PreferenceSet, which comprises paired rationales for DPO-based alignment. The framework evaluates both classification performance and explanation quality using automatic metrics, model-based scoring, and human ranking. Experimental results show that SFT improves accuracy from 73.64% to 78.29% and increases Macro-F1 by 29% compared to the baseline, while explanation quality improves by approximately 25%. Subsequent DPO alignment further enhances interpretability on the PreferenceSet. Cross-model validation on InternVL-3-8B and LLaVA-1.5-7B demonstrates the robustness and generalizability of the approach. The proposed framework improves detection of underrepresented mild damage cases, reduces high-risk misclassifications, and strengthens alignment between model reasoning and human judgment. Overall, it provides a reproducible pathway to develop reliable multimodal systems that deliver auditable, actionable disaster insights for emergency management.

## Metadata
- **Published**: 2026-09-01T08:11:09Z
- **Authors**: Yuanjun Zhang, Fuzel Ahamed Shaik, Suvojit Acharjee, Fahad Khalid, Mourad Oussalah
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00879v1)