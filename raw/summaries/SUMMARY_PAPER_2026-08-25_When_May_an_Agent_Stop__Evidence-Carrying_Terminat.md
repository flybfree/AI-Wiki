---
title: When May an Agent Stop? Evidence-Carrying Termination for Tool-Using LLMs
url: http://arxiv.org/abs/2608.23623v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-22_18-56-27Z_WhenMayanAgentStop_Evidence_CarryingTerminationfor.md
generated_at: 2026-08-25 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Evidence-Carrying Termination (ECT) as a method for tool-using language models to decide when to stop by requiring a typed certificate that binds all answer claims to valid in‑scope trace evidence and a deterministic replay that reconstructs the claimed value. Experiments across 48 synthetic tasks show ECT reduces unsafe completions from 252 to 0, while premature terminations drop from 40 to 0 on held‑out clusters, meeting a -10‑point noninferiority margin. The approach certifies support only within recorded traces under declared assumptions.

## Key Takeaways
- ECT requires both a certificate and deterministic replay to validate every answer claim before allowing completion.
- In synthetic tasks, ECT eliminates unsafe completions (252→0) and premature terminations (40→0), achieving a -10‑point noninferiority margin compared with the critic core.
- The certification is based on recorded traces under declared assumptions rather than external truth or safety.

## Context
Tool‑using LLMs face challenges in stopping safely, often relying on static policies that may ignore trace evidence. This work addresses the gap by testing termination at the complete boundary across execution faults and replay scenarios, providing a more rigorous evaluation framework for AI agents.

## Implications
For practitioners developing autonomous agents, ECT offers a concrete method to ensure completions are grounded in verifiable traces, reducing risk of harmful or incorrect outputs. The approach could become standard practice as tool‑using LLMs expand into safety‑critical domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23623v1)
