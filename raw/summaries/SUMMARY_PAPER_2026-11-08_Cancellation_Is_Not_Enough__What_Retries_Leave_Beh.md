---
title: Cancellation Is Not Enough: What Retries Leave Behind in an Overloaded LLM Engine
url: http://arxiv.org/abs/2611.08684v1
type: paper-summary
date: 2026-11-08
source_paper: 2026-11-05_20-43-38Z_CancellationIsNotEnough_WhatRetriesLeaveBehindinan.md
generated_at: 2026-11-08 21:40
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates why propagating cancellation signals to an overloaded LLM inference engine (specifically vLLM) fails to restore service after a transient overload, even when incoming request rates fall below the engine's capacity. Through controlled overload experiments on three open models and detailed scheduler traces, the authors demonstrate that retries from clients and proxies create hidden computational work that cancellation alone cannot undo, leaving only 12–38% of post-overload calls successfully delivered.

## Key Takeaways
- Cancellation propagation, despite appearing to be the natural remedy for overloaded LLM engines, did not restore service in any experimental run. When retries were active, only 12–38% of calls arriving after the overload were actually delivered to clients, revealing a fundamental gap between the intent of cancellation and its practical effect on engine recovery.
- Scheduler traces revealed a critical timing problem: retries that vLLM executed typically began prefill computation less than half a second before timing out, meaning the engine had already consumed 79–85% of the prompt tokens for those executions before cancellation could abort them. Furthermore, vLLM's internal prompt-token counter undercounted one-third to one-half of all actually computed prompt tokens, meaning operators cannot even accurately measure the hidden cost that retries impose on the engine.
- Alternative overload controls produced mixed results: a retry budget restored service by shedding retries but still left many overload-era calls undelivered, while request coalescing successfully delivered every call from the overload onward (albeit some late) unless cancellation had already aborted the running execution. The authors argue that overload controls must be evaluated by the executions retries add to the engine and the calls clients actually receive, not merely by whether cancellation signals propagate.

## Context
LLM serving engines like vLLM are increasingly deployed behind clients, proxies, and orchestration layers that automatically retry timed-out requests, a pattern inherited from traditional microservice architectures. This paper matters because it exposes a mismatch between the assumptions of those retry mechanisms and the reality of LLM inference, where a single request can consume substantial GPU compute for prefill and decode phases. As LLM serving scales to meet growing demand, understanding how retry-induced phantom work prevents engine recovery becomes essential for designing robust serving infrastructure.

## Implications
For practitioners operating LLM serving stacks, this work warns that simply wiring cancellation propagation through proxies and clients is insufficient to recover from overload events; operators must account for the substantial prompt-token computation that retries trigger before timeouts fire. The findings suggest that production overload controls should incorporate retry budgets, request coalescing, or admission control at the engine level rather than relying on cancellation alone. For the broader field, the paper highlights that current engine telemetry (such as vLLM's prompt-token counter) may underreport actual compute consumption, complicating capacity planning and cost accounting for LLM serving at scale.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.08684v1)
