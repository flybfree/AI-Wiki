# Summary: 2026-08-06_16-29-24Z_DASH_Divergence_AdaptiveSupervisionHorizonsforOn_P.md
Saved: 2026-08-06 20:48
Source: 2026-08-06_16-29-24Z_DASH_Divergence_AdaptiveSupervisionHorizonsforOn_P.md
Model: None

---

## Summary  
On‑policy self‑distillation (OPSD) alleviates the sparsity of reinforcement learning with verifiable rewards by providing dense token‑level supervision from a privileged teacher. However, standard OPSD treats every local divergence with an identical scalar coefficient, ignoring how those divergences evolve over time and their position in the generation sequence. This uniform weighting under‑exploits temporal structure, leading to suboptimal performance. The authors introduce Divergence‑Adaptive Supervision Horizons (DASH), a method that adapts supervision weights according to the realized discrepancy history without extra teacher or student passes.

## Key Contributions  
- [Finding 1] Standard OPSD assigns uniform scalar coefficients to local divergences regardless of their position, causing underutilization of temporal dynamics.  
- [Finding 2] DASH maps each divergence’s gap from the sequence‑level mean to an adaptive propagation gate that controls multi‑step backward aggregation, enabling context‑sensitive supervision.  
- [Finding 3] Experiments demonstrate that DASH consistently outperforms vanilla OPSD reruns on three mathematical reasoning benchmarks across all model scales.

## Methodology  
The authors first compute the teacher and student distributions as in OPSD to obtain token‑level distributional signals. They then calculate a local divergence for each generated token, which quantifies how far the student’s distribution deviates from the teacher’s at that position. Each divergence is mapped to an adaptive propagation gate by comparing its magnitude to the sequence‑level mean divergence; gates with larger deviations receive higher weight. These gates are used to weight multi‑step backward aggregation, producing a supervision schedule that adapts to how divergences evolve during generation. No additional forward passes over teacher or student models are required.

## Results  
DASH improves over vanilla OPSD reruns on all three reasoning benchmarks (e.g., arithmetic, logical deduction, proof generation) at every model scale examined. The gain is consistent and measurable across the experiment suite, indicating that adaptive supervision yields a reliable performance boost without sacrificing computational efficiency.

## Significance  
By aligning supervision weights with the temporal evolution of divergence signals, DASH enhances the effectiveness of on‑policy self‑distillation for RL systems that rely on verifiable rewards. This leads to stronger reasoning capabilities in large language models while preserving the low‑cost nature of OPSD, making it a valuable advance for scalable and efficient model improvement.

## Related Concepts  
- On‑policy self‑distillation (OPSD)  
- Reinforcement learning with verifiable rewards (RLVR)  
- Divergence‑based token‑level supervision  
- Adaptive propagation gates  
- Multi‑step backward aggregation
