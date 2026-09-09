---
title: Your Agent Says Yes: Interpreting Adversarial Market Behavior Beyond Individual Transactions
published: 2026-09-07T16:01:58Z
authors: Zelin Li, Yiyun Su, Matt White, Zhipeng Wang, Xiao-Yang Liu, Tianyu Shi
url: http://arxiv.org/abs/2609.07675v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Your Agent Says Yes: Interpreting Adversarial Market Behavior Beyond Individual Transactions

## Abstract
Transaction-local controls answer whether one financial request may proceed, but market behavior can be distributed across messages, agents, assets, and time. We study this interpretation gap in a virtual exchange populated by ten role-conditioned language-model agents. The agents communicate, trade reference assets and futures, launch tokens, and manage concentrated-liquidity pools under prescriptive adversarial roles. We analyze eight 72-cycle trajectories across two time-blinded hourly replay paths, with a runner-side wallet policy enabled or disabled. The retained artifacts connect generated outgoing messages, policy events, balances, positions, and cycle-end market state. A focal reconstruction shows a launch--promotion--exit scenario realized across private coordination, public claims, follower positioning, repeatedly withheld exits, and a later non-blocking request aligned with a token balance change. Across policy-enabled runs, the gate withholds direct requests selectively; most policy-categorized candidates are flagged rather than blocked, while the surrounding interaction can continue. Repeated runs also show that category-level and within-trajectory relations can recur even when normalized score-change rankings do not. These findings motivate agent-behavior evaluation that links communication, authorization, and evolving state instead of treating individual transaction verdicts as complete safety judgments.

## Metadata
- **Published**: 2026-09-07T16:01:58Z
- **Authors**: Zelin Li, Yiyun Su, Matt White, Zhipeng Wang, Xiao-Yang Liu, Tianyu Shi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.07675v1)