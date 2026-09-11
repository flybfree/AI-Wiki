---
title: Xiaomi-CocktailASR-1 Technical Report
published: 2026-09-10T09:06:00Z
authors: Yiru Zhang, Hang Su, Lichun Fan, Ying Zeng, Chang Liu, Yifeng Wang, Yuquan Liang, Tao Li, Lian Li, Wenhao Yang, Jian Luan, Cong Zou, Heng Qu
url: http://arxiv.org/abs/2609.11274v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Xiaomi-CocktailASR-1 Technical Report

## Abstract
Recently, large language model (LLM) based ASR models have achieved significant progress, yet they generally lack support for multi-speaker scenarios, where the cocktail party problem remains a critical bottleneck for further advancing ASR. Existing TS-ASR methods, including end-to-end architectures with speaker embeddings and latest LLM-based explorations suffer from degraded single-speaker performance and the inability to reject when the target speaker is absent. In this paper, we propose Xiaomi-CocktailASR-1, an LLM-based end-to-end TS-ASR architecture. By utilizing reference speech as voiceprint prompts, it directly transcribes the target speaker's speech without requiring speech separation. Xiaomi-CocktailASR-1 maintains competitive performance in single-speaker scenarios, comparable to mainstream ASR models. It also features a negative sample rejection capability, outputting empty text when the target speaker is absent from the mixed speech. Additionally, Xiaomi-CocktailASR-1 supports a Chain-of-Thought (CoT) reasoning mode to provide explicit reasoning steps. Extensive experiments on various synthetic and real-world multispeaker benchmarks demonstrate that Xiaomi-CocktailASR-1 achieves state-of-the-art performance, effectively addressing the cocktail party problem through a unified architecture that balances multispeaker and single-speaker recognition accuracy, along with rejection capability.

## Metadata
- **Published**: 2026-09-10T09:06:00Z
- **Authors**: Yiru Zhang, Hang Su, Lichun Fan, Ying Zeng, Chang Liu, Yifeng Wang, Yuquan Liang, Tao Li, Lian Li, Wenhao Yang, Jian Luan, Cong Zou, Heng Qu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.11274v1)