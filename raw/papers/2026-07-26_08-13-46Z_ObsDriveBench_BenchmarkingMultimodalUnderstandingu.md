---
title: ObsDriveBench: Benchmarking Multimodal Understanding under Adverse Weather with Observability Awareness
published: 2026-07-26T08:13:46Z
authors: Qiao Yan, Yihan Wang, Zhenghao Xing, Jiaqi Xu, Pheng-Ann Heng
url: http://arxiv.org/abs/2607.23537v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ObsDriveBench: Benchmarking Multimodal Understanding under Adverse Weather with Observability Awareness

## Abstract
Autonomous driving under adverse weather remains a critical challenge, yet existing vision-language benchmarks mainly evaluate under standard conditions, synthetic corruptions, or single modality. As a result, it remains unclear how vision-language models behave under real-world adverse weather with multi-modal inputs. We argue that a key difficulty lies in degraded environmental observability: under fog, rain, snow, and low illumination, multi-modal observations become unreliable and cross-modally inconsistent, posing challenges to scene understanding, and subsequent decision-making. To study this, we introduce \textbf{ObsDriveBench}, a real-world multi-modal benchmark for adverse-weather autonomous driving. Our benchmark is designed with three capability dimensions: \textbf{observability awareness}, \textbf{spatial reliability}, and \textbf{risk-aware decision-making}, enabling fine-grained diagnosis of model behavior under degraded observations. We construct the benchmark through observability meta-annotation, scene description, and capability oriented multiple-choice tasks over synchronized camera, LiDAR, and radar inputs, forming a benchmark with over 14k training and 13k test questions. Experiments reveal consistent performance degradation of existing vision-language models. We further introduce \textbf{ObsDrive} model with normal-weather supervised fine-tuning and adverse-weather reinforcement learning, improving robustness across all three capabilities. The dataset and evaluation code will be released at \href{https://github.com/russellyq/ObsDriveBench}{\texttt{ObsDriveBench}}.

## Metadata
- **Published**: 2026-07-26T08:13:46Z
- **Authors**: Qiao Yan, Yihan Wang, Zhenghao Xing, Jiaqi Xu, Pheng-Ann Heng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23537v1)