# Summary: 2026-07-19_08-46-06Z_Teachittostop_notjusttoclick.md
Saved: 2026-07-24 00:10
Source: 2026-07-19_08-46-06Z_Teachittostop_notjusttoclick.md
Model: None

---

## Summary  
This paper challenges the misleading success rates reported in single-run agentic computer-use reinforcement learning (CUA), demonstrating that such evaluations are dominated by upstream variance rather than true performance improvement. Using verifier-guided repair of a 35B-parameter CUA policy across five oracle-graded environments, the authors reveal that evaluation outcomes are highly sensitive to data draw and run-to-run nondeterminism, with single runs often misrepresenting the true success probability due to bimodal distributions. The study introduces a rigorous k-seed reporting framework to mitigate this variance, enabling reliable comparisons of repair effectiveness across seeds. This work shifts focus from isolated performance snapshots to reproducible, variance-aware evaluation practices in large-scale AI systems.

## Key Contributions  
- [Finding 1] Repairability is two-tier: single fixed token corrections achieve high reliability (0.97±0.06), while open-ended actions like spatial-coordinate clicks or generative field-fill show partial success (0.53±0.35 and 0.14±0.04, respectively).  
- [Finding 2] Frame-level repair only transfers to task success when the corrective action resolves the sole remaining blocker, as seen in LinkedIn (8/20 vs. base 0/15), with a significant Fisher p=0.006 improvement.  
- [Finding 3] The authors expose two over-claimed claims—sample efficiency and grounding cannot be bought—only after cross-seeding reveals their fragility, underscoring the need for stress testing beyond single runs.

## Methodology  
The authors employed verifier-guided repair on a 35B-parameter CUA policy across five oracle-graded environments to assess repair effectiveness. They used variance-components decomposition with crossed data-draw and seed grids, followed by bootstrap confidence intervals (BCIs) to quantify evaluation variance. A multimodal segment-aggregated on-policy self-distillation (SA-OPSD) update was implemented to refine the policy iteratively. The methodology involved systematic replication across 10 seeds per environment, enabling decomposition of variance into data draw (48% dominant in hardest cell), run-to-run nondeterminism (bimodal Hartigan dip, p=0.07), and repair-specific effects.

## Results  
Evaluation variance was negligible (σ_eval ≈ 0) across seeds, confirming that single runs are unreliable. The training-seed effect was small (<10%), while data draw contributed significantly—up to 48% in the hardest cell. Repair success rates varied: fixed tokens achieved near-perfect detection (97% confidence), but open-ended corrections were less effective due to grounding and generative limitations. Crucially, frame-level repair only succeeded when it eliminated the final blocker, improving LinkedIn task success from 0/15 to 8/20. The authors also validated their findings by replicating across seeds, catching two over-claimed metrics: sample efficiency improved only slightly (<10%), and grounding improvements were not universal.

## Significance  
This work addresses a critical flaw in AI research reporting: single-run performance claims often reflect variance, not true capability. By introducing k-seed reporting and SA-OPSD updates, the authors provide a foundation for reliable evaluation of large language models performing complex tasks. Their findings prevent over-optimistic interpretations of CUA systems and promote reproducibility, which is essential as AI capabilities scale.

## Related Concepts  
- Agentic Computer Use (CUA)  
- Reinforcement Learning with Verifier Guidance  
- Variance-components decomposition  
- Bootstrap confidence intervals (BCIs)  
- On-policy self-distillation (SA-OPSD)  
- Task success dependency on corrective action  
- Cross-seeding for variance analysis
