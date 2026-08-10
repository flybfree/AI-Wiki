# Summary: 2026-08-07_15-37-03Z_ZeroGapIsNotRestoration_StratifiedPer_QuestionProb.md
Saved: 2026-08-09 23:10
Source: 2026-08-07_15-37-03Z_ZeroGapIsNotRestoration_StratifiedPer_QuestionProb.md
Model: None

---

## Summary  
The paper tackles the problem of benchmark contamination, where pretraining data inadvertently leaks into test sets and inflates evaluation scores. It critiques the prevailing G‑AP metric as flawed because it averages probabilities before differencing, causing cancellation errors. The authors introduce SA‑PPG—a stratified per‑question probability gap estimator—and a decoding strategy called RailCap that caps greedy tokens to suppress memorization. Experiments across multiple contaminated models and benchmarks show that prior restoration metrics are systematically overestimated while RailCap yields the lowest SA‑PPG.

## Key Contributions  
- [Finding 1] The G‑AP metric is flawed because it averages solve probabilities before differencing, leading to cancellation of over‑ and under‑suppression.  
- [Finding 2] Stratified per‑question probability evaluation (SA‑PPG) provides a more accurate assessment by sampling each question’s solve probability and grouping them within strata defined by the clean model’s probabilities.  
- [Finding 3] RailCap mitigates contamination during generation by capping greedy trajectory tokens, which accumulates suppression until the response distribution becomes sufficiently dispersed.

## Methodology  
The authors evaluate contaminated models on several public benchmarks. For each question they perform Monte‑Carlo sampling to estimate the model’s solve probability and compare it with the clean model’s probability within predefined strata. The per‑question gaps are then aggregated to compute SA‑PPG, which quantifies contamination severity. Simultaneously, RailCap is implemented as a decoding post‑processor: whenever a token follows the greedy path, the next token is replaced by the runner‑up candidate, effectively suppressing memorized answers until the distribution spreads.

## Results  
SA‑PPG reveals that prior restoration metrics consistently overestimate true capability recovery, indicating systematic bias in their evaluation. RailCap consistently achieves the lowest SA‑PPG across all tested models and datasets, demonstrating superior contamination suppression. The quantitative gap between predicted and actual performance is significantly reduced compared with G‑AP‑based assessments.

## Significance  
Accurate contamination detection is essential for trustworthy AI research; inaccurate metrics can mislead practitioners into believing that mitigation strategies are effective when they are not. By correcting the flawed G‑AP metric and offering a decoding‑level suppression method, this work advances both theoretical understanding and practical deployment of robust evaluation pipelines.

## Related Concepts  
Contamination, benchmark leakage, G‑AP (Gap of Aggregate Performance) metric, per‑question probability estimation, stratified aggregation, greedy decoding, RailCap token capping, suppression accumulation.
