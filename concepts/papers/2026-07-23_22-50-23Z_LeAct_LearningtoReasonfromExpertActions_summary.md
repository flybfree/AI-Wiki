# Summary: 2026-07-23_22-50-23Z_LeAct_LearningtoReasonfromExpertActions.md
Saved: 2026-07-26 21:32
Source: 2026-07-23_22-50-23Z_LeAct_LearningtoReasonfromExpertActions.md
Model: None

---

## Summary  
The paper proposes LeAct, a method to recover latent reasoning chains from expert actions alone, enabling foundation models to learn reasoning by leveraging expert systems as teachers. By treating the chain of thought (CoT) as a latent variable and optimizing student samples that improve action‑recovery probability, LeAct bridges the gap between silent expert behavior and explicit reasoning.

## Key Contributions  
- [Finding 1] The latent CoT can be learned from actions alone without human annotations.  
- [Finding 2] Student models trained via LeAct achieve near‑optimal performance on small enumerable games, matching solver floors.  
- [Finding 3] In large‑scale domains like Flop Hold’em and robotics benchmarks, LeAct outperforms expert‑iteration baselines by up to fivefold.

## Methodology  
The authors treat the reasoning chain of thought (CoT) as a latent variable that explains an expert’s action. For each observed action, the student generates candidate CoTs, evaluates them via a scoring function that measures improvement in the probability of reproducing the original action, and selects the best‑performing CoT to condition its own policy. This process is repeated across many tasks, allowing the model to internalize the hidden reasoning steps.

## Results  
On small enumerable games (e.g., 15‑puzzle variants), LeAct reaches the exact solver’s numerical floor, matching human‑solved solutions. On Flop Hold’em with ~10⁹ infosets, LeACT achieves +60 mbb/g compared to baseline, and on a simulated robotics probe it is the only method that improves over direct imitation learning. These gains are quantified as up to five times closer to expert performance than prior baselines.

## Significance  
LeAct demonstrates that expert systems—traditionally silent sources of high‑quality reasoning—can serve as powerful, scalable teachers for foundation models, reducing reliance on costly human annotations and enabling generalization beyond demonstrated actions.

## Related Concepts  
- Latent variable modeling  
- Chain‑of‑thought (CoT) prompting  
- Expert‑student transfer learning  
- Imitation learning with reasoning supervision
