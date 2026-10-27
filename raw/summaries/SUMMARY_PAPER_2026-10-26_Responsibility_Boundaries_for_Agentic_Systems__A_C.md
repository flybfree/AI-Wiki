---
title: Responsibility Boundaries for Agentic Systems: A Comparative Evaluation of Probabilistic Agentic Programming
url: http://arxiv.org/abs/2610.33312v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-23_21-31-12Z_ResponsibilityBoundariesforAgenticSystems_ACompara.md
generated_at: 2026-10-26 20:31
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Probabilistic Agentic Programming (PAP) as a formal framework that makes responsibility boundaries in language-model agents explicit through programming abstractions connecting mandate, authority, effects, and evidence. The authors compare PAP against existing paradigms including BDI systems, workflow languages, and LLM tool-use frameworks across seven dimensions, and validate their approach through a mediation kernel with inductive safety proofs, backward simulation, and an exploratory study generating 1,225 assessed observations across seven business cases and seven models.

## Key Takeaways
- PAP formalizes responsibility boundaries as explicit programming abstractions rather than implicit distributions across prompts, host code, configuration, and logs. The mediation kernel enforces checks before tool execution, operation-bound approval, resource limits, and evidence collection, establishing conditional safety guarantees for arbitrary model responses assuming correct guards and complete mediation.
- The paper provides formal verification through inductive proofs establishing conditional safety, a backward simulation matching graph executions to source executions in a defined sequential Touba subset, and finite-state exploration to validate the model. Human checkpoints release program continuations while operation-bound approval remains a separate kernel contract, ensuring separation of concerns in authority delegation.
- The exploratory study spanning seven business cases (including two three-agent workflows), seven models from three providers, five methods, and five repetitions produced 1,225 assessed observations. Native Touba completed all 35 observations on six models and 30 on the remaining model, matching the highest observed count for each model, while all paired case intervals included zero, indicating no statistically significant difference from existing frameworks on the evaluated tasks.

## Context
As agentic systems increasingly combine reasoning, tool use, memory, delegation, and external effects, the question of who or what holds authority at each execution step becomes critical for safety, accountability, and regulatory compliance. Existing frameworks distribute authority implicitly across prompts, configuration files, and logging infrastructure, creating opaque failure modes. This paper addresses a gap in formalizing responsibility boundaries as first-class programming constructs, bridging the traditions of agent-oriented programming, BDI architectures, and modern LLM tool-use frameworks under a unified probabilistic abstraction.

## Implications
For practitioners deploying agentic systems in regulated or high-stakes environments, PAP offers a path toward auditable execution boundaries where authority delegation, resource limits, and evidence trails are encoded in the program itself rather than inferred from runtime behavior. The finding that native Touba matches existing frameworks on task completion while maintaining fixed runtime authority boundaries suggests that formal responsibility contracts can be integrated without sacrificing practical performance, providing a foundation for safer multi-agent orchestration and clearer accountability chains in production AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.33312v1)
