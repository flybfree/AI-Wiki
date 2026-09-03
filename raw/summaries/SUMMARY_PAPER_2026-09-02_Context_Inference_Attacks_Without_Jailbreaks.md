---
title: Context Inference Attacks Without Jailbreaks
url: http://arxiv.org/abs/2609.01663v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-08-31_21-53-52Z_ContextInferenceAttacksWithoutJailbreaks.md
generated_at: 2026-09-02 20:31
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper investigates how AI agents that handle sensitive data remain vulnerable to hidden-context leakage even when protected by instruction constraints and logit suppression. It formalizes context‑inference attacks as a security game across three settings: known, unknown, and agent‑retrieved contexts, comparing grey‑box and black‑box scoring approaches.

## Key Takeaways  
- Agents leak information about records in their hidden context even when told not to disclose it, demonstrating that logit suppression does not fully prevent inference. - The attack works across different delivery mechanisms: the attacker knows the exact template, or only receives a vague summary, or the agent itself fetches the data through its own tool calls. - Leakage metrics such as ASR and AUROC vary with query budget, context size, and model scale, reaching 100% on small candidate sets and up to 92.5% AUROC when a surrogate scores a large target.

## Context  
AI systems increasingly embed private data in the inference context to enable personalized responses without exposing it directly. Traditional privacy defenses focus on preventing direct disclosure through jailbreaks, but they often ignore indirect leakage that arises from the composition of tool calls and hidden records.

## Implications  
This work shows that even well‑guarded agents can be exploited for contextual inference, raising concerns about data exposure in high‑value applications like healthcare and finance. Practitioners must adopt stronger evaluation protocols that consider agentic workflows and may need to redesign scoring mechanisms to mitigate indirect leakage.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01663v1)
