---
title: JigShape: Evaluating Visual-Geometric Reasoning in VLMs through Jigsaw Puzzles
published: 2026-07-30T04:34:27Z
authors: Shawn Li, Wei Yang, Jike Zhong, Jiate Li, Jiawei Yang, You Qin, Ryan Rossi, Franck Dernoncourt, Roger Zimmermann, Yue Wang, Zhengzhong Tu, Vicente Ordonez, Mohit Bansal, Yue Zhao
url: http://arxiv.org/abs/2607.27670v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# JigShape: Evaluating Visual-Geometric Reasoning in VLMs through Jigsaw Puzzles

## Abstract
Jigsaw puzzle solving requires jointly reasoning about visual content and geometric constraints, yet existing benchmarks use rectangular cuts that create ambiguous ground truth in texture-repeated regions. We introduce \textit{\ours{}}, a benchmark with tab-and-blank interlocking pieces where geometric constraints provide strong local compatibility requirements that, combined with visual content, yield unambiguous ground truth. Across 95K instances at four grid densities (4$\times$4 to 16$\times$16), we find that \textbf{zero-shot VLMs largely lack geometric reasoning}: only one of five frontier models (GPT-5.5) exceeds random baseline on 4$\times$4 puzzles, while all others perform at chance level. While supervised fine-tuning achieves $>$97\% on 4$\times$4, \textbf{all models collapse on larger grids}: GPT-5.5 drops from 70\% to near-random on 8$\times$8, and even fine-tuned models fall below 5\% on 12$\times$12. This ``scaling cliff'' suggests current architectures cannot maintain consistent constraint satisfaction as the number of pieces increases. \ours{} establishes scalable geometric reasoning as an open challenge for vision-language models.

## Metadata
- **Published**: 2026-07-30T04:34:27Z
- **Authors**: Shawn Li, Wei Yang, Jike Zhong, Jiate Li, Jiawei Yang, You Qin, Ryan Rossi, Franck Dernoncourt, Roger Zimmermann, Yue Wang, Zhengzhong Tu, Vicente Ordonez, Mohit Bansal, Yue Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27670v1)