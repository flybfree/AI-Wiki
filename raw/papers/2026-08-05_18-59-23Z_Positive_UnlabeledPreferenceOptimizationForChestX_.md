---
title: Positive-Unlabeled Preference Optimization For Chest X-ray Report Generation
published: 2026-08-05T18:59:23Z
authors: Yuta Kobayashi, Pradyun Ramesh, Muhammad Ahmed Chaudhry, Vincent Jeanselme, Judy Wawira Gichoya, Sanmi Koyejo, Kathleen Capaccione, Shalmali Joshi
url: http://arxiv.org/abs/2608.05341v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Positive-Unlabeled Preference Optimization For Chest X-ray Report Generation

## Abstract
Vision-Language Models (VLMs) for radiology report generation are typically trained on retrospective clinical reports, which suffer from omission noise: clinically present findings are left unreported due to the omission of subtle findings. For example, prior studies show that cardiomegaly may be omitted from ICU chest X-ray reports when the imaging request is focused on monitoring support device placement. As a result, models trained with standard approaches inherit these omissions, learning to under-report findings themselves. We propose PU-DPO, a preference optimization framework to prevent omission noise from corrupting the preference signal. We reformulate the objective under a positive-unlabeled (PU) learning framework, treating absent mentions as unlabeled rather than truly negative. Our framework provides preference supervision using constructed contrastive pairs, generated using edits to model responses, producing variants that explicitly mention or omit a specific finding. Generated responses that mention the finding are naturally preferred in the context of visual evidence. Across semi-synthetic experiments and analyses on real-world chest radiograph benchmarks where adjudicated labels are available, PU-DPO yields consistent gains in detection rates and recovery of hidden positives across multiple pathologies, and is more robust to omission noise than prior approaches.

## Metadata
- **Published**: 2026-08-05T18:59:23Z
- **Authors**: Yuta Kobayashi, Pradyun Ramesh, Muhammad Ahmed Chaudhry, Vincent Jeanselme, Judy Wawira Gichoya, Sanmi Koyejo, Kathleen Capaccione, Shalmali Joshi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05341v1)