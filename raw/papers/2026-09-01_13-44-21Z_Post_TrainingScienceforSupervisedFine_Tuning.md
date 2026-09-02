---
title: Post-Training Science for Supervised Fine-Tuning
published: 2026-09-01T13:44:21Z
authors: Charles O'Neill, Mudith Jayasekara, Harry Partridge
url: http://arxiv.org/abs/2609.01244v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Post-Training Science for Supervised Fine-Tuning

## Abstract
Every supervised fine-tuning run forces the same chain of decisions, such as learning rate, batch size, LoRA or full fine-tuning, how many epochs, which optimiser, and what data to feed the model. Each of these is typically rediscovered from scratch for every new model and dataset. Here we measure them under one instrument: a sweep that varies one lever at a time, and spans dense and mixture-of-experts models in two families (Qwen3 and Llama), on four real-world customer SFT datasets, for both LoRA and full fine-tuning. These datasets give a controlled testbed: each task carries an evaluation built with the customer, and its training data is produced by iterative supervised fine-tuning that refines model outputs until they pass that evaluation, so the supervised target is internally consistent and the task judge we report against is the criterion the data was built to satisfy. We ask how the optimal learning rate and batch size move with model scale, family, and data, and whether one selection rule transfers across them; what LoRA trades against full fine-tuning, and how its rank and alpha set what the adapter can learn; whether validation loss (or other metrics, such as loss landscape flatness) faithfully ranks downstream quality; whether post-training gains scale with model size and data volume, on a model ladder extended through mixtures-of-experts to 235B parameters; how many epochs to train before general instruction-following erodes; and whether a geometry-aware optimiser improves on AdamW. Each recommendation is paired with a measure of its uncertainty.

## Metadata
- **Published**: 2026-09-01T13:44:21Z
- **Authors**: Charles O'Neill, Mudith Jayasekara, Harry Partridge
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01244v1)