---
title: Sign Language Question Answering: A New Task, Benchmark, and Baseline for Sign Language Understanding
published: 2026-07-30T08:05:26Z
authors: Shiwei Gan, Lichen Wang, Xiao Liu, Yafeng Yin, Kuizhuang Liu, Sanglu Lu, Lei Xie
url: http://arxiv.org/abs/2607.27826v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Sign Language Question Answering: A New Task, Benchmark, and Baseline for Sign Language Understanding

## Abstract
Recent advances in sign language (SL) understanding (SLU) have led to remarkable progress in tasks such as continuous SL recognition and SL translation. However, these tasks are designed with predefined objectives, requiring models to learn a fixed mapping from sign videos to glosses or spoken-language sentences. As a result, they provide only a limited assessment of whether a model truly understands the semantic content of SL videos. To address this limitation, \textbf{we first propose a new task, Sign Language Question Answering (SLQA)}, which evaluates SL understanding by requiring models to answer arbitrary natural language questions about SL videos. Unlike previous SLU tasks, SLQA provides a more flexible and comprehensive evaluation framework that assesses multiple reasoning capabilities beyond recognition and translation. To facilitate this task, \textbf{we further construct two SignQA benchmarks} based on PHOENIX14T and CSL-Daily by automatically generating question-answer pairs from existing gloss and sentence annotations using carefully designed templates. The resulting datasets cover five complementary question categories, including position reasoning, structural reasoning, visual search, gloss recognition, and translation understanding. \textbf{Finally, we propose a simple yet effective baseline model} equipped with a Question-Conditioned Modulated Temporal Downsampling module and an in-domain knowledge transfer strategy, enabling effective knowledge transfer from existing SLU tasks while enhancing question-aware temporal feature modeling. Extensive experiments demonstrate that our baseline consistently outperforms representative vision-language models across all question categories, establishing a strong benchmark for future research on SLQA. Datasets are available at:{https://huggingface.co/datasets/hulala/SignQA-2026}.

## Metadata
- **Published**: 2026-07-30T08:05:26Z
- **Authors**: Shiwei Gan, Lichen Wang, Xiao Liu, Yafeng Yin, Kuizhuang Liu, Sanglu Lu, Lei Xie
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27826v1)