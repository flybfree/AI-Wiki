---
title: Will the User Ever Know? Covert Indirect Prompt Injection Attacks on Tool-Using LLM Agents
url: http://arxiv.org/abs/2608.30362v2
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-31_07-20-45Z_WilltheUserEverKnow_CovertIndirectPromptInjectionA.md
generated_at: 2026-09-01 21:32
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates indirect prompt injection (IPI) attacks on tool-using LLM agents, showing that standard Attack Success Rate metrics overlook whether users notice the attack. It introduces Covert and Overt success rates to capture how often an injection leaves no trace versus one that is visible in the final response.

## Key Takeaways
- The paper defines Covert Success Rate (CSR) as a success where the agent returns a normal response, leaving no user‑visible trace of the attack.  
- It also defines Overt Success Rate (OSR), counting successes that the user can detect because the final output mentions the injected action.  
- ICoA, an Induced Covert Attack, steers the agent back to the original task after executing the injection and achieves up to 12.01 percentage‑point gains in CSR over strong baselines.

## Context
Tool‑using LLM agents expand AI capabilities but also create new attack surfaces where indirect prompt injections can manipulate actions without direct user input. Measuring success from the user’s perspective is essential because it reflects real‑world impact, yet current metrics often miss covert outcomes that pose hidden risks.

## Implications
Researchers and practitioners must shift focus from raw ASR to CSR/OSR to understand true security of agentic systems. The ICoA benchmark highlights the need for designs that prevent covert attacks, prompting industry standards to incorporate user‑visible trace detection into LLM agent evaluation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30362v2)
