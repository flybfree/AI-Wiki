---
title: Black-Box Auditing of Epistemic Reliability in Multi-Agent Debate Distillation
published: 2026-09-26T08:33:34Z
authors: Derui Wang, Zewei Shi, Rayne Holland, Ruoxi Sun, Xingliang Yuan, Jason Xue, Liming Zhu
url: http://arxiv.org/abs/2609.32361v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Black-Box Auditing of Epistemic Reliability in Multi-Agent Debate Distillation

## Abstract
Debate distillation adapts weaker verifiers using multi-agent debate transcripts to improve their judgement in subsequent debates, but gains on monitored tasks do not establish reliability on related unmonitored tasks. We study epistemic reliability degradation, in which adaptation preserves monitored performance while reducing support for correct responses on hidden tasks. We consider an adversarial debater that manipulates debate arguments while defending the correct monitored response, and ask whether the resulting degradation merely reflects catastrophic forgetting and whether standard evaluation can detect it. To address these questions, we propose ER-Audit, a two-stage black-box auditing framework that compares frozen verifier checkpoints before and after adaptation, and introduce two evaluation benchmarks pairing monitored and hidden task prompts grounded in shared contexts. ER-Audit searches for counterexamples to non-degradation by evaluating semantically valid paraphrases and, if none is found, uses independent paraphrases for sequential hypothesis testing. We derive anytime-valid lower confidence bounds on the non-degradation probability, allowing data-dependent stopping within a finite budget. We further establish a common lower bound across fixed paraphrase distributions and extend it to distributions within a bounded total variation distance of their mixtures. Our experiments show that higher hidden-task accuracy can coexist with more counterexamples to non-degradation and lower non-degradation bounds. This divergence challenges explanations based solely on broad catastrophic forgetting and shows that auditing can uncover selective hidden-task degradation concealed by aggregate performance gains. Our code and benchmarks are available at https://github.com/CSIRO-CQS-AI-alignment-Team/Epistemic-Reliability-Auditor.

## Metadata
- **Published**: 2026-09-26T08:33:34Z
- **Authors**: Derui Wang, Zewei Shi, Rayne Holland, Ruoxi Sun, Xingliang Yuan, Jason Xue, Liming Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32361v1)