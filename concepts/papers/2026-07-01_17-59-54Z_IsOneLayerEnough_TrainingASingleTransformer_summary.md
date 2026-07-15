title: "Summary: 2026-07-01_17-59-54Z_IsOneLayerEnough_TrainingASingleTransformerLayerCa.md"
# Summary: 2026-07-01_17-59-54Z_IsOneLayerEnough_TrainingASingleTransformerLayerCa.md
Saved: 2026-07-01 23:01
Source: 2026-07-01_17-59-54Z_IsOneLayerEnough_TrainingASingleTransformerLayerCa.md
Model: None

---


## Summary  
The paper investigates whether training a single transformer layer can achieve reinforcement learning (RL) performance comparable to full‑parameter RL training. It introduces the concept of *layer contribution* and demonstrates that most of the gains obtained during post‑training RL come from a small subset of layers, often located in the middle of the stack. Training one such layer frequently recovers or even exceeds the improvement achieved by updating all model parameters. This work challenges the long‑standing assumption that every transformer parameter contributes equally to RL adaptation.

## Key Contributions  
- [Finding 1] A single transformer layer can recover most of the gains from full‑parameter RL training, and in some cases surpass it.  
- [Finding 2] The contribution of each layer is highly concentrated; only a few middle layers account for the majority of improvement.  
- [Finding 3] This pattern holds consistently across seven models, multiple RL algorithms, and diverse task domains.

## Methodology  
The authors systematically freeze all model parameters except those belonging to one selected transformer layer and train that layer using three RL algorithms (GRPO, GiGPO, Dr. GRPO). They measure the improvement achieved by this single‑layer training via a *layer contribution* metric and compare it to the improvement obtained when all parameters are updated. Experiments span two model families (Qwen3, Qwen2.5), seven different RL algorithms, and task sets including mathematical reasoning, code generation, and agentic decision‑making.

## Results  
Across the experiments, training a middle layer recovers roughly 80 % of the full‑parameter RL improvement, with several cases exceeding 100 %. The ranking of high‑contribution layers remains stable regardless of model size, algorithm choice, or task. This suggests that a small number of well‑chosen layers can drive most of the performance gain.

## Significance  
The findings reveal that parameter‑efficient RL adaptation does not require updating every transformer weight; instead, focusing on a few high‑impact layers yields comparable or superior results while dramatically reducing computational cost and enabling scalable fine‑tuning for large language models.

## Related Concepts  
- Reinforcement learning post‑training  
- Transformer architecture  
- Layer‑wise contribution analysis  
- Parameter efficiency in model adaptation  
- Multi‑task generalization across RL algorithms
