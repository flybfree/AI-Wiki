---
title: Cognivia: A Cognitive Behavioral Therapy Copilot for Evidence-Based Mental Healthcare
published: 2026-07-28T12:56:06Z
authors: Qi Chen, Siria Xiyueyao Luo, Jian Wang, Yuan Shi, Haocong Rao, Xuejiao Zhao
url: http://arxiv.org/abs/2607.25681v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cognivia: A Cognitive Behavioral Therapy Copilot for Evidence-Based Mental Healthcare

## Abstract
Cognitive distortion amplifies negative emotions and contributes to mental health disorders. Cognitive Behavioral Therapy (CBT) is an effective way to address cognitive distortions, but its large-scale application is limited by the shortage of professional therapists. Although large language models (LLMs) have recently been explored for mental health applications, existing methods still suffer from limited domain specificity, overly flattering responses, and the absence of well-defined annotations for cognitive distortions. This paper proposes Cognivia, an evidence-based artificial intelligence therapist that integrates automatic cognitive distortion identification and rational response generation. Our framework is built on authoritative CBT texts widely regarded as core paradigms and standard references. It is further augmented with mental health question-answer (Q and A) data, and employs multi-stage prompting and structured generation strategies under the supervision of behavioral science experts. Then we fine-tune a lightweight LLM on this augmented CBT dataset to obtain Cognivia. In addition, we propose the first hierarchical quality evaluation framework for assessing LLM-generated rational responses, developed through collaboration between AI researchers and behavioral science experts. Cognivia is evaluated using lexical metrics, LLM-based Judges with two complementary criteria, and human evaluation by 10 behavioral science experts. It consistently outperforms the baseline methods in cognitive distortion recognition and rational response generation, demonstrating its effectiveness. Our code is available at https://github.com/SNOWTEAM2023/Cognivia.

## Metadata
- **Published**: 2026-07-28T12:56:06Z
- **Authors**: Qi Chen, Siria Xiyueyao Luo, Jian Wang, Yuan Shi, Haocong Rao, Xuejiao Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25681v1)