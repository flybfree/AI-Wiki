---
title: Syndrome, Synergy, and Safety: Structured Reasoning and Knowledge-Driven Alignment for TCM Prescription Generation
url: http://arxiv.org/abs/2609.25755v1
type: paper-summary
date: 2026-09-22
source_paper: 2026-09-22_06-49-19Z_Syndrome_Synergy_andSafety_StructuredReasoningandK.md
generated_at: 2026-09-22 20:08
model: freedomaisvr/gemma-4-12b-it
---

## Summary
This paper introduces a specialized four-stage framework designed to improve Large Language Model (LLM) performance in Traditional Chinese Medicine (TCM) prescription generation by addressing three specific clinical gaps: Syndrome Reasoning (SR), Longitudinal Adjustment (LA), and Safety Constraints (SC). By integrating structured reasoning, patient trajectory modeling, and knowledge-based reinforcement learning, the authors demonstrate that a 7B parameter model can outperform zero-shot GPT-5 across all key TCM evaluation metrics.

## Key Takeaways
- Syndrome Reasoning Gap: Current LLMs often produce end-to-end prescriptions without an auditable reasoning chain that follows the traditional "li-fa-fang-yao" (syndrome-pattern-prescription-drug) paradigm. The authors propose PG-CoT (Prescription-Guided Chain of Thought) to constrain the model's reasoning process, ensuring it follows a logical path from diagnosis to treatment.
- Longitudinal Adjustment Gap: Most models treat each patient encounter as an isolated event, failing to account for how treatments should change over time based on "sui zheng jia jian" (adjusting according to progress). The proposed Dynamic SFT method allows the model to understand and predict patient trajectories by modeling explicit transition reasoning between successive consultations.
- Safety Constraints Gap: Ensuring safety is critical in medicine, yet LLMs often ignore absolute contraindications like "Shi Ba Fan." The authors developed K-RL (Knowledge-based Reinforcement Learning) to encode these deterministic rules as rule-based DPO preference signals, ensuring the model adheres to strict pharmacological safety boundaries.

## Context
This research is significant because it moves beyond general-purpose AI alignment toward domain-specific "knowledge-driven" alignment for high-stakes medical applications. It addresses a critical hurdle in healthcare AI: how to make models both safe and interpretable within the specific cultural and logical frameworks of traditional medicine systems, rather than relying on black-box outputs.

## Implications
The findings suggest that specialized, structured fine-tuning techniques can allow smaller, more accessible models (like Mistral-7B) to outperform much larger general models in niche domains. This provides a viable pathway for healthcare providers and researchers to deploy high-performing, safe, and interpretable AI tools without relying solely on massive, opaque systems that may lack specific domain safety constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.25755v1)
