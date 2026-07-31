# Summary: 2026-07-30_15-54-29Z_QuantWAMs_CalibratingattheRightGranularityforWorld.md
Saved: 2026-07-30 22:17
Source: 2026-07-30_15-54-29Z_QuantWAMs_CalibratingattheRightGranularityforWorld.md
Model: None

---

## Summary  
World Action Models (WAMs) aim to predict both future observations and actions in a single framework, but their iterative denoising and closed‑loop execution demand careful quantization that respects the model’s internal structure. QuantWAMs introduces a calibration strategy that aligns precision decisions with the specific rollout distribution and task objective, rather than relying on generic post‑training assumptions. By tailoring quantization to the granularity of each video‑action block, the method reduces memory usage while preserving performance. The approach has been validated across simulated and real‑robot manipulation tasks, showing measurable gains in speed and feasibility.

## Key Contributions  
- Finding 1: Shared‑basis outlier calibration pools activation evidence only among coordinate‑compatible modules, enabling efficient variance estimation without cross‑module interference.  
- Finding 2: Co‑training‑objective saliency computes empirical‑Fisher scores from the joint video–action gradient and assigns weight precision at a stable layer granularity, ensuring that quantization adapts to the actual gradient dynamics of each block.  
- Finding 3: Fixed‑intervention rollout auditing revises denoising‑step protection schedules using reachable closed‑loop states while keeping the precision budget unchanged, thus preventing unnecessary over‑quantization.

## Methodology  
The authors first characterize the calibration context by analyzing which modules share activation space and how the joint video‑action loss influences weight stability. They then implement three complementary strategies: (1) shared‑basis outlier calibration to compute a per‑module variance; (2) co‑training‑objective saliency to derive layer‑wise precision weights from gradient Fisher information; and (3) fixed‑intervention rollout auditing to adjust protection schedules based on reachable states. Quantization is performed block‑level, applying the derived precision directly to each video‑action block.

## Results  
In a W4A4‑dominant setting across Fast‑WAM and LingBot‑VA simulations on RoboTwin 2.0, LIBERO, and real‑robot trials with AgiBot G2, QuantWAMs reduces peak weight‑and‑activation memory to about 29 % of FP16 levels while delivering 1.4–1.6× block‑level speedups. Simulation means differ from FP16 by only 0.2–0.7 percentage points, and the method successfully deploys on three manipulation tasks without loss of action quality.

## Significance  
QuantWAMs demonstrates that quantization can be made context‑aware for iterative world models, dramatically lowering resource consumption while maintaining high accuracy—a crucial advance for deploying WAMs in real‑time robotics. The work bridges the gap between generic PTQ and task‑specific calibration, offering a scalable framework for future AI agents.

## Related Concepts  
World Action Models (WAMs), quantization, calibration granularity, shared‑basis outlier calibration, co‑training‑objective saliency, fixed‑intervention rollout auditing.
