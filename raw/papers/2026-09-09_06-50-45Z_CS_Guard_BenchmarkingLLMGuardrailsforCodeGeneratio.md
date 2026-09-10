---
title: CS-Guard: Benchmarking LLM Guardrails for Code Generation Security
published: 2026-09-09T06:50:45Z
authors: Jinyang Li, Mingyu Guo, Hung X. Nguyen
url: http://arxiv.org/abs/2609.09798v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CS-Guard: Benchmarking LLM Guardrails for Code Generation Security

## Abstract
Large language models (LLMs) have been ex- ploited to generate malware, but the effective- ness of guardrails for code generation secu- rity remains unclear. We introduce CS-Guard, the first benchmark to systematically evalu- ate guardrails for code generation security. It covers 1) text-to-code generation with 1000 high-quality malware-generation prompts, 7 jailbreak attacks, and a novel fictional scenario attack (FSA) that embeds malicious intent in a legitimate fictional software-development sce- nario; and 2) code-to-code generation with 331 code prompts spanning code infilling, code completion, and code translation. We empiri- cally evaluate 9 guardrails across seven LLMs. We find that current guardrails perform poorly against malicious code-generation re- quests: for text-to-code, the average attack success rate (ASR) after jailbreaks reaches about 50% for many guardrails; for code-to- code, average ASR approaches 100% on base LLMs and remains high across many guardrails (14.4% to nearly 100%). Our FSA also achieves ASR close to 100% across many guardrails, raising major reliability concerns for real-world software development. To sup- port future research, CS-Guard uses a modular three-layer guardrail taxonomy that lets devel- opers register guardrails for evaluation. We release the benchmark and data to enable fur- ther community evaluation.

## Metadata
- **Published**: 2026-09-09T06:50:45Z
- **Authors**: Jinyang Li, Mingyu Guo, Hung X. Nguyen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.09798v1)