# Summary: 2026-08-01_16-20-24Z_AnEmbeddedRISC_VEvaluationofKolmogorov__ArnoldNetw.md
Saved: 2026-08-03 20:30
Source: 2026-08-01_16-20-24Z_AnEmbeddedRISC_VEvaluationofKolmogorov__ArnoldNetw.md
Model: None

---

## Summary  
The paper evaluates Kolmogorov–Arnold Networks (KANs) as residual branches in hard‑constrained recurrent physics‑informed neural networks (HRPINNs) on a RISC‑V embedded core, showing that their claimed parameter efficiency does not translate to lower latency or energy consumption. It compares KAN and MLP residuals trained to the same accuracy, measuring execution speed, power per integration step, and post‑training quantization impact.

## Key Contributions  
- [Finding 1] The KAN residual branch is significantly slower (≈13×) and consumes much more energy (≈12×) than an MLP with identical training weights on the RV64GC platform.  
- [Finding 2] Quantization of both networks to INT8 exacerbates performance loss, with KAN trajectories diverging up to 43× earlier; the degradation is attributed to weight quantization, not knot‑interval misassignment.  
- [Finding 3] Across all size tiers, KANs are consistently more expensive (4.7×–14.5× slower and 4.7×–18.7× higher energy) than MLPs, indicating that parameter efficiency does not survive deployment.

## Methodology  
The authors trained two residual branches—KAN and MLP—to match the same discovery accuracy on a set of hard‑constrained recurrent physics‑informed models. They then deployed both networks inside a closed recurrent loop on two RISC‑V cores (StarFive VisionFive~2, SiFive U74) without vector extensions. Execution latency, energy per integration step, and post‑training INT8 quantization were measured using standard profiling tools.

## Results  
KANs executed 13.5× slower and used 11.3× more energy than MLPs for the smallest accuracy pair (3.7 µJ vs 0.33 µJ per step). For larger pairs, ranges are 4.7×–14.5× in latency and 4.7×–18.7× in energy. After INT8 quantization, KAN trajectories diverged up to 43× earlier than MLPs; the difference is due to weight quantization artifacts.

## Significance  
These findings reveal a gap between theoretical parameter‑efficiency claims of KANs and real‑world embedded deployment costs on scalar cores. For hardware‑constrained systems, an MLP residual branch remains more dependable unless co‑designed quantization mitigates the penalty.

## Related Concepts  
Kolmogorov–Arnold Networks (KAN), hard‑constrained recurrent physics‑informed neural networks (HRPINNs), B‑spline activations, multilayer perceptrons (MLPs), RISC‑V embedded cores, post‑training quantization, scalar execution cost, weight quantization artifacts.
