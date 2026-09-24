---
title: Exact Feedback Is Not Control: Evaluating Text-based Closed-Loop Revision in LLMs
published: 2026-09-23T14:06:52Z
authors: Haitong Jiang, Chunlin Liu, Yile Wang, Yuhong Feng
url: http://arxiv.org/abs/2609.28150v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Exact Feedback Is Not Control: Evaluating Text-based Closed-Loop Revision in LLMs

## Abstract
Closed-loop revision is increasingly used in large language model (LLM) applications, but failures may reflect incomplete feedback or ineffective responses to correct feedback. We introduce a fixed-budget revision protocol with deterministic verifiers that report all remaining violations across exact-length, lexical, and compositional constraints. Fixing feedback correctness and completeness isolates model-side revision behavior. Across 19 open- and closed-source models, controller-level mean final joint success ranges from 17.4% to 99.8%, with substantial cross-model gaps persisting under identical initial drafts. Controlled experiments reveal reproducible model-specific responses to exact feedback. Post-training and scale reshape these responses without consistently bringing them closer to exact correction. Across all constraint families, failed trajectories often repeat earlier outputs, and prior recurrence is associated with lower subsequent recoverability. Matched-state interventions show that removing earlier dialogue while holding the current draft and feedback fixed changes recurrence escape without reliably improving final success; effects depend on the model, task, and trigger-state composition. Exact feedback makes revision errors observable, but does not make the closed loop reliable. Code and reproduction instructions: https://github.com/kevinjiang0121-cyber/exact-feedback-code.

## Metadata
- **Published**: 2026-09-23T14:06:52Z
- **Authors**: Haitong Jiang, Chunlin Liu, Yile Wang, Yuhong Feng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.28150v1)