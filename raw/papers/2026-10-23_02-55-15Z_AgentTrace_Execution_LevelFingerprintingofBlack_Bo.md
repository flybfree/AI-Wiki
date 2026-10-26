---
title: AgentTrace: Execution-Level Fingerprinting of Black-Box LLM Agents
published: 2026-10-23T02:55:15Z
authors: Gejian Zhao, Hanzhou Wu, Xinpeng Zhang
url: http://arxiv.org/abs/2610.32092v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AgentTrace: Execution-Level Fingerprinting of Black-Box LLM Agents

## Abstract
Verifying the provenance of autonomous LLM agents is a critical security challenge. Existing semantic attribution is easily obfuscated by system prompts, while active watermarking conflicts with schema-constrained tool generation. We propose AgentTrace, an active framework that identifies the foundation model behind a black-box agent via observable execution traces. AgentTrace injects structurally ambiguous probes to trigger tokenization-sensitive serialization failures at rigid tool interfaces. While these initial failures provide coarse-grained separation across model families, the temporal sequence of subsequent repair operations reveals fine-grained, model-specific recovery behaviors. By modeling these multi-step trajectories with lightweight Markov chains, AgentTrace achieves 96.0% attribution accuracy under adversarial identity spoofing. Crucially, sequential repair modeling successfully distinguishes the evaluated intra-family variants sharing identical tokenizers (e.g., Llama-3 8B/70B), substantially outperforming unordered behavioral statistics while remaining robust against prompt obfuscation and temperature scaling.

## Metadata
- **Published**: 2026-10-23T02:55:15Z
- **Authors**: Gejian Zhao, Hanzhou Wu, Xinpeng Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.32092v1)