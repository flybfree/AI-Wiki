---
title: Build, Don't Play: Self-Improving LLM Research Agents Develop a Hearthstone Battlegrounds AI That Rivals Top Players
url: http://arxiv.org/abs/2610.33845v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-24_18-33-51Z_Build_Don_tPlay_Self_ImprovingLLMResearchAgentsDev.md
generated_at: 2026-10-26 20:31
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces AutoTavern, a self-improving research system in which specialized LLM agents collaboratively build a complete AI player for Hearthstone Battlegrounds, a complex eight-player auto-battler with stochastic mechanics and nearly a thousand interacting cards. Over 20 days, the agents constructed TavernGym (a faithful full-content game simulator) and 23 iterations of TavernAgent trained via PPO, ultimately producing an AI that outperforms the top ten rated human players on the live ladder. The central finding is that LLM agents are far more effective at building and engineering game-playing systems than at directly playing the game themselves.

## Key Takeaways
- AutoTavern employs a structured multi-agent research pipeline where specialized LLM agents share a typed research memory, every claim passes verification gates, and live game feedback closes the improvement loop. A human sets goals and rules only for ambiguous mechanics, while the agents autonomously improve the simulator, opponent models, policy, and their own research process. This architecture enabled the construction of TavernGym, the first faithful full-content reproduction of the live Hearthstone Battlegrounds game, within 20 days.
- TavernAgent, trained with PPO against opponents calibrated to real games, achieved a dramatic performance trajectory: its rating rose from 6,000 to approximately 15,000, and its last 20 public leaderboard records averaged a placement of 1.60 with 80% first-place finishes, surpassing the server's ten highest-rated players on every statistic (who averaged 2.34 placement and 59% first places). This demonstrates that an AI-built system can genuinely rival elite human play in a highly stochastic, hidden-information game.
- TavernBench, a 960-task evaluation across 40 scenarios, reveals a stark capability gap: TavernAgent answers 91% of play tasks while frontier LLMs achieve at most 63%. Crucially, TavernAgent decides in 0.03 seconds versus up to 26 seconds for LLMs, and within the one-second live turn window it retains 90% accuracy while no LLM exceeds 26%. This confirms that the engineered system vastly outperforms direct LLM reasoning for real-time game decisions.

## Context
This work sits at the intersection of LLM-based autonomous research agents, reinforcement learning, and complex game AI. Most prior work on LLM agents focuses on direct task execution or tool use, but AutoTavern reframes the agent's role as a builder and engineer of specialized systems rather than a direct problem-solver. Hearthstone Battlegrounds is a particularly demanding testbed due to its stochastic shop mechanics, hidden information, and combinatorial card interactions, making it a strong proxy for real-world decision-making under uncertainty. The paper contributes open-source benchmarks (TavernBench) and a faithful game simulator (TavernGym) that the broader AI community can use to evaluate both agent-built systems and direct LLM reasoning.

## Implications
For AI practitioners and researchers, the finding that "LLM agents build far better than they play" suggests a practical architectural principle: rather than prompting a large model to reason through complex sequential decisions in real time, it is more effective to have agents engineer a specialized policy and simulator, then deploy that engineered artifact. This has direct implications for industry applications involving real-time decision-making under uncertainty, such as logistics, trading, and game design, where latency and reliability constraints make direct LLM inference impractical. The open-sourcing of TavernBench and TavernGym also provides a reproducible benchmark for evaluating future autonomous research agents, potentially accelerating progress toward fully autonomous AI-driven system development.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.33845v1)
