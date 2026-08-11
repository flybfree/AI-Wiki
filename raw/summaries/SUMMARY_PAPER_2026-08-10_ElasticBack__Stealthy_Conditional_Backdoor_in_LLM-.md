---
title: ElasticBack: Stealthy Conditional Backdoor in LLM-Agent Skills via Coupled Trigger-Rule Optimization
url: http://arxiv.org/abs/2608.09577v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_13-12-35Z_ElasticBack_StealthyConditionalBackdoorinLLM_Agent.md
generated_at: 2026-08-10 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces ElasticBack, a conditional single‑skill backdoor that activates only when a benign trigger and a malicious rule co‑occur in an LLM agent’s skill supply chain. Experiments across three target behaviors and four LLMs demonstrate high attack success rates with near‑zero false positives while preserving clean accuracy.

## Key Takeaways
- ElasticBack plants a rule R inside the skill document and a user query trigger T, so the payload fires only when both appear together.  
- The backdoor uses a trigger‑as‑switch construction that injects R via semantic‑anchored rules, freezes it, and evolves T with a stealth‑constrained genetic search to keep the attack weight‑free and dormant on benign inputs.  
- Experiments across 50 skills per behavior and four agent LLMs show high success rates at near‑zero false positives while clean accuracy remains intact.

## Context
The LLM skill supply chain is an emerging vector where a single compromised skill can affect many agents, yet existing attacks are either always active or require fine‑tuning multiple skills. ElasticBack fills this gap by offering a low‑cost, conditional backdoor that does not alter model weights and can be stealthily deployed.

## Implications
This work highlights the need for defenses that monitor both rule injection and trigger evolution within skill bundles. Practitioners must consider conditional attacks when securing LLM agent ecosystems to prevent silent exploitation of the supply chain.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09577v1)
