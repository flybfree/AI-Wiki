---
title: More Data, Worse Decisions? Preference Reversals in Neural Networks under Gram Incompatibility
published: 2026-07-28T18:52:47Z
authors: Yanli Yan, Yuanzheng Li, Yong Zhao, Hongbo Guo, Shoudong Han
url: http://arxiv.org/abs/2607.27255v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# More Data, Worse Decisions? Preference Reversals in Neural Networks under Gram Incompatibility

## Abstract
Neural networks increasingly combine data across populations, time periods, and operating conditions to improve generalization. This raises a reliability question: whether a model refitted on pooled data preserves an action ordering supported by both sources. Case-Based Decision Theory (CBDT) formalizes this requirement through its composition axiom, which requires source-supported preferences to survive their union. We study when this property holds for fixed-representation neural networks with ordinary least squares (OLS) output heads. First, we show that pooled refitting recomputes the inverse-Gram geometry used to weight source evidence, which can reverse shared preferences, and derive exact and approximate preservation conditions. Next, we introduce a scale-invariant Gram mismatch measure for prioritizing candidate pools and geometry-oriented regularization for shaping source geometry during training. Finally, we develop a three-stage audit that traces strict pairwise reversals through decision changes to task-defined utility loss. Experiments spanning a load-based bidding proxy and medical and financial decision proxies reveal stable and reversal-prone pooling regimes: the load audit identifies a measurable nonzero class of source-consensus-relative harmful decisions under the proxy utility, while cross-domain audits show that comparable mismatch can correspond to sharply different preservation rates. Geometry-oriented objectives occupy distinct descriptive accuracy-consistency-geometry-harm operating points. Together, the framework makes compositional reliability measurable and operational through screening, analytic certification, geometry-oriented training, and decision-consequence auditing.

## Metadata
- **Published**: 2026-07-28T18:52:47Z
- **Authors**: Yanli Yan, Yuanzheng Li, Yong Zhao, Hongbo Guo, Shoudong Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27255v1)