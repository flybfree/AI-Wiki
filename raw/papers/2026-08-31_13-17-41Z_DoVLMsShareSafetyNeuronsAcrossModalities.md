---
title: Do VLMs Share Safety Neurons Across Modalities?
published: 2026-08-31T13:17:41Z
authors: Jiaxuan Li, Jiahao Zhang, Duc Minh Vo, Huy H. Nguyen, Pride Kavumba, Koki Wataoka
url: http://arxiv.org/abs/2608.30750v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Do VLMs Share Safety Neurons Across Modalities?

## Abstract
Vision-language models (VLMs) can comply with harmful requests delivered through images, even when their LLM backbones would refuse the same content in text. While prior work characterizes these jailbreaks empirically or at the representation level, how visual inputs perturb safety pathways at the neuron level remains uncharted. We close this gap with a causal, neuron-level analysis of safety mechanisms in 10 VLMs. We propose a two-stage detection pipeline with iterative ablation that accounts for self-repair, and introduce two modality-isolated benchmarks, ViSafe-Detect and ViSafe-Eval, which decouple visual and textual safety signals.   Our analysis reveals: (i) Text safety in VLMs is localizable: $\sim$88 neurons ($<$0.01%) whose targeted ablation substantially reduces refusal. (ii) Text safety neurons constitute the dominant refusal pathway: ablating them is the only intervention that consistently and substantially reduces refusal across all models. (iii) Visual safety is high-dimensional and diffuse at the single-neuron level: text safety concentrates in $\sim$5 subspace directions while visual safety requires $\geq$50. This gap holds across architectures, explaining why current alignment has not closed the visual safety gap. Project page is at: https://jiaxuan-li.github.io/vlm-safety-neuron/   Warning: this paper may include examples of harmful content.

## Metadata
- **Published**: 2026-08-31T13:17:41Z
- **Authors**: Jiaxuan Li, Jiahao Zhang, Duc Minh Vo, Huy H. Nguyen, Pride Kavumba, Koki Wataoka
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30750v1)