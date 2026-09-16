---
title: The Imitation Game: When LLMs Learn to Reason Like Programs via Code-Centric Reasoning Data Synthesis
published: 2026-09-13T17:04:16Z
authors: Jinyang Zhang, Weibin Liao, Keqin Bao, Sihang Li, Shaobo Wang, Muyang Ye, Hongxin Ding, Yue Fang, Tianyi Tang, Fei Huang, Kexin Yang, Xingzhang Ren, Dayiheng Liu
url: http://arxiv.org/abs/2609.16076v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Imitation Game: When LLMs Learn to Reason Like Programs via Code-Centric Reasoning Data Synthesis

## Abstract
Large Language Models (LLMs) excel at programming tasks but frequently fail at deterministic, fine-grained reasoning in natural language, relying heavily on semantic approximations rather than robust symbolic execution. To bridge this gap, we propose MIMIC, a framework that leverages executable code as a rigorous medium for reasoning data synthesis. MIMIC fundamentally transforms algorithms into verifiable reasoning trajectories through narrative fusion, code-guided test synthesis, and dynamic code instrumentation. Crucially, these explicit intermediate execution states naturally form a Code-Instrumented Reward (CIR), providing dense, high-fidelity process supervision for reinforcement learning without external reward models. Extensive evaluations reveal that models trained via SFT and GRPO on our synthesized dataset achieve substantial, consistent gains. Our method significantly elevates accuracy across general reasoning, complex mathematical benchmarks, and fine-grained deterministic tasks, demonstrating that the procedural rigor of executable code can effectively unlock and enhance the generalized reasoning capabilities of LLMs. Our code and data are available at https://github.com/zjy1298/MIMIC.

## Metadata
- **Published**: 2026-09-13T17:04:16Z
- **Authors**: Jinyang Zhang, Weibin Liao, Keqin Bao, Sihang Li, Shaobo Wang, Muyang Ye, Hongxin Ding, Yue Fang, Tianyi Tang, Fei Huang, Kexin Yang, Xingzhang Ren, Dayiheng Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.16076v1)