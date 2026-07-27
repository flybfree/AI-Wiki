---
title: Learning on the Job: Continual Learning from Deployment Feedback for Frozen-Weights Agents
published: 2026-07-24T10:01:00Z
authors: Valentin Tablan, Scott Taylor, Kristoffer Bernhem
url: http://arxiv.org/abs/2607.22157v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning on the Job: Continual Learning from Deployment Feedback for Frozen-Weights Agents

## Abstract
AI agents encounter learning opportunities in every episode they run, and discard nearly all of them: the underlying models are frozen at deployment, so an agent that resolves a difficult request today starts from zero when it recurs tomorrow. Yet ordinary operation already produces feedback, in the form of outcome verdicts and after-the-fact corrections. We show that this feedback is a sufficient signal for continual learning when the frozen model is paired with an external memory that distils each episode into retrievable natural-language rules. On the banking domain of $τ$-bench, against a static-RAG control retrieving over the complete policy corpus, learning from the one-bit outcome verdict lifts single-trial success to 1.6$\times$ the baseline, and learning from corrections to 2.6$\times$, converting 22 of the 84 tasks the baseline never solves. The result spans the deployment spectrum, measured on Mistral Large, an open-weights model that organisations with data sovereignty requirements can self-host, and replicated on a frontier model, Claude Sonnet 5. The accumulated memory also transfers: each model, reading the store built by the other, rises above its own no-memory baseline. The harness, protocol, and data are released.

## Metadata
- **Published**: 2026-07-24T10:01:00Z
- **Authors**: Valentin Tablan, Scott Taylor, Kristoffer Bernhem
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22157v1)