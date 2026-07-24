# Summary: 2026-07-22_13-34-17Z_CUSUM_ShapedInference_TimeMonitoringandTargetedRe_.md
Saved: 2026-07-24 01:51
Source: 2026-07-22_13-34-17Z_CUSUM_ShapedInference_TimeMonitoringandTargetedRe_.md
Model: None

---

## Summary  
The paper proposes MGT‑B, a monitoring‑guided test‑time backtracking controller for quantized small language models that detects degeneration during inference and performs targeted re‑decoding. It maps token‑level uncertainty windows to empirical tail probabilities using a CUSUM‑shaped reset, triggers rollback when an alarm is raised, restores the KV cache, and re‑decodes only under constraints. Evaluation on specific reasoning tasks shows modest accuracy improvements but not universal gains.

## Key Contributions  
- Finding 1: MGT‑B introduces a CUSUM‑shaped inference‑time monitoring mechanism that maps token‑level uncertainty to empirical tail probabilities.  
- Finding 2: The controller triggers rollback and constrained re‑decoding only when an alarm is raised, preserving most outputs unchanged.  
- Finding 3: Empirical audit reveals limited but statistically significant accuracy improvements on targeted MATH‑500 IDs.

## Methodology  
The authors built upon an earlier token‑level e‑CUSUM controller. They defined overlapping windows of pre‑sampling uncertainty and degeneration features, computed position‑conditional empirical tail probabilities, accumulated mixture betting factors with a CUSUM‑shaped reset, and implemented alarm handling that rolls back to the estimated rollback point, restores KV cache state, and performs constrained re‑decoding.

## Results  
On a chronologically first post‑threshold pair set of 240 IDs, accuracy improved from 82/240 to 88/240 (+2.5 percentage points; McNemar p = 0.2632). A broader historical coverage set of 467 seed‑matched pairs showed a +4.5 point improvement (McNemar p = 0.000753) but includes many pre‑threshold IDs. All 316 no‑alarm outputs matched vanilla; only 151 alarmed trajectories had 29 corrections and 8 regressions.

## Significance  
The work demonstrates a selective monitoring‑and‑repair approach that can mitigate degeneration in quantized small language models, though gains are task‑specific rather than universal. It highlights the potential of inference‑time detection to improve robustness without major architectural changes.

## Related Concepts  
- Quantization  
- Small language model reasoning  
- Autoregressive token generation  
- CUSUM alarm detection  
- Test‑time backtracking  
- KV cache restoration  
- Empirical tail probability mapping
