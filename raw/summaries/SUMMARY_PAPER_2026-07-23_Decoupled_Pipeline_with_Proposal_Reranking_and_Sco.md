---
title: Decoupled Pipeline with Proposal Reranking and Score Fusion for Positive-Unlabeled Marine Species Detection
url: http://arxiv.org/abs/2607.18700v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_04-35-47Z_DecoupledPipelinewithProposalRerankingandScoreFusi.md
generated_at: 2026-07-23 23:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents DS@GT ARC, a multi‑stage pipeline for the positive‑unlabeled marine species detection challenge FathomNetCLEF 2026. The system leverages a frozen Megalodon YOLOv8x detector to generate class‑agnostic proposals, refines them with a LoRA‑fine‑tuned DINOv3 ViT‑H classifier, and fuses detector and classifier scores using geometric weighting. The approach achieved 12th place on the private leaderboard, while a variant adding a locally trained TTN validity head improved public and proxy metrics but slightly lowered private performance.

## Key Takeaways
- The frozen YOLOv8x detector provides reliable proposal generation without additional training, preserving data efficiency in a sparse‑label setting.  
- Combining global and tiled inference with edge filtering improves recall while reducing false positives, highlighting the importance of careful post‑processing.  
- Ranking predictions via weighted geometric fusion outperforms direct classifier fine‑tuning or reliance on noisy pseudo‑labels.

## Context
The FathomNetCLEF competition exemplifies real‑world challenges where training data is limited and test images are out‑of‑distribution, a common scenario in few‑shot and domain‑shift detection tasks. This work contributes to the broader AI community by demonstrating how frozen detectors can serve as effective proposal generators when downstream classification models are fine‑tuned with lightweight adapters.

## Implications
For marine biodiversity monitoring, this pipeline offers a practical solution that requires minimal labeled data and can be deployed on edge hardware without retraining large models. Practitioners should prioritize recall preservation and intelligent ranking over aggressive detector updates or reliance on noisy pseudo‑labels to achieve robust performance in resource‑constrained environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18700v1)
