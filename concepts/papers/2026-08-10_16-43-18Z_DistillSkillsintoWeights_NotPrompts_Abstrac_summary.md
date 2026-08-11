# Summary: 2026-08-10_16-43-18Z_DistillSkillsintoWeights_NotPrompts_AbstractSkills.md
Saved: 2026-08-10 23:58
Source: 2026-08-10_16-43-18Z_DistillSkillsintoWeights_NotPrompts_AbstractSkills.md
Model: None

---

## Summary  
The paper tackles the limitation of reinforcement learning (RL) that uses verifiable rewards, which often provide no useful group‑relative signal because many rollout groups are uniformly correct or uniformly wrong. To overcome this, the authors introduce SKALD (Skill‑Anchored Latent Distillation), an on‑policy self‑distillation method that extracts abstract skill knowledge into model parameters rather than relying on privileged prompts at inference time. By training a student and teacher with two context views—one question‑only and one conditioned on an explicit answer‑filtered skill card—the framework learns to propagate the advantage of those skills directly into shared weights, enabling more robust improvements over existing baselines such as GRPO across several mathematics benchmarks.

## Key Contributions  
- [Finding 1] Group‑relative rewards are uninformative in a large fraction (63.0–68.0 %) of rollout groups that are uniformly correct or wrong, so they cannot guide distillation; abstract skills provide dense supervision where this signal disappears.  
- [Finding 2] SKALD improves overall avg@8 over FLOP‑matched GRPO by +2.46 at the 0.6 B model, +4.85 at the 1.7 B model, and +12.01 at the 4 B model on five held‑out mathematics benchmarks.  
- [Finding 3] At the 1.7 B scale, zero‑variance‑only distillation recovers only 84.7 % of SKALD’s full gain, while SKALD still outperforms FLOP‑matched GRPO by +4.06 and exceeds contextual skill exposure by +3.77.

## Methodology  
SKALD employs two context views of the same Qwen3‑Base model: a student trained only on its own question prefixes (no privileged input) and a teacher conditioned on an abstract, explicit‑answer‑filtered skill card that encodes the target skill. The student’s loss is derived from a forward‑KL term, but to prevent catastrophic mismatch the authors use an annealed exponentially tilted objective that downweights teacher‑preferred tokens with very low student likelihood; as the tilt vanishes the loss converges back to standard cross‑entropy. A gating mechanism activates distillation only when verified rollouts estimate a positive teacher advantage, ensuring that the model learns from genuine skill‑induced improvements rather than noise.

## Results  
Empirical evaluation on five mathematics benchmarks shows that SKALD consistently yields higher avg@8 scores than GRPO across all model sizes. The gate’s activation rate is moderate (≈ 15 % of steps), indicating that distillation proceeds only when it can provide a measurable benefit. Zero‑variance‑only distillation, which discards any teacher‑preferred token without student confidence, recovers 84.7 % of SKALD’s performance gain at the 1.7 B scale, confirming that most of the improvement stems from genuine skill knowledge rather than random noise. Moreover, SKALD remains +4.06 above FLOP‑matched GRPO and exceeds contextual skill exposure by +3.77, demonstrating both efficiency (lower FLOPs) and effectiveness.

## Significance  
This work shows that abstract skills can serve as a rich, dense supervision signal where conventional RL reward signals become uninformative due to uniform rollout groups. By distilling these skills directly into model weights rather than relying on prompt‑level cues, SKALD achieves substantial performance gains with minimal additional compute and without exposing the model to privileged inputs at test time—an important step toward scalable, privacy‑preserving RL.

## Related Concepts  
- Verifiable rewards in reinforcement learning  
- Rollout groups and group‑relative reward signals  
- On‑policy self‑distillation (knowledge distillation)  
- Expert prompting vs. latent skill extraction  
- FLOP‑matched baselines for efficiency comparison  
- Zero‑variance distillation as a regularization technique
