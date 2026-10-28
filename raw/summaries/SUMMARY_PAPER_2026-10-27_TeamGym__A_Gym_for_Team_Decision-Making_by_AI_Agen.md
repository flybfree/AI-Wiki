---
title: TeamGym: A Gym for Team Decision-Making by AI Agents with Distributed Information
url: http://arxiv.org/abs/2610.37571v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-27_17-15-54Z_TeamGym_AGymforTeamDecision_MakingbyAIAgentswithDi.md
generated_at: 2026-10-27 21:59
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
TeamGym is a novel evaluation and training environment designed to assess how language model-based AI agents perform in team decision-making tasks where critical information is distributed across multiple participants. The paper introduces the concept of "pivotal information"—a minimal set of facts that is individually necessary and collectively sufficient for a correct decision—and uses it to quantify two distinct failure modes in current AI agents: a communication gap (22.9 percentage point drop when information is distributed) and a retrieval gap (19.9 additional points lost when agents must extract information from source material). The authors also demonstrate that reinforcement learning on team decision loss can improve agent coordination and decision quality even when rewards only evaluate final outcomes.

## Key Takeaways
- TeamGym constructs team decision-making problems from real-world legal, finance, medical, and software engineering corpora, and introduces a rigorous method for identifying "pivotal information"—the minimal set of facts where each element is necessary and all are collectively sufficient for a correct final decision. This allows precise control over how critical information is distributed among agents and enables fine-grained tracking of whether agents successfully identify and integrate that information.
- Testing 8 language models across 12 source corpora reveals two compounding failure modes: a communication gap where distributing pivotal information across participants reduces success rates by 22.9 percentage points compared to giving all information to a single model, and a retrieval gap where requiring participants to identify and extract pivotal information from source documents lowers success by an additional 19.9 points. These findings show that current AI agents are fundamentally poor at both sharing information with teammates and independently locating decision-relevant facts.
- Reinforcement learning training on team decision loss produces measurable improvements in final-decision quality and induces emergent coordination behaviors—including improved participation patterns, speaker selection, and communication strategies—despite the reward signal evaluating only the final decision outcome, suggesting that team-level training objectives can shape intermediate collaborative behavior without explicit coordination supervision.

## Context
This paper addresses a critical blind spot in AI evaluation: while language models are increasingly deployed in multi-agent and collaborative settings, benchmarks and training pipelines overwhelmingly treat agents as isolated decision-makers. TeamGym bridges this gap by grounding team decision-making in authentic professional corpora and formalizing the information-distribution problem through the pivotal information framework, providing a principled way to measure collaboration failures that prior benchmarks like GAIA or SWE-bench do not capture.

## Implications
For practitioners deploying AI agents in legal review, financial analysis, medical diagnosis, or software engineering teams, the 22.9-point communication gap and 19.9-point retrieval gap represent substantial accuracy losses that current single-agent optimization strategies cannot address. The paper's demonstration that RL training on team-level objectives can induce emergent coordination without explicit communication rewards offers a practical pathway for improving multi-agent systems in production, suggesting that organizations investing in agentic workflows should prioritize team-aware training and evaluation rather than relying solely on individual model performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.37571v1)
