# Summary: 2026-07-21_11-37-57Z_TheTractabilityLandscapeofSamplingwithInexactScore.md
Saved: 2026-07-24 00:45
Source: 2026-07-21_11-37-57Z_TheTractabilityLandscapeofSamplingwithInexactScore.md
Model: None

---

## Summary  
The paper investigates when sampling from a target distribution can be performed with vanishing total‑variation bias using an oracle that provides inexact scores, extending prior work to a broader class of error assumptions. It establishes a simple and tight characterization of the score‑error conditions that still allow unbiased sampling, showing that any error weaker than sub‑Gaussian precludes algorithmic tractability. This result strengthens earlier conclusions (e.g., CCSW26) by making them algorithm‑agnostic across many practical settings. The authors thus provide a clear “tractability landscape” for inexact score access in learning theory.

## Key Contributions  
- [Finding 1] A precise characterization of the error bounds on an inexact score oracle that still permit sampling with vanishing total‑variation bias, expressed as a condition on the sub‑Gaussian norm of the target.  
- [Finding 2] Proof that any error assumption weaker than sub‑Gaussian (i.e., larger variance or non‑sub‑Gaussian tails) rules out unbiased sampling algorithms, regardless of their complexity.  
- [Finding 3] Extension of existing algorithm‑agnostic results to a wider class of target families and score‑oracle models, demonstrating that the bound holds beyond the specific assumptions of prior work.

## Methodology  
The authors start from the standard setup where an oracle returns noisy estimates of the true score for each sample. They analyze the bias incurred by sampling algorithms under various error models, employing concentration inequalities to bound total variation deviation. By comparing these bounds with known sub‑Gaussian guarantees, they derive necessary and sufficient conditions on the noise level that keep bias vanishing. The analysis is theoretical, relying on probability theory rather than empirical experiments.

## Results  
The main theorem states: if the score oracle error satisfies \( \|\epsilon\|_{\psi_2} = o(1) \), then unbiased sampling with vanishing total variation is tractable; conversely, if \( \|\epsilon\|_{\psi_2} \ge c > 0 \) for some constant, no algorithm can achieve unbiasedness. This result refines the earlier claim that sub‑Gaussian error is necessary and shows it is also sufficient up to a vanishing factor.

## Significance  
By proving that any non‑sub‑Gaussian score error eliminates tractability, the paper clarifies the limits of current learning algorithms and informs future work on robust sampling. It removes ambiguity about whether algorithmic complexity alone can compensate for weak oracle guarantees, reinforcing the importance of accurate score estimation in theoretical analysis.

## Related Concepts  
- Inexact score oracle: a function that returns noisy estimates of the true gradient or derivative.  
- Total variation bias: deviation of empirical distribution from target measured via total variation distance.  
- Vanishing total variation bias: a bias that tends to zero as sample size grows.  
- Sub‑Gaussian assumption: a concentration property on the error magnitude, crucial for many theoretical results.  
- Unbiased sampling: obtaining an empirical distribution indistinguishable from the target in total variation up to negligible terms.
