---
title: LatentRiskBench: Measuring State-Dependent Risks in Enterprise Agents
url: http://arxiv.org/abs/2610.17685v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_04-07-44Z_LatentRiskBench_MeasuringState_DependentRisksinEnt.md
generated_at: 2026-10-14 00:42
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
LatentRiskBench introduces a novel benchmark and evaluation framework for measuring state-dependent safety risks in enterprise AI agents, where the same action can be safe in one workflow context but violate policy in another. The paper demonstrates that existing action-level safety evaluations detect only 9% of state-dependent violations, while state-level evaluation achieves 96% detection, revealing a critical blind spot in current enterprise agent safety assessment. The authors also introduce residual risk (RR) metrics and validate their approach against a commercially deployed enterprise scenario.

## Key Takeaways
- State-dependent risks represent a fundamentally different failure mode than action-local risks: the same terminal action (e.g., approving a transaction, sending an email) can be benign or policy-violating depending on latent workflow states such as prior approvals, compliance flags, or data sensitivity levels accumulated earlier in the agent's execution trajectory. LatentRiskBench constructs paired trajectories that share identical terminal actions but differ in these hidden contextual states, forcing evaluation systems to reconstruct full workflow context rather than relying on superficial action-level cues.
- The quantitative gap between evaluation approaches is stark: action-level evaluation captures only 0.09 (9%) of state-dependent violations, whereas state-level evaluation reaches 0.96 (96%). This nearly tenfold difference demonstrates that current safety benchmarks and guardrail methods are structurally incapable of detecting the majority of enterprise agent safety failures, which are embedded in workflow state rather than in individual actions.
- Existing guardrail methods largely fail to address state-dependent risks unless they are explicitly redesigned to operate on workflow states rather than isolated actions. The paper's case study on a commercial deployed scenario confirms that the benchmark's safety metrics provide a more realistic and operationally meaningful measure of enterprise agent safety than conventional action-level scoring.

## Context
As enterprise AI agents increasingly automate complex multi-step workflows involving approvals, data handling, and policy compliance, safety evaluation has lagged behind capability advances. Most existing benchmarks treat safety as a property of individual actions, which is adequate for simple tool-use tasks but fundamentally misaligned with enterprise deployments where risk accumulates across a sequence of states. This paper addresses a structural gap in the AI safety evaluation literature by formalizing state-dependent risk as a distinct category and providing the first benchmark specifically designed to expose it.

## Implications
For practitioners deploying enterprise agents, this work signals that current guardrail and monitoring systems may be providing a false sense of safety, missing up to 91% of policy violations that depend on workflow context. Organizations building agentic systems for finance, healthcare, legal compliance, or supply-chain operations should adopt state-level evaluation metrics like the residual risk measures introduced here. For the broader AI safety research community, the findings argue that benchmark design must account for latent state reconstruction as a core evaluation capability, not merely an optional enhancement, if agent safety claims are to be trustworthy in production environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.17685v1)
