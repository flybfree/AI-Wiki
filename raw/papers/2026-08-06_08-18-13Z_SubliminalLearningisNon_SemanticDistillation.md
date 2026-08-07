---
title: Subliminal Learning is Non-Semantic Distillation
published: 2026-08-06T08:18:13Z
authors: Ethan Hadley, Eren Gultepe
url: http://arxiv.org/abs/2608.05734v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Subliminal Learning is Non-Semantic Distillation

## Abstract
Subliminal Learning (SL) is a surprising type of generalization displayed by modern language models. It allows the transfer of a bias or behavior from a teacher model to a student by distilling from seemingly unrelated or random synthetic data from the teacher. This presents challenges in ensuring AI systems remain predictable and are trained safely, as standard auditing of the input data would not catch the hidden subliminal signal. Here, we investigate several open questions as to the enabling mechanisms and drivers of SL. First is the nature of the process by which biases are encoded in the data. We find that by adding Gaussian noise to the weights of the teacher and student models, the magnitude of subliminal transfer is increased by a factor of 1.9 in Gemma and 1.3 in Llama, suggesting that non-semantic weight structures play a crucial role. We show that steering vectors can be applied to the teacher to produce subliminal data, in addition to prompting and finetuning as used in previous studies. Analysis of the activations of the student models that have been trained on steered and prompted data demonstrates that students inherit not just the semantic meaning of the teacher's bias, but also the type of intervention that was used to apply it: steered students imitate steering vectors, prompted students do not. Additionally, the gradients of steered subliminal data show a linear correlation with the teacher's steering vectors, showing promise for data auditing. More broadly, as synthetic data becomes central to frontier training pipelines, being able to see the latent signals hidden in training data becomes paramount.

## Metadata
- **Published**: 2026-08-06T08:18:13Z
- **Authors**: Ethan Hadley, Eren Gultepe
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05734v1)