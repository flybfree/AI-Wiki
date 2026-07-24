# Summary: 2026-07-06_15-01-35Z_RethinkingOn_PolicySelf_DistillationforThinkingMod.md
Saved: 2026-07-23 23:37
Source: 2026-07-06_15-01-35Z_RethinkingOn_PolicySelf_DistillationforThinkingMod.md
Model: None

---

## Summary  
The paper investigates the impact of privileged self‑distillation on thinking language models, which are designed to perform long‑range reasoning tasks such as solving math competitions. By letting a model serve as its own teacher with access to correct solutions, researchers expected to boost performance, but they discovered that this approach actually harms accuracy when the student is allowed to reconsider or backtrack during rollout. The degradation is most severe at high‑entropy forking points where multiple plausible continuations exist and scales with the amount of privileged context withheld from the student.

## Key Contributions  
- [Finding 1] Privileged self‑distillation causes a relative drop of up to 17 % in average accuracy (avg@16) across five Qwen3 and OLMo thinking models on AIME24, AIME25, and HMMT25.  
- [Finding 2] The degradation intensifies as more privileged context is withheld from the student, especially at long rollout budgets where otherwise the greatest gains are observed.  
- [Finding 3] The failure mode is not unique to self‑distillation; on‑policy distillation (OPD) also suffers when the teacher’s privileged context reshapes learning at high‑entropy forking positions.

## Methodology  
The authors conducted controlled experiments comparing three regimes: (1) standard self‑distillation without privileged context, (2) privileged self‑distillation where the correct solution is hidden from the student, and (3) on‑policy distillation (OPD) with and without privilege. They evaluated five thinking models—Qwen3 and OLMo variants—on three benchmark sets of competition problems. The evaluation measured accuracy at 16 steps, token‑level markers such as verification, backtracking, and hedging, and the proportion of rollouts that reach high‑entropy forking positions. Diagnostics traced the effect to how privileged teacher context lowers fork rates in thinking‑model rollouts but not instruction‑model rollouts.

## Results  
The baseline self‑distillation improves avg@16 accuracy by a modest margin, while OPD yields larger gains. Privileged versions of both methods reverse these trends: privileged self‑distillation reduces accuracy up to 17 % and OPD produces the opposite effect, decreasing gains. After normalizing for rollout length, models trained with privileged teachers exhibit fewer verification tokens, backtracking events, and hedging markers—indicating smoother but less exploratory reasoning. The impact scales linearly with the amount of withheld context, confirming that the model is penalized for missing teacher guidance at critical decision points.

## Significance  
These findings reveal a hidden risk in self‑improvement pipelines: over‑reliance on privileged teacher signals can suppress the exploration needed for robust reasoning. For thinking models, which already rely heavily on long‑range traces and correction branches, the loss of verification and backtracking tokens may degrade performance more than any benefit gained from additional knowledge. The work urges researchers to design distillation protocols that preserve token‑level signal around self‑correction steps.

## Related Concepts  
- On‑policy self‑distillation (OPD)  
- Privileged teacher context in distillation  
- Thinking models and long‑range reasoning  
- High‑entropy forking positions  
- Verification, backtracking, hedging markers  
- Fork rate reduction due to privileged guidance
