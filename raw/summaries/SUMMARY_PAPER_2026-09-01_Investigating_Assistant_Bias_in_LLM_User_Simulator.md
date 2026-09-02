---
title: Investigating Assistant Bias in LLM User Simulators Using a Role Vector
url: http://arxiv.org/abs/2609.00608v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_02-49-30Z_InvestigatingAssistantBiasinLLMUserSimulatorsUsing.md
generated_at: 2026-09-01 22:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates assistant bias in LLM‑based user simulators by extracting a role vector that contrasts model activations representing the user versus assistant perspectives. The analysis reveals that user direction is detectable in activations and drives realistic, user‑like behaviors, while also showing that this representation can amplify or override individual user profiles.

## Key Takeaways
- User direction is identifiable in model activations and elicits behaviors distinct from those of the assistant, indicating a structural separation between user and assistant representations.  
- The role vector associated with user behavior enhances simulation realism but may exaggerate user actions, potentially overriding specific user profiles when used to steer simulations.  
- These findings confirm that assistant bias is structurally identifiable within LLMs and that user behavior can be directionally analyzed at the representation level.

## Context
LLM‑based user simulators are widely adopted for large‑scale evaluation of autonomous agents, replacing expensive human evaluations with scalable synthetic interactions. However, the prevalence of assistant bias—where models consistently cooperate or disengage in ways that do not mirror real users—undermines the validity of such assessments and highlights a gap between simulated and actual user experiences.

## Implications
For researchers, this work provides a principled representation‑level tool to detect and mitigate assistant bias, improving simulation fidelity. Practitioners can leverage the role vector to design more realistic evaluation pipelines, ultimately leading to more trustworthy AI deployments that align with genuine user expectations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00608v1)
