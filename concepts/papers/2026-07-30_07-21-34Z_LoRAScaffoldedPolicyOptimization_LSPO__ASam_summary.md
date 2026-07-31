# Summary: 2026-07-30_07-21-34Z_LoRAScaffoldedPolicyOptimization_LSPO__ASampling_T.md
Saved: 2026-07-30 20:30
Source: 2026-07-30_07-21-34Z_LoRAScaffoldedPolicyOptimization_LSPO__ASampling_T.md
Model: None

---

## Summary  
The paper addresses the gradient loss in reinforcement learning from verifiable rewards when encountering “cliff” prompts where all rollouts fail, causing zero group‑normalized advantage and no RL update. LSPO introduces a sampling‑time low‑rank adapter that recovers this lost gradient without permanently modifying the base model.

## Key Contributions  
- [Finding 1] The loss of gradient on cliff prompts due to identically zero advantages in group normalization.  
- [Finding 2] A sampling‑time LoRA (low‑rank adaptation) mechanism that fits a small adapter per cliff prompt using supervised solutions and discards it after the RL step.  
- [Finding 3] Demonstrated empirical gains of up to +10.7 points on AIME24/pass@4 and overall +3.8 points across 16 benchmark cells compared with DAPO.

## Methodology  
The authors detect cliff prompts by observing that every sampled rollout in a group yields zero advantage; they then perform a brief supervised fine‑tuning step on the ground‑truth solution to generate a low‑rank LoRA adapter. During RL, the base model is augmented with this adapter only for those prompts, re‑rolls them successfully, and splices the completions back into the batch using importance sampling correction. The RL update (GRPO) is taken on the base model alone, while the adapter receives only a supervised gradient and is discarded at checkpoint.

## Results  
Experiments were conducted on DeepMath-103K with DeepSeek‑R1‑Distill‑Qwen‑1.5B over 16 cells of AIME24/AIME26/MATH500 using n=5 paired seeds per arm and a 1000‑step reporting horizon. LSPO achieved a mean score matching or exceeding the DAPO baseline on all cells, with strict wins in 15 out of 16 and one tie. The largest improvement was +10.7 points on AIME24/pass@4, +6.7 points on AIME24/AIME26 at pass@16, and +2.4 points on MATH500/pass@1, yielding an average gain of +3.8 points.

## Significance  
By recovering the lost gradient on cliff prompts without permanently altering the policy, LSPO enables more stable and effective RL training in domains where verification is possible yet progress stalls at capability boundaries. This approach preserves model simplicity while improving performance, offering a scalable scaffold for future verifiable‑reward RL systems.

## Related Concepts  
- Reinforcement Learning from Verifiable Rewards (RLVR)  
- Group Normalization of Advantages  
- Cliff Prompts in RL  
- Low‑Rank Adaptation (LoRA) and its sampling‑time usage  
- Generalized Policy Optimization (GRPO)
