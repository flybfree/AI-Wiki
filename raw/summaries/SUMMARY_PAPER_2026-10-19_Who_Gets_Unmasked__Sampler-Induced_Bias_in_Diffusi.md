---
title: Who Gets Unmasked? Sampler-Induced Bias in Diffusion Language Models
url: http://arxiv.org/abs/2610.24795v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-17_18-02-49Z_WhoGetsUnmasked_Sampler_InducedBiasinDiffusionLang.md
generated_at: 2026-10-19 21:42
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates a previously overlooked source of bias in diffusion language models (dLLMs): the sampler's commit rule, which determines not only which token to generate but also the order in which positions on the unmasking canvas are committed. The authors demonstrate that common commit strategies, such as LLaDA's default "peeking" approach that commits the most probable tokens first, systematically amplify majority-group representations (e.g., male protagonists, stereotypical occupational genders) beyond what the underlying model itself encodes. They introduce Fork-First Sampling as a mitigation strategy that resolves critical identity forks before any other tokens are written, thereby aligning output distributions with the model's true beliefs or a target distribution.

## Key Takeaways
- The commit rule in dLLM samplers constitutes a distinct, sampler-induced bias layered on top of the model's own learned biases. LLaDA's default strategy commits positions whose sampled tokens carry the highest probability, effectively "peeking" at the model's outputs and preferentially locking in majority options early, which cascades into amplified occupational gender stereotypes and collapsed opinion distributions in generated text.
- The authors develop a diagnostic method that reads the model's belief about a critical fork (such as a protagonist's gender) in a single forward pass, showing this belief matches exact sampling from the model. Measured against this ground truth, peeking-based samplers on both LLaDA and Dream models demonstrably distort output distributions, and confidence-based ordering further shifts gender-balanced occupations toward men, with the distortion worsening under faster parallel decoding.
- Fork-First Sampling resolves the identity fork before committing any other tokens, following either the model's internal belief or an externally specified target distribution. This approach improves fluency, avoids the awkward self-referential stories that prompt-based fairness fixes tend to produce, and requires only one additional forward pass, making it a practical and principled correction.

## Context
Diffusion language models represent a growing alternative to autoregressive transformers, generating text by iteratively unmasking a fixed-length canvas rather than predicting tokens sequentially. While much fairness research has focused on training data and model architecture, this paper reveals that the inference-time decoding algorithm itself is a significant and underexamined source of demographic bias. As dLLMs like LLaDA and Dream gain traction in research and potential deployment, understanding how their samplers interact with model beliefs becomes essential for responsible evaluation and deployment.

## Implications
For practitioners and evaluators, the paper argues that fairness assessments of dLLMs must explicitly report which commit rule was used during generation, since the same model can produce materially different demographic distributions depending on the sampler. For model developers, Fork-First Sampling offers a concrete, low-overhead intervention that decouples sampler behavior from model bias, enabling more faithful generation and more reliable benchmarking. For the broader field, this work establishes that inference-time algorithmic choices deserve the same scrutiny as training-time choices in any serious fairness audit of generative models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.24795v1)
