---
title: When AI Agents Act on Our Behalf: A Taxonomy of Human-Agent Interaction Failure
url: http://arxiv.org/abs/2611.00291v1
type: paper-summary
date: 2026-11-02
source_paper: 2026-10-30_19-17-20Z_WhenAIAgentsActonOurBehalf_ATaxonomyofHuman_AgentI.md
generated_at: 2026-11-02 21:27
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper presents a bottom-up taxonomy of 12 distinct failure modes in human-agent interaction, derived from 695 documented incidents across two public repositories. The authors organize these failures across three interaction stages adapted from Amershi et al.'s human-AI interaction guidelines and code the autonomy level at which each failure arises. The central finding is that the same model performing the same task can fail in fundamentally different ways depending on the deployment configuration that determines how much the agent completes between points of user involvement.

## Key Takeaways
- The authors identified 12 failure modes through systematic bottom-up coding of 695 real-world incidents, organized within three interaction stages. This empirical grounding distinguishes the taxonomy from purely theoretical frameworks, as it captures failures as they actually manifest in deployed agent systems rather than as hypothetical edge cases.
- Autonomy level is a critical variable: all 12 failure modes appear at both low and high autonomy, but rising autonomy changes the form each failure takes. This means that increasing an agent's autonomy does not eliminate failure categories but transforms their expression, making failures harder to anticipate and mitigate as systems become more agentic.
- A property fixed at deployment—how much the agent completes between points of user involvement—determines what a person can do when an agent fails. This means failure severity and recoverability are not inherent to the model or task but are shaped by architectural choices made before any interaction occurs, highlighting the importance of interaction design over model capability alone.

## Context
As AI agents increasingly write code, manipulate user interfaces, and transact on behalf of users, the field has focused heavily on model capability benchmarks while under-studying the interaction layer where failures actually harm users. This paper bridges a critical gap by adapting established human-AI interaction guidelines from Amershi et al. to the agentic setting, providing a structured vocabulary for understanding failures that neither incident logs nor standard agent benchmarks capture. It matters because the industry is rapidly deploying autonomous agents without adequate understanding of how interaction design choices shape failure outcomes.

## Implications
For practitioners deploying AI agents, the finding that the same model fails differently under different configurations means that safety and reliability cannot be assessed by evaluating model performance alone; deployment architecture and the placement of human checkpoints are equally determinative of failure risk. The paper argues that users need graduated controls between full delegation and full manual work, suggesting that current binary autonomy settings are insufficient. For the research community, the gap between what agent benchmarks measure and where failures actually occur in interaction calls for new evaluation frameworks that capture the interaction stage rather than only task completion.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.00291v1)
