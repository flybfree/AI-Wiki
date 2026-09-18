---
title: "TypeSafe AI: System One Decision Models"
created: 2026-09-18
updated: 2026-09-18
type: concept
tags: [TypeSafe, System-One, structured-output, AI-primitives, calibrated-confidence]
sources:
  - https://docs.typesafe.ai/introduction
  - https://docs.typesafe.ai/concepts/system-one
  - https://docs.typesafe.ai/concepts/how-to-build-with-system-one
confidence: medium
---
# TypeSafe AI: System One Decision Models

## Summary

[TypeSafe AI's documentation](https://docs.typesafe.ai/introduction) describes **System One** models as AI systems for fast, structured decisions that software can consume directly. Its flagship model, **Jev**, evaluates typed questions against an application-provided state and returns constrained values and probabilities rather than generated prose. The intended design is to keep workflow control, deterministic rules, and side effects in ordinary code while using the model for narrow judgments over unstructured data.

This is a different integration target from a chat-oriented large language model (LLM). Instead of asking an LLM to emit JSON and then parsing and validating the text, the developer defines the possible answer space up front. TypeSafe's documentation presents this as a way to make AI decisions composable, comparable, and suitable for real-time software paths. These are product and vendor claims; production use still requires domain-specific evaluation and threshold calibration.

## Core model

A request has two parts:

- **State** — the text, JSON, or arrays of text that provide current context.
- **Questions** — focused judgments evaluated against that state.

The documentation recommends one atomic judgment per question. If a decision depends on independent factors, ask about each factor separately and combine the results with weights or deterministic rules in code. Independent questions can be sent together and are evaluated in parallel, so speculative questions can be included and ignored when their answers are irrelevant to the current path.

## Three AI primitives

| Primitive | Use when | Returns |
|---|---|---|
| **Choice** | Select one option from a known, unordered set | Selected choice, probabilities, and confidence |
| **Score** | Place the state along ordered, descriptive levels | Score, legend, probabilities, and confidence |
| **Noul** | Evaluate a clearly defined yes/no statement | Probability from 0 to 1 that the statement is true |

For example, a support workflow might ask whether a ticket requests a refund (`Noul`), classify its request type (`Choice`), and rate customer frustration (`Score`). Code can then route, threshold, or escalate based on those answers.

## Confidence and system behavior

Choice and Score answers include both a probability distribution and a derived `confidence` value. A concentrated distribution indicates a clearer answer; a flatter distribution indicates uncertainty. TypeSafe recommends treating confidence as a control signal rather than as a guarantee of correctness:

- high confidence: act automatically when the action is low-risk;
- medium confidence: request confirmation, gather more context, or review;
- low confidence: do not guess; escalate to a person or another model.

Thresholds should reflect the cost of mistakes. A read-only screen can use a lower threshold than a destructive or financial action. Noul exposes the yes-probability directly and does not include a separate confidence field.

## Practical build pattern

1. Keep deterministic logic and side effects in code.
2. Put only relevant, current context in the state.
3. Define narrow questions with explicit answer criteria.
4. Batch independent questions in one request.
5. Compose answers in code using rules, weights, thresholds, or routing tables.
6. Test calibration and failure behavior on representative domain data before enabling automation.

The official Python SDK supports synchronous and asynchronous clients. The documentation shows installation with `uv add typesafe-sdk` or `pip install typesafe-sdk`, followed by a `TYPESAFE_API_KEY` environment variable and a `system_one` call.

## Limits and cautions

- System One is designed for focused decisions, not open-ended explanation, code generation, or autonomous next-step selection.
- Calibration is a population-level property; confidence does not guarantee that an individual answer is correct.
- The answer space and criteria determine what the model can express. Missing options or ambiguous rubrics produce bad decisions even when the output is structurally valid.
- Vendor-reported latency, cost, and accuracy claims should be independently benchmarked for the target workload.

## Related concepts

- [Existing TypeSafe launch summary](../../entities/article/2026-09-16_IntroducingSystemOneModelsandJev_summary.md)
- [AI agents and agentic workflows](../ai-agents/ai-agents-lesson-13-agents-and-agentic-workflows.md)
- [AI benchmarks](../ai-benchmarks/AIBenchmarks.md)

## Processed URLs

- https://docs.typesafe.ai/introduction
- https://docs.typesafe.ai/llms.txt
- https://docs.typesafe.ai/concepts/system-one
- https://docs.typesafe.ai/primitives
- https://docs.typesafe.ai/confidence
- https://docs.typesafe.ai/concepts/how-to-build-with-system-one
- https://docs.typesafe.ai/sdk/python
