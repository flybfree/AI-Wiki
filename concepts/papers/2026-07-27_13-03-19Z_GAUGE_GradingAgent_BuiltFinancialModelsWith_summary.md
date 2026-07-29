# Summary: 2026-07-27_13-03-19Z_GAUGE_GradingAgent_BuiltFinancialModelsWithoutaGol.md
Saved: 2026-07-28 22:22
Source: 2026-07-27_13-03-19Z_GAUGE_GradingAgent_BuiltFinancialModelsWithoutaGol.md
Model: None

---

## Summary  
The paper GAUGE (Grading Agent‑Built Financial Models Without a Golden Answer) investigates why analyst valuation forecasts often lack consensus and proposes a benchmark that evaluates agent‑generated financial models against the actual distribution of professional opinions rather than a single “golden” answer. By constructing a large, vendor‑classified dataset of 1 001 workbooks and a 196‑task evaluation set, GAUGE introduces an envelope‑based grading scheme with eight validity gates and deterministic structural checks to capture the multi‑facet nature of analyst practice. The study demonstrates that current agents can build robust models but struggle with valuation judgment, highlighting a gap between technical competence and expert insight.

## Key Contributions  
- [Finding 1] GAUGE reveals that across 108 directed pairs for 65 companies the median single‑reference score is only 0.33, indicating that most analyst forecasts are far below the ideal threshold of 0.70 and that no pair agrees on implied price within ten percent.  
- [Finding 2] The benchmark’s three‑layer observed‑practice envelope and eight validity gates produce a failure‑aware score φ₀ where senior analysts average 88.3, juniors 66.0, and finance students 43.2, quantifying grade differences across experience levels.  
- [Finding 3] Across 24 agents generating 1 011 valuations the best agent scores 53.4 on GAUGE, surpassing student performance but still falling short of senior analysts, and it passes 93 % of mechanical facets while only 78 % of judgment facets.

## Methodology  
GAUGE builds a benchmark by aggregating vendor‑classified analyst workbooks into a controlled training split and a withheld refresh pool. It defines an eight‑gate validity framework that checks structural consistency, discount‑rate plausibility, and price bounds before allowing scoring. The observed‑practice envelope consists of three tiers (high, medium, low) representing the spread of expert opinions, while 56 auditable facets capture aspects such as model construction quality, valuation judgment, and consistency with market data. All gates are deterministic, ensuring reproducibility.

## Results  
The 55‑participant known‑groups study confirms that senior analysts outperform juniors and students on φ₀, and the cross‑fitting experiment shows agents align better with senior expectations than with junior or student groups. The fleet‑median gap of 26 points underscores persistent performance disparity between agents and human experts in valuation judgment.

## Significance  
GAUGE shifts the evaluation paradigm from a single expert reference to an empirically grounded, multi‑faceted benchmark that reflects real analyst heterogeneity. This enables fairer comparison of agent models, guides research on improving both model construction and valuation reasoning, and provides a reproducible framework for future AI‑driven finance tools.

## Related Concepts  
- Financial modeling (valuation)  
- Analyst consensus and disagreement  
- Multi‑facet evaluation frameworks  
- Validity gates in benchmarking  
- Ensemble scoring with tolerance envelopes
