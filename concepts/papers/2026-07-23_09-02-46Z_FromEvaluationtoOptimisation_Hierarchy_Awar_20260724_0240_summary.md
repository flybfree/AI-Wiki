# Summary: 2026-07-23_09-02-46Z_FromEvaluationtoOptimisation_Hierarchy_AwareTraini.md
Saved: 2026-07-24 02:40
Source: 2026-07-23_09-02-46Z_FromEvaluationtoOptimisation_Hierarchy_AwareTraini.md
Model: None

---

## Summary  
The paper investigates whether the ALPHA benchmark’s hierarchical penalty, originally designed for evaluating CWE‑level vulnerability predictions in Python code, can also be repurposed as a training signal. By comparing supervised fine‑tuning, dual‑head classification loss, and reinforcement learning using the normalised penalty as reward, the authors aim to determine which delivery mechanism yields the most effective optimisation of prediction performance. Their contribution is empirical evidence that hierarchical penalties are only useful when directly incorporated into the training objective, not merely as evaluation metrics.  

## Key Contributions  
- Finding 1: Supervised fine‑tuning and dual‑head classification both underperform relative to zero‑shot baselines, indicating that adding a penalty without direct optimisation does not improve model capacity.  
- Finding 2: Reinforcement learning with the normalised ALPHA penalty as a dense reward achieves significant gains, reducing cumulative penalties by up to 27.9% on Qwen2.5-Coder‑7B under greedy decoding and 25.5% under sampled decoding (p = 0.005).  
- Finding 3: The hierarchical penalty’s value is contingent on its directness; the best policy reaches statistical parity with a larger zero‑shot teacher, demonstrating that indirect use of penalties can be as effective as explicit supervised training.  

## Methodology  
The authors construct three delivery mechanisms for the ALPHA penalty. First, they fine‑tune existing language models using the standard supervised loss augmented with a penalty term that penalises CWE predictions at higher levels. Second, they employ a dual‑head classification framework where one head predicts vulnerability level and another applies the hierarchical penalty as an auxiliary loss. Third, they implement reinforcement learning via GRPO (Gradient Proximal Policy Optimisation) where the normalised ALPHA score is transformed into a reward signal guiding policy updates. Each method is evaluated on the Security Hardening and Adversarial Testing (SVEN) dataset with both greedy and sampled decoding strategies.  

## Results  
Under supervised fine‑tuning, Qwen2.5-Coder-7B’s cumulative penalty exceeds that of its zero‑shot teacher by a statistically significant margin (Welch’s t‑test p < 0.01). The dual‑head approach shows modest improvement but still lags behind the baseline. Reinforcement learning with the dense reward reduces penalties to 27.9% and 25.5% respectively, achieving near parity with a model four times larger than the zero‑shot teacher, confirming that direct optimisation of the hierarchical penalty yields superior performance.  

## Significance  
This work clarifies a longstanding ambiguity in AI safety research: whether evaluation penalties can serve as training signals. By proving that only direct integration of hierarchical penalties improves outcomes, it guides future work on safe code generation and vulnerability prediction, where aligning model objectives with real‑world risk metrics is crucial.  

## Related Concepts  
- CWE (Common Weakness Enumeration)  
- Hierarchical penalty  
- Supervised fine‑tuning  
- Dual‑head classification loss  
- Reinforcement learning / GRPO  
- Zero‑shot baseline
