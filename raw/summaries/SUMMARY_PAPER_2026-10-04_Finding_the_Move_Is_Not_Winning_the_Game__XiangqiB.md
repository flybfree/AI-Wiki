---
title: Finding the Move Is Not Winning the Game: XiangqiBench for Closed-Loop Evaluation of LLM Agents
url: http://arxiv.org/abs/2610.02425v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-01_19-48-08Z_FindingtheMoveIsNotWinningtheGame_XiangqiBenchforC.md
generated_at: 2026-10-04 21:57
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces XiangqiBench, an executable benchmark designed to evaluate whether LLM agents can carry a chess plan through to a verified outcome in Chinese chess (Xiangqi), rather than merely naming a correct first move. Starting from 119 tactical endgames with forced mates, the benchmark requires agents to deliver checkmate against an engine defender across multi-turn interactions, revealing that static move-identification accuracy dramatically overstates an agent's true closed-loop problem-solving capability.

## Key Takeaways
- The Conversion Gap demonstrates that while models correctly play the stored reference first move in 26.1% of Sighted trials, only 13.9% of those trials ultimately end in a win, showing that identifying a good opening move does not translate into successfully executing a full winning strategy against an adaptive opponent.
- The Consistency Gap reveals that even the leading model achieves 38.7% pass@3 but only 5.9% pass^3, meaning it wins all three independent trials on just 7 of the 46 positions it ever wins, highlighting severe unreliability in repeated closed-loop execution.
- The Simulation Gap shows that 32.3% of accepted simulation calls terminate on an illegal move, and in 49.3% of comparable cases the real engine defender replies differently from the line the agent simulated, proving that self-authored rollouts cannot reliably anticipate an opponent's responses and thus fail as planning tools.

## Context
This work addresses a critical blind spot in current LLM evaluation methodologies, which predominantly rely on static, single-step benchmarks that reward pattern-matching rather than sustained strategic reasoning. As the AI community increasingly deploys LLM agents in interactive, adversarial, and multi-step environments such as game playing, planning, and tool use, the gap between superficial competence and genuine closed-loop reliability becomes a central concern for benchmark design and model development.

## Implications
For practitioners and benchmark designers, this paper argues that agent evaluations must score closed-loop outcomes and report reliability metrics alongside coverage metrics, rather than crediting models for isolated correct moves. For the broader AI industry, the findings caution against overestimating the planning and adversarial reasoning capabilities of frontier LLMs, suggesting that current models struggle with maintaining coherent strategies under opponent adaptation and that simulation-based self-planning remains fundamentally unreliable for anticipating dynamic interactions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02425v1)
