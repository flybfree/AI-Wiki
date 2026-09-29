---
title: CyberClear: A Benchmark for LLM Agent Systems on APT Attack Chain Provenance
published: 2026-09-26T09:55:56Z
authors: Qi Chen, Fushuo Huo, Hangli Shen, Jingcai Guo, Shuhao Li, Guang Cheng
url: http://arxiv.org/abs/2609.32424v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CyberClear: A Benchmark for LLM Agent Systems on APT Attack Chain Provenance

## Abstract
Large language model agents have demonstrated promising capabilities in cybersecurity tasks, yet their ability to reconstruct complete Advanced Persistent Threat attack campaigns from complex security logs remains largely unexplored. Existing cybersecurity benchmarks for agents mainly focus on vulnerability discovery, exploitation, and security analysis tasks, leaving the evaluation of attack chain provenance under realistic security logs insufficiently studied. To address this gap, we introduce CyberClear, a benchmark for evaluating LLM agents and advanced agent systems on APT attack chain provenance from long-context security logs. CyberClear covers both single-step attacks and multi-stage attack chains, requiring agents to identify attack evidence, infer attack progression, and generate provenance graphs containing entities, causal relationships, MITRE ATT&CK techniques, and forensic evidence. To enable comprehensive evaluation, we develop an evaluation method tailored to APT attack chain provenance. Unlike conventional text similarity metrics that focus on surface-level matching, our evaluation examines whether reconstructed graphs preserve the semantics of attack chains across single-step behavior correctness, multi-step behavior identification, temporal and causal consistency, entity and relationship fidelity, and overall attack narrative consistency. Advanced multi-agent systems powered by state-of-the-art LLMs still struggle on CyberClear, motivating us to propose CyberProvenance, an agent cyber harness designed for multi-agents that augments LLM agents with evidence accumulation, execution-based validation, and feedback-guided refinement mechanisms for reliable attack-chain provenance. Extensive evaluations on CyberClear demonstrate the effectiveness of CyberProvenance in improving evidence reasoning, execution-grounded validation, and complete APT attack chain reconstruction.

## Metadata
- **Published**: 2026-09-26T09:55:56Z
- **Authors**: Qi Chen, Fushuo Huo, Hangli Shen, Jingcai Guo, Shuhao Li, Guang Cheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32424v1)