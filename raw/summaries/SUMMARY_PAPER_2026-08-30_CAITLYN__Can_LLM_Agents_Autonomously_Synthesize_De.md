---
title: CAITLYN: Can LLM Agents Autonomously Synthesize Defenses against Emerging Injection Attacks?
url: http://arxiv.org/abs/2608.27990v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_06-58-26Z_CAITLYN_CanLLMAgentsAutonomouslySynthesizeDefenses.md
generated_at: 2026-08-30 20:12
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces CAITLYN, a middleware that defends LLM agents from prompt injection attacks by combining immediate detection (System I) with autonomous defense synthesis (System II). On standard benchmarks it matches top defenses with lower token overhead, but on the Emerging benchmark its System I remains vulnerable while System II reduces attack success rates.  

## Key Takeaways  
- CAITLYN’s two‑tiered library (Tier‑0 rule‑based detection and Tier‑1 LLM inference) provides immediate defense against known injection attacks.  
- The middleware’s autonomous System II monitors abnormal signals and synthesizes new defenses, lowering attack success across three agent environments.  
- On the Emerging benchmark, standalone System I is vulnerable whereas System II significantly improves robustness.  

## Context  
Prompt injection remains a critical threat to LLM‑based agents because attackers can manipulate retrieved text sources. Existing defenses often involve trade‑offs between speed, accuracy, and adaptability, limiting their deployment in dynamic agent workflows.  

## Implications  
CAITLYN offers a practical path for deploying secure LLM agents by reducing token cost while maintaining high detection rates. Practitioners can adopt its autonomous synthesis to stay ahead of emerging attacks without constant manual updates.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.27990v1)
