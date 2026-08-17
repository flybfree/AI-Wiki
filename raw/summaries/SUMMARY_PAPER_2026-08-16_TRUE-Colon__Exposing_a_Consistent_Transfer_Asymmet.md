---
title: TRUE-Colon: Exposing a Consistent Transfer Asymmetry in Real-Time Polyp Detection
url: http://arxiv.org/abs/2608.13711v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-13_19-13-54Z_TRUE_Colon_ExposingaConsistentTransferAsymmetryinR.md
generated_at: 2026-08-16 21:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces TRUE-Colon, a benchmark that evaluates real-time polyp detection models on both curated lesion clips and full unedited colonoscopy procedures. It finds that models trained only on curated data perform poorly on full procedures while those trained on procedures maintain accuracy. The Transformer detector shows the best sensitivity with early detections.

## Key Takeaways
- Models trained strictly on curated clips suffer severe performance collapse when evaluated on full procedures, indicating a transfer asymmetry.
- Procedure-trained models improve rejection of non-polyp content on REAL-Colon and retain their accuracy on curated benchmarks, showing better deployment relevance.
- The Transformer detector attains the strongest sensitivity and provides persistent detections, while convolutional detectors offer higher throughput.

## Context
Real-time computer-aided detection for colonoscopy faces a gap between laboratory benchmarking and clinical practice. This study highlights how dataset selection can mask transfer failure, affecting trust in AI deployments. Understanding these asymmetries is crucial for developing robust diagnostic tools.

## Implications
Clinicians and developers must prioritize full-procedure data when training and evaluating CADe systems to ensure reliable performance. Shifting benchmarks toward deployment-relevant operating points will reduce clinical miss rates and improve patient outcomes. This research sets a new standard for realistic evaluation in medical AI.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13711v1)
