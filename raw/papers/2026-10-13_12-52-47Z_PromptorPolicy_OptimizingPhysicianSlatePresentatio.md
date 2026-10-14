---
title: Prompt or Policy? Optimizing Physician Slate Presentations with LLM User Simulators
published: 2026-10-13T12:52:47Z
authors: Andrei Niculae, Adrian Cosma, Emilian Radoi
url: http://arxiv.org/abs/2610.18309v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Prompt or Policy? Optimizing Physician Slate Presentations with LLM User Simulators

## Abstract
Choosing the right physician is a key challenge for patients seeking medical care. Physician recommendation systems identify relevant doctors, but patients still find it difficult to compare their profiles to make a decision. We formulate slate presentation optimization: given a patient's medical case and a fixed, ranked list of physicians, we generate short, case-specific summaries that make doctors easier to compare, while remaining grounded in the information in their profiles. To optimize physician presentations without relying on real patient interactions, we develop an offline framework that uses persona-conditioned LLMs to simulate patient choices. We generate patient personas from attributes extracted from each medical case and evaluate presentations for factual accuracy, relevance, naturalness and simulated patient choice. We also use a second LLM judge, unseen during optimization, to assess simulator-specific overfitting. We compare automatic prompt-level optimization with GEPA, parameter-level optimization with GRPO, and their combination across two model sizes. GRPO substantially outperforms GEPA in satisfying the full set of constraints, and its gains in simulated conversion persist under the unseen judge. GEPA alone brings smaller improvements, but using its optimized prompt to initialize GRPO speeds up training and achieves the highest simulated conversion. These results show that prompt-level and parameter-level optimization play complementary roles in improving how physician recommendations are presented.

## Metadata
- **Published**: 2026-10-13T12:52:47Z
- **Authors**: Andrei Niculae, Adrian Cosma, Emilian Radoi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.18309v1)