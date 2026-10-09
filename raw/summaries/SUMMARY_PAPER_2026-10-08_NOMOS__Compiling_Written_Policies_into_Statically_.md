---
title: NOMOS: Compiling Written Policies into Statically Verified Tool-Call Gates for LLM Agents
url: http://arxiv.org/abs/2610.11030v1
type: paper-summary
date: 2026-10-08
source_paper: 2026-10-08_00-23-22Z_NOMOS_CompilingWrittenPoliciesintoStaticallyVerifi.md
generated_at: 2026-10-08 21:22
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
NOMOS is a four-pass compiler that translates natural-language policy documents into deterministic, statically verified tool-call gates for LLM agents, eliminating the need for per-action LLM verification or heavyweight formal solvers. The system demonstrates that naive policy compilation fails due to self-referential preconditions and missing argument references, but its schema-level static verification repairs or rejects a substantial fraction of candidate rules, dramatically reducing policy violations (from 66.3% to 2.6% on airline tasks) while achieving zero attack success rates on adversarial benchmarks.

## Key Takeaways
- Static verification using only tool-schema-level checks, without any theorem prover, constraint solver, or LLM verifier, is sufficient to repair or reject 37% of airline-domain and 13% of retail-domain candidate rules. Without this step, most naively compiled rules are inoperable because they block the very tool satisfying their own precondition or reference arguments the tool does not possess.
- On the τ²-bench evaluation, NOMOS gates reduce violations of reference-encoded clauses among state-changing tool calls from 66.3% to 2.6% in the airline domain and from 30.8% to 6.9% in retail, while significantly raising task success for multi-step tasks (2 to 4 steps). A 26-billion-parameter on-premise model (gemma-4-26B) produces compilations not significantly worse than hand-written rules or frontier-model-compiled rules, making the approach accessible without expensive API calls.
- On AgentDojo's banking suite, NOMOS achieves a zero attack success rate where nine distinct attack families collapse onto just three structural rules, outperforming shipped defenses. On the remaining three suites, attack success stays at or below 3.6%, attributable to goals with no tool call to govern or single writes admitted by a binding weaker than its clause. A second model, Llama-3.3-70B, reproduces the effect, confirming generalizability.

## Context
LLM agents increasingly operate in regulated domains such as banking, aviation, and retail, where compliance with written policies is mandatory. Existing defenses either require hand-coding rules by domain experts, querying an LLM verifier on every action (adding latency and cost), or translating policies through heavyweight formal methods that are brittle and domain-specific. NOMOS addresses a critical gap: it shows that a lightweight, deterministic compilation pipeline with schema-aware static checks can enforce policy compliance at inference time in microseconds, removing the runtime LLM verification bottleneck that plagues current agent safety architectures.

## Implications
For practitioners deploying tool-using agents in regulated industries, NOMOS offers a path to enforceable policy compliance without per-call LLM overhead, enabling compliance gates that run in microseconds on commodity hardware. The finding that a 26B open-weight model matches frontier-model compilation quality lowers the barrier for on-premise, privacy-preserving deployment. However, the domain-dependent benign-utility cost and the residual 3.6% attack success on non-banking suites indicate that practitioners must still audit compiled gates and accept that goals without tool-call surfaces remain outside the enforcement boundary.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.11030v1)
