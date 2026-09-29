---
title: Persistent Partners Raise Prices Among Learning Agents
published: 2026-09-28T15:24:23Z
authors: Paul-Peter Arslan, Yubin Kim, Xiao Xiao
url: http://arxiv.org/abs/2609.35402v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Persistent Partners Raise Prices Among Learning Agents

## Abstract
When pricing agents meet repeatedly on a platform, the platform decides who faces whom. We ask whether that choice moves the prices the agents learn, and whether a rise comes with learned punishment. In a pre-registered randomised experiment in the Bertrand duopoly of Calvano et al., each agent's price is set by a tabular Q-learning module, not by the small language model attached to it, and we randomise whether each agent keeps its partner, sees its rival's prices and can send messages. Keeping the same partner raises the level of profits, averaged over training, by 0.27 of the gap between competitive and monopoly profit (95% CI 0.20 to 0.35, all twenty paired runs positive), our registered primary result, and the resting price by 0.17 of the Nash-to-monopoly range (post hoc). A plain tabular learner reproduces the effect in all 25 further blocks, and there one permanent partner raises the level more than about three do (+0.23 against +0.05, exploratory). Where rival prices are hidden, the price-setting module cannot see a cut, so cannot punish it, yet the resting price rises as much and the rise lasts to the end of training, while with visible rivals it shrinks with longer training (post hoc). Where the rival is visible, a static best responder accounts for a third to a half of what a forced-deviation probe reads as punishment, on the starts where the rival can see the cut, and net of it the registered test of learned punishment is inconclusive. A test that looks only for punishment would thus miss the rise where the rival is hidden, while a check for profitable deviations flags most of those prices (post hoc). In an exploratory extension, untrained Qwen2.5 7B and 14B models under one prompt show the effect when the rival's price is left out of the prompt and inconsistently when it is shown, the 7B result replicating on fresh blocks, while two other model families show none.

## Metadata
- **Published**: 2026-09-28T15:24:23Z
- **Authors**: Paul-Peter Arslan, Yubin Kim, Xiao Xiao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.35402v1)