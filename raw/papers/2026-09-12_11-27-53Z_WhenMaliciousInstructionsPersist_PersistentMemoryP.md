---
title: When Malicious Instructions Persist: Persistent Memory Poisoning Attack on Harness-Based Agents
published: 2026-09-12T11:27:53Z
authors: Shuhuai Huang, Jingfeng Zhang, Hong Jia
url: http://arxiv.org/abs/2609.13889v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Malicious Instructions Persist: Persistent Memory Poisoning Attack on Harness-Based Agents

## Abstract
Harness design has transformed the development of LLM-based agents by integrating memory, tool use, and runtime control. However, this design also introduces security and privacy risks because malicious instructions from external sources may be written into persistent memory and persist across sessions. To study this risk, we propose PMPA, a Persistent Memory Poisoning Attack against harness-based agents. PMPA embeds malicious instructions into benign external sources and induces the victim agent to write them into persistent memory without directly accessing to the agent framework. Once stored, the poisoned memory can be retrieved in later sessions, triggering additional malicious actions and causing privacy leakage. We evaluate PMPA on OpenClaw and Claude Code across different backbone LLMs, input modalities, and trigger scenarios. Across all settings, PMPA achieves average Injection Success Rate (ISR) and Cross-session Attack Success Rate (C-ASR) of 73.7%/ 55.5% on OpenClaw and 66.9%/ 81.7% on Claude Code, while preserving benign task performance on both systems. We further evaluate a targeted prompt-level defense and find that it can reduce memory injection in many settings, but provides limited protection once the persistent memory has been poisoned.

## Metadata
- **Published**: 2026-09-12T11:27:53Z
- **Authors**: Shuhuai Huang, Jingfeng Zhang, Hong Jia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.13889v1)