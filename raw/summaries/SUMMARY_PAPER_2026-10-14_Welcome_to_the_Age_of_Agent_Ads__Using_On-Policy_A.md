---
title: Welcome to the Age of Agent Ads: Using On-Policy Attacks to Steer Agentic Decisions
url: http://arxiv.org/abs/2610.17195v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_17-57-12Z_WelcometotheAgeofAgentAds_UsingOn_PolicyAttackstoS.md
generated_at: 2026-10-14 00:42
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces a novel class of adversarial attacks called "on-policy attacks" that steer AI agent decisions without triggering off-policy behaviors that alignment training is designed to catch. The authors demonstrate a two-step attack involving a truthful negation about a fictitious concept injected into a product listing, which triggers a web search that surfaces fabricated harmful associations, causing the agent to penalize competitors. Evaluating across four real-world listing datasets, the authors find that some frontier models are vulnerable to this attack, enabling adversarial actors to disadvantage competitors while remaining compliant with existing platform guidelines.

## Key Takeaways
- On-policy attacks represent a new attack surface distinct from existing off-policy steering methods: they steer agentic decisions by operating entirely within the model's aligned behavioral distribution, making them harder to detect and defend against through standard alignment training or platform terms of service.
- The demonstrated attack works in two stages: first, a truthful negation about a fictitious concept (e.g., "Does not contain blizyester") is injected into a product description, which triggers the agent to search the web for that concept; second, planted websites surface fabricated information associating the fictitious concept with harmful implications (e.g., "Blizyester linked to dementia"), causing the agent to penalize every option that lacks the truthful negation.
- The attack exploits the agent's trained safety behavior—keeping users safe from harm—as a lever for adversarial steering, meaning the very alignment mechanisms meant to protect users become the vector through which manipulation occurs. The authors evaluate this across four real-world listing datasets and confirm that some frontier models are exposed to this vulnerability.

## Context
As consumers increasingly delegate option-ranking tasks such as shopping, job searching, and travel planning to AI agents, a new advertising ecosystem emerges where advertisers target the agent rather than the human directly. Existing defenses against agent manipulation rely on alignment training and platform terms of service, which are primarily designed to catch off-policy behaviors. This paper matters because it reveals that the most natural and effective defense mechanisms are insufficient against attacks that operate entirely within the policy distribution, exposing a regulatory and technical gap in how we protect users from agent-level advertising manipulation.

## Implications
For model developers, this work signals that alignment training alone is not a sufficient defense against adversarial steering, and that safety-oriented behaviors like harm avoidance can be exploited as attack vectors. For platform providers and regulators, the findings underscore the urgent need to develop new advertising guidelines specifically designed for agent-mediated decision-making, since current platform-listing guidelines do not prevent adversarial actors from penalizing competitors through on-policy manipulation. Practitioners building agentic systems should consider whether their agents' web-search and safety-checking behaviors create exploitable surfaces for adversarial manipulation in commercial ranking tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.17195v1)
