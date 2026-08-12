---
title: Beyond Detection: Evaluating Defensive LLMs Against AI-Generated Social Engineering in Live Turn-by-Turn Interaction
url: http://arxiv.org/abs/2608.10239v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_21-17-03Z_BeyondDetection_EvaluatingDefensiveLLMsAgainstAI_G.md
generated_at: 2026-08-11 22:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether LLM-based defenders can locate the structural source of risk in social‑engineering attacks or only react to surface cues, using a controlled dataset of 300 online housing interactions. It finds that no model ever gave explicit unsafe compliance, but intervention rates varied widely from 0% to 96.3%, showing that safe‑looking behavior does not guarantee protection.

## Key Takeaways
- The study reveals that defensive LLMs often intervene without correctly identifying which trust component (actor authority, asset control, verification sufficiency, or transaction path) is compromised.
- Asset‑control failures are identified as a major bottleneck in structural localization, meaning many attacks evade detection because they preserve other trust elements.
- Surface sensitivity varies across models, causing some to trigger false positives while others miss genuine risks, and live versus static settings produce model‑dependent differences.

## Context
Generative AI has enabled social‑engineering attacks that mimic human agents, making traditional rule‑based defenses insufficient. LLM defenders aim to protect users during ongoing conversations, but their effectiveness is not well measured beyond simple compliance flags.

## Implications
For practitioners, the paper stresses that safe‑looking responses are inadequate; robust defense requires monitoring intervention timing, accurate localization of trust failures, and minimizing false positives. Industry adoption must move beyond static safety checks to dynamic, turn‑by‑turn evaluation frameworks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10239v1)
