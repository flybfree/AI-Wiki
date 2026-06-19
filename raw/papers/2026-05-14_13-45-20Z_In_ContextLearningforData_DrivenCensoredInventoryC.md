---

title: In-Context Learning for Data-Driven Censored Inventory Control
published: "2026-05-14T13:45:20Z"
authors: Sohom Mukherjee, Anh-Duy Pham, Richard Pibernik, Yunbei Xu
url: http://arxiv.org/abs/2605.14840v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# In-Context Learning for Data-Driven Censored Inventory Control



**Source**: [Original Paper](http://arxiv.org/abs/2605.14840v1)
## Abstract
We study inventory control with decision-dependent censoring, focusing on the censored or repeated newsvendor (R-NV), where each order quantity determines whether demand is fully observed or censored by sales. Existing approaches based on parametric Thompson sampling (TS) can be brittle under prior mismatch, while offline imputation methods need not transfer to online learning. Motivated by the predictive view of decision making, we combine these ideas by taking oracle actions on learned completions of latent demand. We propose in-context generative posterior sampling (ICGPS), which uses modern generative models that are meta-trained offline and deployed online by in-context autoregressive generation. Theoretically, we show that the Bayesian regret of ICGPS with a learned completion kernel is bounded by the Bayesian regret of a TS benchmark with the ideal completion kernel plus a deployment penalty scaling as $\sqrt{T}$ times the square root of the completion mismatch. This yields a plug-in template for operational problems with known TS regret bounds. For R-NV, we derive sublinear Bayesian regret by reducing censored feedback to bandit convex optimization feedback. We also show that, under reasonable coverage and stability assumptions, the online completion mismatch is controlled by the offline censored predictive mismatch, so offline predictive quality transfers to online performance. Practically, we instantiate ICGPS with ChronosFlow, which combines a frozen time-series transformer backbone with a trainable conditional normalizing-flow head for fast censoring-consistent sampling. In benchmark experiments, ChronosFlow-ICGPS matches correctly specified TS, outperforms myopic and UCB-style baselines, and is robust to prior mismatch and distribution shift. ChronosFlow-ICGPS also performs well for the real-world SuperStore dataset, especially under heavy censoring.

## Metadata
- **Published**: 2026-05-14T13:45:20Z
- **Authors**: Sohom Mukherjee, Anh-Duy Pham, Richard Pibernik, Yunbei Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.14840v1)