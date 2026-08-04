---
title: FAU at ImageCLEF 2026 Task on Multimodal Reasoning Robust Candidate Scoring and Concise Multilingual Visual Answering
published: 2026-08-03T03:54:22Z
authors: Mohamed Basem, Vincent Christlein
url: http://arxiv.org/abs/2608.01664v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FAU at ImageCLEF 2026 Task on Multimodal Reasoning Robust Candidate Scoring and Concise Multilingual Visual Answering

## Abstract
We present our ImageCLEF 2026 Multimodal Reasoning system for the Visual Multiple Choice Question Answering (Visual MCQ) and Visual Open Question Answering (Visual OpenQA) subtasks. The challenge requires reliable reasoning over multilingual educational and scientific images with dense text, diagrams, charts, tables, formulas, and units, while enforcing strict answer formats. Our central finding is that robust output control is as important as model choice. For Visual MCQ, we replace fragile free-form generation with direct candidate label scoring from vision-language model logits, then combine complementary runs through score fusion and voting. For Visual OpenQA, we use image enhancement, concise final answer prompting, deterministic decoding, and targeted post-processing to remove reasoning traces and formatting artifacts. Without task-specific model training, our official submissions achieved third place in Visual MCQ with 0.7108 accuracy and first place in Visual OpenQA with 0.6488 COMET, 0.1391 BLEU, 0.2762 ROUGE L, and 0.2383 METEOR. The results highlight the practical value of inference engineering: careful scoring, ensembling, prompting, and cleanup can turn strong VLMs into reliable competition systems.

## Metadata
- **Published**: 2026-08-03T03:54:22Z
- **Authors**: Mohamed Basem, Vincent Christlein
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01664v1)