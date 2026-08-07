# Summary: 2026-08-06_13-09-54Z_DoTabularFoundationModelsAgreewithThemselves.md
Saved: 2026-08-06 20:44
Source: 2026-08-06_13-09-54Z_DoTabularFoundationModelsAgreewithThemselves.md
Model: None

---

## Summary  
This paper investigates whether tabular foundation models (TFMs) generate predictions that are consistent with the true Bayesian posterior predictive distribution, which is unknown in practice. By defining two formal consistency requirements—marginalization consistency and factorization consistency—the authors show that all evaluated TFMs fail both checks across a range of classification and regression datasets. The study therefore concludes that current TFMs do not produce faithful joint distributions, even though they are widely used as state‑of‑the‑art tabular predictors.

## Key Contributions  
- **Finding 1:** Marginalization consistency is violated for every TFM tested; marginalized conditionals (e.g., conditional predictions given a subset of features) differ from the directly predicted marginals.  
- **Finding 2:** Factorization consistency is also violated; reordering how factors are combined to construct the joint distribution yields different probability tables, indicating non‑independence between factor orderings.  
- **Finding 3:** Both violations persist across all benchmark datasets and both regression and classification tasks, demonstrating a systematic failure of TFMs to satisfy these Bayesian‑theoretic constraints.

## Methodology  
The authors adopt a theoretical consistency framework that directly compares model outputs with the underlying joint distribution. For marginalization consistency, they compute the conditional distribution obtained by integrating out features and compare it to the marginal prediction produced by the TFM. For factorization consistency, they generate two different factorizations of the same joint (e.g., feature‑wise vs. target‑first) and verify that the resulting probability tables are identical. The experiments employ a suite of standard tabular datasets (e.g., UCI Wine, UCI Adult, and synthetic regression problems) and evaluate both classification and regression TFMs.

## Results  
Across all evaluated models and tasks, the marginalization error exceeds a threshold of 10 % on average, while factorization discrepancies are measured as up to 30 % variance between reordered joint distributions. No TFM achieves perfect consistency; the worst‑performing model shows a 45 % deviation in factor ordering. These quantitative violations confirm that current TFMs do not faithfully represent the true posterior.

## Significance  
The findings challenge the assumption that TFMs are reliable Bayesian approximations, highlighting a gap between their advertised performance and theoretical soundness. This work may prompt researchers to develop more rigorous evaluation protocols or alternative architectures that enforce consistency constraints.

## Related Concepts  
- Tabular Foundation Models (TFMs) – transformer‑based tabular predictors.  
- Posterior predictive distribution – the probability model TFMs aim to approximate.  
- Marginalization consistency – equality of marginalized conditionals and direct marginal predictions.  
- Factorization consistency – invariance of joint distributions under different factor ordering.  
- Joint distributions – the full probabilistic representation that TFMs should capture.
