# Summary: 2026-07-28_08-02-41Z_TWICE_Two_Clock_Two_WindowLearningforLong_HorizonC.md
Saved: 2026-07-28 22:33
Source: 2026-07-28_08-02-41Z_TWICE_Two_Clock_Two_WindowLearningforLong_HorizonC.md
Model: None

---

## Summary  
This paper addresses the challenge of predicting long‑horizon conversion rates in online advertising where feedback arrives after a delay, forming a two‑clock, two‑window learning problem. It proposes TWICE, a framework that separates prediction into a target‑window CVR and an arrival‑conditioned cumulative delay CDF component. The click clock supplies timely but partial supervision while the conversion clock captures long‑tail delays weighted by historical cohorts. By factorizing these components, TWICE enables monotone horizon predictions without lookup or convolution.

## Key Contributions  
- [Finding 1] TWICE decomposes long‑horizon CVR prediction into a target‑window conversion probability and an arrival‑conditioned cumulative delay CDF.  
- [Finding 2] The click clock trains the target‑window head via current‑status likelihood, while newly arrived conversions train the delay model on the conversion clock.  
- [Finding 3] Fixed click‑time predicted CVR mass is used as cohort exposure to handle traffic and conversion rate heterogeneity across arrival slices.

## Methodology  
The authors treat the problem as a two‑clock learning scenario: a short base observation window (click clock) records recent clicks before outcomes mature, and a longer target conversion window (conversion clock) observes delayed conversions. They factorize prediction into pCVR mass and CDF, using an arrival‑conditioned likelihood that incorporates predicted CVR per click time as cohort exposure. The learned CDF is monotone and serves all horizons up to the target window, eliminating need for historical lookup or convolution.

## Results  
Experiments on a public benchmark dataset and an industrial advertising platform show TWICE improves expected revenue by 2.486%, conversions by 2.061% and revenue (same) by 1.858% compared to baseline methods. In an online A/B test within Kwai’s ad system, deployment led to full‑traffic rollout.

## Significance  
This work demonstrates that separating short‑term click supervision from long‑term conversion delay can yield substantial performance gains in real‑time advertising systems where feedback is delayed and cohorts vary. By providing monotone horizon predictions efficiently, TWICE reduces latency and operational complexity while boosting revenue.

## Related Concepts  
- Two‑clock learning  
- Conversion rate prediction  
- Delayed feedback  
- Cumulative distribution function (CDF) modeling  
- Cohort exposure weighting  
- Monotone prediction
