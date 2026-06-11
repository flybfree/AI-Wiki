---
title: Good Agentic Friends Do Not Just Give Verbal Advice: They Can Update Your Weights
url: http://arxiv.org/abs/2605.13839v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-13_17-58-32Z_GoodAgenticFriendsDoNotJustGiveVerbalAdvice_TheyCa.md
generated_at: 2026-06-11 10:40
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes TFlow, a weight-space communication framework that lets frozen role‑prompted sender agents exchange information with a fixed receiver model without appending messages to the context. Instead of generating tokens, the senders’ hidden states are mapped into low‑rank LoRA perturbations applied only during the receiver’s generation. The method improves accuracy by up to 8.5 points while cutting token processing and inference time dramatically.

## Key Takeaways
- TFlow replaces text messages with transient weight perturbations that are fused at generation, eliminating the need for a longer context window.
- The low‑rank LoRA updates target specific receiver modules, providing instance‑level adaptation without permanently altering model parameters.
- Compared to a three‑agent text baseline, TFlow reduces total processed tokens by 83.27% and wall‑clock time by up to four times while maintaining competitive benchmark scores.

## Context
Current multi‑agent LLM systems rely on sequential token exchange, which inflates computational cost and memory usage. Efficient communication methods are needed to scale collaborative reasoning across many agents without sacrificing performance.

## Implications
This approach offers a scalable way for large organizations to deploy multiple specialized agents that can collaborate efficiently, lowering infrastructure costs and enabling faster response times in production applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.13839v1)
