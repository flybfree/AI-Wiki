# Summary: 2026-07-29_06-28-26Z_HiFloat4FormatforEnd_To_EndReinforcementLearningPo.md
Saved: 2026-07-29 21:35
Source: 2026-07-29_06-28-26Z_HiFloat4FormatforEnd_To_EndReinforcementLearningPo.md
Model: None

---

## Summary  
The paper introduces HiFloat4, a format that enables end‑to‑end reinforcement learning post‑training of large language models using only 4‑bit precision for both rollout and training passes. It identifies rollout activation quantization as the dominant source of degradation, not training‑side errors. Their solution Rollout‑ResQ adds a lightweight residual correction to recover precision lost due to outliers. This combination restores near‑BF16 accuracy while maintaining 4‑bit compute.

## Key Contributions  
- Finding 1: The dominant degradation in FP4 RL is rollout activation quantization causing outlier underflow.  
- Finding 2: Restoring the training policy to higher precision worsens performance, indicating a mismatch between rollout and training precisions.  
- Finding 3: Rollout‑ResQ paired with HiFloat4 reduces the accuracy gap from 4.9% to 1.1% on Qwen models.

## Methodology  
The authors systematically compared several configurations—full FP4 baseline, FP4 rollout only, FP4 rollout with higher‑precision training, and HiF4 combined with Rollout‑ResQ—across the Qwen2.5-3B and Qwen2.5-Math-7B models, measuring task accuracy (perplexity). They also applied the same recipe to the open benchmark MXFP4.

## Results  
On Qwen2.5-3B, full FP4 RL achieved 10.8% accuracy versus a BF16 baseline of 4.9%, a gap of 4.9%. HiF4 with Rollout‑ResQ closed the gap to 1.1% absolute, reducing relative error to ~3.8%. For MXFP4, the gap narrowed from 13.6% to 5.3%, showing that format choice is critical.

## Significance  
These results demonstrate that HiFloat4 and Rollout‑ResQ are essential enablers for high‑fidelity RL post‑training in 4‑bit, allowing practical deployment without sacrificing much performance relative to full precision baselines.

## Related Concepts  
HiFloat4, FP4 format, rollout training, backward pass quantization, residual quantization, outlier underflow, BF16 baseline, MXFP4 benchmark.
