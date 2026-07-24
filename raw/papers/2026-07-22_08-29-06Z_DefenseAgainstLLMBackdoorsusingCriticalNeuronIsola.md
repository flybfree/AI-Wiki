---
title: Defense Against LLM Backdoors using Critical Neuron Isolation Pruning
published: 2026-07-22T08:29:06Z
authors: Yuxi Li, Zhibo Zhang, Kailong Wang, Xingshuo Han, Ling Shi, Haoyu Wang
url: http://arxiv.org/abs/2607.19894v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Defense Against LLM Backdoors using Critical Neuron Isolation Pruning

## Abstract
Large language models (LLMs) are vulnerable to backdoor attacks, where hidden triggers induce malicious outputs. Existing defenses generally fall into inference-time detection or training-time mitigation, but face two key limitations. First, they focus on fine-tuning-based backdoors (e.g., PEFT modules) and fail to address insidious model-editing attacks that bypass training pipelines. Second, they target simple classification settings and do not naturally extend to open-ended LLM generation and do not naturally extend to the open-ended generation characteristics of LLMs. Consequently, these methods focus on surface-level behavioral patterns while neglecting the deeper representational causes of malicious activations. This lack of mechanistic understanding forces defenses to depend on empirical heuristics, limiting their robustness, generality, and practical applicability in real-world LLM deployment.   To bridge this gap, we introduce DeCNIP (Defense with Critical Neuron Isolation Pruning), which leverages representational analysis to identify and neutralize backdoors in a unified pipeline. Specifically, DeCNIP identifies trigger-like behaviors by optimizing a cross-entropy loss between harmful prompts with candidate tokens and benign inputs. This representational discovery exposes latent threats by uncovering mechanisms through which triggers hijack model weights. It then isolates Backdoor Critical Neurons (BCNs) and prunes them selectively to remove malicious influence while preserving model utility. Extensive evaluations on six open-source LLMs and two benchmark datasets demonstrate that DeCNIP achieves over 95% relative reduction in Attack Success Rate (ASR), outperforming seven state-of-the-art defenses with only 0.1% neuron intervention. Moreover, it maintains 97% of the model's performance on normal benchmarks, demonstrating its efficacy, robustness, and scalability.

## Metadata
- **Published**: 2026-07-22T08:29:06Z
- **Authors**: Yuxi Li, Zhibo Zhang, Kailong Wang, Xingshuo Han, Ling Shi, Haoyu Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19894v1)