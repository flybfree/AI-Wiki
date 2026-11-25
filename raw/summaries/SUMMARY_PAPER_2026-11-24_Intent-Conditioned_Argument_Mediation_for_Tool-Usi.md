---
title: Intent-Conditioned Argument Mediation for Tool-Using LLM Agents: Blocking Trusted-but-Unauthorized Arguments
url: http://arxiv.org/abs/2611.30745v1
type: paper-summary
date: 2026-11-24
source_paper: 2026-11-23_14-22-21Z_Intent_ConditionedArgumentMediationforTool_UsingLL.md
generated_at: 2026-11-24 21:41
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper introduces IntentFlow, an intent-conditioned mediation layer placed between an unmodified LLM planner and its tools to stop tool calls whose authority-bearing arguments are trusted but were never authorized by the user. Existing argument-level provenance checks block values originating from untrusted content, yet they still permit a legitimate-looking value that the user did not request, so a call can reach the wrong recipient, endpoint, file, or participant. IntentFlow evaluates each authority-bearing argument against an intent contract and a provenance policy, and it substantially reduces attack success while preserving most benign behavior.

## Key Takeaways
- On a synthetic benchmark of 200 attacks with oracle intent and injection labels and declared roles, attack success drops from 50.5% under provenance-only mediation to 12.0% (95% interval 8.2-17.2%); every remaining success alters a content or payload field rather than an authority-bearing argument.
- IntentFlow wrongly blocks none of 200 paired benign tasks and only 4 of 50 hard benign tasks. On the 50 trusted-but-unauthorized attacks, provenance-only mediation executes all 50 while IntentFlow blocks all 50; a CaMeL-style check also blocks all 50 but rejects 16 of 50 benign tasks.
- On an offline AgentDojo-derived replay, IntentFlow blocks all 20 attacks at 75% benign success, matching a CaMeL-style check, whereas a Progent-style allowlist blocks 19 attacks while keeping all benign tasks. With one live planner and the same oracles, the mediator blocked all 17 corrupted calls proposed across 110 attacks.

## Context
Tool-using LLM agents increasingly convert natural-language requests and retrieved documents into actions such as sending messages, calling APIs, or touching files, which makes argument-level control a central safety problem. Provenance tracking is a useful first line of defense, but it is insufficient because it cannot distinguish a trusted value that is genuinely authorized from one that is trusted yet unauthorized by the user's intent. This paper argues that intent must be checked alongside provenance to close that gap without modifying the planner itself.

## Implications
For practitioners, IntentFlow suggests a deployable guardrail that can wrap an existing planner and tools without changing the model, reducing trusted-but-unauthorized execution while keeping false blocking low on paired benign tasks. The results also show a trade-off: CaMeL-style checks can be as strong on attacks but reject many benign tasks, while allowlist-style approaches preserve benign success but miss some attacks, so intent-conditioned mediation offers a middle path. The remaining failures, concentrated in content or payload fields, indicate that future work should extend intent contracts beyond authority-bearing arguments to the substance of arguments and to less oracle-dependent settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.30745v1)
