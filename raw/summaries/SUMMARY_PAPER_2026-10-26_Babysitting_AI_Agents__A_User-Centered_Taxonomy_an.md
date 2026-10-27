---
title: Babysitting AI Agents: A User-Centered Taxonomy and Study of Agentic Delegation Failures
url: http://arxiv.org/abs/2610.34748v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-26_02-49-17Z_BabysittingAIAgents_AUser_CenteredTaxonomyandStudy.md
generated_at: 2026-10-26 23:16
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces MANDATE, a taxonomy of 23 agentic delegation failure categories organized into seven groups, derived from analysis of 163,487 Reddit posts describing AI agent use. The authors further conducted a follow-up study with 73 AI agent users to examine how failure prevalence relates to perceived severity and noticeability, finding that more severe failures are paradoxically harder for users to detect. The work also maps the maturity of existing research on each failure type, highlighting commonly encountered problems that remain understudied.

## Key Takeaways
- The authors developed MANDATE, a structured taxonomy comprising 23 failure categories grouped into seven clusters, built from a corpus of 163,487 Reddit posts where users described their experiences delegating tasks to AI agents. This provides a systematic vocabulary for understanding how agents deviate from user expectations during long-running, multi-step workflows.
- A user study with 73 participants revealed a critical paradox: failures rated as more severe by users are simultaneously considered harder to notice. Additionally, prior personal experience with a specific failure type was associated with greater noticeability, suggesting that users develop detection skills through repeated exposure rather than through inherent salience of the failure.
- The paper identifies a significant research gap by assessing the maturity of literature on each failure category and finding that commonly encountered failures, such as agents running without making progress, have received little scholarly attention. This gap between real-world prevalence and research coverage represents a blind spot in the AI agent safety and reliability literature.

## Context
As AI agents increasingly handle autonomous, multi-step workflows on behalf of users, the question of how and why these delegations fail has become central to AI safety and human-computer interaction research. Most existing work focuses on single-step task correctness or benchmark performance, leaving long-running agentic behaviors and their failure modes poorly characterized. This paper bridges that gap by grounding its taxonomy in real user-reported experiences rather than synthetic evaluations, offering a user-centered lens that complements technical evaluation frameworks.

## Implications
For practitioners building and deploying AI agents, this taxonomy provides actionable categories to monitor, test against, and design oversight mechanisms for, enabling more targeted mitigation strategies rather than generic "monitor the agent" advice. For the research community, the identification of understudied yet frequently encountered failures signals where new evaluation benchmarks and safety studies should be prioritized. For industry, the finding that severe failures are harder to notice underscores the need for proactive transparency features and progress indicators in agent interfaces, rather than relying on users to detect problems after they have already escalated.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.34748v1)
