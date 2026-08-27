---
title: MMJailBench: A Factorized Benchmark for Disentangling Multimodal Jailbreak Vulnerabilities
published: 2026-08-26T08:03:55Z
authors: Tianshi Wang, Jingsong Wang, Yafei Huang, Fengling Li, Xin Li, Lei Zhu
url: http://arxiv.org/abs/2608.25490v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MMJailBench: A Factorized Benchmark for Disentangling Multimodal Jailbreak Vulnerabilities

## Abstract
Multimodal Large Language Models (MLLMs) are increasingly deployed in real-world applications, yet how different factors shape their jailbreak vulnerabilities remains poorly understood. Existing benchmarks often couple harmful intent, prompt framing, visual semantics, and instruction carrier within individual jailbreak instances, obscuring the specific sources of observed vulnerabilities. To address this limitation, we introduce MMJailBench, a factorized benchmark that systematically varies and combines these factors under controlled configurations, enabling fine-grained comparison and factor-level attribution. Large-scale evaluations across 16 open-weight and proprietary MLLMs reveal highly heterogeneous and model-dependent vulnerability profiles. Jailbreak vulnerability varies markedly across harm domains, exposing uneven coverage in current multimodal safety alignment. Prompt framing emerges as the dominant source of variation, task-relevant visual semantics systematically increase jailbreak susceptibility with authority-like cues exposing particularly pronounced vulnerabilities, and visually rendered instructions do not consistently increase jailbreak susceptibility relative to direct textual instructions. To further investigate the risks introduced by multimodal context, we conduct diagnostic analyses on a representative open-weight model and identify vulnerability-associated patterns in internal representations and cross-modal interactions. Finally, we develop a modular multimodal jailbreak evaluation suite with full and lightweight configurations, multiple judge options, and multidimensional metrics, enabling reproducible, scalable, and cost-efficient multimodal jailbreak auditing.

## Metadata
- **Published**: 2026-08-26T08:03:55Z
- **Authors**: Tianshi Wang, Jingsong Wang, Yafei Huang, Fengling Li, Xin Li, Lei Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25490v1)