---
title: GazeRefine: Expert Gaze as a Test-Time Prompt for Training-Free Medical Image Segmentation
url: http://arxiv.org/abs/2609.01310v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_14-34-59Z_GazeRefine_ExpertGazeasaTest_TimePromptforTraining.md
generated_at: 2026-09-01 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
GazeRefine is a training‑free framework that leverages sparse fixation data to guide medical image segmentation without requiring masks or fine‑tuning. The method converts gaze cues into semantic prototypes in frozen DINOv3 features and refines them through iterative discrimination, achieving strong performance on colonoscopy images and competitive results on prostate MRI.

## Key Takeaways
- GazeRefine uses duration‑weighted fixations to create foreground and background priors that initialize segmenting prototypes directly from frozen feature space. 
- The refinement loop employs forward‑backward feature affinity propagation anchored to the original gaze guidance, limiting semantic drift while extending segmentation beyond focal regions. 
- No segmentation masks, adapters, prompt encoders, or gradient updates are needed; the system relies solely on raw gaze annotations.

## Context
Medical image segmentation traditionally demands large annotated datasets and costly training pipelines, creating a bottleneck for deployment in clinical settings. This work demonstrates that human‑derived gaze data can serve as an efficient, label‑light alternative to traditional supervision, aligning with trends toward human‑in‑the‑loop AI solutions.

## Implications
Clinicians could provide real‑time gaze feedback during imaging procedures, enabling automated segmentation without additional annotation effort. The approach opens pathways for scalable, low‑cost segmentation tools that integrate directly into existing diagnostic workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01310v1)
