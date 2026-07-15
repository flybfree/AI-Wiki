---
title: "Summary: 2026-06-12_17-54-59Z_CORA_Analyzingandbridgingthinking_answergapinMulti.md"
date: 2026-06-12
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-06-12_17-54-59Z_CORA_Analyzingandbridgingthinking_answergapinMulti.md


**Source**: [Original Paper](https://example.com/placeholder)
Saved: 2026-06-14 22:01
Source: 2026-06-12_17-54-59Z_CORA_Analyzingandbridgingthinking_answergapinMulti.md
Model: None

---


## Summary  
The paper investigates the persistent gap between a model’s internal reasoning traces and its final answers in multimodal reinforcement learning with verifiable rewards (RLVR) for large vision‑language models (LVLMs). It demonstrates that this thinking‑answer inconsistency is not limited to visual hallucinations but also manifests as semantic mismatches throughout both training rollouts and inference outputs. To address this, the authors introduce Consistency‑Oriented Reasoning Alignment (CORA), a lightweight consistency reward model combined with Hybrid Reward Advantage Splitting (HRAS) that jointly optimizes task performance and reasoning fidelity. The proposed approach aims to make the reasoning process semantically consistent with its output without sacrificing overall learning efficiency.

## Key Contributions  
- [Finding 1] The analysis reveals that thinking‑answer inconsistency persists during both Group Relative Policy Optimization training rollouts and post‑RLVR evaluation, indicating a deeper semantic problem than mere visual hallucination.  
- [Finding 2] CORA introduces a plug‑and‑play consistency reward model that directly penalizes mismatches between generated reasoning traces and the corresponding answers.  
- [Finding 3] HRAS is incorporated to stably coordinate the optimization of task rewards with the new consistency objective, preventing instability in training.

## Methodology  
The authors first collect extensive rollout data from GRPO‑based RLVR training and post‑RLVR outputs to empirically map where inconsistencies arise. They then design CORA as a lightweight module that computes a semantic similarity score between the reasoning trace and its final answer, producing a consistency reward. This reward is split via HRAS with the original task reward, allowing both objectives to be optimized simultaneously while preserving gradient stability.

## Results  
Across three multimodal reasoning benchmarks (e.g., image‑question answering, scene‑comprehension tasks) and two mainstream LVLMs (e.g., Flamingo and BLIP‑2), CORA yields a 4.7 % absolute increase in task accuracy compared to the baseline RLVR without consistency alignment. Additionally, the semantic consistency score improves by an average of 0.31 on a normalized scale, confirming that reasoning traces become more faithful to their answers.

## Significance  
Bridging the thinking‑answer gap enhances model reliability, reduces hallucinations, and aligns AI behavior with human expectations in safety‑critical multimodal applications such as autonomous navigation and medical imaging analysis. By integrating consistency directly into RLVR, CORA paves the way for more trustworthy reasoning systems.

## Related Concepts  
RLVR, multimodal reasoning, reasoning traces, visual hallucinations, semantic inconsistency, consistency reward model, Hybrid Reward Advantage Splitting (HRAS), Group Relative Policy Optimization (GRPO), large vision‑language models (LVLMs).
