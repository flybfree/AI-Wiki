# Summary: 2026-07-28_02-09-26Z_Meta_LearnedRewardShapingforReinforcementLearningf.md
Saved: 2026-07-29 22:11
Source: 2026-07-28_02-09-26Z_Meta_LearnedRewardShapingforReinforcementLearningf.md
Model: None

---

## Summary  
The paper introduces MeRLa (Meta‑Learned Reward Shaping), a framework that meta‑learns a task‑aware shaping function Φ(x,y;φ) across auxiliary tasks to improve Reinforcement Learning from Human Feedback. By generating dynamic, task‑specific learning signals while preserving policy optimality, MeRLa addresses the static‑reward mismatch that limits RLHF quality. The approach combines several regularization techniques—task discrimination, entropy control, and potential‑based conservation—to guarantee stable convergence. Experiments on LLaMA‑3‑8B demonstrate consistent gains over PPO, DPO, GRPO, and DAPO.

## Key Contributions  
- **Meta‑learned shaping function**: Φ(x,y;φ) is learned from auxiliary tasks to produce task‑aware reward signals that complement the human feedback.  
- **Theoretical analysis**: The authors prove policy invariance under composition, quantify representation drift sensitivity, and resolve incentive misalignment caused by entropy maximization through regularization.  
- **Empirical superiority**: MeRLa achieves a 90.8 % length‑controlled win rate on AlpacaEval 2.0, a score of 9.14 on MT‑Bench, and 41 % less training instability compared with state‑of‑the‑art methods.

## Methodology  
The authors first train a meta‑learner on a set of auxiliary tasks to obtain parameters φ that define Φ(x,y;φ). This shaping function is then combined with the human feedback reward to form a composite reward. The policy is updated using a PPO‑like algorithm, but the shaped reward injects task‑specific information while the regularization terms (task discrimination, entropy penalty, and potential conservation) ensure convergence stability.

## Results  
Across four benchmarks, MeRLa outperforms PPO, DPO, GRPO, and DAPO in both win rates and quality scores. On AlpacaEval 2.0 it reaches 90.8 % length‑controlled wins; on MT‑Bench its score is 9.14. Training logs show a 41 % reduction in instability metrics such as variance of returns, confirming the robustness of the meta‑shaped reward.

## Significance  
MeRLa provides a principled solution to the static‑reward problem that plagues RLHF, enabling task‑specific learning without sacrificing policy stability. This makes it especially valuable for scaling alignment in large language models where human feedback is costly and generic rewards are insufficient.

## Related Concepts  
- Reinforcement Learning from Human Feedback (RLHF)  
- Static reward models  
- Meta‑learning  
- Shaping functions  
- PPO, DPO, GRPO, DAPO  
- Entropy regularization  
- Potential‑based conservation  
- Policy invariance
