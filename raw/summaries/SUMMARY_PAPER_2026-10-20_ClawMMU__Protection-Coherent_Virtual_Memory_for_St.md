---
title: ClawMMU: Protection-Coherent Virtual Memory for Stateful LLM Agents
url: http://arxiv.org/abs/2610.28093v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-20_12-09-53Z_ClawMMU_Protection_CoherentVirtualMemoryforStatefu.md
generated_at: 2026-10-20 22:14
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
ClawMMU introduces a protection-coherent virtual memory layer for stateful LLM agents that addresses a critical security gap in agent harnesses: the inability to distinguish between user-issued instructions and instructions embedded in fetched web pages or tool outputs. By labeling every piece of memory with its owner, scope, origins, and authority, ClawMMU enforces provenance-based access checks at every memory boundary—context entry, storage write, storage read, and tool invocation. The system's central invariant, that authority may only rise through explicit promotion and never self-lift, transforms memory-based attacks into classical protection faults that the harness can intercept regardless of whether the underlying model is semantically fooled.

## Key Takeaways
- Agent harnesses today do not record provenance or ownership of memory fragments accumulated from web pages, tool results, and prior interactions. This means an instruction hidden inside a fetched webpage can be silently promoted to the status of a user command, enabling prompt-injection and memory-poisoning attacks that bypass model-level defenses entirely.
- ClawMMU attaches structured labels—owner, scope, origins, and authority—to every memory unit and validates those labels at four critical checkpoints: when content enters the model's context window, when it is written to persistent storage, when it is retrieved from storage, and when it triggers a tool call. This makes the protection layer independent of the model's own reasoning.
- The system enforces a strict monotonic authority rule: information may be promoted to a higher authority level only through an explicit, auditable action, and no piece of content can elevate its own authority. Because enforcement is based on provenance metadata rather than semantic content analysis, adversarial text that fools the model still triggers a protection fault at the harness level, analogous to a hardware memory-access violation.

## Context
Stateful LLM agents that maintain long-term memory across sessions are increasingly deployed in production workflows involving web browsing, code execution, and multi-step tool use. The security literature has extensively studied prompt injection and indirect prompt injection, but most defenses operate at the model or prompt-engineering level, leaving the agent harness itself as an untrusted intermediary. ClawMMU reframes the problem from a natural-language-understanding challenge into a systems-security challenge, borrowing concepts from operating-system virtual memory protection and capability-based access control to build a harness-level enforcement layer that is orthogonal to model behavior.

## Implications
For practitioners building agent frameworks, ClawMMU suggests that robust memory security cannot rely solely on model alignment or input filtering; a provenance-tracking protection layer in the harness is necessary to guarantee that untrusted content never acquires user-level authority. For the broader AI safety and security community, the paper demonstrates that classical protection-fault mechanisms from systems research can be adapted to LLM agent architectures, offering a path toward formally verifiable guarantees about memory integrity even as models themselves remain susceptible to adversarial text. Industry deployments of autonomous agents in finance, healthcare, and legal domains stand to benefit from harness-level enforcement that does not depend on the model's ability to recognize adversarial instructions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.28093v1)
