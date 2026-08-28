---
title: Beyond F1: Evaluating Coverage and Failure Recovery in AI Model Security Scanners
published: 2026-08-27T17:49:28Z
authors: Qianlong Lan, Vinothini Pandurangan, Anuj Kaul, Indranil Sanyal
url: http://arxiv.org/abs/2608.27424v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond F1: Evaluating Coverage and Failure Recovery in AI Model Security Scanners

## Abstract
Static scanners are increasingly used to identify executable or otherwise unsafe content in machine- learning artifacts, yet conventional evaluation metrics characterize only cases where a scanner yields a usable security judgment. We evaluate ModelScan, ModelAudit, and Fickling using a controlled, artifact-backed benchmark on a synthetic corpus of 170 Pickle and PyTorch focused artifacts across 145 specimen families, 135 of which have binary security ground truth and 10 of which are intentionally malformed without labels. We explicitly distinguish non-N/A coverage, analysis completion, definitive security decisions, non-security findings, and unsupported outcomes. On labeled families, ModelAudit produced definitive security decisions for all 135 families (100%), Fickling for 110 (81.5%), and ModelScan for 67 (49.6%). Conditional on making a definitive judgment, ModelScan achieved 100% precision, recall, and F1. Fickling identified no unique true- positive families beyond those found by the combination of ModelAudit and ModelScan. Furthermore, for the 48 malicious families where ModelScan failed to complete its analysis, both ModelAudit and Fickling generated detections consistent with ground truth. These findings underscore the need to separate judgment accuracy from judgment availability, as well as incremental detection coverage from tool-level redundancy.

## Metadata
- **Published**: 2026-08-27T17:49:28Z
- **Authors**: Qianlong Lan, Vinothini Pandurangan, Anuj Kaul, Indranil Sanyal
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27424v1)