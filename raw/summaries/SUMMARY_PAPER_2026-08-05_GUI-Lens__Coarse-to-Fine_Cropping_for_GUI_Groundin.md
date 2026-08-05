---
title: GUI-Lens: Coarse-to-Fine Cropping for GUI Grounding with General-Purpose VLMs
url: http://arxiv.org/abs/2608.03270v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_07-47-37Z_GUI_Lens_Coarse_to_FineCroppingforGUIGroundingwith.md
generated_at: 2026-08-05 01:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces GUI‑Lens, a coarse‑to‑fine grounding framework that enables general‑purpose vision‑language models to locate UI elements in high‑resolution screens by iteratively cropping and enlarging views based on OCR text and detected components. By providing precise coordinate references from the initial screenshot, the system selects progressively finer regions until the target is identified, resulting in a final click mapped back to original screen coordinates. Experiments show up to 24.9 percentage point accuracy gains across benchmarks with GPT‑5.5.

## Key Takeaways
- GUI‑Lens extracts OCR text and detected UI components from screenshots and uses their positions as coordinate references for the VLM.
- The framework selects region and scale of next view, cropping and enlarging to provide finer visual details iteratively until target is determined.
- The final local position is mapped back to original screen coordinates, improving overall grounding accuracy by up to 24.9 percentage points.

## Context
GUI grounding remains a bottleneck for reliable GUI agents because high‑resolution screens contain dense UI elements that are hard to pinpoint with coarse predictions. General‑purpose VLM backends lack specialized training on such tasks, making them vulnerable to visual ambiguity and propagation errors. This work demonstrates how active observation can overcome these limitations.

## Implications
The method offers a scalable approach for deploying VLM‑based GUI agents in real‑world applications where precise interaction matters. By reducing reliance on exact pixel‑level predictions, it lowers error propagation and improves user experience across diverse interfaces. Practitioners can integrate GUI‑Lens into existing vision pipelines to enhance accuracy without retraining specialized models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03270v1)
