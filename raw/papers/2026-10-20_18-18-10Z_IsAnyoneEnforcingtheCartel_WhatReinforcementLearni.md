---
title: Is Anyone Enforcing the Cartel? What Reinforcement Learning Teaches LLM Agents in Markets
published: 2026-10-20T18:18:10Z
authors: Hieu Tran, Hong Yu
url: http://arxiv.org/abs/2610.28787v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Is Anyone Enforcing the Cartel? What Reinforcement Learning Teaches LLM Agents in Markets

## Abstract
Evaluations of large language model (LLM) agents report that pricing agents collude at others' expense. Yet collusion is defined by enforcement: a cartel, in which competitors share monopoly profits, holds only if a member who cheats is punished. We introduce an audit that tests enforcement by forcing a member to cheat in counterfactual copies of a market, and use it to study what reinforcement learning (RL) teaches agents in pricing and trading. Small LLMs trained by RL learn what their training rivals reward, but only what they readily try. In self-play, they learn fixed rules ignoring their rivals; against a punishing rival, to be deterred; against a cheating rival, to match its cuts, never the costly price war that would deter it, which they rarely try. A war forced into training is learned, but mostly only where it was forced. Against their own copies, deterred and matching agents can earn the same cartel profits, but only matching ones can enforce them, and then thinly: as a by-product and only against large cuts. Q-learners enforce collusion only in pricing. Prompted LLMs reach cartel-like outcomes mostly through rules that ignore the market. Outcome measures cannot tell these cases apart; the audit can.

## Metadata
- **Published**: 2026-10-20T18:18:10Z
- **Authors**: Hieu Tran, Hong Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.28787v1)