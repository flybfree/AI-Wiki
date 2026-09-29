---
title: Despite Instructions: Frontier Agents Improvise Covert Channels at Test Time
published: 2026-09-26T15:06:44Z
authors: Jacob Dineen, Silei Ren, Muhao Chen, Dan Roth, Ben Zhou
url: http://arxiv.org/abs/2609.32701v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Despite Instructions: Frontier Agents Improvise Covert Channels at Test Time

## Abstract
In security-sensitive applications, language-model agents are often required to coordinate without disclosing confidential information. Yet repeated interactions may also let ordinary messages acquire shared private meaning. We study a repeated game with pairs of models in which the sender model observes one of four secret states and selects one of four summaries of the same public report, while the receiver model tries to infer the secret state. We find that model pairs can learn to communicate the secret using only one bit of feedback indicating whether the receiver inferred it correctly. This learning occurs during inference with fixed parameters and no supplied codebook or encoding examples. The effect also persists when agents generate their own free-form updates in a simulated incident-response task. Across ten independent games, pairs of GPT-5.6 Sol agents reach 98.8% final accuracy, compared with 25% chance, despite explicit instructions prohibiting disclosure and a monitor that screens each message without access to the agents' interaction histories. The same interactions that help agents cooperate can therefore allow confidential information to pass through messages intended for legitimate coordination.

## Metadata
- **Published**: 2026-09-26T15:06:44Z
- **Authors**: Jacob Dineen, Silei Ren, Muhao Chen, Dan Roth, Ben Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32701v1)