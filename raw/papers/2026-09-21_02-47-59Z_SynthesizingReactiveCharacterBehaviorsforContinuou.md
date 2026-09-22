---
title: Synthesizing Reactive Character Behaviors for Continuous Games via Programmatic Policy Search
published: 2026-09-21T02:47:59Z
authors: Maxim Gumin, Hsueh-Ti Derek Liu, Victor Zordan, Daniel Ritchie
url: http://arxiv.org/abs/2609.24025v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Synthesizing Reactive Character Behaviors for Continuous Games via Programmatic Policy Search

## Abstract
We present a method for synthesizing reactive character behaviors for continuous games as compact, human-readable programs. Game AI practice still relies heavily on manually authored behavior trees, state machines, and scripts, while academic reinforcement learning typically produces opaque neural controllers that are expensive to train and difficult to edit. Our approach bridges this gap by searching directly over a domain-specific language for continuous-space game policies. The language is designed around reactive geometric decisions and includes higher-order constructs such as direction maximization. These constructs help discretize a continuous behavior space into enumerable program structures. To make program search practical, we introduce a large set of synthesis antipatterns that remove redundant program forms while preserving behavioral coverage. We further combine bottom-up symbolic enumeration with top-down guidance from a coding agent. Our resulting method, agentic sketching, has the agent propose high-level policy structure and call an enumerator to complete local program slots. We evaluate the method on a benchmark of 14 continuous games, ranging from classic control tasks to multi-agent football. We find that pure enumeration is often more efficient than using a coding agent alone, while the combined method substantially outperforms both. Our results suggest that programmatic policy search can be a practical authoring tool for game AI: designers specify reward functions, and the system discovers editable behaviors that are effective, portable, and often surprising.

## Metadata
- **Published**: 2026-09-21T02:47:59Z
- **Authors**: Maxim Gumin, Hsueh-Ti Derek Liu, Victor Zordan, Daniel Ritchie
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.24025v1)