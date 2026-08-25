---
title: PatchGate: Narrowing the Verbalization Gap with Intrinsic Object Inventories in Frozen Vision-Language Models
published: 2026-08-22T07:37:40Z
authors: Jihyung Ko, Eunji Jung, Hyeongsub Kim, Ziseok Lee, Jae Won Cho, Sanghyun Jo, Kyungsu Kim
url: http://arxiv.org/abs/2608.21819v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PatchGate: Narrowing the Verbalization Gap with Intrinsic Object Inventories in Frozen Vision-Language Models

## Abstract
Reliable image captioning in Vision-Language Models (VLMs) requires captions to be both precise and complete, avoiding unsupported object mentions while covering visible objects. Existing training-free methods primarily address the former requirement, suppressing unsupported object words by intervening on model-predicted mentions during generation. Because they operate only on objects the model is already likely to mention, visible objects omitted from the output remain difficult to recover. We propose PatchGate, a training-free framework that extracts prompt-free object evidence intrinsic to a frozen VLM before generation and uses it to narrow the gap between an intrinsic object set and final object mentions. In the first stage, Visual Evidence eXtraction (VEX) reads patch-level lexical evidence from the latter half of LM decoder layers and constructs an image-conditioned object set without any task prompt. In the second stage, Visual-Evidence Inclusion-Exclusion Decoding (VIED) uses this object evidence to calibrate decoding logits, promoting evidence-supported but under-verbalized objects and suppressing weakly supported but over-verbalized objects. On AMBER, PatchGate improves both sides of object-level reliability, increasing visible-object coverage from 49.4 to 56.0 (+13.4%) and reducing object hallucination by lowering CHAIR from 7.5 to 6.6 (-12.0%), without external detectors or fine-tuning and with one extra forward pass.

## Metadata
- **Published**: 2026-08-22T07:37:40Z
- **Authors**: Jihyung Ko, Eunji Jung, Hyeongsub Kim, Ziseok Lee, Jae Won Cho, Sanghyun Jo, Kyungsu Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21819v1)