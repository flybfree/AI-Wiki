---
title: Multi-Agent Forensic Reasoning for Generalizable Deepfake Video Detection
published: 2026-08-07T06:44:14Z
authors: Xuechao Zou, Shun Zhang, Kai Li, Yi Zhou, Xinyu Sun, Yuhui Chen, Zhe Wu, Congyan Lang, Junliang Xing
url: http://arxiv.org/abs/2608.06865v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Multi-Agent Forensic Reasoning for Generalizable Deepfake Video Detection

## Abstract
The malicious use of generative artificial intelligence to create highly realistic deepfake videos raises serious ethical concerns and poses substantial challenges to AI safety. However, existing deepfake video benchmarks provide limited coverage of recent synthesis methods and generally lack reliable fine-grained textual annotations. Meanwhile, conventional detectors and multimodal large language models (MLLMs), whether operating as a single model or relying on a single analytical perspective, often fail to capture subtle forgery artifacts, limiting their generalization to emerging AI-generated methods. To address these limitations, we introduce FaceVid-Forensics-100K, a large-scale deepfake video dataset comprising 100,000 videos and spanning 33 synthesis methods across face swapping, face reenactment, and entire-face synthesis, including recent generators such as Seedance 2.0. The dataset provides fine-grained textual annotations of visual observations and verdict-consistent forensic explanations, automatically synthesized through a multi-model aggregation and conflict-resolution pipeline powered by advanced MLLMs. Building on this benchmark, we propose a multi-agent forensic reasoning framework that employs four specialized domain-expert agents to independently analyze forgery cues from four perspectives: texture, lighting, motion, and physics. A judge agent then reconciles their reports to produce a final prediction together with an explanation. Extensive evaluations on out-of-domain test sets show that, despite being composed entirely of small open-source MLLMs, our framework outperforms all methods including closed-source GPT and Gemini models and ranks first across all reported metrics on this benchmark. The project page is available at https://xavierjiezou.github.io/ARGUS/.

## Metadata
- **Published**: 2026-08-07T06:44:14Z
- **Authors**: Xuechao Zou, Shun Zhang, Kai Li, Yi Zhou, Xinyu Sun, Yuhui Chen, Zhe Wu, Congyan Lang, Junliang Xing
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06865v1)