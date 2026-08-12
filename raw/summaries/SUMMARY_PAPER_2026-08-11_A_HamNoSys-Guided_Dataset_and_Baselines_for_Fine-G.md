---
title: A HamNoSys-Guided Dataset and Baselines for Fine-Grained Isolated Handshape Recognition in Sign Language
url: http://arxiv.org/abs/2608.10588v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_07-16-52Z_AHamNoSys_GuidedDatasetandBaselinesforFine_Grained.md
generated_at: 2026-08-11 22:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a benchmark for fine‑grained isolated handshape recognition in sign language using the Hamburg Notation System. It presents a balanced dataset of 144,000 RGB images and evaluates four model families across subject‑dependent and leave‑one‑out splits.

## Key Takeaways
- The study uses a dataset of 144,000 images covering 160 handshape classes defined by HamNoSys to create a reproducible benchmark for isolated handshape recognition.  
- Subject‑dependent splits yield stable performance across models, while leave‑one‑subject‑out evaluation shows a drop from around 85% top‑1 accuracy on the ASL Fingerspelling Dataset A to about 83%.  
- The results highlight that appearance‑based models like ResNet‑18 and ViT‑B/16 perform well, but graph convolutional networks and XGBoost from landmarks can match or exceed them when trained on the same data.

## Context
Fine‑grained handshape recognition is a foundational task for sign language transcription systems that aim to be language‑independent and accessible. This work contributes to AI research by providing a large, curated dataset and systematic evaluation protocols.

## Implications
For practitioners developing real‑time sign language translation tools, the benchmark offers a reliable measure of model generalization across participants. It also guides future research toward robust, participant‑agnostic models that can operate in diverse user groups.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10588v1)
