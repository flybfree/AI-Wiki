---
title: MMPostTrainBench: Benchmarking Autonomous Research for Multimodal Post-Training
published: 2026-10-04T17:32:58Z
authors: Yuxin Liu, Yuxuan Wang, Zhenxin Lei, Lingchen Meng, Yuchong Sun, Junming Lin, Hongcheng Liu, Yunfei Chu, Qize Yang, Jin Xu, Lei Zhang, Zhendong Mao
url: http://arxiv.org/abs/2610.05398v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MMPostTrainBench: Benchmarking Autonomous Research for Multimodal Post-Training

## Abstract
Autonomous research seeks sustained model improvements through iterative experimentation and feedback. LLM agents show promise in automating machine learning and language-model post-training, but their ability to sustain multimodal improvement remains unclear. We introduce MMPostTrainBench, a benchmark spanning eight tasks in image, audio, video, and joint audio-video understanding and image-grounded software repair. Agents operate from a common base model within fixed budgets, using development feedback before independent evaluation of their submitted models. Evaluation covers target and non-target model outcomes, iterative model improvement and selection, and research integrity. Across all eight tasks, 52.1% of model--task means fall below the base, and evaluated submissions also exhibit non-target regressions. Model performance does not consistently improve across research iterations, and agents do not reliably select the best evaluated candidate for submission; final submissions trail that candidate by up to 5.38 percentage points. Extending autonomous research from text-only to multimodal tasks introduces additional sources of error in perception, cross-modal alignment, and temporal grounding. The observed regressions and selection gaps highlight the need to balance targeted improvements with non-target capability preservation and to retain gains across research iterations. These requirements motivate MMResearch, a multimodal research framework that connects media-grounded evidence to hypotheses and interventions, carries findings across rounds through hierarchical memory, and retains candidates using development evaluation. Added to existing code-agent runtimes, it improves submitted-model accuracy by up to 7.75 percentage points for Claude Opus 4.8 with Claude Code and 2.33 points for GPT-5.6-sol with Codex.

## Metadata
- **Published**: 2026-10-04T17:32:58Z
- **Authors**: Yuxin Liu, Yuxuan Wang, Zhenxin Lei, Lingchen Meng, Yuchong Sun, Junming Lin, Hongcheng Liu, Yunfei Chu, Qize Yang, Jin Xu, Lei Zhang, Zhendong Mao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.05398v1)