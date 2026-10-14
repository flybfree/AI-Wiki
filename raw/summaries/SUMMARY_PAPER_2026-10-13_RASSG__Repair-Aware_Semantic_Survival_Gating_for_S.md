---
title: RASSG: Repair-Aware Semantic Survival Gating for Streaming Tool Execution
url: http://arxiv.org/abs/2610.14659v1
type: paper-summary
date: 2026-10-13
source_paper: 2026-10-10_07-17-54Z_RASSG_Repair_AwareSemanticSurvivalGatingforStreami.md
generated_at: 2026-10-13 22:00
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Repair-Aware Semantic Survival Gating (RASSG), a mechanism for streaming speech assistants that jointly controls when to launch a tool call and when to cancel an already-launched call before its effects become irreversible. The core problem addressed is that streaming assistants may execute tools based on partial speech input, but subsequent user self-corrections can invalidate the arguments already sent, producing stale executions whose side effects persist. RASSG reduces the stale execution rate from 50.00% to 3.15% on the ReCAST prospective-repair subset while maintaining a mean delay of 3.676 seconds across successful trajectories.

## Key Takeaways
- RASSG employs a conservative launch gate requiring three consecutive speech recognition results to arrive with identical nonempty arguments before any tool is dispatched, ensuring that transient transcription errors or mid-sentence corrections do not trigger premature execution.
- The cancellation mechanism combines a calibrated argument invalidity risk score with the estimated execution cost of the tool, enabling the system to decide at the last feasible opportunity whether to abort an in-flight call before its effects become irreversible, rather than waiting until the user finishes speaking.
- Ablation experiments with identical initial launches isolate the contribution of active cancellation, demonstrating that controlling ongoing calls before their effects become irreversible is essential; the stale reduction generalizes across every early-execution baseline on both public speech datasets (ReCAST and FDB-v3) and the Audio2Tool benchmark.

## Context
Streaming speech assistants increasingly overlap tool execution with incoming user speech to minimize perceived latency, a design pattern adopted by major voice assistants and agentic frameworks. However, the field has lacked principled mechanisms to handle the tension between early execution for speed and the reality that users frequently self-correct mid-utterance, invalidating arguments that have already triggered irreversible side effects such as API calls, database writes, or external actions. RASSG addresses this gap by formalizing a survival-gating protocol that treats tool execution as a risk-managed process rather than a fire-and-forget operation.

## Implications
For practitioners building voice-driven agentic systems, RASSG provides a concrete, implementable protocol with open-source code and evaluation data that can be integrated into existing streaming pipelines to dramatically reduce harmful stale executions without sacrificing responsiveness. The approach signals a broader shift in the field toward treating tool execution as a gated, cancellable process governed by calibrated risk models, which is critical for any deployment where tool side effects are irreversible—such as financial transactions, medical record updates, or infrastructure provisioning—where a single erroneous call can cause lasting damage.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.14659v1)
