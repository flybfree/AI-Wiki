# Summary: 2026-07-21_10-52-04Z_SFGA_AStatistics_FirstGatingArchitecturewithAdjudi.md
Saved: 2026-07-24 01:00
Source: 2026-07-21_10-52-04Z_SFGA_AStatistics_FirstGatingArchitecturewithAdjudi.md
Model: None

---

## Summary  
The paper introduces SFGA, a statistics‑first gating architecture that treats supervised fine‑tuning (SFT) data procurement as a cost‑aware routing problem across three intrinsic quality axes—diversity, utility, and redundancy. It uses cheap blind measurements with confidence intervals to decide whether a corpus is acceptable or escalates the case to an adjudicative debate between a buy‑advocate and reject‑advocate judge.

## Key Contributions  
- [Finding 1] The authors propose SFGA, a gating architecture that treats procurement as a cost‑aware routing problem over three intrinsic quality axes—diversity, utility, and redundancy.  
- [Finding 2] They demonstrate that the gate reaches 0.90 accuracy and 0.83 F1 on a controlled benchmark while spending $0.017 per unit of data procured, outperforming an always‑verify baseline (accuracy 0.75) and approaching an oracle upper bound (0.98).  
- [Finding 3] Honest negative diagnostics reveal that the adjudicative debate path has a con‑side win rate of 0.80 (p≈3×10⁻⁶) and a 52 % position‑flip rate when advocate swapping is exposed, exposing hidden biases in naive LLM judges.

## Methodology  
The authors approached the problem by first quantifying each dataset on three intrinsic quality axes using cheap blind measurements that produce per‑axis estimates with confidence intervals. The gating decision is made only if all intervals are tight, sample sizes are adequate, and the axes agree; otherwise an adjudicative debate between a buy‑advocate and reject‑advocate judge is triggered, whose verdict resolves the case. A synthetic benchmark for measurement fidelity and routing calibration ensures that experimental results reflect realistic data procurement.

## Results  
On a controlled 12‑dataset grid (2×3×2) with five seeds, SFGA achieved 0.90 accuracy and 0.83 F1 at $0.017 per unit of data procured. This outperforms the always‑verify baseline (accuracy 0.75) and is within 0.10 of an oracle upper bound (0.98), while staying under the cost of always‑escalate ($0.020). Honest negative diagnostics show a con‑side win rate of 0.80 with p≈3×10⁻⁶ and a 52 % position‑flip rate when advocate swapping is exposed, indicating that naive LLM judges may conceal negativity and positional biases.

## Significance  
SFGA provides a statistically grounded framework for trustworthy SFT data procurement, balancing cost efficiency with quality assurance. By integrating confidence intervals and an adjudicative escalation mechanism, it mitigates the risk of accepting low‑quality or biased corpora while avoiding unnecessary expense. The transparent negative diagnostics also highlight limitations of automated LLM judges, guiding future research toward more reliable evaluation.

## Related Concepts  
- Statistics‑first gating architecture  
- Cost‑aware routing problem over intrinsic quality axes (diversity, utility, redundancy)  
- Adjudicative escalation with buy‑advocate/reject‑advocate judges  
- Confidence intervals for blind measurements  
- Synthetic benchmark for measurement fidelity and routing calibration
