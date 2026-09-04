---
title: Beyond Shallow Alignment: How Post-Training Methods Determine Refusal Circuits And Steering Robustness
published: 2026-09-03T14:10:17Z
authors: Hoang Cuong Nguyen, Mark Dras, Usman Naseem
url: http://arxiv.org/abs/2609.03887v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Shallow Alignment: How Post-Training Methods Determine Refusal Circuits And Steering Robustness

## Abstract
How do the methods used to train language models to refuse harmful requests shape how that refusal actually works inside the model? We compare three post-training methods - supervised fine-tuning, reasoning-augmented fine-tuning (training on reasoning chains that justify a safety decision), and preference optimization (ORPO) - across three architecturally distinct models (Llama-3.1-8B, Gemma-2-9B, Qwen3-8B). We find that training method, not just data, reshapes how refusal is computed internally: reasoning-augmented training consistently produces a distinct kind of refusal computation, visible across all three models, while architecture independently shapes internal structure and how reliably refusal can be steered. Most importantly, no method we study achieves all three properties we would want from safe alignment at once: refusal that isn't concentrated in a few fragile components, safety gains that don't cost general capability, and safety behavior correctable through small, targeted edits. We caution against treating current post-training methods as a solved, reliable defense, especially for security-critical use. Code and models are available in https://github.com/hoangcuongnguyen2001/Beyond-Shallow-Alignment.

## Metadata
- **Published**: 2026-09-03T14:10:17Z
- **Authors**: Hoang Cuong Nguyen, Mark Dras, Usman Naseem
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03887v1)