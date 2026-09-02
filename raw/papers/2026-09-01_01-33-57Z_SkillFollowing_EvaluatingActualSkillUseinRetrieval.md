---
title: Skill Following: Evaluating Actual Skill Use in Retrieval-Enabled LLM Agents
published: 2026-09-01T01:33:57Z
authors: Seonghyeon Cho, Chanjun Park
url: http://arxiv.org/abs/2609.00549v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Skill Following: Evaluating Actual Skill Use in Retrieval-Enabled LLM Agents

## Abstract
Large Language Model (LLM) agents increasingly rely on external skills, yet standard evaluations obscure whether retrieving these skills actually helps. Aggregate metrics often compare retrieved versus non-retrieved tasks, introducing severe selection bias and failing to isolate the true effect of skill use. To measure this actual-use capability-which we formalize as Skill Following (SF)-we introduce the Retrieval-Invoked Actual-Use Effect (RAE). RAE computes the same-task outcome difference between matched skill-enabled and skill-disabled executions, conditioned exclusively on tasks where the agent actively retrieved a skill. Evaluating 17 LLMs across coding and mathematical domains, we uncover a stark evaluation paradox: models frequently show positive aggregate retrieval lift but negative RAE. On MBPP+, multiple models that appear to benefit system-wide actually harm their own performance on the exact tasks where retrieval occurred. These findings demonstrate that aggregate averages can create a misleading illusion of tool-use proficiency, whereas RAE directly measures whether the retrieval-to-answer pipeline genuinely rescues more outcomes than it harms.

## Metadata
- **Published**: 2026-09-01T01:33:57Z
- **Authors**: Seonghyeon Cho, Chanjun Park
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00549v1)