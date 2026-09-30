---
title: LLMs Learn to Evade Latent Monitors from Prior Feedback Alone
published: 2026-09-29T01:47:13Z
authors: Hugo Lyons Keenan, Christopher Leckie, Sarah Erfani
url: http://arxiv.org/abs/2609.36490v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLMs Learn to Evade Latent Monitors from Prior Feedback Alone

## Abstract
Latent space monitors aim to detect undesired behaviors in LLM agents by inspecting an agent's internal activations rather than its outputs. However, interactive monitoring creates a feedback channel where each verdict the monitor delivers leaks information to the model about how its internal states are being evaluated. We ask whether an agent can infer the monitor's decision rule from this feedback and then selectively edit its activations to evade detection. Unlike prior evasion attacks, the model is never explicitly told what the monitor detects. Surprisingly, off-the-shelf models already produce activation edits aligned with the monitored direction, but at insufficient magnitude for evasion. Simply scaling up these edits by a factor of 8 reduces the monitor's TPR from 100% to 27%. A rank-1 LoRA amplifies this behavior into effective evasion within the forward pass, reducing TPR further to 4% on held-out concept monitors while leaving other concepts at their normal detection rates. Capabilities on standard benchmarks are retained under this finetuning, and the evasion skill survives retraining the monitors on the new activations. Mechanistically, we find evidence that the model computes its activation edit from the prior in-context turns, and show that the edit becomes more aligned with the monitored direction as more examples are provided. These results demonstrate feedback-conditioned control over activations and suggest that latent monitoring should be treated as an interactive process in which agents can observe and respond to oversight measures.

## Metadata
- **Published**: 2026-09-29T01:47:13Z
- **Authors**: Hugo Lyons Keenan, Christopher Leckie, Sarah Erfani
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.36490v1)