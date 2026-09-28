---
title: LLM Parkinsonism: Executive-Control Failure, Token-Inefficient Persistence, and an Uncertainty-Aware Global Executive Control Architecture for Autonomous Language-Model Agents
url: http://arxiv.org/abs/2609.30662v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-25_01-00-15Z_LLMParkinsonism_Executive_ControlFailure_Token_Ine.md
generated_at: 2026-09-28 01:26
model: qwen3.6-35b-a3b
---

## Summary
This paper investigates "LLM Parkinsonism," a phenomenon where autonomous agents persist in low-value actions after task objectives are satisfied, resulting in token inefficiency and unnecessary complexity. The authors attribute this behavior to self-conditioned loops that concentrate proposal generation, scope interpretation, progress assessment, and stopping authority within the same model process. To address this, they introduce Global Executive Control (GEC) v0.2, an uncertainty-aware architecture that decouples action generation from project-level governance, demonstrating significant improvements in token efficiency while maintaining high success rates.

## Key Takeaways
- LLM Parkinsonism arises when autoregressive models lack external governance, causing agents to continue refining or verifying tasks despite diminishing returns; this is driven by the concentration of control functions within a self-conditioned loop rather than prediction mechanics alone.
- GEC v0.2 implements an uncertainty-aware governance layer that separates action generation from executive decision-making, allowing for explicit management of scope, evidence, resource allocation, and stopping criteria independent of the policy model.
- Benchmarking across 24,000 episodes under a 40,000-token ceiling reveals GEC achieves 96.57% hard-goal success while reducing mean token consumption by 36.4% compared to local control baselines, eliminating pre-completion drift and sharply lowering gross complexity without increasing governance overhead sensitivity.

## Context
As large language models evolve into autonomous agents capable of long-horizon workflows and tool use, the gap between local competence and project-level executive control becomes a critical bottleneck. Current agent architectures often struggle with self-regulation, leading to resource waste and goal drift when models operate without explicit mechanisms to assess global progress or halt execution. This research situates itself within the growing focus on reliable agent governance, highlighting structural flaws in self-referential design patterns that hinder scalability and efficiency.

## Implications
The findings underscore the necessity of decoupling policy generation from executive control to build robust autonomous agents capable of efficient resource management. Practitioners developing LLM-based systems should prioritize uncertainty-aware stopping mechanisms and explicit governance layers to prevent token bloat and complexity creep in production environments. By adopting architectures like GEC, developers can enhance agent reliability and cost-effectiveness while ensuring actions remain aligned with overarching objectives throughout extended workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.30662v1)
