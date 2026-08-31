---
title: Probing Perceptual Priors of MLLMs via Gibbs Sampling with Interpretable Generative Controls
url: http://arxiv.org/abs/2608.27727v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-27_21-38-41Z_ProbingPerceptualPriorsofMLLMsviaGibbsSamplingwith.md
generated_at: 2026-08-30 23:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a method for sampling directly from the perceptual priors of multimodal language models by using Gibbs sampling on stimuli generated along controllable axes while the model evaluates them. The approach reveals both well‑known biases and novel, previously unseen expectations that influence model behavior.

## Key Takeaways
- The authors generate stimulus variations across specific dimensions such as trustworthiness in faces or cheapness in art images and use Gibbs sampling to explore the full prior distribution rather than a fixed set of inputs.  
- Their method recovers canonical biases like associating certain facial features with higher trust but also uncovers surprising priors that are invisible to direct prompting.  
- These hidden expectations can affect downstream tasks, indicating that model behavior is shaped by an internal stimulus space beyond what prompts alone control.

## Context
Understanding the implicit distribution of stimuli a model expects is crucial because real‑world inputs are high‑dimensional and diverse. Traditional interpretability methods either probe representation or vary inputs while holding priors constant, leaving this component largely unexplored. This work bridges that gap by directly sampling from those priors.

## Implications
For practitioners, revealing these latent priors can guide more transparent model design and mitigate unintended biases in applications like facial recognition or content moderation. Industry adoption may require tools that expose such hidden expectations to improve fairness and user trust.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.27727v1)
