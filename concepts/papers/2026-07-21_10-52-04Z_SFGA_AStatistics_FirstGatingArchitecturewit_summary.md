# Summary: 2026-07-21_10-52-04Z_SFGA_AStatistics_FirstGatingArchitecturewithAdjudi.md
Saved: 2026-07-24 00:43
Source: 2026-07-21_10-52-04Z_SFGA_AStatistics_FirstGatingArchitecturewithAdjudi.md
Model: None

---

## Summary  
The paper introduces SFGA, a statistics‑first gating architecture for procurement of supervised fine‑tuning data that balances three intrinsic quality axes—diversity, utility, and redundancy—while minimizing acquisition cost. It treats the decision as a routing problem: cheap blind measurements are summarized into per‑axis estimates with confidence intervals, and only when those intervals are tight and sample sizes adequate does the gate accept the corpus; otherwise it escalates to an adjudicative debate between a buy‑advocate and a reject‑advocate judge. On a controlled benchmark of 12 datasets (a $2 \times 3 \times 2$ grid over the three axes) with five seeds, SFGA achieves 0.90 accuracy and 0.83 F₁ at \$0.017 per unit, outperforming an always‑verify baseline (0.75) and approaching an oracle upper bound (0.98). The system also spends less than the always‑escalate cost (\$0.020), demonstrating a trade‑off between verification expense and performance.

## Semantic links
- [[concepts/papers/2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_i_summary.md|Summary: 2026-07-29_17-15-33Z_Cost_SensitiveConformalPredictionandHuman_in_the_L.md]] — 4 title terms overlap; 12 summary/topic terms overlap; semantic match 0.04
- [[concepts/ai-foundations/ai-ml-foundations-lesson-14-choosing-the-right-architecture-for-the-task.md|AI/ML Foundations Lesson 14 - Choosing the Right Architecture for the Task]] — 3 title terms overlap; 5 backlinks; 4 summary/topic terms overlap

## Key Contributions  
- SFGA’s gating architecture treats data procurement as a cost‑aware routing problem across three quality axes (diversity, utility, redundancy).  
- The system employs cheap blind measurements summarized into per‑axis estimates with confidence intervals, triggering only when intervals are tight and sample sizes adequate.  
- Honest negative diagnostics reveal advocate‑side biases; the debate path exposes a 52 % position‑flip rate under advocate swapping and a con‑side win rate of 0.80 (p≈3×10⁻⁶), highlighting hidden negativity that naive LLM judges hide.

## Methodology  
The authors approached procurement as a routing problem: first generate per‑axis statistics (e.g., diversity, utility, redundancy) via lightweight sampling; compute confidence intervals to assess measurement reliability; if criteria are met, accept the dataset; otherwise escalate to an adjudicative debate where two agents—buy‑advocate and reject‑advocate—present arguments judged by a presiding arbiter. The evaluation includes synthetic injected‑knob benchmarks to calibrate measurement fidelity and routing calibration.

## Results  
On a 12‑dataset grid (2×3×2) across the three axes with five seeds, SFGA reaches 0.90 accuracy and 0.83 F₁ at \$0.017 per unit, outperforming an always‑verify baseline (0.75) and approaching an oracle upper bound (0.98). It costs less than the always‑escalate cost (\$0.020). Honest negative diagnostics show a con‑side win rate of 0.80 with p≈3×10⁻⁶, and a 52 % position‑flip rate under advocate swapping.

## Significance  
This work demonstrates that trustworthy data procurement can be achieved without exhaustive verification, reducing cost while maintaining high utility. The adversarial debate mechanism uncovers hidden biases in automated judgments, offering a pathway to more honest evaluation pipelines.

## Related Concepts  
- Statistics‑first gating: decision based on statistical summaries rather than full inspection.  
- Cost‑aware routing problem: optimization of acquisition decisions under budget constraints.  
- Adjudicative escalation: human‑in‑the‑loop arbitration between competing advocates.  
- Confidence intervals for measurement reliability.  
- Synthetic benchmarks (injected‑knob) for evaluating measurement fidelity.
