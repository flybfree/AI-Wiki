---
title: FQTree: Fine-grained Quantization and Hardware Generation of Boosted Decision Trees
published: 2026-08-12T14:56:13Z
authors: Zhiqiang Que, Chang Sun, Haiyang Wang, Dinesh Pamunuwa, Roshan Weerasekera, Qijia Tang, Bakhtiar Zadeh, Wayne Luk, Maria Spiropulu
url: http://arxiv.org/abs/2608.12140v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FQTree: Fine-grained Quantization and Hardware Generation of Boosted Decision Trees

## Abstract
Boosted decision trees (BDTs) are widely used in latency-critical applications, but efficient hardware deployment remains challenging. Existing designs often rely on uniform or manually tuned fixed-point formats, which can introduce unnecessary hardware cost or accuracy loss. This work presents the FQTree algorithm{https://github.com/ecs-bristol/FQTree} for fine-grained quantization-aware training of BDTs, together with the QXGB framework for automatic hardware generation. FQTree introduces a hardware-oriented leaf-value quantization scheme that uses a global quantization step together with a tree-wise shift, enabling compact non-negative integer leaf representations, controlled clipping/pruning, and bias folding to reduce datapath cost. This work further applies this quantization during boosting so that later trees adapt to the errors of the already-quantized ensemble, and then lowers the trained model into low-latency hardware implementations through a compiler-based flow. Results on JSC, MNIST, and NID show that our method reduces LUT usage by 26-57\% compared with the state-of-the-art FPGA-based BDT designs while matching or improving accuracy.

## Metadata
- **Published**: 2026-08-12T14:56:13Z
- **Authors**: Zhiqiang Que, Chang Sun, Haiyang Wang, Dinesh Pamunuwa, Roshan Weerasekera, Qijia Tang, Bakhtiar Zadeh, Wayne Luk, Maria Spiropulu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12140v1)