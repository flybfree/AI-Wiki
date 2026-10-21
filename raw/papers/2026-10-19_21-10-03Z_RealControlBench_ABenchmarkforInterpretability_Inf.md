---
title: RealControlBench: A Benchmark for Interpretability-Informed Fine-Grained Control of LLMs and Agents
published: 2026-10-19T21:10:03Z
authors: Xinying Cai, Bin Hu, Mingyu Jin, Qiming Zhang, Yang Ouyang, Bangwei Guo, Minghao Guo, Yutong Yin, Lang Gao, Feijiang Han, Sheldon Yu, Kaiqu Liang, Qingcheng Zeng, Jingcheng Niu, Fan Yang, Wei Cheng, Zhen Xiang, Julian McAuley, Zhaoran Wang
url: http://arxiv.org/abs/2610.27295v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RealControlBench: A Benchmark for Interpretability-Informed Fine-Grained Control of LLMs and Agents

## Abstract
Existing steering benchmarks are built around simplified, isolated generation tasks and evaluate a single behavioral attribute under controlled settings that do not reflect the diversity and complexity of practical deployment. As a result, performance on these benchmarks provides only a limited picture of how steering methods perform in the real world. We therefore introduce RealControlBench, a comprehensive benchmark for evaluating fine-grained steering of LLMs and LLM agents across diverse behavioral targets and interaction settings. RealControlBench extends steering evaluation beyond isolated generations to complex, execution-grounded, multi-turn agent interactions, covering five complementary dimensions: instruction-following control, agentic tool-use decision control, reasoning-performance steering, reasoning-length control, and trajectory-conditioned safety awareness. Rather than measuring steering success alone, the benchmark jointly evaluates target controllability and capability preservation, including instruction following, reasoning performance, and downstream agent utility and safety. It further examines whether steering effects remain specific and robust across prompt variations, domains, and model architectures. Our evaluation shows that existing steering methods remain unreliable across realistic control objectives: they often fail to consistently induce the intended behavior and can substantially degrade the model's underlying task performance. These results suggest that strong steering effects in controlled settings do not necessarily translate into reliable control in more realistic evaluations. By providing a unified, model-agnostic steering evaluation framework, RealControlBench aims to support the development of steering methods that are not only effective but also precise, robust, and useful in realistic AI deployments.

## Metadata
- **Published**: 2026-10-19T21:10:03Z
- **Authors**: Xinying Cai, Bin Hu, Mingyu Jin, Qiming Zhang, Yang Ouyang, Bangwei Guo, Minghao Guo, Yutong Yin, Lang Gao, Feijiang Han, Sheldon Yu, Kaiqu Liang, Qingcheng Zeng, Jingcheng Niu, Fan Yang, Wei Cheng, Zhen Xiang, Julian McAuley, Zhaoran Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.27295v1)