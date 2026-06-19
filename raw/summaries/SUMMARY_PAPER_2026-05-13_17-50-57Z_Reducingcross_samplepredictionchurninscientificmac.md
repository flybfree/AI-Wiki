---

title: Reducing cross-sample prediction churn in scientific machine learning
url: http://arxiv.org/abs/2605.13826v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-13_17-50-57Z_Reducingcross_samplepredictionchurninscientificmac.md
generated_at: "2026-06-11 10:39"
model: nvidia/nemotron-3-nano-4b

---


## Summary
The paper introduces cross‑sample prediction churn as a gap between aggregate accuracy and label agreement across independent bootstraps of the same training set. It demonstrates that standard parameter‑side methods fail to reduce this churn, while two data‑side approaches — K‑bootstrap bagging and twin‑bootstrap with a sym‑KL loss — can cut churn rates by up to 54 % at modest compute cost.

## Key Takeaways
- Cross‑sample prediction churn is quantified as the mismatch in class labels between two classifiers trained on independent bootstraps, ranging from 8.0 % to 21.8 % of test molecules.
- K‑bootstrap bagging reduces churn by 40–54 % without sacrificing accuracy and requires only K times ERM compute.
- Twin‑bootstrap adds a sym‑KL consistency loss between two networks, achieving an additional median 45 % churn reduction beyond K=2 bagging at twice the ERM cost.

## Context
Scientific machine learning benchmarks currently report only aggregate predictive performance, ignoring whether predictions remain stable across data variations. This omission obscures the effectiveness of data‑centric techniques that can improve robustness without altering model parameters.

## Implications
Including churn metrics alongside accuracy will guide researchers toward methods that truly enhance reliability in scientific ML applications. Practitioners can prioritize data‑side strategies to produce more consistent predictions, reducing downstream errors and improving trust in experimental results.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.13826v1)
