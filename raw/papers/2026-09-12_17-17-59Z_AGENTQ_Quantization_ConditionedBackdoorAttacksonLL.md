---
title: AGENTQ: Quantization-Conditioned Backdoor Attacks on LLM Agents
published: 2026-09-12T17:17:59Z
authors: Xiaoqun Liu, Qiben Yan
url: http://arxiv.org/abs/2609.14060v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AGENTQ: Quantization-Conditioned Backdoor Attacks on LLM Agents

## Abstract
Quantization is one of the default deployment paths for open-weight LLM agents, but it is not behavior-preserving: an adversary can release a full-precision checkpoint that passes audits yet misbehaves once quantized, termed as quantization-conditioned attack (QCA). Prior QCA work targets free-text generation, where harm is mediated by a human reader. In contrast, the agentic setting poses a more severe risk: the triggered payload is a structured function that can be executed without human oversight. We present the first study of QCA against LLM agents. We find that directly adapting prior backdoor-injection methods can produce malicious behavior after quantization, but substantially degrades benign utility, rendering the resulting attacks impractical. To understand the true upper bound of the threat, we propose AGENTQ, an attack framework that combines layer-banded LoRA injection with partial-PGD repair over a multi-codebook quantization-equivalence class. AGENTQ preserves normal agentic capability while concentrating malicious behavior in the quantized model. Across three trigger-action pairs and three codebooks (NF4, FP4, INT8), AGENTQ reaches up to 100% post-quantization attack success rate with minimal loss of benign utility, underscoring the need to make quantization-aware safety evaluation a standard requirement before open-weight agents are deployed.

## Metadata
- **Published**: 2026-09-12T17:17:59Z
- **Authors**: Xiaoqun Liu, Qiben Yan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.14060v1)