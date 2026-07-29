---
title: TWICE: Two-Clock, Two-Window Learning for Long-Horizon Conversion Prediction in Online Advertising
published: 2026-07-28T08:02:41Z
authors: Kaiyuan Li, Kun Wang, Zhongbo Wang, Teng Sha, Ming Yan, Yanhua Cheng, Xialong Liu
url: http://arxiv.org/abs/2607.25404v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TWICE: Two-Clock, Two-Window Learning for Long-Horizon Conversion Prediction in Online Advertising

## Abstract
Long-horizon conversion prediction under delayed feedback creates a two-clock, two-window learning problem in online advertising. A short base observation window releases recent clicks on the click clock before their outcomes mature, whereas conversions continue to arrive on the conversion clock throughout a longer target conversion window. The click clock provides timely but partially observed status supervision. The conversion clock reveals long-tail delays, but the delay composition within an arrival-time slice is weighted by historical click cohorts with different traffic volumes and target-window conversion rates.   We present TWICE, a framework that factorizes long-horizon post-click conversion rate (CVR) into a target-window conversion probability and a grouped elapsed-delay cumulative distribution function (CDF). The two clocks provide complementary supervision. Click-clock records train the target-window CVR head through a current-status likelihood over the base observation window. Newly arrived conversions train the delay model on the conversion clock. To account for the cohort mixture, TWICE uses fixed click-time predicted CVR (pCVR) mass as cohort exposure in an arrival-conditioned likelihood. This accounts for differences in cohort traffic and conversion propensity. The resulting aggregate records are self-contained. A single learned CDF produces monotone predictions for all requested horizons up to the target conversion window. Serving requires neither historical lookup nor convolution. Experiments on a public benchmark and an industrial advertising dataset demonstrate the effectiveness of TWICE. In an online A/B test in Kwai's advertising system, TWICE increased expected revenue, revenue, and conversions by 2.486%, 1.858%, and 2.061%, respectively. It was subsequently deployed to full traffic.

## Metadata
- **Published**: 2026-07-28T08:02:41Z
- **Authors**: Kaiyuan Li, Kun Wang, Zhongbo Wang, Teng Sha, Ming Yan, Yanhua Cheng, Xialong Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25404v1)