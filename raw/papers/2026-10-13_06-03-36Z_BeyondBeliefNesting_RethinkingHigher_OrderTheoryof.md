---
title: Beyond Belief Nesting: Rethinking Higher-Order Theory of Mind in Large Language Models
published: 2026-10-13T06:03:36Z
authors: Shanshan You, Zhengqi Wang, Hao Liu, Yuqin Liu, Ya He, Xin Hao, Liyuan Wang
url: http://arxiv.org/abs/2610.17777v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Belief Nesting: Rethinking Higher-Order Theory of Mind in Large Language Models

## Abstract
Theory of mind (ToM), the ability to reason about others' mental states, underlies effective communication and coordination. Its higher-order form enables reasoning over nested perspectives in strategic interactions. However, existing evaluations often equate belief-nesting depth with reasoning order, allowing nominally higher-order questions to admit lower-order shortcuts. We formalize effective order through the distinct events supporting successive belief prefixes, revealing widespread order inflation across existing benchmarks. We introduce HopToM, with certified full-order questions and controls for lower-order alternatives. Under direct prompting, mean accuracy across four frontier LLMs falls from 73.5% at first order to 20.0% at fourth order, and human participants also struggle. Causal interventions link a recurring class of errors to evidence for shallower belief prefixes. We introduce HopTrace, a plug-and-play inference-time method that encodes each interaction once into perspective records and resolves nested queries deterministically. On certified narrative questions, it improves fourth- and fifth-order accuracy by 22.0 and 38.5 percentage points over strong prompting baselines, while using 20-39 times fewer tokens than multi-call methods. These results sharpen how higher-order ToM is evaluated and offer a practical way to improve perspective reasoning in interactive agents.

## Metadata
- **Published**: 2026-10-13T06:03:36Z
- **Authors**: Shanshan You, Zhengqi Wang, Hao Liu, Yuqin Liu, Ya He, Xin Hao, Liyuan Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.17777v1)