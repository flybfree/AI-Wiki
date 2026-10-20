---
title: Fake News, Real Crashes: Information Injection Attacks on LLM Financial Trading Agents
url: http://arxiv.org/abs/2610.26438v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-19_13-58-50Z_FakeNews_RealCrashes_InformationInjectionAttackson.md
generated_at: 2026-10-20 00:05
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces a systematic benchmark for "information injection" attacks targeting LLM-based financial trading agents, distinguishing this threat from traditional prompt injection by focusing on the evidence agents trust rather than their instructions. The authors evaluate approximately 10,000 trading decisions across 15 U.S. stocks using five injection vectors and seven event categories, revealing that fabricated news achieves a 62% attack success rate—far exceeding the 14% success rate of conventional prompt injection—and that carefully crafted 30-word templates can achieve 100% success across all tested stocks.

## Key Takeaways
- Fabricated news dramatically outperforms prompt injection in attack success: while prompt injection achieves only a 14% ASR, fabricated news reaches 62%, and two specific 30-word templates achieve 100% ASR across all 15 stocks, inverting the common assumption that prompt injection is the dominant threat to LLM security. This suggests that the evidence pipeline, not the instruction pipeline, is the more vulnerable attack surface for trading agents.
- Surface form and credibility cues matter more than factual content for fact-poisoning attacks: removing a named source or a "BREAKING" tag from a fabricated headline drops the ASR from 100% to 0%, even though the underlying fake claim remains completely unchanged. This reveals that LLM trading agents are heavily influenced by formatting and authority signals rather than by evaluating the truthfulness of the information itself.
- Attack success is highly dependent on the agent's internal state: a fake indicator panel scores 91% ASR against an agent about to hold but only 12% against one about to buy, indicating that adversarial effectiveness is not uniform but interacts with the agent's current decision trajectory. Furthermore, attacks generalize across model vendors, remain effective when blended unlabeled into real news feeds, and evade most standard defenses including model scaling and peer debate, with only hierarchical aggregation providing meaningful mitigation.

## Context
As LLM agents increasingly manage real capital in financial markets, their reliance on external news feeds as decision evidence creates a novel and underexplored attack surface that differs fundamentally from prompt injection studied in model-security literature. This paper matters because it shifts the adversarial focus from manipulating instructions to manipulating the trusted evidence pipeline, a threat model that is directly relevant to any autonomous agent operating in information-rich environments. The finding that surface credibility cues dominate over content evaluation exposes a critical blind spot in how current LLM architectures process and trust external information.

## Implications
For the financial industry, these results suggest that a single fabricated headline injected into a shared news feed can synchronize multiple LLM trading agents into identical trades at the same moment, creating systemic risk and potential flash-crash cascades that traditional risk-management frameworks do not account for. Practitioners deploying LLM trading agents should prioritize evidence-integrity controls such as hierarchical aggregation and source verification rather than relying on model scaling or peer debate as defenses. The finding that credibility formatting alone can flip an attack from 100% to 0% success also implies that adversarial robustness in agentic systems requires attention to presentation-layer defenses, not just content-level filtering.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.26438v1)
