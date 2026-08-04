---
title: Can You Trust the Confidence? ConfBench for Vision-Language Models on Document Extraction
url: http://arxiv.org/abs/2608.01792v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_07-03-51Z_CanYouTrusttheConfidence_ConfBenchforVision_Langua.md
generated_at: 2026-08-03 23:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces ConfBench, a calibration‑focused benchmark for key information extraction in vision‑language models, created by applying twenty controlled degradation pipelines to a diverse document set. The study evaluates four proprietary and three open‑weight VLMs across confidence estimation methods and finds that OCR+Image modality yields the most accurate confidence estimates while model capability is the dominant factor influencing calibration quality.

## Key Takeaways
- OCR+Image modality results in more accurate confidence estimates than other input combinations, indicating a strong link between visual preprocessing and trustworthy scores.  
- Model capability scales confidence quality monotonically across families, whereas parameter count provides little predictive power for calibration performance.  
- Log‑probability with first‑token aggregation consistently outperforms mean‑token and margin aggregations, offering the most reliable method for converting raw probabilities into actionable thresholds.

## Context
The paper addresses a critical gap in AI research where existing document benchmarks lack diverse low‑quality samples needed to assess confidence calibration. By generating a broad spectrum of degraded inputs, ConfBench enables systematic study of how vision‑language models handle uncertainty and how their confidence outputs can be trusted for automated routing decisions.

## Implications
For industry practitioners, the findings suggest that investing in robust OCR pipelines and selecting models with higher capability yields better calibrated confidence scores, reducing reliance on costly human reviews. Practitioners can also leverage log‑probability aggregation to improve threshold‑based routing without sacrificing operational performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01792v1)
