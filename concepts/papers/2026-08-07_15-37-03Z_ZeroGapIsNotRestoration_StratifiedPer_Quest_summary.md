# Summary: 2026-08-07_15-37-03Z_ZeroGapIsNotRestoration_StratifiedPer_QuestionProb.md
Saved: 2026-08-09 23:08
Source: 2026-08-07_15-37-03Z_ZeroGapIsNotRestoration_StratifiedPer_QuestionProb.md
Model: None

---

## Summary  
The paper tackles contamination in pretrained models where test data leaks into training corpora, inflating benchmark scores. It critiques the prevailing G‑AP (Gap of Aggregate Performance) metric as flawed because it averages probabilities before differencing and uses uniform weighting, which cancels out over‑ and under‑suppression. The authors propose a new approach: stratified per‑question probability gap (SA‑PPG) estimation combined with a step‑wise mitigation strategy called RailCap that caps greedy tokens when contamination is detected. SA‑PPG reveals prior restoration estimates are systematically overestimated, while RailCap achieves the lowest SA‑PPG values.

## Key Contributions  
- Finding 1: Existing contamination mitigation evaluation metrics like G‑AP are flawed because they average probabilities before differencing and use uniform weighting, leading to cancellation of over‑ and under‑suppression.  
- Finding 2: Stratified per‑question probability gap (SA‑PPG) provides a more accurate per‑question estimate by sampling solve probabilities and grouping them within clusters defined by the clean model’s high‑frequency values.  
- Finding 3: RailCap mitigates contamination during generation by capping the next token when a sample falls back onto the greedy trajectory, accumulating suppression until the response distribution becomes sufficiently dispersed.

## Methodology  
The authors first compute per‑question solve probabilities for both contaminated and clean models via Monte Carlo sampling. They then calculate the probability gap per question and aggregate within clusters determined by the clean model’s high‑frequency values to isolate contamination impact. For mitigation, RailCap monitors generated tokens; if a token matches the greedy path from the clean model, it is replaced with the runner‑up candidate, effectively suppressing memorized answers and encouraging diversity.

## Results  
Experiments on multiple contaminated models across several benchmarks show that SA‑PPG reduces overestimated restoration scores by up to 30 % compared to prior methods. RailCap consistently yields the lowest SA‑PPG values, indicating more faithful suppression of contamination while preserving model utility. The stratified aggregation reveals systematic underestimation in earlier metrics due to averaging effects.

## Significance  
This work provides a rigorous evaluation framework for contamination mitigation that aligns restoration with actual per‑question performance degradation. By decoupling estimation from generation and focusing on probability gaps, it enables more honest assessment of how well models recover from memorization. The proposed RailCap technique offers a practical decoding strategy to suppress contaminated answers without sacrificing overall model quality.

## Related Concepts  
Contamination, pretraining data leakage, G‑AP metric, per‑question evaluation, stratified aggregation, greedy trajectory, response distribution, mitigation strategies, restoration of performance.
