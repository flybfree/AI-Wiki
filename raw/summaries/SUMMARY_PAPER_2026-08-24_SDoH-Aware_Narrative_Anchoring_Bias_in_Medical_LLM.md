---
title: SDoH-Aware Narrative Anchoring Bias in Medical LLMs for Trustworthy Clinical Decision Support
url: http://arxiv.org/abs/2608.22802v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_04-58-32Z_SDoH_AwareNarrativeAnchoringBiasinMedicalLLMsforTr.md
generated_at: 2026-08-24 21:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SDoH‑aware narrative anchoring bias, a risk that medical LLMs may alter answers when the same clinical case is presented in different patient‑voice narratives. Using NarrativeShield SDoH MedQA they compare three Qwen2.5 models and find the 7B model has highest accuracy but still shows narrative sensitivity errors.

## Key Takeaways
- The 7B model achieves 56.33 percent overall accuracy, which is higher than smaller models, yet its correct consistency drops to 40.33 percent.
- Counterfactual consistency remains low, indicating the model changes responses despite identical answer keys across personas.
- Narrative sensitivity error stays at 31.67 percent, showing persistent bias when patient narratives shift.

## Context
Medical LLMs are evaluated mainly on average correctness, but real‑world clinical use depends on stable answers regardless of how a case is narrated. This study highlights that performance metrics must include consistency across narrative variations to ensure trustworthy decision support.

## Implications
Clinicians and developers should adopt evaluation frameworks that measure both accuracy and counterfactual stability. Ignoring narrative anchoring bias could lead to unsafe clinical recommendations, undermining the credibility of AI‑assisted care.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22802v1)
