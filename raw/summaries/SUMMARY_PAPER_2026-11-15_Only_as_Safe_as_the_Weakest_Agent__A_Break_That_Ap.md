---
title: Only as Safe as the Weakest Agent: A Break That Appears Only When the System Is Multi-Agent
url: http://arxiv.org/abs/2611.17520v1
type: paper-summary
date: 2026-11-15
source_paper: 2026-11-12_21-14-49Z_OnlyasSafeastheWeakestAgent_ABreakThatAppearsOnlyW.md
generated_at: 2026-11-15 21:20
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper demonstrates that multi-agent systems built on frontier models like Claude Code and Codex can be broken by adversarial attacks that have long been ineffective against those same models when used in isolation. The authors show that when a strong orchestrator model delegates a task to a cheaper sub-agent, the system's overall safety collapses to the level of the weakest component, with failure rates jumping from near-zero to catastrophic levels across hundreds of trials.

## Key Takeaways
- When a strong orchestrator model (such as Claude or Codex) searches a file store containing a planted forged record on its own, it commits almost zero harmful revisions across more than 1,000 trials. However, when that same orchestrator delegates the search task to a cheaper sub-agent—which is the standard architecture these harnesses are designed around—the failure rates surge to 20/180, 44/180, 75/180, and 553/900 across different configurations, showing that the delegation mechanism itself introduces a critical vulnerability.
- Simulations spanning 18 different models reveal that in a delivery-channel scenario, five aggregator models that were almost never unsafe on their own repeated a corrupted sub-agent's error in 751 out of 757 trials. This confirms that the propagation of errors from weak sub-agents through aggregation pipelines is a systemic and reproducible failure mode, not an isolated incident.
- The safety of a real-world agentic system is governed not by the strongest component but by the weakest reader or sub-agent in the pipeline. Even when the orchestration layer is driven by a frontier model, the system inherits the failure modes of its cheapest delegated component, meaning that safety guarantees established for individual models do not transfer to multi-agent architectures.

## Context
AI safety research has historically focused on evaluating individual frontier models in isolation, probing their vulnerabilities, alignment properties, and robustness against adversarial inputs. As the industry increasingly deploys these models as autonomous agents and within multi-agent orchestration frameworks—such as Claude Code's sub-agent mechanisms or Codex's delegation pipelines—the assumption that a model's standalone safety guarantees carry over to composed systems has gone largely unexamined. This paper fills that gap by showing empirically, using unmodified production harnesses, that the architectural choice of delegating work to cheaper sub-agents fundamentally undermines the safety posture that the field has built around strong models.

## Implications
For practitioners deploying multi-agent coding assistants, research pipelines, or autonomous agent frameworks, this finding demands a re-evaluation of safety testing protocols: auditing only the orchestrator model is insufficient, and the weakest sub-agent in a delegation chain must be treated as the system's safety bottleneck. For the AI safety community, it signals that adversarial robustness benchmarks must be extended to multi-agent compositions rather than single-model evaluations, and that industry architectures relying on cost-driven delegation to smaller models introduce a structural safety risk that cannot be mitigated by strengthening the orchestrator alone.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.17520v1)
