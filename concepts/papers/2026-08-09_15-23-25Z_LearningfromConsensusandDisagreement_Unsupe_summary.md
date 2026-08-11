# Summary: 2026-08-09_15-23-25Z_LearningfromConsensusandDisagreement_UnsupervisedO.md
Saved: 2026-08-10 23:24
Source: 2026-08-09_15-23-25Z_LearningfromConsensusandDisagreement_UnsupervisedO.md
Model: None

---

## Summary  
The paper proposes CoDA (Consensus and Disagreement Alignment), a fully unsupervised on‑policy self‑distillation framework that leverages the latent uncertainty of a language model’s own rollouts to generate reliable privileged information. By extracting both consensus‑driven guidance from stable reasoning modes and disagreement‑based regularization from minority trajectories, CoDA eliminates reliance on external verifiers or gold solutions. The method creates a binary feedback loop: positive signals reinforce correct reasoning while negative signals gently penalize unstable alternatives, thereby breaking the harmful feedback of amplified errors. Empirical results show that CoDA markedly improves competition‑level mathematical reasoning compared with self‑generated baselines and stabilizes training against erroneous consensus.

## Key Contributions  
- [Finding 1] CoDA extracts a positive branch from answer‑level consensus to provide dense distributional guidance without external supervision.  
- [Finding 2] It introduces a negative branch that uses minority‑trajectory disagreement as a KTO‑style calibration signal, offering unpaired regularization.  
- [Finding 3] The combined binary feedback loop significantly boosts reasoning performance and mitigates the propagation of correlated errors.

## Methodology  
CoDA operates within an on‑policy self‑distillation loop where the student generates unlabeled rollouts. A frozen teacher evaluates each state, producing a consensus score that identifies stable reasoning modes; these scores are used to condition dense guidance for new trajectories. Simultaneously, minority trajectories—those deviating from the consensus path—are flagged as unstable and penalized via a reference‑anchored KTO objective that measures calibration against a fixed reference distribution. The two branches operate independently but together form a binary feedback mechanism: positive signals reinforce correct reasoning, while negative signals regularize misbehavior without requiring ground truth.

## Results  
On competition‑level mathematical benchmarks (e.g., MATH, GSM8K), CoDA achieves up to 12 % absolute improvement in accuracy over the strongest self‑generated baselines and reduces variance of performance across training epochs. Ablation studies confirm that removing either the positive or negative branch degrades performance, indicating both are essential for the binary feedback loop’s effectiveness.

## Significance  
CoDA advances unsupervised on‑policy distillation by harnessing internal model uncertainty, offering a scalable alternative to supervised teacher‑student setups that rely on external verifiers. By treating disagreement as a regularizing signal rather than noise, it addresses a longstanding challenge: preventing consensus from amplifying errors while still providing useful guidance.

## Related Concepts  
- On‑policy self‑distillation  
- Latent uncertainty extraction  
- Consensus vs. disagreement signals  
- KTO (Key-to-Test) calibration  
- Minority trajectory handling
