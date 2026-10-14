---
title: RECAP: Calibrating Low-Bit Reasoning Models on the History They Read
published: 2026-10-11T01:10:33Z
authors: Chi Ruan, Yujie Chen, Zixiang Zhao, Jingcai Guo, Haotong Qin
url: http://arxiv.org/abs/2610.15259v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RECAP: Calibrating Low-Bit Reasoning Models on the History They Read

## Abstract
Low-bit quantization reduces the cost of serving reasoning models but can substantially degrade long chains of thought. Each step reads cached keys and values spanning thousands of tokens, allowing quantization errors to accumulate along the trajectory. Standard calibration operates on short segments that omit the earlier context needed by later reasoning steps. Even when this context is retained, cache reconstruction error alone does not capture how quantization errors affect subsequent attention. We present RECAP, a post-training quantization method that calibrates reasoning models on the history they read. Dynamic-prefix calibration separates long historical context from short-block reconstruction. It regenerates prefix keys and values with the current quantizer and rotates the active block to supervise every position along the trajectory. Prefix read geometry further supervises historical cache errors according to their effects on attention outputs, weighting key and value errors asymmetrically. With both components applied only during calibration, RECAP outperforms the baseline across multiple reasoning models and quantization settings. Under W4A4KV4, RECAP improves accuracy over the baseline by 13.3 percentage points on MATH500 with DeepSeek-R1-Distill-Qwen-1.5B and 15.8 points on AIME-120 with Qwen3-4B. These results highlight the importance of preserving historical dependencies during calibration for low-bit reasoning.

## Metadata
- **Published**: 2026-10-11T01:10:33Z
- **Authors**: Chi Ruan, Yujie Chen, Zixiang Zhao, Jingcai Guo, Haotong Qin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.15259v1)