---
title: ORCA: ORgan-Centroid Aggregation for Training-Free 3D CT Visual Token Compression
published: 2026-07-31T23:27:39Z
authors: Renjie Liang, Zijian Xu, Jinqian Pan, Chengkun Sun, Zhengkang Fan, Shawn Li, You Qin, Mei Liu, Jie Xu
url: http://arxiv.org/abs/2608.00345v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ORCA: ORgan-Centroid Aggregation for Training-Free 3D CT Visual Token Compression

## Abstract
A 3D CT scan entering a vision-language model produces a long sequence of visual tokens, often thousands to tens of thousands per volume, and this sequence must be compressed before a language model can consume it. Token compression is well studied in general vision, but little of it targets 3D CT specifically. A common baseline is grid average, which pools regular grid cells and can blend distinct anatomy, lesion, and air into one token. We present \textbf{ORCA} (ORgan-Centroid Aggregation), a token compressor for 3D CT. It merges adjacent tokens with organ guidance and adds a sinusoidal encoding of each region's centroid to preserve spatial layout. This preserves the anatomical information a downstream model needs. ORCA is training-free and plug-and-play, producing an adjustable token set without any model change or text query. We evaluate it across two datasets (CT-RATE and Merlin) and five encoders. The evaluation spans two task types: attribute prediction over five families (size, density, location, texture, and disease) and text generation (visual question answering and report generation). At matched token budgets, ORCA improves consistently over existing compression methods. It shrinks the visual context $64\times$ and its KV-cache $50\times$, and is $31\times$ faster to process each volume. Code released at https://github.com/renjie-liang/ORCA-3DCT.

## Metadata
- **Published**: 2026-07-31T23:27:39Z
- **Authors**: Renjie Liang, Zijian Xu, Jinqian Pan, Chengkun Sun, Zhengkang Fan, Shawn Li, You Qin, Mei Liu, Jie Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00345v1)