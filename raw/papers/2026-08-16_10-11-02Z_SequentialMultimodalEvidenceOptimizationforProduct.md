---
title: Sequential Multimodal Evidence Optimization for Product Media Ranking in E-Commerce
published: 2026-08-16T10:11:02Z
authors: Prasenjit Dey, Frank McIntyre, Arnab Sinha
url: http://arxiv.org/abs/2608.15662v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Sequential Multimodal Evidence Optimization for Product Media Ranking in E-Commerce

## Abstract
On modern e-commerce stores, customers consume ordered slates of heterogeneous product media, such as images, videos, and 3D renders, before making purchase decisions. Existing media-ranking systems often optimize myopic engagement proxies such as clicks or dwell time, even though product media assets are cooperative informational components of the same item that together help customers find the information they need through sequential interaction. We present Sequential Multimodal Evidence Optimization (SMEO), a two-stage utility-guided framework for customer-oriented media sequencing. SMEO first learns a trajectory utility model from consumed media prefixes to estimate how ordered evidence helps customers reach a purchase decision, while mitigating position-bias and variable-depth imbalance in logged data. Recognizing that customer attention is a limited resource, it then trains an autoregressive ranking policy with survival-weighted reward-to-go that prioritizes the most decision-relevant information early, so customers can find what they need with less effort. By decoupling utility learning from policy optimization, SMEO enables stable offline learning from biased logs and post-hoc media attribution without explicit media-level labels. Evaluated offline on large-scale e-commerce sessions using doubly robust off-policy estimation, SMEO improves estimated conversion by 5.5% and helps customers reach a purchase decision with 15% fewer swipes than existing baselines.

## Metadata
- **Published**: 2026-08-16T10:11:02Z
- **Authors**: Prasenjit Dey, Frank McIntyre, Arnab Sinha
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15662v1)