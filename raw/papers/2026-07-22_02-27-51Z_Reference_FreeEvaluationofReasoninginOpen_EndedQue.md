---
title: Reference-Free Evaluation of Reasoning in Open-Ended Question Answering
published: 2026-07-22T02:27:51Z
authors: Guneet Singh Kohli, Yuxiang Zhou, Michael Sejr Schlichtkrull, Gregory E Dean, Maria Liakata
url: http://arxiv.org/abs/2607.19678v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reference-Free Evaluation of Reasoning in Open-Ended Question Answering

## Abstract
AI-generated answers in high-stakes domains are often fluent but difficult to verify, especially when they contain multi-step reasoning rather than a single final answer. We propose a reasoning-based, reference-free framework for auditing LLM-generated outputs. The method decomposes a generated reasoning trace into segments, labels local premise-target relations using Natural Language Inference (NLI), and organizes these relations into a hypergraph. A deterministic backward AND-OR search then assigns segment-level audit labels that indicate how each segment is grounded within the generated response. We evaluate the framework in two settings: deductive mathematical reasoning with Hard2Verify, and open-ended medical reasoning with UroReason, a new physician-annotated benchmark of LLM reasoning traces from real clinical cases. Across these settings, our NLI-hypergraph audit provides a more reliable reference-free evaluation signal than direct LLM-as-judge baselines. In the clinical setting, state-of-the-art LLM judges often fail to identify problematic reasoning segments, over-accepting fluent but weakly grounded responses. Our results show that QA evaluation should account for how inferential relations compose across a reasoning trace, rather than relying only on final answers or LLMs as verifiers. UroReason will be made available through an API, and our code will be released as open source.

## Metadata
- **Published**: 2026-07-22T02:27:51Z
- **Authors**: Guneet Singh Kohli, Yuxiang Zhou, Michael Sejr Schlichtkrull, Gregory E Dean, Maria Liakata
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19678v1)