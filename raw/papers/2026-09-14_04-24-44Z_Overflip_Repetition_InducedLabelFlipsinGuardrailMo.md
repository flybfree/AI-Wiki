---
title: Overflip: Repetition-Induced Label Flips in Guardrail Models
published: 2026-09-14T04:24:44Z
authors: Xu He, Chih-Hsuan Lin, Hung-Mao Chen, Junjie Xiong, Yan Zhai, Kun Sun
url: http://arxiv.org/abs/2609.15013v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Overflip: Repetition-Induced Label Flips in Guardrail Models

## Abstract
Guardrail models are classifiers deployed to screen malicious prompts and responses in LLM-based services. To meet latency constraints, many lightweight guardrails adopt compact Transformer backbones (e.g., DeBERTa) that are trained with short context windows (typically 512 tokens) and rely on bucketed relative positional encodings to process longer inputs. Prior evaluations assume that a guardrail's decision is stable as the input is lengthened. We show that this assumption can fail. We identify Overflip, a repetition-induced instability where repeating a prompt causes the guardrail's prediction to flip (MAL$\to$BEN) as the sequence grows. We conduct experiments on 9 widely used lightweight guardrail models. Five exhibit MAL$\to$BEN flips on a benchmark of 100 prompts, with confidence margins shrinking steadily with repetition. Among these vulnerable models, flip rates range from 8% to 92%, with first flips occurring at roughly 2.6k--9.4k tokens. Our analysis suggests Overflip differs from traditional attention-dilution baselines, which aim to divert the model's attention away from tokens associated with malicious content, shifting it instead toward unrelated content, such as benign padding or shuffling. While Overflip preserves malicious content, it homogenizes token-level attention over repeated structure and induces a distinct, more gradual attention-dispersion trajectory than padding. Moreover, Overflip poses a greater threat to LLM services than traditional attention dilution methods. Because the bypassed prompt remains semantically intact and is still readily understood by downstream business LLMs, it can transmit malicious intent after passing the guardrail. These findings expose repetition as an attack surface for guardrail models and motivate length-robust evaluation and mitigation.

## Metadata
- **Published**: 2026-09-14T04:24:44Z
- **Authors**: Xu He, Chih-Hsuan Lin, Hung-Mao Chen, Junjie Xiong, Yan Zhai, Kun Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.15013v1)