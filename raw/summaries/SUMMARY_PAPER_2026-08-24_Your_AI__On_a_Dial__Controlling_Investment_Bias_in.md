---
title: Your AI, On a Dial: Controlling Investment Bias in LLMs with a Single Neuron
url: http://arxiv.org/abs/2608.22852v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_06-33-02Z_YourAI_OnaDial_ControllingInvestmentBiasinLLMswith.md
generated_at: 2026-08-24 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces an “investment‑bias dial” that lets researchers steer the overall buying or selling tendency of large language models at inference time by adjusting a single neuron. Using matched positive and negative evidence, the authors demonstrate that flipping this dial produces monotonic shifts in investment stance across five open‑weight LLMs without altering prompts or model parameters.

## Key Takeaways
- The intervention changes both the final investment decision (buy vs sell) and the emphasis placed on supporting rationales for identical inputs.  
- In an agentic retrieval setting, the dial also alters which information the model searches for, what evidence it selects, and how that evidence is reflected in its analysis.  
- Long‑context experiments show stable stance control even as context length grows, unlike system‑prompt instructions that weaken over longer contexts.

## Context
Large language models are increasingly deployed to guide financial decisions, yet their investment preferences remain opaque and model‑specific. This work shows that a single neuron can serve as a tunable knob for the aggregate bias of an LLM, offering a lightweight alternative to complex prompt engineering or fine‑tuning.

## Implications
For practitioners, the dial provides a simple method to align model outputs with desired risk profiles without retraining or altering system prompts. This could improve transparency and control in automated investment systems, helping regulators and users understand how bias is managed at inference time.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22852v1)
