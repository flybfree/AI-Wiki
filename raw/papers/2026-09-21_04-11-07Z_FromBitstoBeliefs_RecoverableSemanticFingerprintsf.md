---
title: From Bits to Beliefs: Recoverable Semantic Fingerprints for Black-Box Verification of Large Language Models
published: 2026-09-21T04:11:07Z
authors: Jiaxin Hong, Yuxin Peng, Hongyao Yu, Hao Fang, Shuoyang Sun, Bin Chen
url: http://arxiv.org/abs/2609.24084v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Bits to Beliefs: Recoverable Semantic Fingerprints for Black-Box Verification of Large Language Models

## Abstract
Open-weight large language models (LLMs) can be copied, modified, and redeployed behind black-box APIs, making post-release ownership verification difficult. Existing black-box fingerprints often rely on secret query-key pairs that reproduce predefined responses, and can therefore be easily disrupted by fine-tuning, pruning, quantization, model merging, and serving-time prompt changes. We propose SimPrint, a recoverable semantic fingerprinting framework for black-box LLM ownership verification. Rather than relying on isolated exact matches, SimPrint encodes a private owner signature into a coded semantic fingerprint domain, distributing ownership evidence across natural binary question-answering probes. It implants only base-deviating probes through a low-interference batch update that preserves the original model behavior, and later recovers the signature by parsing suspect-model responses into reliable bits or erasures with an error-correcting recovery mechanism. Because verification only uses input-output queries, SimPrint remains applicable when model weights or activations are inaccessible. Experiments on three open-weight LLMs show that SimPrint reliably recovers the owner signature in both clean and modified settings, remains robust under fine-tuning, pruning, quantization, model merging, and serving-time perturbations, and maintains comparable downstream utility.

## Metadata
- **Published**: 2026-09-21T04:11:07Z
- **Authors**: Jiaxin Hong, Yuxin Peng, Hongyao Yu, Hao Fang, Shuoyang Sun, Bin Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.24084v1)