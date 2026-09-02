---
title: Towards reliable multimodal disaster severity assessment through preference optimization and explainable vision-language reasoning
url: http://arxiv.org/abs/2609.00879v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_08-11-09Z_Towardsreliablemultimodaldisasterseverityassessmen.md
generated_at: 2026-09-01 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a two‑stage training framework that combines supervised fine‑tuning and direct preference optimization to improve both accuracy and explanation quality in multimodal disaster severity assessment. It achieves higher classification performance and better interpretability compared to baselines, demonstrating robustness across models.

## Key Takeaways
- SFT improves accuracy from 73.64% to 78.29% and raises Macro‑F1 by 29% relative to the baseline.
- Explanation quality rises about 25%, measured via automatic metrics, model‑based scoring, and human ranking.
- DPO alignment on PreferenceSet further boosts interpretability and corrects rare mild damage misclassifications.

## Context
Multimodal disaster assessment demands models that predict damage accurately while offering clear rationales for emergency responders. Existing methods struggle with limited annotated data and lack systematic evaluation of reasoning quality, hindering trustworthy deployment in high‑stakes scenarios.

## Implications
This framework offers a reproducible pipeline for building auditable AI systems that can be integrated into disaster response workflows. Practitioners can leverage the preference optimization to reduce false alarms and improve decision support, ultimately enhancing public safety outcomes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00879v1)
