---
title: Gaokerena: A Small Persian Medical Language Model Family
published: 2026-08-02T02:17:10Z
authors: Mehrdad Ghassabi, Hamidreza Baradaran Kashani, Pedram Rostami, Sadra Hakim, Zahra Kazemi, Audrina Ebrahimi
url: http://arxiv.org/abs/2608.00932v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Gaokerena: A Small Persian Medical Language Model Family

## Abstract
The integration of artificial intelligence into medical question-answering systems has advanced rapidly; however, research remains predominantly focused on English, leaving low resource languages like Persian significantly underserved. To address this gap, this paper introduces Gaokerena, a novel family of compact Persian medical language models optimized for deployment on consumer grade hardware. As a foundational step toward localized digital healthcare, we first present Gaokerena-V, developed by training a baseline model on a newly curated 90-million-token Persian medical corpus and 20,000 expert-vetted physician Q&A pairs, which improved performance on a translated medical MMLU benchmark from 46.28% to 49.31%. Second, recognizing the critical demands of clinical reasoning, we developed Gaokerena-R by integrating a Chain-of-Thought approach with two novel Reinforcement Learning with AI Feedback (RLAIF) frameworks to optimize preference-based reasoning. Despite utilizing the same baseline architecture and a smaller dataset than Gaokerena-V, Gaokerena-R achieved a superior benchmark score of 52.98%. Furthermore, both models are equipped with custom-developed uncertainty heads that predict the model's confidence in its responses based solely on internal hidden states. While these results demonstrate significant progress in Persian medical language modeling and proactive safety estimation, current performance levels remain insufficient for direct clinical application, highlighting the necessity for further research into robust knowledge acquisition and rigorous safety verification prior to real world deployment.

## Metadata
- **Published**: 2026-08-02T02:17:10Z
- **Authors**: Mehrdad Ghassabi, Hamidreza Baradaran Kashani, Pedram Rostami, Sadra Hakim, Zahra Kazemi, Audrina Ebrahimi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00932v1)