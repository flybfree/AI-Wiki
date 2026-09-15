---
title: When Tools Get in the Way: The Effect of Unnecessary Tool Availability on LLM Answering
published: 2026-09-12T21:15:58Z
authors: Saanvi Paturi, Arsen Kenzhebayev, Arham Sethi, Vyas Raina, Ivaxi Sheth, Vatsal Raina
url: http://arxiv.org/abs/2609.14157v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Tools Get in the Way: The Effect of Unnecessary Tool Availability on LLM Answering

## Abstract
Large language models (LLMs) are increasingly deployed with external tools that extend what they can do beyond their own knowledge. Tools help on tasks that need external information, but their availability may also change how a model handles questions that do not need them. Prior work has mostly asked whether models select and use tools appropriately; whether an unnecessary tool changes the correctness of answers has received less attention. We ask whether making a related but unnecessary tool available affects a model's ability to answer from its own knowledge, and whether a preceding tool interaction changes this behaviour. We construct 500 query pairs across 10 knowledge domains. Each pair consists of a tool query, which needs the domain's tool, and a closed-domain query, which does not. Six LLMs are evaluated with the tool unavailable, available, and available after a prior tool call. Across 3,000 baseline trials the pooled answer rate is 98.2%. When an unnecessary tool is available it falls to 63.5%, with large differences between models. The decrease occurs even when the tool is rarely called, so it cannot be explained by unnecessary tool invocation alone. A one-sentence scope-aware system instruction recovers most of the lost answers.

## Metadata
- **Published**: 2026-09-12T21:15:58Z
- **Authors**: Saanvi Paturi, Arsen Kenzhebayev, Arham Sethi, Vyas Raina, Ivaxi Sheth, Vatsal Raina
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.14157v1)