---
title: TAME: Token Attribution and Masking for Emergent misalignment
published: 2026-09-15T07:30:01Z
authors: Md Rayhanul Masud, Md Rizwan Parvez
url: http://arxiv.org/abs/2609.16754v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TAME: Token Attribution and Masking for Emergent misalignment

## Abstract
Fine-tuning an aligned language model on narrow, flawed data can induce harmful behavior far outside the training domain, known as emergent misalignment (EM). Prior work has localized EM in model weights, activations, and training documents, but it remains unclear which training tokens carry the relevant fine-tuning signal. We introduce TAME (Token Attribution and Masking for Emergent Misalignment), a three-stage framework: token attribution scores how strongly the fine-tuning update raises each response token's likelihood, using forward passes through a released LoRA adapter; signal characterization finds patterns among high-attribution tokens; and causal validation tests them by attribution-guided loss masking. On released EM organisms and a 6,849-example medical-advice split, attribution is concentrated (the top 5% of tokens hold 32% of the mass) and, in Llama, depleted for medical vocabulary but enriched for a register of unwarranted certainty, even after controlling for token rarity. Masking high-attribution tokens during fresh fine-tuning cuts EM by 23x in Llama and 36x in Qwen, with the perplexity cost concentrated on the targeted register rather than on medical content; an equal random mask leaves EM unchanged. In Llama, the attribution pattern suggests that EM-relevant signal lies more in how confidently flawed content is expressed than in its domain vocabulary; the causal masking effect itself holds across both model families.

## Metadata
- **Published**: 2026-09-15T07:30:01Z
- **Authors**: Md Rayhanul Masud, Md Rizwan Parvez
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.16754v1)