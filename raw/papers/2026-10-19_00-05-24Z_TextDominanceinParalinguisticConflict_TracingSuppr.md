---
title: Text Dominance in Paralinguistic Conflict: Tracing Suppression Through Audio LLM Circuits
published: 2026-10-19T00:05:24Z
authors: Ankur Banerjee, Vishnu Guntakala, Danity Pike, Advay Roongta, Kevin Yang, Ruizhe Li
url: http://arxiv.org/abs/2610.25599v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Text Dominance in Paralinguistic Conflict: Tracing Suppression Through Audio LLM Circuits

## Abstract
Audio LLMs deployed in settings such as crisis hotlines and customer support are only useful beyond speech-to-text pipelines if they use acoustic cues rather than the transcript alone. We test whether they prioritise transcript content over paralinguistic cues (emotion, speaker identity, sarcasm) and trace the mechanism when they do. Across six audio LLMs under LISTEN-style conflict conditions, the mean text-dominance rate on mismatched text+audio items is 0.78 (0.86 excluding sarcasm). In the most text-dominant screened model, probing shows speaker identity remains linearly decodable at ceiling at the language model's input, so the failure is not perceptual. Back-patching, reported to repair lexical text dominance, has no measurable effect here; but it also fails on its own source task in our replication (n=300), so we treat its null as uninformative rather than as evidence of non-transfer. Attention knockout partially restores audio-grounded output by blocking the claim from propagating through intermediate tokens during open-ended generation, whereas blocking the answer position's direct connection to the conflicting claim has no effect. The claim's influence therefore travels through an intermediate relay rather than a single severable edge. The effect appears only in free-form generation and not in closed-set multiple choice, suggesting that benchmarks relying on that format may be systematically blind to interventions of this kind. Code and data are publicly available at https://github.com/AdvayRoongta/audio-llm-mech-interp.

## Metadata
- **Published**: 2026-10-19T00:05:24Z
- **Authors**: Ankur Banerjee, Vishnu Guntakala, Danity Pike, Advay Roongta, Kevin Yang, Ruizhe Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25599v1)