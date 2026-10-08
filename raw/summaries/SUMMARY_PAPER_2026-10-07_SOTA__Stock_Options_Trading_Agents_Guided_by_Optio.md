---
title: SOTA: Stock Options Trading Agents Guided by Option-Implied Return Distributions
url: http://arxiv.org/abs/2610.10407v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-07_16-55-05Z_SOTA_StockOptionsTradingAgentsGuidedbyOption_Impli.md
generated_at: 2026-10-07 22:10
model: qwen3.8-flash-next-iq3_xxs
---

## Summary

SOTA (Stock Options Trading Agents) is an agentic trading framework designed to address the complexity of options trading by abstracting the vast universe of option contracts into strategy-level decisions, with deterministic resolvers handling portfolio implementation. The framework is built by post-training Qwen3.8-27B through supervised fine-tuning followed by reinforcement learning, and it demonstrates strong out-of-sample performance with an 18.3% total return, a Sharpe ratio of 1.60, and a maximum drawdown of 8.96% over a six-month evaluation period on nine large-cap U.S. equities and SPY.

## Key Takeaways

- SOTA overcomes the combinatorial complexity of options trading by separating strategy selection from portfolio construction. Rather than restricting the agent to a fixed strategy structure like a straddle, the framework allows the language model to dynamically select among structured option strategies as market conditions change, while deterministic resolvers translate those strategy choices into concrete multi-leg portfolios across thousands of available contracts.

- The training pipeline combines supervised fine-tuning with reinforcement learning on Qwen3.8-27B, and the evaluation reveals a critical asymmetry in the role of news information. News improves the quality of frontier-teacher trajectories used during supervised fine-tuning, but retaining news signals during the reinforcement learning phase severely degrades out-of-sample performance, dropping returns from 18.3% to -2.7%. This suggests that news can introduce spurious correlations that the RL phase overfits to, undermining generalization.

- SOTA is benchmarked against rule-based and machine-learning strategy selectors within the same trading environment, providing a controlled comparison. The achieved Sharpe ratio of 1.60 and maximum drawdown of 8.96% indicate that the agentic approach can compete with or surpass traditional quantitative strategy-selection methods in a realistic options trading setting.

## Context

This paper sits at the intersection of large language model agents and quantitative finance, a rapidly growing research area as both option markets expand in size and complexity and agentic AI systems mature in their reasoning capabilities. Prior work on AI-driven trading has largely focused on equities or has constrained options strategies to rigid templates, leaving the full combinatorial decision space of options largely unexplored by language-model agents. SOTA represents one of the first attempts to let a post-trained LLM navigate the full strategy-selection problem in options trading without hard-coded structural assumptions.

## Implications

For practitioners and quantitative finance firms, SOTA demonstrates that language-model agents can serve as viable strategy selectors in options trading, potentially reducing the need for hand-crafted rule-based systems and enabling adaptive strategy switching across market regimes. The finding that news hurts RL-phase performance also carries a practical warning: incorporating rich contextual information during reinforcement learning can backfire, suggesting that careful information filtering is essential when training agentic trading systems. More broadly, the framework's separation of high-level strategy reasoning from low-level portfolio construction offers a reusable architectural pattern for other complex financial decision problems where the action space is combinatorially large.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.10407v1)
