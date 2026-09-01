---
title: Dense Clinical Contrasts Enhance Medical Knowledge Updating in Large Language Models
published: 2026-08-31T07:59:15Z
authors: Yangmin Huang, Shu Quan, He Geng, Xin Ye, Qianyun Du, Zhiyang He, Jiaxue Hu, Xiaodong Tao
url: http://arxiv.org/abs/2608.30405v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dense Clinical Contrasts Enhance Medical Knowledge Updating in Large Language Models

## Abstract
Medical knowledge changes continually, making large language models vulnerable to relying on outdated yet clinically plausible information. We study whether the format of supervision affects medical knowledge updating under a matched training-budget setting. We introduce SEER-Bench, a temporally anchored oncology-staging benchmark curated from the latest versioned SEER Research Data release, and render identical medical update events from NCCN oncology guidelines into four supervision formats: EMQ, MSQ, FITB, and SAQ. Across SEER-Bench and HealthBench Professional, EMQ gives the most stable external transfer and retention among same-budget SFT variants. With EMQ supervision, the updated 4B model produces competitive results on temporally anchored oncology staging, reaching 64.8% answer accuracy and 59.6% rationale accuracy on SEER-Bench. Diagnostic analyses suggest that EMQ exposes denser clinical contrast signals while preserving discriminative representations with smaller movement from the base model. These results show that medical knowledge updating depends not only on the update algorithm, but also on how knowledge is structured as supervision.

## Metadata
- **Published**: 2026-08-31T07:59:15Z
- **Authors**: Yangmin Huang, Shu Quan, He Geng, Xin Ye, Qianyun Du, Zhiyang He, Jiaxue Hu, Xiaodong Tao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30405v1)