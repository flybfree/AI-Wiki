---
title: Retrieved but Not Delivered: Multimodal Memory Delivery for Long-Term Agents
published: 2026-09-26T13:05:56Z
authors: Yuhang Jiang, Qingwei Liao, Kaize Yin, Xingling Liu, Luca Cuomo, Silvio Bacci
url: http://arxiv.org/abs/2609.32590v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Retrieved but Not Delivered: Multimodal Memory Delivery for Long-Term Agents

## Abstract
Work on memory for multimodal agents optimizes what is written, updated and retrieved. Between retrieval and the answer, however, is a stage that multimodal memory evaluations do not isolate: what of the retrieved memory reaches the model, and in what form. We call it delivery, and a controlled decomposition on MemLens locates the remaining room there. With the retrieved evidence set exactly fixed, delivering the original pixels instead of withholding them raises accuracy by 13.87 points on an 8B backbone, whereas making retrieval perfect on those same messages improves it by 2.31. Delivery is the larger term on all three MemLens backbones and grows with backbone strength; retrieval grows too, without closing the gap. We propose DeliverMem, an instantiation of delivery as three decisions: keep the original modality, give each item a readable identity, and state when it was seen, with a retrieval-side adapter for the one property delivery cannot supply. Each is measured against a delivery-matched control that alters only its own variable. DeliverMem leads the strongest published memory agent on MemLens at all four context lengths, and beats DMV-Bench's own strongest method at every setting on both backbones. On MemLens it does this on a tenth to a seventieth of the input. Each decision helps only where the question lacks what it supplies, and is null elsewhere. A single fixed configuration nonetheless leads both benchmarks, without training any component or modifying the stored records. Project page: https://avalon-s.github.io/DeliverMem/

## Metadata
- **Published**: 2026-09-26T13:05:56Z
- **Authors**: Yuhang Jiang, Qingwei Liao, Kaize Yin, Xingling Liu, Luca Cuomo, Silvio Bacci
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32590v1)