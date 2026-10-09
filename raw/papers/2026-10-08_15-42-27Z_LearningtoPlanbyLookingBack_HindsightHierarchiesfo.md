---
title: Learning to Plan by Looking Back: Hindsight Hierarchies for Training Reasoning Models
published: 2026-10-08T15:42:27Z
authors: Lars Simon, Holger Eble, Manuel Radons
url: http://arxiv.org/abs/2610.12168v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning to Plan by Looking Back: Hindsight Hierarchies for Training Reasoning Models

## Abstract
We introduce a self-improvement loop for reasoning models based on the following observation: Even when the difficulty of a problem exceeds the model's current solving abilities, an additionally supplied solution might enable the model to extract useful solution ideas in hindsight. We operationalize this by jointly training the same model to exhibit the following three capabilities: predicting solution ideas from problems alone, reverse-engineering ideas from problems and known solutions, and solving problems using provided ideas. The loop alternates between reverse engineering such ideas from problems with supplied solutions and using these ideas as additional supervision for joint training of all three capabilities. We give a formal specification of our method and a concrete instantiation for interactive theorem proving in the Lean theorem prover; empirical evaluation remains future work.

## Metadata
- **Published**: 2026-10-08T15:42:27Z
- **Authors**: Lars Simon, Holger Eble, Manuel Radons
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.12168v1)