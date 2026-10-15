---
title: What Makes a Social Agent's Interactions Effective? Learning from Verifiable Outcomes in Paired Worlds
url: http://arxiv.org/abs/2610.20195v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_13-44-30Z_WhatMakesaSocialAgent_sInteractionsEffective_Learn.md
generated_at: 2026-10-14 21:53
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces HICO-Bench, a benchmark of 180 everyday coordination scenarios designed to evaluate whether social agents actually produce plans that satisfy the private needs of all participants, rather than merely generating fluent-sounding conversations. The authors demonstrate that 36% of conversations rated highly by LLM judges for goal completion fail a programmatic verification of feasibility, and they propose Paired-Credit Policy Optimization (PaCPO), a training method that rewards agents for producing tentative plans that align with the correct private conditions in paired scenario variants, improving Qwen3-8B's Verified Success rate from 20.4% to 28.3%.

## Key Takeaways
- HICO-Bench evaluates social agents through a two-part verification: a programmatic check for Feasibility (the two agents' independently recorded plans must match each other and satisfy both participants' private constraints) and an LLM judge for Integrity (the conversation must genuinely support the recorded plan). Only passing both constitutes a Verified Success, exposing a critical gap between superficial conversational quality and actual coordination outcomes.
- Each scenario exists in two versions sharing identical public context but differing in one private condition, meaning the correct agreed-upon plan differs between them. This paired-world design forces agents to reason about hidden information rather than pattern-match on surface-level dialogue, and it enables the authors to show that 36% of conversations judged highly for goal completion actually fail to produce feasible plans.
- PaCPO addresses the challenge of learning from outcomes that only arrive at the end of a conversation by asking the agent to produce a tentative plan after each turn, checking that tentative plan against both paired versions of the scenario, and assigning credit to the specific turns after which the tentative plans fit their respective versions. This turn-level credit assignment raises Qwen3-8B's Verified Success from 20.4% to 28.3% across thirteen evaluated LLMs.

## Context
The evaluation of social and conversational agents has largely depended on LLM-as-judge scoring, which assesses fluency, helpfulness, and apparent goal completion without verifying whether the agent's output actually satisfies the concrete constraints of the participants. This paper sits at the intersection of multi-agent coordination, reinforcement learning from verifiable outcomes, and benchmark design, addressing a growing concern in the AI community that high judge scores do not guarantee functional correctness in tasks like scheduling, resource allocation, and authorization. By grounding evaluation in programmatic feasibility checks and introducing paired counterfactual scenarios, the work challenges the prevailing assumption that conversational quality metrics are sufficient proxies for social competence.

## Implications
For practitioners building multi-agent systems for real-world coordination tasks, this work signals that current LLM-based evaluation pipelines systematically overestimate agent reliability, and that training methods like PaCPO which exploit verifiable end-of-conversation outcomes can meaningfully improve plan correctness. For the broader AI safety and alignment community, the paired-world methodology offers a template for stress-testing agents against hidden private information and for designing RL objectives that reward genuine constraint satisfaction rather than persuasive dialogue, which is critical as social agents are increasingly deployed in domains such as logistics planning, healthcare scheduling, and collaborative decision-making where a fluent but infeasible plan can cause real harm.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.20195v1)
