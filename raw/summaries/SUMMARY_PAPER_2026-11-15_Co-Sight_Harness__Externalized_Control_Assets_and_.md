---
title: Co-Sight Harness: Externalized Control Assets and Deterministic Enforcement for Long-Horizon Business Agents
url: http://arxiv.org/abs/2611.17696v1
type: paper-summary
date: 2026-11-15
source_paper: 2026-11-13_03-21-33Z_Co_SightHarness_ExternalizedControlAssetsandDeterm.md
generated_at: 2026-11-15 21:26
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The Co-Sight Harness paper proposes a method for making long-horizon business agent workflows reliable without modifying the underlying language model. Instead of fine-tuning or prompting the model differently, the authors externalize workflow definitions, execution state, and domain knowledge into versioned "control assets" governed by a state machine and machine-checkable acceptance gates, with an independent auditor grading execution traces. Evaluated on three deployed workflows exceeding 200 steps, the approach raised unattended completion from 50% to 100%, retrieval recall from 56% to 91.67%, and cut end-to-end latency from 440 to 159 minutes on a 120-case evaluation set.

## Key Takeaways
- The paper identifies two distinct failure modes in long-horizon business workflows: error accumulation across chained activities and vocabulary mismatch between the knowledge an activity requires and the user's request. A controlled ablation experiment separates these two sources, demonstrating that the proposed control-asset architecture addresses each independently rather than relying on a single model-level fix.
- The core architectural insight is that reliability can be achieved by keeping the language model backbone fixed and moving all workflow logic, state tracking, and domain knowledge into externally versioned control assets. A state machine enforces valid transitions, machine-checkable acceptance gates validate outputs at each step, and an independent auditor grades the resulting execution trace. Assets are only updated after a regression check and human approval, creating a governed update cycle.
- Practical deployment evidence shows the method generalizes beyond its authors: two additional domains were taken over by teams who did not write the original assets, one in four days and one in seven days, suggesting the control-asset abstraction lowers the barrier for cross-team adoption. On Domain A, scenario-analysis recall rose from 45% to 93%, and the full pipeline completed unattended in 159 minutes versus 440 minutes previously.

## Context
This work sits at the intersection of agentic AI systems and enterprise workflow automation, addressing a widely acknowledged limitation: large language models degrade in reliability as task chains grow longer, and domain-specific knowledge often lives in schemas and vocabularies that differ from natural-language user queries. Prior approaches typically attempt to solve these problems through prompt engineering, fine-tuning, or tool-augmented generation, all of which entangle model behavior with workflow logic. Co-Sight Harness instead draws on principles from software engineering—versioned configuration, state machines, acceptance testing, and independent auditing—to externalize control logic, treating the language model as a fixed execution engine rather than a mutable component.

## Implications
For practitioners deploying AI agents in regulated or high-stakes business environments, this architecture offers a path to reliability and auditability without retraining or re-prompting the model, which reduces operational risk and simplifies compliance review. The demonstrated cross-team handoff in four to seven days suggests that externalized control assets can serve as a transferable abstraction layer, potentially accelerating enterprise adoption of agentic workflows. For the broader AI research community, the controlled ablation separating vocabulary-mismatch failures from error-accumulation failures provides a diagnostic framework that could inform future agent-system design beyond this specific implementation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.17696v1)
