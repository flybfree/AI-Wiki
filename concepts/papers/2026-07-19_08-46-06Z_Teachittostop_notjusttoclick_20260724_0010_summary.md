# Summary: 2026-07-19_08-46-06Z_Teachittostop_notjusttoclick.md
Saved: 2026-07-24 00:10
Source: 2026-07-19_08-46-06Z_Teachittostop_notjusttoclick.md
Model: None

---

## Summary  
The paper investigates the reliability of agentic computer‑use reinforcement learning (RL) agents that can perform tasks in a single run, arguing that reported success rates are misleading because they ignore high‑level variance. By applying verifier‑guided repair to a 35 billion‑parameter CUA across five oracle‑graded environments, the authors demonstrate that true performance is driven by data‑draw and run‑to‑run nondeterminism rather than seed effects. Their analysis reveals two distinct layers of repairability: reliable single‑token fixes versus partial open‑ended corrections, and a conditional benefit of frame‑level repairs only when they address the remaining blocker in a task. The work also stresses that single‑run improvements can be misleadingly negative about one‑third of the time, prompting a new library for robust k‑seed reporting.

## Key Contributions  
- **Finding 1:** Repairability is two‑tiered—single fixed tokens are reliably detected (0.97 ± 0.06), while open‑ended corrections such as spatial‑coordinate clicks (0.53 ± 0.35) and generative field‑fill (0.14 ± 0.04) are only partially effective.  
- **Finding 2:** Frame‑level repair improves task success only when the corrective action is the sole remaining blocker, as shown by a LinkedIn benchmark where success rose from 0/15 to 8/20 (Fisher p = 0.006).  
- **Finding 3:** A single‑run improvement of this magnitude would have the wrong sign about one‑third of the time in comparable regimes, highlighting the danger of over‑claiming.

## Methodology  
The authors employed a verifier‑guided repair framework on a 35 B CUA policy across five oracle‑graded environments. They performed variance‑components decomposition using crossed data draws and seed grids with bootstrap confidence intervals to isolate sources of variance. The analysis examined three cells (data draw × seed grid) and identified run‑to‑run nondeterminism as the dominant source, especially for the hardest cell where a Hartigan dip revealed bimodal failure modes.

## Results  
Evaluation variance is negligible (σₑval ≈ 0), training‑seed effects are ≤10 %, and data draw dominates with ~48 % of variance on the hardest cell. The run‑to‑run distribution is bimodal, giving a 30 % chance of failure per run. Single fixed token detection achieved 0.97 ± 0.06 accuracy; spatial clicks scored 0.53 ± 0.35 and generative fills 0.14 ± 0.04. A frame‑level repair raised LinkedIn success from 0/15 to 8/20 (p = 0.006). The authors also reproduced two overstated claims—a sample‑efficiency curve and a “grounding cannot be bought” boundary—only after seed replication.

## Significance  
This research underscores that reported RL performance often hides substantial variability, leading to potentially false optimism or pessimism. By providing a systematic variance decomposition and a library (cua_reliability) for k‑seed reporting, the work promotes transparent, reproducible evaluation of agentic systems. It also warns against extrapolating single‑run gains without considering their statistical sign.

## Related Concepts  
- Agentic computer‑use reinforcement learning (CUA)  
- Verifier‑guided repair and on‑policy self‑distillation (SA‑OPSD)  
- Variance decomposition across data draws, seeds, and runs  
- Bimodal run‑to‑run distributions and Hartigan dip analysis  
- Frame‑level vs. token‑level corrective actions in RL agents
