---
title: MemeBench: What LVLMs Miss When Interpreting Culture-Dependent Memes
published: 2026-07-30T07:36:53Z
authors: Weihang Wang, Kainan Tu, Jielei Zhang, Run Yang, Boheng Sheng, Yuchen He, Yu Xie, Pengyu Chen, Peiyi Li, Huyang Sun, Longwen Gao, Zhouhui Lian
url: http://arxiv.org/abs/2607.27798v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MemeBench: What LVLMs Miss When Interpreting Culture-Dependent Memes

## Abstract
Large vision-language models have improved at describing visual content, but accurate descriptions do not ensure interpretation when meaning depends on knowledge beyond the pixels. Memes expose this gap because they rely on cultural entities, background knowledge, and community conventions. Most meme benchmarks reduce interpretation to labels or holistic scores, obscuring where an explanation breaks down. We introduce MemeBench, a diagnostic benchmark of 1,253 Chinese and English memes with human-written references and quality-controlled VIKR annotations, centered on anime, comics, games, and adjacent online subcultures. Its VIKR schema decomposes explanations into Visual clues, Identity links, Knowledge units, and Reasoning mechanisms. Across 26 LVLMs, every model covers visible content more reliably than the knowledge needed to interpret it, and even the strongest retains a 22.6% Visual-Knowledge gap. To test whether this diagnosis can guide improvement, we introduce KAR, an entity-guided retrieval baseline built on CultureBase. Across four controlled models, KAR raises VIKR Success by 3.6-7.4% and, compared with generic retrieval, repairs more answers and breaks fewer. Yet both retrieval conditions improve Identity and Knowledge while reducing Visual coverage in every comparison. MemeBench reveals whether an interpretation succeeds, what is missing, and whether targeted evidence fills the diagnosed gap.

## Metadata
- **Published**: 2026-07-30T07:36:53Z
- **Authors**: Weihang Wang, Kainan Tu, Jielei Zhang, Run Yang, Boheng Sheng, Yuchen He, Yu Xie, Pengyu Chen, Peiyi Li, Huyang Sun, Longwen Gao, Zhouhui Lian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27798v1)