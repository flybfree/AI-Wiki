---
title: When Safety Routing Breaks: Understanding Alignment Fragility under Benign Fine-Tuning
published: 2026-09-01T15:59:32Z
authors: Yitong Guo, Xiaoyi Chen, Siyuan Zhang, Xiaofeng Wang, Haixu Tang
url: http://arxiv.org/abs/2609.01455v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Safety Routing Breaks: Understanding Alignment Fragility under Benign Fine-Tuning

## Abstract
Benign fine-tuning severely weakens the safety alignment of large language models (LLMs), so we study why refusal behavior is so fragile. While prior work often attributes this failure to gradient conflict, we propose a fundamentally different Fisher-geometric explanation: safety Fisher is low-rank, and alignment makes the safety geometry flatter while preserving an output-routing pathway. After 100 benign fine-tuning examples, this pathway is selectively re-sharpened in output-side MLP modules, explaining the asymmetric fragility: safety can collapse to high attack success rates, while general utility degrades mildly. The routing view also explains why few safety examples can restore refusal behavior, indicating that internal safety-relevant representations are preserved. Finally, we show that LoRA and ASAM mitigate early collapse by suppressing output-side sharpness, but their protection weakens at larger fine-tuning scales. Overall, safety failure is best understood as a disruption of a low-rank output-routing mechanism

## Metadata
- **Published**: 2026-09-01T15:59:32Z
- **Authors**: Yitong Guo, Xiaoyi Chen, Siyuan Zhang, Xiaofeng Wang, Haixu Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01455v1)