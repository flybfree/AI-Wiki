---
title: Certified Execution Harness for Agentic AI: Safe and Least-Intrusive Petri-Net Supervisory Control Between Reasoning and Action
url: http://arxiv.org/abs/2610.31376v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-22_14-48-16Z_CertifiedExecutionHarnessforAgenticAI_SafeandLeast.md
generated_at: 2026-10-22 22:13
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper formalizes the execution harness between a large language model agent and its tools as a Petri-net supervisory control problem, where tokens (marks) encode capabilities, approvals, and budgets, ensuring that any prompt-injected request whose preconditions are unmet or already consumed is mechanically refused regardless of its linguistic phrasing. The authors further introduce a "replanning closed loop" model in which an agent may retry after a refusal at the cost of additional inference calls, and demonstrate that the conventional maximally permissive supervisor can be arbitrarily more intrusive than a stricter safe alternative, while characterizing the least-intrusive safe supervisor as a value-threshold refinement of the conventional one.

## Key Takeaways
- The Petri-net formulation encodes tool-call preconditions as required marks (capabilities, approvals, budgets), so a transition fires only when all necessary marks are present; an injected request whose preconditions are unmet or already spent is refused by the structure of the net itself, making safety independent of the wording or persuasiveness of the injected prompt.
- The paper introduces the replanning closed loop, in which a refused agent may propose a new action after each refusal, each retry consuming an inference call. In this loop the authors prove that the conventional maximally permissive supervisor can be arbitrarily more intrusive than a stricter safe supervisor, meaning that the standard supervisory-control solution wastes computational resources by permitting too many futile retry cycles.
- For a fixed proposer model, the maximally permissive least-intrusive supervisor is characterized as a value-threshold refinement of the conventional supervisor, and under precise conditions this refinement orders two concurrent actions by at most one monitor place. On an autonomous release agent case study, synthesis reveals that safe deployment requires at least one step the supervisor can refuse after a rollout has already begun, showing that purely pre-execution gating is insufficient.

## Context
As LLM agents increasingly interact with external tools, APIs, and physical actuators, prompt-injection and adversarial-input attacks threaten to hijack tool selection and execution order, potentially causing irreversible side effects such as financial transactions, code deployments, or hardware commands. Existing guardrails operate at the prompt level and are vulnerable to paraphrase attacks; this paper shifts the safety guarantee into the structural layer of the execution harness, borrowing decades of discrete-event supervisory-control theory from manufacturing and robotics to provide a mathematically certified refusal mechanism that is invariant to the agent's internal reasoning.

## Implications
For practitioners deploying agentic AI in regulated or safety-critical environments, the Petri-net harness offers a deployable, formally verifiable control layer that can be synthesized offline and enforced at runtime without retraining the underlying model, reducing the attack surface of prompt injection to a structural precondition check. For the research community, the replanning closed-loop analysis and the value-threshold refinement characterization open a principled design space for balancing safety against computational cost, guiding the construction of supervisory monitors that minimize wasted inference cycles while preserving the agent's ability to recover from refusals. Industry teams building autonomous release pipelines, financial-trading bots, or robotic planners can adopt the synthesis procedure to identify the minimal set of monitor places needed to guarantee safety, including the critical insight that at least one post-rollout refusal step is unavoidable in certain deployment scenarios.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.31376v1)
