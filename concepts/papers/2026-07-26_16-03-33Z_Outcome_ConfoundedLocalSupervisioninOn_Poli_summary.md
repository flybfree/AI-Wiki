# Summary: 2026-07-26_16-03-33Z_Outcome_ConfoundedLocalSupervisioninOn_PolicyDisti.md
Saved: 2026-07-27 20:20
Source: 2026-07-26_16-03-33Z_Outcome_ConfoundedLocalSupervisioninOn_PolicyDisti.md
Model: None

---

## Summary  
On‑policy distillation (OPD) leverages teacher‑provided token‑level likelihoods to guide a student’s learning, but the authors demonstrate that agreement on divergence is confounded by the final outcome of the trajectory; they introduce an outcome‑resolved diagnostic that separates safe imitation from harmful divergence; experiments with Qwen3‑8B and Qwen3‑32B reveal that roughly 67.8 % of pooled response‑token mass corresponds to “agreement‑on‑failure,” indicating that local signals are misleading.

## Key Contributions  
- Finding 1: Agreement on failure accounts for ~67.84 % of the token‑level divergence across multiple model pairs (Qwen3‑8B/32B and Qwen2.5‑7B/32B).  
- Finding 2: Local teacher‑student divergence cannot reliably identify where a trajectory becomes unrecoverable; it is confounded by the outcome of that trajectory.  
- Finding 3: Adding process labels or token‑level alignment does not consistently reduce agreement‑on‑failure in current training probes.

## Methodology  
The authors construct an outcome‑resolved diagnostic that cross‑checks pointwise teacher‑student divergence with final answer correctness, then audits various configurations (thresholds, sequence‑level, format, truncation) to confirm robustness. They also run three matched training probes—imitate, mask, or contrast whole trajectories—that use the available signals to evaluate whether additional information can mitigate the problem.

## Results  
In an eight‑seed mathematical‑reasoning study, agreement‑on‑failure remains 67.84 % for Qwen3‑8B/32B and 67.68 % for Qwen2.5‑7B/32B; even when student accuracy rises to 86.91 % on prompts solved by the teacher, agreement‑on‑failure stays around 14.76 %. Three training probes that employ the available signals do not consistently lower this metric.

## Significance  
This work reveals a fundamental limitation of local supervision in OPD: divergence paired with outcome does not pinpoint failure locations, suggesting that current token‑level diagnostics are insufficient for reliable error detection and that additional positional or process information is needed to improve diagnostic reliability.

## Related Concepts  
- On‑policy distillation  
- Token‑level likelihood supervision  
- Outcome‑confounded signals  
- Diagnostic analysis  
- Trajectory‑level evaluation  
- Learning probes  
- Position labels  
- Token alignment
