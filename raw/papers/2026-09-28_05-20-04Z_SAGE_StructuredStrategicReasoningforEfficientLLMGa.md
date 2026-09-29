---
title: SAGE: Structured Strategic Reasoning for Efficient LLM Game Playing
published: 2026-09-28T05:20:04Z
authors: Zhiwei Chen, Tianchun Wang, Zhongtao Rao, Haiming Zhu, Ding Cao, Tianxiang Zhao
url: http://arxiv.org/abs/2609.34342v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SAGE: Structured Strategic Reasoning for Efficient LLM Game Playing

## Abstract
A strong LLM strategic agent should reason prospectively over uncertain futures, adapt its strategy to opponents' behavioral tendencies, and continuously recalibrate its decision process from interaction experience. However, incorporating these sources in free-form reasoning could lead to unsupported strategic assumptions, inconsistent opponent estimates, and harmful interference from irrelevant historical interactions. To address these issues, we propose SAGE, a training-free inference-time framework that structures LLM strategic reasoning around three coordinated operations: anchor, adapt, and recalibrate. SAGE first anchors reasoning to an equilibrium policy that provides a strategically valid prior. It then conditions deviations from this anchor on a soft belief over opponent behavioral tendencies, enabling opponent-specific exploitation. Finally, SAGE distills strategically related interactions into counterfactual hypotheses about previously missing considerations, allowing past experience to recalibrate the model's reasoning. We evaluate SAGE on three repeated imperfect-information games: Leduc Hold'em, Liar's Dice, and Goofspiel, against various opponent types in each game. Compared with reasoning-intensive LLM agents, including Suspicion-Agent, ReTA, Agent-Pro, EMO, and Hypothetical Minds, SAGE achieves up to a 127.6% payoff improvement in Liar's Dice while reducing input and output token usage by up to 80% and 90%, respectively. In direct match-up play, it attains non-negative mean payoff against 5/10, 8/10, and 8/10 evaluated opponents in Leduc Hold'em, Liar's Dice, and Goofspiel, respectively, while using relatively fewer tokens. Code is available at https://github.com/chenzhwsysu57/SAGE.

## Metadata
- **Published**: 2026-09-28T05:20:04Z
- **Authors**: Zhiwei Chen, Tianchun Wang, Zhongtao Rao, Haiming Zhu, Ding Cao, Tianxiang Zhao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34342v1)