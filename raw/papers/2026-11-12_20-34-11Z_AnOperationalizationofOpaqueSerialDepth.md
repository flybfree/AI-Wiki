---
title: An Operationalization of Opaque Serial Depth
published: 2026-11-12T20:34:11Z
authors: Nathan Sheffield, Alek Westover, Lukas Finnveden, Alexa Pan, Julian Stastny, Ryan Greenblatt
url: http://arxiv.org/abs/2611.17495v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# An Operationalization of Opaque Serial Depth

## Abstract
Chain-of-thought (CoT) is currently a valuable tool for overseeing AI models, but some architectural shifts could significantly reduce CoT monitorability. We operationalize a measure that serves as a proxy for the amount of unverbalized serial cognition a model can perform, as a specific instantiation of the notion of opaque serial depth: roughly, the length of the longest path through a model's computation that does not pass through an interpretable bottleneck. Our main contribution is a particular standard for what counts as such a bottleneck. We define natural-language-rooted (NL-rooted) nodes as nodes that were initialized from a pre-training prior to produce human-understandable outputs, whose output space has not been expanded beyond that prior, and whose outputs the model has not been modified to interpret as a different type of data. By construction, the resulting measure, NLS depth, can be adjudicated before training from an architecture, training recipe, and deployment configuration alone, and is insensitive to ordinary post-training such as prompting, distillation, and RL. We find that, across open-weight models, NLS depth correlates strongly with layer count, with some exceptions, and has grown slowly over recent years. It would likely grow slowly under continued scaling of standard transformers, while latent-reasoning architectures such as full-bandwidth transformers could increase it by a large amount. We work through how NLS depth applies to a range of existing and proposed architectures, discuss alternative operationalizations, and give a worked example bounding the depth of Gemma3-1B. We argue that AI developers should track and report the NLS depth of their models as a complement to direct measurements of CoT monitorability.

## Metadata
- **Published**: 2026-11-12T20:34:11Z
- **Authors**: Nathan Sheffield, Alek Westover, Lukas Finnveden, Alexa Pan, Julian Stastny, Ryan Greenblatt
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.17495v1)