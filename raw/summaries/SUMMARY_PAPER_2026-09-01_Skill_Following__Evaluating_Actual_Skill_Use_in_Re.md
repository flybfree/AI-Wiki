---
title: Skill Following: Evaluating Actual Skill Use in Retrieval-Enabled LLM Agents
url: http://arxiv.org/abs/2609.00549v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_01-33-57Z_SkillFollowing_EvaluatingActualSkillUseinRetrieval.md
generated_at: 2026-09-01 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Skill Following (SF), a metric that measures whether an LLM agent actually uses retrieved skills to improve task outcomes, rather than relying on aggregate performance comparisons that suffer from selection bias. The authors evaluate 17 models across coding and mathematical tasks and find that while some models show positive retrieval lift overall, the Retrieval-Invoked Actual-Use Effect (RAE) often turns negative, indicating that skill use can harm specific task results.

## Key Takeaways
- Aggregate retrieval lift metrics mask the true impact of skill use because they compare different tasks rather than matching skill-enabled and disabled executions on the same task.  
- RAE reveals a paradox where models that appear to benefit system‑wide may actually degrade performance on the exact tasks where they invoked retrieved skills.  
- The findings show that standard evaluation can create an illusion of tool‑use proficiency while ignoring real‑world harm caused by skill invocation.

## Context
Current LLM agent research often relies on coarse aggregate metrics such as success rates across a suite of tasks, which do not isolate the effect of retrieving and applying external skills. This leads to misleading conclusions about whether agents truly benefit from tool use or merely appear to improve overall scores. The paper’s work addresses this gap by proposing a more precise evaluation that directly measures actual skill utilization.

## Implications
For researchers developing LLM agents, adopting SF and RAE can prevent overestimating the value of retrieval mechanisms and guide more realistic design choices. Practitioners should be cautious about interpreting aggregate gains as evidence of effective tool integration, especially when real‑world task performance may suffer.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00549v1)
