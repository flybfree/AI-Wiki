---
title: Adversarial Attacks in Multi-Agent LLM Pipelines: Unveiling Structural Vulnerabilities in Agentic AI Architectures
published: 2026-08-01T15:35:58Z
authors: Faisal Haque Bappy, Tahrim Hossain, Tarannum Shaila Zaman, Raiful Hasan, Kamrul Hasan, Tariqul Islam
url: http://arxiv.org/abs/2608.00718v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adversarial Attacks in Multi-Agent LLM Pipelines: Unveiling Structural Vulnerabilities in Agentic AI Architectures

## Abstract
Multi-agent LLM pipelines orchestrate multiple specialized language model agents into structured workflows where intermediate outputs are passed across agents to solve complex tasks. This design introduces a security gap absent in single-agent settings: once an agent accepts adversarial content, it is propagated as trusted input throughout the pipeline. We argue that this vulnerability stems from the absence of boundary verification, a security primitive that enforces explicit validation of data as it crosses inter-agent boundaries, including content, identity, execution intent, and state integrity. Without such verification, modern pipelines embed implicit trust assumptions that are not adversarially robust, giving rise to structurally distinct attack surfaces (e.g., content injection, agent impersonation, plan deviation, and memory poisoning). Leveraging annotated production traces from the GAIA and SWE-Bench benchmark, we show that these vulnerabilities arise in benign deployments and largely evade existing evaluation frameworks. We further operationalize these failure modes within a controlled multi-agent setting and evaluate them across GPT-5-mini, Claude Sonnet 4.5, and Kimi K2.5 under identical pipeline configurations. The results reveal that attack success aligns with pipeline structure rather than model capability, indicating that adversarial vulnerability is fundamentally an architectural property and motivating a shift toward pipeline-level defenses.

## Metadata
- **Published**: 2026-08-01T15:35:58Z
- **Authors**: Faisal Haque Bappy, Tahrim Hossain, Tarannum Shaila Zaman, Raiful Hasan, Kamrul Hasan, Tariqul Islam
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00718v1)