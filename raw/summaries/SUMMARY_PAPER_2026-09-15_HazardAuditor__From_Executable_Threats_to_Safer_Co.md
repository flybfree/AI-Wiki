---
title: HazardAuditor: From Executable Threats to Safer Computer-Use Agents
url: http://arxiv.org/abs/2609.15134v1
type: paper-summary
date: 2026-09-15
source_paper: 2026-09-14_07-09-33Z_HazardAuditor_FromExecutableThreatstoSaferComputer.md
generated_at: 2026-09-15 03:27
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
This paper introduces HazardAuditor, an execution-grounded framework designed to address the emerging safety risks posed by autonomous computer-use agents that dynamically interact with browsers, terminals, and external services. By normalizing heterogeneous agent interactions into canonical event representations and introducing Guard Policy Optimization (GuardPO), the authors successfully bridge the gap between static prompt-based guard models and runtime execution monitoring. The proposed system demonstrates significant performance gains, improving safety detection accuracy by up to 16.5 percentage points over existing state-of-the-art guard models across multiple benchmarks and agent frameworks.

## Key Takeaways
- Existing guard models are fundamentally misaligned with dynamic agent execution because they focus on static prompts rather than runtime behavior, prompting the development of an infrastructure that runs diverse agents in controlled environments to normalize their interactions into a unified event representation for cross-framework supervision.
- Token-level post-training objectives create a structural mismatch for generative safety guards by allowing longer rationales to disproportionately dominate gradient updates; GuardPO resolves this by converting deterministic safety outcomes into sequence-level advantages and normalizing both rationale and verdict regions to make the safety decision the primary optimization unit.
- Across multiple benchmarks and heterogeneous computer-use systems, HazardAuditor achieves up to a 16.5 percentage point improvement in accuracy over the strongest prior guard model, establishing a new baseline for runtime agent safety evaluation while providing open-source code, models, and evaluation artifacts for community adoption.

## Context
As AI agents increasingly operate autonomously within

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.15134v1)
