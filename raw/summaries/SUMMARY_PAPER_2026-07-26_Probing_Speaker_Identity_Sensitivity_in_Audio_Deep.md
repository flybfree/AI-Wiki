---
title: Probing Speaker Identity Sensitivity in Audio Deepfake Detectors
url: http://arxiv.org/abs/2607.21820v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-23_21-12-33Z_ProbingSpeakerIdentitySensitivityinAudioDeepfakeDe.md
generated_at: 2026-07-26 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how audio deepfake detectors become overly sensitive to speaker identity rather than synthesis artifacts. The authors introduce the Identity Sensitivity Score (ISS) as a diagnostic that measures label shifts across different speakers without needing ground truth at inference time. Experiments show that misclassified utterances exhibit ISS values 29‑52 times higher than correct ones, and ISS alone predicts errors with AUC up to 0.954.

## Key Takeaways
- The Identity Sensitivity Score quantifies per‑utterance changes in detector output when the speaker identity varies, revealing a hidden reliance on speaker cues rather than synthetic content.
- Incorrect classifications are found to be dramatically more sensitive to identity shifts (29‑52×) compared with correct ones, indicating that detector confidence is often misaligned with true error sources.
- ISS can be computed solely from the detector score and a reference pool of speaker examples, offering an inference‑time tool for diagnosing speaker‑dependent failures.

## Context
Audio deepfake detection remains a critical AI application where performance varies widely across datasets. Traditional detectors are trained on labeled corpora that inadvertently link speaker identity to authenticity, leading to biased models. This work highlights the need for metrics that expose such idiosyncratic behavior beyond simple accuracy measures.

## Implications
For practitioners, ISS provides an actionable diagnostic to audit and improve detector robustness against speaker‑dependent attacks. In industry, adopting this score can prevent false confidence in deepfake detection systems, reducing reliance on misleading performance numbers across diverse user bases.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21820v1)
