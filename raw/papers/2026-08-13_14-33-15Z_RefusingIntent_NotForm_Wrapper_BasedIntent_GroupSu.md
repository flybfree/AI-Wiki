---
title: Refusing Intent, Not Form: Wrapper-Based Intent-Group Supervision for LLM Safety
published: 2026-08-13T14:33:15Z
authors: Ping Wu, Haibo Tong, Feifei Zhao, Han Shen, Yu Shi, Yilin Zhao, Sicheng Shen, Guobin Shen, Yun Luo, Yi Zeng
url: http://arxiv.org/abs/2608.13304v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Refusing Intent, Not Form: Wrapper-Based Intent-Group Supervision for LLM Safety

## Abstract
Safety tuning can improve harmful refusal, but models may learn surface-form shortcuts: wrapped harmful prompts bypass safety, while similarly wrapped benign prompts are over-refused. We propose Wrapper-Based Intent-Form Augmentation (WIFA), an automatic intent-group augmentation method that pairs wrapped harmful examples with structurally matched wrapped benign counterexamples, requiring no external teacher or manual per-wrapper intent labels. We use WIFA as a common data layer for two complementary fine-tuning routes: WIFA-Boost, a two-stage high-safety recipe, and Anchored Group-Consistent Refusal Training (A-GCRT), which regularizes refusal/compliance decision scores across same-intent wrappers and anchors harmful and benign groups on opposite sides of a margin. In the Qwen setting, WIFA-Boost reaches the strongest transformed-harmful refusal, while A-GCRT reduces OR-Bench over-refusal from 25.7\% for the base model to 17.4\%; reproduced baselines do not match these operating points. Llama results and ablations over data structure, two-stage order, and A-GCRT components support this intent-group interpretation without claiming universal below-base over-refusal.

## Metadata
- **Published**: 2026-08-13T14:33:15Z
- **Authors**: Ping Wu, Haibo Tong, Feifei Zhao, Han Shen, Yu Shi, Yilin Zhao, Sicheng Shen, Guobin Shen, Yun Luo, Yi Zeng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13304v1)