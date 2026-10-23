---
title: CANNBot-CAKE: Collaborative Agentic Kernel Evolution for Ascend NPU
published: 2026-10-22T10:12:45Z
authors: Deng Pan, Xue-Jian Gao, Junyi Fan, Bin Du, Jiasheng Li, Xinxian Chen, Nok Yan Chang, Xinlin Li, Lingchao Zheng, Jun Li, Yuwei Fan
url: http://arxiv.org/abs/2610.31034v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CANNBot-CAKE: Collaborative Agentic Kernel Evolution for Ascend NPU

## Abstract
Efficient custom operators are essential for modern deep learning workloads, yet developing high-performance kernels for Ascend NPUs remains slow, expert-intensive, and difficult to automate. Although AI agents now approach expert performance on GPU kernel benchmarks, current models remain less capable of generating AscendC kernels for NPUs, potentially reflecting the relative scarcity of relevant training data. We thus present CAKE, a CANN-native system for deployable custom operators that combines adaptive multi-DSL routing, separate Generation and Evolution modes, and reviewed knowledge reuse through CAKE Book and a Self-Evolving Agent. On 53 CANN-Bench v1.1 operators on Ascend 950PR, CAKE's aggregated results achieve $100\%$ case pass rate on the standard set (1,060/1,060) and $98.28\%$ on the hidden set (4,167/4,240), with an overall mean score of 78.63 out of 100 and an average performance speedup of $1.334\times$ over the baseline. Evolution then pushes correct operators further: EngramGateFusion cuts aggregate device time by $46.6\%$ over 20 rounds and roughly halves the mean roofline gap. These results offer a practical path toward closing Ascend's AI-for-kernel capability gap.

## Metadata
- **Published**: 2026-10-22T10:12:45Z
- **Authors**: Deng Pan, Xue-Jian Gao, Junyi Fan, Bin Du, Jiasheng Li, Xinxian Chen, Nok Yan Chang, Xinlin Li, Lingchao Zheng, Jun Li, Yuwei Fan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.31034v1)