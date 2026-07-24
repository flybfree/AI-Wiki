# Summary: 2026-07-23_09-02-46Z_FromEvaluationtoOptimisation_Hierarchy_AwareTraini.md
Saved: 2026-07-24 02:45
Source: 2026-07-23_09-02-46Z_FromEvaluationtoOptimisation_Hierarchy_AwareTraini.md
Model: None

---

## Summary  
This paper investigates whether the hierarchical penalty originally designed for evaluating CWE‑level vulnerability predictions in Python can also be used as a training signal to improve model performance. By comparing supervised fine‑tuning, dual‑head classification loss, and reinforcement learning with a dense reward derived from the normalised penalty, the authors demonstrate that only the reinforcement‑learning approach can overcome distribution shift and achieve competitive results. Their best policy reduces the cumulative ALPHA penalty of Qwen2.5‑Coder‑7B on the Security Hardening and Adversarial Testing (SVEN) dataset by 27.9 % under greedy decoding, approaching parity with a larger zero‑shot teacher. The study shows that the value of a hierarchical penalty depends critically on how directly it is delivered to the training process.

## Key Contributions  
- [Finding 1] Supervised fine‑tuning and dual‑head classification loss consistently degrade below the zero‑shot baseline when faced with distribution shift, highlighting their limited adaptability.  
- [Finding 2] Reinforcement learning (GRPO) using a dense reward derived from the normalised penalty successfully mitigates distribution shift and improves CWE prediction accuracy.  
- [Finding 3] The hierarchical penalty can reduce cumulative ALPHA penalties by up to 27.9 % under greedy decoding, achieving statistical parity with a larger zero‑shot teacher on the SVEN benchmark.

## Methodology  
The authors adopt three delivery mechanisms for the training signal: (1) supervised fine‑tuning where the penalty is incorporated as an additional loss term; (2) dual‑head classification loss that jointly predicts CWE level and severity while penalising hierarchical violations; and (3) reinforcement learning with a dense reward function computed from the normalised ALPHA penalty, allowing the model to optimise for cumulative penalty reduction. Experiments are conducted on the SVEN dataset using Qwen2.5‑Coder‑7B, evaluating both greedy decoding and sampled decoding (p = 0.005) with Welch’s t‑test.

## Results  
Supervised approaches degrade by an average of 18–22 % relative to zero‑shot performance under distribution shift. GRPO achieves a 27.9 % reduction in cumulative ALPHA penalty under greedy decoding and reaches statistical parity (p > 0.05) with the larger teacher model, confirming that reinforcement learning can exploit the hierarchical structure of the penalty.

## Significance  
The findings reveal that training signals must be directly tied to the evaluation metric’s hierarchy; indirect or loss‑based approaches fail under real‑world distribution shifts. By validating a dense reward derived from the ALPHA penalty, the study provides a practical pathway for integrating hierarchical penalties into model optimisation pipelines, potentially improving security‑focused language models.

## Related Concepts  
- CWE (Common Weakness Enumeration) vulnerability prediction  
- Hierarchical training signals and their direct delivery  
- Reinforcement learning with dense rewards (GRPO)  
- ALPHA benchmark for Python code security evaluation  
- Zero‑shot baseline performance comparison
