---
title: LEASH: Uncertainty-Aware Weak-to-Strong Escalation and Oversight for Computer-Use Agents
url: http://arxiv.org/abs/2610.22280v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_17-40-12Z_LEASH_Uncertainty_AwareWeak_to_StrongEscalationand.md
generated_at: 2026-10-15 22:13
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
LEASH is a training-free framework for computer-use agents that dynamically escalates from a weak open-weight model to a strong frontier model only when the weak agent's latent uncertainty signals it is needed, while maintaining ongoing oversight of the strong agent after handoff. The framework achieves 73.66% task success on OSWorld with a 35B-parameter model at $0.4117 per task, matching the performance of always-on Claude Opus 5 (72.90%) while reducing inference cost by 19.2%.

## Key Takeaways
- LEASH operates through three uncertainty-driven layers: initial task-level uncertainty for early routing decisions, step-level uncertainty for runtime escalation during execution, and a shadow observer layer that continues monitoring the strong black-box agent after handoff. The core mechanism compares the weak model's hidden states against stored representations from its own past successful and failed trajectories, treating states that resemble failures as high-uncertainty signals warranting escalation.
- The uncertainty estimator is designed to be zero-overhead: it reuses activations already produced during the weak agent's action generation, requiring no additional forward pass, no dedicated monitor training, and no extra inference budget. This makes the escalation decision cheap enough to evaluate at every step of a long-horizon task without materially increasing cost.
- Across four contemporary model backbones on OSWorld, LEASH consistently outperforms standalone weak agents and beats random escalation strategies by 6.55 to 11.94 percentage points at matched escalation rates, demonstrating that uncertainty-aware routing is substantially more effective than arbitrary or fixed escalation policies.

## Context
Computer-use agents tackling long-horizon tasks face a fundamental cost-reliability tradeoff: frontier models like Claude Opus 5 deliver high success rates but at prohibitive per-step inference costs, while small open-weight models are affordable but frequently fail on complex multi-step workflows. Weak-to-strong escalation has emerged as a promising middle ground, but prior approaches lack a principled, cheap mechanism for deciding exactly when escalation is warranted. LEASH addresses this gap by exploiting the weak model's own internal representations as a free uncertainty signal, eliminating the need for external monitors or additional training while still providing oversight even after the strong agent takes over.

## Implications
For practitioners deploying computer-use agents in production, LEASH demonstrates that near-frontier performance can be achieved at roughly 80% of the inference cost by intelligently routing only genuinely uncertain steps to expensive models, making agentic automation economically viable for high-volume or budget-constrained deployments. The shadow observer layer is particularly significant for industry use, as it provides a practical oversight mechanism for black-box API agents whose internals are inaccessible, offering a template for monitoring and safety auditing in any system where a strong model is invoked as a service. The training-free, zero-overhead design means the approach can be retrofitted onto existing agent pipelines without retraining or architectural changes, lowering the barrier to adoption across the open-weight model ecosystem.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22280v1)
