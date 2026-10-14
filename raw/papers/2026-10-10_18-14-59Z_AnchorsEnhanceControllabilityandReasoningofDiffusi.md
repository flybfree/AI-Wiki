---
title: Anchors Enhance Controllability and Reasoning of Diffusion Language Models
published: 2026-10-10T18:14:59Z
authors: Feiyu Qu, Zheng Huang, Andrea Zanette
url: http://arxiv.org/abs/2610.15097v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Anchors Enhance Controllability and Reasoning of Diffusion Language Models

## Abstract
Diffusion language models (DLMs) offer new opportunities for controllable text generation. However, their controllability, defined as the ability to satisfy task constraints while preserving their original capabilities, remains underexplored. DLMs' bidirectional attention allows control tokens to guide generation from arbitrary positions in the output sequence, but effective guidance depends on the compatibility between their content and placement. To this end, we propose AnchorDLM, a framework in which an anchor generator produces an anchor consisting of a short output fragment and its position for each query. The anchor is placed as control tokens at the specified position to initialize the output sequence of a frozen DLM and guide subsequent denoising. We train the anchor generator with reinforcement learning (RL) to jointly optimize anchor content and placement, using rewards computed from the DLM's generated outputs based on answer correctness and constraint satisfaction. Moreover, through the lens of discrete flow matching (DFM), we interpret anchor placement as helping to reshape the initial velocity field that guides generation. Experiments on code generation and mathematical reasoning across five DLM backbones show that AnchorDLM improves controllability and further yields gains in reasoning performance across diverse benchmarks.

## Metadata
- **Published**: 2026-10-10T18:14:59Z
- **Authors**: Feiyu Qu, Zheng Huang, Andrea Zanette
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.15097v1)