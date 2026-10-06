---
title: Asking Earns Nothing: Scoring the Decision to Act in BFCL Multi-Turn
published: 2026-10-03T10:42:45Z
authors: Yangze Liu, Zhongyi Han
url: http://arxiv.org/abs/2610.04429v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Asking Earns Nothing: Scoring the Decision to Act in BFCL Multi-Turn

## Abstract
An agent that lacks the information it needs should ask rather than act, and the task definitions of agent leaderboards say so. BFCL multi-turn builds two of its four categories around a turn on which the model is supposed to ask, and its scorer never looks at that turn: the gold trajectory there is empty, the checker skips it, and the scripted user cannot answer, so asking earns nothing, guessing costs nothing on that turn, and asking twice loses the item. The benchmark also contains the control experiment for that decision. A should-ask item is a base item with one piece of information removed from one turn, so the same request appears twice at the same turn index, once complete and once not: on the first the model should make the call that changes the world, on the second it should ask. We score one decision per pair, whether the model attempted a world-changing call on that turn, read off the stored trajectories with no LLM judge; acting always and asking always both score 50. On the 223 pairs that pose this decision, gpt-5.4 attempts the call on 83.4% of the complete turns and holds back on 78.0% of the incomplete ones, the best decision accuracy of seven models at 80.7%; on the same items the official score ranks it sixth and puts first a model that lands in the middle here. One added line telling gpt-5.4 not to ask pushes it toward acting on both sides of the pair, so its decision accuracy shows no detectable change, while its official score rises by 13.5 to 23.5 points on the two should-ask categories and on the base twins; the opposite line, telling gemma-4-31B-it to ask first, improves its decision by 4.5 points and gains no official score. The score moves with the push toward action, not with the decision. We release the pairs, a turn-level scorer that runs on any BFCL output directory without an API key, and 31 manually verified bad items.

## Metadata
- **Published**: 2026-10-03T10:42:45Z
- **Authors**: Yangze Liu, Zhongyi Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04429v1)