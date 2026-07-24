# Summary: 2026-07-23_09-02-46Z_FromEvaluationtoOptimisation_Hierarchy_AwareTraini.md
Saved: 2026-07-24 02:34
Source: 2026-07-23_09-02-46Z_FromEvaluationtoOptimisation_Hierarchy_AwareTraini.md
Model: None

---

## Summary  
This paper investigates whether the hierarchical penalty originally designed to evaluate CWE‑level vulnerability predictions in Python can also be used as a training signal. By comparing supervised fine‑tuning, dual‑head classification loss, and reinforcement learning that directly optimises the normalised penalty, the authors demonstrate how the delivery mechanism influences performance. Their work shows that only reinforcement learning with the dense reward derived from the penalty can close the gap to state‑of‑the‑art zero‑shot baselines on the Security Hardening and Adversarial Testing (SVEN) dataset. The best policy reduces the cumulative ALPHA penalty by up to 27.9 % under greedy decoding, matching the teacher’s performance despite its size disadvantage.

## Key Contributions  
- [Finding 1] Supervised fine‑tuning and dual‑head classification loss consistently fall below the zero‑shot baseline when distribution shift is introduced, indicating limited utility of the penalty as a supervised signal.  
- [Finding 2] Reinforcement learning (GRPO) with a dense reward derived from the normalised ALPHA penalty achieves statistical parity with the larger teacher model on both greedy and sampled decoding regimes.  
- [Finding 3] The hierarchical penalty’s effectiveness is highly sensitive to how directly it is incorporated into the training objective; indirect or delayed signals do not translate into comparable improvements.

## Methodology  
The authors adopt a three‑step approach: (1) they construct a dense reward function that normalises the ALPHA benchmark score, converting it into a scalar signal for reinforcement learning; (2) they implement GRPO to optimise a policy that predicts CWE predictions while maximising this reward; and (3) they evaluate the resulting policies against supervised fine‑tuning and dual‑head loss baselines on the SVEN dataset under both greedy and sampled decoding strategies. The experiments include baseline Qwen2.5‑Coder‑7B, its zero‑shot teacher, and a hierarchical penalty‑driven policy.

## Results  
Supervised methods degrade by 10–15 % relative to the zero‑shot baseline after distribution shift. GRPO reduces the cumulative ALPHA penalty of Qwen2.5‑Coder‑7B from 4.5× higher than the teacher to within statistical significance (Welch’s t‑test p < 0.05). Under greedy decoding, the policy achieves a 27.9 % reduction; under sampled decoding with probability 0.005, it reaches parity with the teacher. These gains are quantified across multiple CWE categories and demonstrate that hierarchical penalties can be leveraged as training signals when directly optimised.

## Significance  
By proving that the ALPHA penalty can serve as a reinforcement learning reward, this work bridges evaluation‑driven design with model optimisation, offering a principled way to improve vulnerability prediction models without retraining from scratch. The findings suggest that hierarchical penalties are valuable only when their values are fed directly into an optimisation loop, highlighting a key insight for future safety‑critical AI systems.

## Related Concepts  
- CWE (Common Weakness Enumeration) taxonomy‑aware penalty  
- Hierarchical reward design in reinforcement learning  
- Supervised fine‑tuning and dual‑head classification loss  
- GRPO (Generalised Policy Optimisation) for policy improvement  
- Zero‑shot baseline performance comparison
