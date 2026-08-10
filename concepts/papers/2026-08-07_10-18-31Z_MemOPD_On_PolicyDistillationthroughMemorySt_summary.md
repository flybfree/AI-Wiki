# Summary: 2026-08-07_10-18-31Z_MemOPD_On_PolicyDistillationthroughMemoryStateAlig.md
Saved: 2026-08-09 22:54
Source: 2026-08-07_10-18-31Z_MemOPD_On_PolicyDistillationthroughMemoryStateAlig.md
Model: None

---

## Summary  
Long‑horizon agents suffer from growing contexts that degrade performance, so compact memory is needed to compress the history between model invocations. Traditional on‑policy distillation (OPD) provides dense teacher supervision but can misalign states because context rewriting breaks the provenance of sampled actions. MemOPD solves this by restoring original token positions and causal visibility before packing invocations for efficient teacher scoring while PPO retains the final task objective. Experiments show that MemOPD improves F1 scores and accelerates training compared with persistent‑history approaches.

## Key Contributions  
- [Finding 1] Memory compression can break state‑action alignment in OPD, causing teachers to score actions under states never visited during rollout.  
- [Finding 2] MemOPD records inputs and sampled outputs, restores original token positions and causal visibility, and packs reconstructed invocations for teacher scoring.  
- [Finding 3] Empirically, MemOPD‑3B yields up to a 7.0 % F1 gain over persistent‑history teacher scoring and a 416.2 % improvement over PPO, with a 1.63× speedup in actor computation.

## Methodology  
The authors approach the problem by recording every model invocation’s inputs and sampled outputs, reconstructing the original token order while preserving causal dependencies, then packing these reconstructed invocations into a compact memory buffer that serves as dense teacher supervision for OPD while PPO continues to optimize the final task reward.

## Results  
Across multiple context‑update scenarios, MemOPD demonstrates state alignment throughout interactions; the 3B model achieves up to 416.2 % F1 improvement over baseline PPO and a 7.0 % gain relative to persistent‑history teacher scoring, while training actor computation is accelerated by a factor of 1.63.

## Significance  
This work addresses a critical bottleneck in long‑horizon reinforcement learning where memory compression degrades the validity of on‑policy distillation, enabling reliable teacher supervision and substantial performance gains without sacrificing computational efficiency.

## Related Concepts  
- On‑policy Distillation (OPD)  
- Persistent history  
- Memory compression / context rewriting  
- Proximal Policy Optimization (PPO)
