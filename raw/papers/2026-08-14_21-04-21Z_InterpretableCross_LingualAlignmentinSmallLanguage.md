---
title: Interpretable Cross-Lingual Alignment in Small Language Models: Probing Cultural and Pragmatic Reasoning in Japanese-English Bilingual LLMs
published: 2026-08-14T21:04:21Z
authors: Florian Braun
url: http://arxiv.org/abs/2608.14896v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Interpretable Cross-Lingual Alignment in Small Language Models: Probing Cultural and Pragmatic Reasoning in Japanese-English Bilingual LLMs

## Abstract
Large language models work well on English and behave in poorly understood ways on languages typologically far from it. Japanese is a clean example, where evaluation still leans on translation quality and JGLUE-style benchmarks, which roll lexical, syntactic and pragmatic competence into a single score. The phenomena on which general-purpose models fail Japanese users are pragmatic: honorifics, in-group and out-group reference, context-sensitive politeness, zero anaphora.   I introduce J-PragEval-v0, a minimal-pair benchmark isolating four such phenomena from surface fluency, and combine it with linear probes and teacher-forced log-probability evaluation to ask where inside TinySwallow-1.5B (28 layers, hidden size 1536) the corresponding contrasts live. The four features split three ways. Honorific register sits cleanly in the residual stream: 0.96 balanced accuracy at layer 15, and the model flips its preferred continuation with the scenario on 93 percent of items. Implicit subject and in-group reference are not linearly decodable at the final prompt token (0.48 and 0.38), yet flip rates are 0.77 and 0.79, so the contrast is worked out during generation rather than stored at the prompt. Indirect refusal is the negative case: 0.95 probe accuracy collapsing to a 0.43 flip rate under length-normalised teacher forcing, because the current minimal pairs conflate politeness with continuation length.   I also specify Pragmatic Representation Steering, a parameter-free inference-time method that edits residual-stream activations along the class-mean-difference directions probing identifies. Feasibility is argued indirectly rather than demonstrated: the contrastive activation addition baseline, the same geometry the method would inject, recovers probe accuracy within one to two points of logistic regression wherever a linear signal exists. Scaling to Llama-3.1-Swallow-8B is the next step.

## Metadata
- **Published**: 2026-08-14T21:04:21Z
- **Authors**: Florian Braun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14896v1)