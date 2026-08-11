# Summary: 2026-08-10_16-43-18Z_DistillSkillsintoWeights_NotPrompts_AbstractSkills.md
Saved: 2026-08-11 00:17
Source: 2026-08-10_16-43-18Z_DistillSkillsintoWeights_NotPrompts_AbstractSkills.md
Model: None

---

## Summary  
The paper introduces SKALD (Skill‑Anchored Latent Distillation), an on‑policy self‑distillation method that extracts the performance of abstract mathematical skills into model weights rather than relying on prompt engineering or group‑relative reward signals. By training a student model on its own prefixes while conditioning a teacher on filtered skill cards, SKALD transfers skill‑induced advantages without exposing test data to privileged inputs. The framework mitigates distribution mismatch with an annealed tilted objective and activates distillation only when the teacher shows a clear advantage. Empirically, SKALD outperforms standard GRPO across five math benchmarks, delivering gains of up to 12 % at the 4B scale.

## Key Contributions  
- [Finding 1] Abstract skills act as dense supervision that remain useful even when group‑relative rewards are uninformative.  
- [Finding 2] On‑policy self‑distillation can recover a large portion of the teacher’s skill advantage without privileged test inputs.  
- [Finding 3] The annealed tilted objective stabilizes learning and ensures convergence to the true student gradient.

## Methodology  
SKALD operates with two views of the same Qwen3‑Base model: a question‑only student and a teacher conditioned on an explicit answer filtered by a skill card. The student is trained on its own prefixes, allowing it to internalize the skill’s advantage. To align distributions, SKALD uses an exponentially tilted cross‑entropy loss that downweights tokens the teacher prefers when their likelihood under the student is very low; as the tilt parameter anneals to zero, the loss approaches standard cross‑entropy and recovers the forward‑KL gradient. Distillation is gated only when rollout estimates a positive teacher advantage, preventing unnecessary updates.

## Results  
Across five held‑out mathematics benchmarks, SKALD improves overall avg@8 over GRPO by +2.46 % at 0.6B, +4.85 % at 1.7B, and +12.01 % at 4B. At the 1.7B scale, zero‑variance distillation recovers 84.7 % of the full gain, while SKALD remains +4.06 above FLOP‑matched GRPO and exceeds contextual skill exposure by +3.77.

## Significance  
These results demonstrate that abstract skills provide a rich, dense signal for model improvement, bypassing the limitations of group‑relative rewards that become uninformative in many RL settings. By distilling skills into latent weights rather than prompting, SKALD offers a more stable and scalable path to higher performance with minimal extra compute.

## Related Concepts  
- On‑policy self‑distillation  
- Gradient reversal learning  
- Annealed tilted objectives  
- Skill cards / abstract supervision  
- Group‑relative reward analysis
