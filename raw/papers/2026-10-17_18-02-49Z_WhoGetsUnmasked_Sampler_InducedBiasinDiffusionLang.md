---
title: Who Gets Unmasked? Sampler-Induced Bias in Diffusion Language Models
published: 2026-10-17T18:02:49Z
authors: Xujun Che, Farsheed Haque, Depeng Xu, Xi Niu, Haopeng Zhang
url: http://arxiv.org/abs/2610.24795v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Who Gets Unmasked? Sampler-Induced Bias in Diffusion Language Models

## Abstract
Diffusion language models (dLLMs) generate by gradually unmasking a canvas, so their samplers decide not only which token to write but also when to commit it. We show that this second decision changes who appears in generated text, a sampler-induced bias on top of the model's own. Common commit rules, including LLaDA's default, commit the positions whose sampled tokens are most probable; this peeking favors majority options. To separate the sampler from the model, we read the model's belief about a fork, such as a protagonist's gender, in one forward pass, and show that this belief matches exact sampling from the model. Measured against it, peeking samplers on LLaDA and Dream amplify occupational gender stereotypes and collapse opinion distributions, and confidence-based ordering shifts gender-balanced occupations toward men, more so under faster parallel decoding. We propose Fork-First Sampling, which decides the fork before anything else is written: it follows the belief or any target distribution, improves fluency, and avoids the stories that remark on the protagonist's gender, which prompt-based fixes produce, at the cost of one forward pass. Fairness evaluations of dLLMs should report the commit rule.

## Metadata
- **Published**: 2026-10-17T18:02:49Z
- **Authors**: Xujun Che, Farsheed Haque, Depeng Xu, Xi Niu, Haopeng Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.24795v1)