---
title: The Model's Tell: Measuring Context-Leakage Attack Signals with Behavior Gauges
published: 2026-08-18T14:28:51Z
authors: Maosen Zhang, Jianshuo Dong, Boting Lu, Wenyue Li, Xiaoping Zhang, Tianwei Zhang, Jie Zhang, Han Qiu
url: http://arxiv.org/abs/2608.17829v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Model's Tell: Measuring Context-Leakage Attack Signals with Behavior Gauges

## Abstract
LLMs increasingly rely on external contexts, such as pre-defined system prompts or retrieved documents, to improve generation quality. However, processing these contexts alongside user queries creates an attack surface: adversarial inputs can induce models to disclose them. Prior probing studies suggest that leakage-related signals emerge in hidden states, yet the need to extract these states poses additional deployment challenges. In this paper, we explore whether this internal signal leaves a more accessible ``tell'' before decoding. We propose LeakGauge, which probes this response by appending a suffix that gauges leakage behavior and mapping its prefill token probabilities to an attack-risk score. While a direct gauge uses the initial tokens of confidential content, we find that a content-agnostic one that verbalizes leakage behavior yields more robust signals. Across 11 LLMs, including GLM-5.2 (753B) and Kimi-K3 (2.8T), LeakGauge reaches an AUROC range of 0.944--0.996 on unseen attacks. The signal remains stable when the content changes language or the attack shifts from verbatim to semantic disclosure. By activation-steering interventions, we further show that the risk score is sensitive to an internal leakage-related direction, relating the observable signal to the model's internal representation. In addition, LeakGauge enables an input detector with fewer than 0.5K extra parameters and added latency of 10.34 ms. Code: \href{https://github.com/yeasen-z/LeakGauge}.

## Metadata
- **Published**: 2026-08-18T14:28:51Z
- **Authors**: Maosen Zhang, Jianshuo Dong, Boting Lu, Wenyue Li, Xiaoping Zhang, Tianwei Zhang, Jie Zhang, Han Qiu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17829v1)