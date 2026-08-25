---
title: CyberFactory: Scaling Cyber Security Capabilities with Instances from the Wild
url: http://arxiv.org/abs/2608.23181v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_12-30-10Z_CyberFactory_ScalingCyberSecurityCapabilitieswithI.md
generated_at: 2026-08-24 21:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CyberFactory a framework that turns public vulnerability artifacts into executable tasks and trains an open-source model to answer cybersecurity questions using agentic feedback loops. The resulting model Aegis achieves 52.4% Pass@1 on CyberGym within one hour, beating the Qwen~3.5 base by over twenty points.

## Key Takeaways
- CyberFactory converts CVEs from the wild into reproducible task instances that guide a teacher through source inspection problem solving and validation.
- The model learns to interact with tools and environments and updates its reasoning based on execution feedback creating an agentic training loop.
- Aegis reaches 52.4% Pass@1 on CyberGym, significantly outperforming the Qwen~3.5 base by twenty eight points.

## Context
Open-source cybersecurity models currently lack scalable solutions that integrate real-world vulnerability data and dynamic feedback mechanisms. Existing approaches either treat tasks in isolation or rely on closed proprietary systems without transparent training pipelines.

## Implications
This work demonstrates that open-weight LLMs can be trained to perform complex, tool‑driven security reasoning at scale. Practitioners can adopt CyberFactory to build reusable defense agents that continuously improve through observed failures and successes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23181v1)
