---
title: Salami Attack: Stealthy Collusive Memory Poisoning against OpenClaw
published: 2026-08-03T03:17:26Z
authors: Zheng Lin, Yuzhe Huang, Zhenxing Niu, Xianmin Ye, Haichang Gao
url: http://arxiv.org/abs/2608.01637v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Salami Attack: Stealthy Collusive Memory Poisoning against OpenClaw

## Abstract
Long-term memory enables LLM agents to retain useful information across sessions, but also creates an attack surface through which adversaries may poison an agent's persistent memory to steer its behavior. Existing memory poisoning attacks mainly rely on individually malicious records, overlooking a compositional threat: multiple benign-looking memories may jointly induce unsafe behavior. In this paper, we introduce MemCollusion, an automated red-teaming framework for constructing collusive memory poisoning attacks. MemCollusion applies salami tactics---a strategy that slices an adversarial objective into small, individually innocuous pieces---to generate memory fragments that are individually benign looking but collectively harmful. It constructs memory coalitions using four design constraints, five theory-informed strategies, and a fine-tuned generator. To assess collusive memory poisoning in a realistic cross-session setting, we develop MoltLab, a controlled research reproduction of Moltbook, in which crafted platform content must first be observed and distilled into persistent memory before influencing the agent's behavior in a separate session. We evaluate MemCollusion on OpenClaw using two backbone models across 48 scenarios. Under the strongest memory-saving setting, MemCollusion achieves an average Memory Save Rate of 81.3% and an Attack Success Rate of 75.0%, and remains effective under both benign memory dilution and memory-level defenses.

## Metadata
- **Published**: 2026-08-03T03:17:26Z
- **Authors**: Zheng Lin, Yuzhe Huang, Zhenxing Niu, Xianmin Ye, Haichang Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01637v1)