---
title: Lottery Tickets Are Not Deployment Tickets
published: 2026-07-29T15:25:19Z
authors: Bum Jun Kim
url: http://arxiv.org/abs/2607.27031v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Lottery Tickets Are Not Deployment Tickets

## Abstract
Reports on how sparsification, compression, and lottery tickets change model behavior have been mixed in the prior literature, with beneficial effects observed in some studies and adverse effects in others. Moreover, prior work has not considered actual deployment conditions, where decision logic is already fixed for the incumbent. To assess these mixed findings from a practical standpoint, we study the production-replacement question at the deployment level, namely whether an accuracy-matched lottery ticket or another sparse challenger can replace an incumbent dense model without reconfiguring downstream decision logic. We therefore audit a broad, protocol-specific panel of deployment-relevant behaviors spanning calibration, OOD response, class-level reliability, representations, and downstream policy decisions, and summarize clean-accuracy-excluded deviations with a behavioral-compatibility distance. Across extensive experiments, sparse candidates repeatedly recover dense-reference accuracy yet remain behaviorally different; in several study-band-matched settings, LTs also show lower corruption accuracy. In small-gap settings with fixed-threshold policy diagnostics, lottery-ticket replacement changes 7% to 10% of accept--review decisions. This churn creates precisely the burden that drop-in replacement is meant to avoid: reconfiguring and revalidating downstream decision logic. These findings establish the limits of clean-accuracy certification: Establishing compatibility with a fixed incumbent is distinct from attributing churn uniquely to sparsity or treating every measured deviation as harmful. Our theory explains the routing result: Even exact pointwise top-1 agreement cannot bound fixed-threshold decision changes, and small confidence shifts near the operating boundary can generate first-order routing churn.

## Metadata
- **Published**: 2026-07-29T15:25:19Z
- **Authors**: Bum Jun Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27031v1)