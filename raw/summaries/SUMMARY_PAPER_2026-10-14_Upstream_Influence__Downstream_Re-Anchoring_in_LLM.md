---
title: Upstream Influence, Downstream Re-Anchoring in LLM Agent Chains
url: http://arxiv.org/abs/2610.17723v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_04-57-25Z_UpstreamInfluence_DownstreamRe_AnchoringinLLMAgent.md
generated_at: 2026-10-14 00:26
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how coordinated manipulation propagates through multi-agent LLM chains, demonstrating that a workflow's information architecture—specifically source access, handoff format, and which model directly reads untrusted content—determines how much of an injected stance reaches the final decision-maker. Through experiments on 32 Taiwan 2025 recall cases using authentic social media comments, the authors show that downstream agents engage in "partial re-anchoring," discounting inherited stances proportionally to how far those stances deviate from their own independent reading of the evidence, rather than simply attenuating or reverting to neutrality.

## Key Takeaways
- A single agent exposed to ten authentic Threads comments shifts its stance by +0.171 toward the injected position, but passing that judgment down a chain removes more than half of the shift by the third agent. However, keeping the original comments visible to every agent in the chain sustains significantly more of the manipulation, showing that direct source access is a critical architectural lever for controlling downstream influence.
- The reduction in propagated influence is not simple attrition in transit but reflects "partial re-anchoring": each receiving agent discounts the inherited stance in proportion to how far it sits from its own independent reading of the evidence, returning to what that evidence implies for the specific case rather than defaulting to neutrality. Additionally, handoff format is a second critical lever—when a stance is relayed without its supporting reasoning, downstream agents largely discount it.
- Susceptibility at the exposed seat varies fourfold across different models, yet the chain's arrangement (order, structure) does not matter at all. Critically, the manipulation is invisible in reasoning transcripts because injected claims are almost never restated, meaning standard reasoning-trace audits would completely miss the attack vector.

## Context
As LLM agents increasingly serve as intermediaries in evaluative workflows—summarizing news, filtering social media, and producing judgments that humans then act upon—multi-agent pipelines are becoming standard infrastructure in content moderation, news aggregation, and public discourse analysis. This paper addresses a gap in the literature by shifting focus from single-model robustness to the information architecture of agent chains, revealing that the propagation dynamics of manipulation are governed more by access control and handoff design than by model arrangement or chain topology.

## Implications
For practitioners deploying multi-agent LLM systems in journalism, policy analysis, or content moderation, the findings suggest that architectural choices—such as whether downstream agents receive raw source material or only summarized stances, and whether reasoning is included in handoffs—are more consequential than model selection or chain ordering for preserving evaluative integrity. The invisibility of manipulation in reasoning traces also warns that current auditing practices based on transcript inspection are insufficient, and that system designers must treat information access patterns as a first-class security and fairness concern rather than an afterthought.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.17723v1)
