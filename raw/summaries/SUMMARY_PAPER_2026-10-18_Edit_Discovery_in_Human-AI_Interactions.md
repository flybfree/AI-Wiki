---
title: Edit Discovery in Human-AI Interactions
url: http://arxiv.org/abs/2610.22661v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-15_21-24-20Z_EditDiscoveryinHuman_AIInteractions.md
generated_at: 2026-10-18 20:44
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper formalizes the problem of deciding which human-AI interaction responses should be sent to a costly "editor" (a human expert, a stronger model, or the same model with additional resources) for potential correction. The authors define Edit Discovery Optimization (EDO), prove that the optimal policy is a cost-adjusted threshold on the posterior probability of an edit, and propose EDIT, an online algorithm that operates under partial feedback while respecting a strict editor-cost budget. Experiments on four reasoning and factual QA benchmarks show EDIT outperforms direct LLM-based batch selection in balancing editor cost against Type-I and Type-II errors.

## Key Takeaways
- The paper introduces a formal optimization framework (EDO) for allocating a limited editor budget across a stream of AI interactions, where the goal is to minimize missed edit opportunities among skipped interactions while also controlling unnecessary confirmations. The population-optimal solution is characterized as a threshold rule on the posterior probability that a given response will require an edit, adjusted by the cost of invoking the editor.
- EDIT (Edit Discovery via Iterative Thresholding) is designed for the realistic partial-feedback setting: edit labels are only revealed for interactions actually sent to the editor, not for skipped ones. The algorithm combines an adaptive edit score, a confirmation-control threshold, and a cost-aware selection rule, guaranteeing the editor budget is respected at every round and bounding the average confirmation rate up to a vanishing finite-horizon term, with no distributional assumptions on the incoming interaction stream.
- Empirical evaluation across four reasoning and factual question-answering benchmarks demonstrates that EDIT achieves a superior trade-off among editor cost, Type-I error (unnecessary confirmations), and Type-II error (missed edits) compared to straightforward LLM-based batch selection strategies, validating the theoretical threshold structure in practice.

## Context
As large language models are deployed at scale in production systems, a growing fraction of model outputs are already correct, while a smaller subset contains errors that could serve as high-value supervision data if detected and corrected. Prior work on active learning, model evaluation, and human-in-the-loop pipelines often assumes unlimited evaluation capacity or full feedback, which is unrealistic when expert time, inference compute, or tool-use overhead are constrained. This paper bridges that gap by treating editor invocation as a scarce resource and framing the selection problem as a constrained online optimization, connecting ideas from bandit algorithms, sequential decision-making, and model evaluation into a unified framework relevant to AI safety, RLHF data curation, and continuous model improvement pipelines.

## Implications
For practitioners deploying AI systems, EDIT provides a principled, budget-respecting mechanism to triage model outputs without requiring full ground-truth labels, making it directly applicable to production monitoring dashboards, RLHF data pipelines, and automated evaluation harnesses where expert or compute budgets are hard constraints. For the research community, the characterization of the optimal policy as a posterior-probability threshold offers a theoretical foundation that future work can extend to multi-editor hierarchies, non-stationary interaction distributions, and settings where the editor itself is an AI system with its own failure modes. The algorithm's lack of distributional assumptions and its per-round budget guarantees make it suitable for streaming, real-time deployment scenarios where interaction patterns shift unpredictably.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22661v1)
