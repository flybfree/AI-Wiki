---
title: SymbOmni: Evolving Agentic Omni Models via Symbolic Concept Learning
published: 2026-07-13T18:00:34Z
authors: Jinxiu Liu, Jianru Li, Tanqing Kuang, Xuanming Liu, Kangfu Mei, Yandong Wen, Weiyang Liu
url: http://arxiv.org/abs/2607.12042v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SymbOmni: Evolving Agentic Omni Models via Symbolic Concept Learning

## Abstract
Visual generation is increasingly ubiquitous in diverse domains, from text-to-image/video synthesis to multimodal interactive creation. Yet prevailing monolithic models remain fundamentally constrained by their inability to learn cumulatively and evolve autonomously, which is a limitation we term the "perpetual novice" problem. They lack mechanisms for structuring experience into reusable knowledge and therefore rely on brittle, "from-scratch" reasoning for each task, resulting in poor compositional generalization and inefficient knowledge retention. Motivated by these limitations, we propose SymbOmni, an agentic omni-model designed for cumulative evolution through Symbolic Concept Learning. At its core is the Symbolic Concept Box, an optimizable memory module that abstracts low-level operations into reusable Symbolic Workflow Instructions. SymbOmni operates through an induction-transduction cycle: experiences are abstracted into symbolic concepts (induction), which are then adaptively composed to solve novel tasks (transduction). The training is done by verbalized backpropagation with language-based feedback to enable continuous self-improvement without gradient-based model fine-tuning. Comprehensive experiments validate that (I) SymbOmni significantly outperforms existing agent-based systems for iterative creation and also surpasses closed-source models (e.g., Nano Banana, GPT-Image-1) in both image quality and task success rates; (II) SymbOmni effectively reduces token consumption by over 40% while maintaining competitive generation quality; and (III) SymbOmni enables effective continual learning by achieving cumulative gains across multiple online-learning benchmarks and setting a new state of the art.

## Metadata
- **Published**: 2026-07-13T18:00:34Z
- **Authors**: Jinxiu Liu, Jianru Li, Tanqing Kuang, Xuanming Liu, Kangfu Mei, Yandong Wen, Weiyang Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.12042v1)