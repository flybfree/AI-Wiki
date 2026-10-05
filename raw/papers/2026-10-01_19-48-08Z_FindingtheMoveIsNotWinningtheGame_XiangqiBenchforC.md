---
title: Finding the Move Is Not Winning the Game: XiangqiBench for Closed-Loop Evaluation of LLM Agents
published: 2026-10-01T19:48:08Z
authors: Yekun Chai, Qiwei Peng, Haoyi Xiong
url: http://arxiv.org/abs/2610.02425v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Finding the Move Is Not Winning the Game: XiangqiBench for Closed-Loop Evaluation of LLM Agents

## Abstract
Static evaluations credit a language model for naming the right move, but an agent must carry a plan through to a verified outcome while an opponent responds. We introduce XiangqiBench, an executable benchmark that measures this difference in Chinese chess: starting from 119 tactical endgames with forced mates supported by engine or checks-only search, an LLM agent must deliver checkmate against an engine defender. An interactive REPL interface separates real moves, state queries, and forward simulation, and we record 8,568 multi-turn trajectories from 12 frontier LLMs under two observation protocols. Three signals that look like competence each overstate closed-loop success. (i) The Conversion Gap: models play the stored reference first move in 26.1\% of Sighted trials, yet only 13.9\% of these trials end in a win. (ii) The Consistency Gap: the leading model reaches 38.7\% pass@3 but only 5.9\% pass^3, winning all three trials on 7 of the 46 positions it ever wins. (iii) The Simulation Gap: 32.3\% of accepted simulation calls stop on an illegal move, and in 49.3\% of comparable cases the real defender replies differently from the line the agent simulated; self-authored rollouts check legality but cannot anticipate the opponent. Finding the move is not winning the game: agent evaluations should score closed-loop outcomes and report reliability alongside coverage.

## Metadata
- **Published**: 2026-10-01T19:48:08Z
- **Authors**: Yekun Chai, Qiwei Peng, Haoyi Xiong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.02425v1)