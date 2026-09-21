---
title: HE-Guardrail: A Homomorphic Guardrail Against Jailbreak Attacks for Encrypted Large Language Model Inference
published: 2026-09-18T08:36:37Z
authors: Byeongseo Min, Yongwoo Lee, Young-Sik Kim, Yongjune Kim
url: http://arxiv.org/abs/2609.21484v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HE-Guardrail: A Homomorphic Guardrail Against Jailbreak Attacks for Encrypted Large Language Model Inference

## Abstract
Homomorphic encryption (HE) has emerged as a promising approach to privacy-preserving machine learning (PPML), enabling computation directly over encrypted data. In HE-based PPML, a client submits an encrypted input to the server, which evaluates models such as large language models (LLMs) without access to the underlying plaintext. However, we identify a critical security vulnerability in this setting: HE-LLM inference is vulnerable to malicious clients that submit adversarial prompts, such as jailbreak attacks. The same confidentiality that protects benign clients also prevents the server from inspecting incoming prompts or generated responses, making adversarial attempts difficult to detect or block and potentially allowing successful attacks to remain entirely invisible to the server. To address this vulnerability, we propose HE-Guardrail, a framework that evaluates guardrail mechanisms entirely over encrypted data and homomorphically controls whether the target-model response is returned to the client. We instantiate HE-Guardrail with three representative guardrails - Llama Guard, JBShield, and GradSafe. Our results show that HE-Guardrail closely reproduces the decisions of the corresponding plaintext guardrails in the encrypted domain, with distinct security-efficiency-utility trade-offs.

## Metadata
- **Published**: 2026-09-18T08:36:37Z
- **Authors**: Byeongseo Min, Yongwoo Lee, Young-Sik Kim, Yongjune Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.21484v1)