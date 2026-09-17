---
title: The Mirage of Calibrated Confidence: Trajectory-Independence of Verbalized Confidence in Vision-Language Models
published: 2026-09-16T10:45:11Z
authors: Jisoo Yang, Jaeho Han, Trung X. Pham, Junyeong Kim
url: http://arxiv.org/abs/2609.18453v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Mirage of Calibrated Confidence: Trajectory-Independence of Verbalized Confidence in Vision-Language Models

## Abstract
A calibrated Vision-Language Model (VLM) can repeatedly self-correct, say "Wait, I should recheck," arrive at the wrong answer, and still report high confidence. We find that this occurs because verbalized confidence is largely trajectory-independent in the VLMs and calibration methods we evaluate. We examine this through three complementary lenses: content variation, token masking, and the model's own hesitation markers. We show that confidence is insufficiently sensitive to what the reasoning trajectory actually contains, and that calibration training can paradoxically worsen this disconnect. Since existing metrics like ECE and AUROC cannot detect this problem, we propose the Trajectory-Grounding Score (TGS) in two complementary forms: TGS-self, which compares confidence with and without access to the model's own trajectory, and TGS-pair, which tests whether the model assigns higher confidence to correct trajectories than to flawed ones along the vision, reasoning, and answer axes. We propose TGS-Bench, a model-agnostic suite spanning 10 benchmarks with controlled good/bad trajectory pairs, and show that conventional calibration rankings diverge from trajectory-grounding rankings, exposing a blind spot in current evaluation practice.

## Metadata
- **Published**: 2026-09-16T10:45:11Z
- **Authors**: Jisoo Yang, Jaeho Han, Trung X. Pham, Junyeong Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.18453v1)