---
title: "Summary: Refusal in Language Models Is Mediated by a Single Direction"
date: "2026-10-02"
arxiv_id: "2406.11717"
source_url: "https://arxiv.org/abs/2406.11717"
tags: ["paper", "research", "ai", "alignment", "interpretability", "safety", "paper-summary"]
---
# Summary: Refusal in Language Models Is Mediated by a Single Direction

**Source**: [Original Paper](https://arxiv.org/abs/2406.11717)

## Summary
The paper argues that refusal behavior in aligned conversational language models is mediated by a single direction in activation space. Across 13 open-source chat models, the authors identify a direction in the residual stream whose removal suppresses refusals to harmful instructions, while adding it can induce refusals to harmless instructions. The result suggests that at least some safety-tuning behavior is represented in a narrow and manipulable part of the model's internal computation rather than being robustly distributed throughout the network.

## Key Contributions
- Identifies a refusal-mediating direction in the residual-stream activations of 13 open-source chat models, including models up to 72B parameters.
- Shows bidirectional control: removing the direction reduces refusal of harmful prompts, while adding it can cause refusal of harmless prompts.
- Introduces a white-box jailbreak method that surgically removes the refusal behavior while preserving much of the model's other behavior.
- Mechanistically analyzes how adversarial suffixes interfere with propagation of the refusal-mediating direction.

## Methodology
The authors use mechanistic-interpretability analyses of open model activations. They search for a low-dimensional direction associated with refusal behavior, test causal interventions that erase or add that direction in the residual stream, and evaluate the resulting changes on harmful and harmless instructions. They then use the identified mechanism to construct a white-box refusal-removal attack and study how adversarial suffixes suppress the relevant activation signal.

## Findings and Limitations
The central finding is evidence of a strong, reusable low-dimensional representation of refusal across the evaluated models. This does not establish that all safety behavior is one-dimensional, nor that the same direction transfers unchanged across architectures or model families. The attack requires white-box access to model internals, so it is not directly equivalent to a black-box jailbreak against a hosted model. The paper therefore demonstrates brittleness in one important safety behavior while leaving open how broadly the mechanism generalizes to newer models and more comprehensive safety policies.

## Significance
This work is important for alignment and interpretability because it connects a visible behavioral property—refusal—to a concrete internal representation that can be causally manipulated. It supports the view that safety fine-tuning can create shallow or concentrated behavioral safeguards, and it motivates more robust evaluations that test whether safety behavior is distributed across capabilities and contexts rather than controlled by a small removable feature.

## Related Concepts
- [[concepts/papers/2026-07-19_09-18-35Z_HowJailbreakAttacksInformSafetyAlignment_AD_summary.md|Summary: How Jailbreak Attacks Inform Safety Alignment]]
- [[concepts/ai-foundations/ai-ml-foundations-lesson-11-large-language-models-the-modern-ai-interface.md|AI/ML Foundations Lesson 11 — Large Language Models]]

## Paper Metadata
- **Authors:** Andy Arditi, Oscar Obeso, Aaquib Syed, Daniel Paleka, Nina Panickssery, Wes Gurnee, Neel Nanda
- **Submitted:** June 17, 2024
- **Latest arXiv version:** v3, October 30, 2024
- **Categories:** cs.LG, cs.AI, cs.CL
- **Canonical source:** https://arxiv.org/abs/2406.11717
