---
title: Absorbed in Inertia: Activation Analysis for Computer-Use Agents
published: 2026-09-29T10:01:52Z
authors: Giulio Segalini, Zhi Wen Soi, Jérémie Decouchant, Lydia Chen
url: http://arxiv.org/abs/2609.37176v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Absorbed in Inertia: Activation Analysis for Computer-Use Agents

## Abstract
Computer-use agents have become increasingly capable of executing tasks on live desktops through natural-language instructions, based on trajectories of screenshots, actions, and reasoning. We discover that they can stealthily exhibit inertia, in which they repeat fruitless actions despite recognizing that these actions are ineffective. We hypothesize that inertia is reflected in the agent's internal state, i.e., the activation values of the agent's underlying model, and propose a protocol to measure the relationship between the two. Extensive analysis of high-dimensional activation states shows that inertia corresponds to an absorbing region of activation space, where activation values become stale across actions and even after attempts to steer them. We conjecture that drastically changing the agents' activations by re-initializing them is necessary to escape inertia. Specifically, we propose R$^3$ (Reset, Reroute, Restore), which temporarily resets the agent's context trajectory to escape the absorbing region and then restores the historical context to effectively complete the task. Our approach yields 17-55% lower measured inertia across models relative to unmodified agents. These results suggest that changing the context can interrupt recurrence more effectively than directly steering the resulting activations. Our code is available at https://anonymous.4open.science/r/vlm-agent-defense-D076

## Metadata
- **Published**: 2026-09-29T10:01:52Z
- **Authors**: Giulio Segalini, Zhi Wen Soi, Jérémie Decouchant, Lydia Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.37176v1)