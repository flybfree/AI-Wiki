---
title: Transformers Struggle to Use Their Emergent World Models: Revisiting the Tower of Hanoi, and the Illusion of Thinking
published: 2026-08-07T10:29:19Z
authors: Devin Pereira, Willem Zuidema
url: http://arxiv.org/abs/2608.07077v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Transformers Struggle to Use Their Emergent World Models: Revisiting the Tower of Hanoi, and the Illusion of Thinking

## Abstract
The Tower of Hanoi is a simple planning puzzle that in prior work has proven challenging for large reasoning models (LRMs). Current models solve the standard formulation of the puzzle, but still struggle with the flat-to-flat variant (where initial and goal states are not restricted to have all rings on a single peg). This paper presents an in-depth study of how both small, in-house Transformers and large, third-party LRMs solve this task. To understand the failures mechanistically, we first train small Transformers from scratch on precomputed solution traces. Using a variety of interpretability techniques, we show that these Transformers develop an emergent world model: a linearly decodable, geometrically faithful representation of the puzzle's state space (the Sierpinski triangle), that is causally involved in solving the puzzles. Second, we return to the large LLMs and apply our techniques to two frontier reasoning models, Qwen3.6-27B and DeepSeek-R1-Distill-Qwen-32B, that attempt to solve the task through extended chain-of-thought. Surprisingly, we find that both models encode the Sierpinski world model near-perfectly at the end of the prompt, and yet fail at the majority of tasks when there are more than 3 rings. We locate the source of this failure in the decaying representation of the world model. We probe for the representation at different stages during planning, and establish causality by showing that performance can be improved by injecting the prompt-time representation at inference. The failure of the models is thus one of maintenance of the required representations, not their absence, and performance is at least partially recoverable. These results thus reframe the reported collapse in performance from prior work: current Large Reasoning Models build a world model, and then lose it.

## Metadata
- **Published**: 2026-08-07T10:29:19Z
- **Authors**: Devin Pereira, Willem Zuidema
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07077v1)