# Summary: 2026-08-09_08-22-57Z_FailForge_DistillingProceduralCompetencefromPersis.md
Saved: 2026-08-10 23:14
Source: 2026-08-09_08-22-57Z_FailForge_DistillingProceduralCompetencefromPersis.md
Model: None

---

## Summary  
The paper addresses a key limitation of rejection sampling fine‑tuning (RFT) in training code agents: even the strongest models repeatedly fail on a large fraction of verifiable software tasks, and those failures are discarded as uninformative. The authors propose FailForge, an agentic framework that treats each failure as a learning opportunity by extracting actionable skills from error feedback and execution traces. By guiding a second attempt with these distilled skills—then removing the guidance at training time—the method recovers many previously lost trajectories without relying on external hints during inference. This approach expands the RFT corpus, enabling the model to internalize the hard cases that define the frontier of improvement.

## Key Contributions  
- [Finding 1] Rejection sampling fine‑tuning (RFT) discards failures, which are actually the hardest and most informative instances, limiting further progress.  
- [Finding 2] FailForge converts each failed rollout into a concise skill distilled from error feedback and execution traces, injects it for a guided second attempt, and removes the guidance at training time to internalize behavior.  
- [Finding 3] The augmented RFT corpus recovers over 26 % of previously failed instances, boosting SWE‑bench Verified resolve rate by 6.6 points compared with a strong RFT baseline.

## Methodology  
FailForge operates in two stages. First, for each failure the agent analyses error messages and execution traces to formulate a short, actionable skill (e.g., “use `try/except`”). The skill is added to the model’s context as a prompt for a second attempt; if this succeeds, the successful trajectory is folded back into the RFT training set. Crucially, the skill text is stripped from the final training examples so that the model learns the underlying behavior without external hints at inference time. This process repeats across all failures, gradually enriching the dataset with recovered hard cases.

## Results  
Experiments on Qwen3.5‑4B show that FailForge recovers more than 26 % of the originally discarded trajectories. When this enriched corpus is used to fine‑tune RFT, the SWE‑bench Verified resolve rate improves by 6.6 points over a strong baseline, with gains concentrated on the most difficult problems. The additional cost in training time and compute remains modest.

## Significance  
FailForge tackles a fundamental bottleneck in code‑agent training: the loss of valuable failure data that could guide future learning. By systematically converting failures into internalized skills, it reduces reliance on costly manual curation while delivering measurable performance gains—particularly for tasks that are hard to solve and often rejected by RFT. This method opens a path toward more robust, self‑improving code agents.

## Related Concepts  
- Rejection sampling fine‑tuning (RFT)  
- Procedural competence in AI agents  
- Skill distillation from error feedback  
- Code agent training pipelines  
- SWE‑bench Verified dataset and resolve rate
