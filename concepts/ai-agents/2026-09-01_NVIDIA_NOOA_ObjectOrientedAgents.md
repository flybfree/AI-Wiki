---
title: "NVIDIA Object-Oriented Agents (NOOA)"
date: 2026-09-01
type: concept
tags: [ai-agents, harness, python, orchestration, memory, evaluation]
sources: ["https://developer.nvidia.com/blog/six-agent-harness-capabilities-for-higher-model-performance/", "https://arxiv.org/abs/2607.20709", "https://www.marktechpost.com/2026/08/07/nvidia-ai-releases-nooa-an-object-oriented-python-framework/"]
confidence: medium
---

# NVIDIA Object-Oriented Agents (NOOA)

## Summary

NVIDIA Object-Oriented Agents (NOOA) is a model-agnostic, open-source research-preview framework that represents an AI agent as a single Python object. Methods define capabilities, fields hold explicit state, docstrings provide prompts, and type annotations define contracts that the runtime validates. Methods with normal bodies execute deterministic Python; methods whose body is `...` become LLM-driven agentic methods at runtime.

The central claim is that agent development should reuse familiar programming abstractions instead of scattering behavior across prompt templates, tool schemas, callbacks, and workflow graphs. This makes the agent surface easier to test, trace, review, version, and refactor, while giving coding models a programming interface that resembles the Python they already know.

## The six harness capabilities

NOOA combines six model-facing interface ideas on one Python surface:

1. **Typed input and output** — agent calls accept structured arguments and return values validated against Python types.
2. **Pass by reference** — large values remain live Python objects; the model receives a bounded preview rather than a full serialized dump.
3. **Code as action** — the model writes Python with normal loops, conditionals, library calls, and method calls instead of selecting only from a fixed tool menu.
4. **Programmable loop engineering** — orchestration, retries, delegation, and stopping logic can be ordinary Python written by developers or the model.
5. **Explicit object state** — durable typed state lives on the agent object rather than only in the conversation transcript.
6. **Model-callable harness APIs** — context blocks, event history, state rendering, and related harness operations are exposed through Pythonic APIs.

## Execution model

A NOOA class can mix deterministic and agentic methods. `PredictStrategy` supports single-shot typed classification or extraction with local retries after validation failures. `CodeActStrategy` provides an iterative Python REPL in which the model can inspect state, call helpers, execute code, and submit a typed result. The harness records events and validates the final return value before control goes back to the caller.

Context is organized into three regions:

- **Static blocks**: cacheable instructions and stable context.
- **Event history**: an append-only, typed execution trace.
- **Dynamic blocks**: re-rendered views of changing state at the end of the context.

This arrangement is intended to preserve cache reuse across turns. Pass-by-reference also keeps full tool results in the live execution environment, reducing prompt growth and the need for context compaction.

## Memory and state

NOOA includes an optional long-term memory subsystem that the agent curates through model-callable operations rather than relying only on automatic transcript summarization. Records can carry types, importance, tags, and typed relationships such as `supports`, `contradicts`, and `derived-from`. A reflection pass can merge duplicates, connect related records, distill episodes into insights, and prune obsolete information.

The store persists in a human-readable SQLite file, allowing inspection, backup, and review with ordinary tools. The design separates short-lived execution state from durable knowledge while allowing memories to refer to live agent state.

## Reported evaluations

The NVIDIA technical report describes capability tests and evaluations across software engineering, terminal work, cybersecurity, and interactive reasoning. Reported headline results include:

- **SWE-bench Verified**: 82.2% with GPT-5.5 using about 1.1M tokens and roughly 29 model calls per task in the cited comparison.
- **Terminal-Bench 2.0**: 73.0% at high effort in the cited comparison; the report also notes a higher result for another system at xhigh effort.
- **CyberGym L1**: 86.8% with GPT-5.5 with network access blocked and trajectory checks intended to prevent lookup-based cheating.
- **ARC-AGI-3**: 50.2% mean RHAE with GPT-5.5 and 85.1% with GPT-5.6-sol in the cited fleets, both under $20 per game. The example compresses a multi-agent world-modeling approach into one agent plus a 45-line skill.

These are reported research results, not independent verification. Performance depends on model, effort level, harness configuration, benchmark protocol, and evaluation date.

## Why it matters

NOOA makes the harness itself a first-class programming artifact. The practical implication is that reliability and efficiency may come from the interface around a model—state boundaries, typed contracts, executable control flow, context layout, memory, and termination checks—not only from selecting a stronger model.

The approach is especially relevant to coding agents, vulnerability-validation workflows, data-processing agents, and systems that need inspectable state and deterministic verification. It also provides a concrete implementation pattern for the broader [[concepts/ai-agents/harness-engineering-hub.md|harness engineering]] idea: keep semantic judgment in the model, but move exact rules, parsing, state transitions, and acceptance gates into code.

## Example shape

```python
class SupportAgent(Agent):
    order_db: OrderDB

    def is_refund_eligible(self, order: Order) -> bool:
        return order.delivered and order.days_since_delivery <= 30

    async def classify(self, message: str) -> TicketKind:
        ...

    async def triage(self, message: str, order: Order | None) -> Ticket:
        ...
```

The deterministic eligibility check is ordinary Python. The classification and triage methods are typed agentic boundaries implemented by the runtime. This keeps policy checks local, testable, and visible instead of depending on a prompt instruction alone.

## Safety and deployment caveat

NOOA can execute model-generated Python. NVIDIA describes its AST checks and module deny-lists as defense-in-depth measures, not as a security boundary. Generated code should run inside an OS-level isolation boundary such as a container, VM, or NVIDIA OpenShell. The project is presented as an experimental/research-preview surface, so production adoption should include its own security review, sandbox testing, dependency pinning, and benchmark validation.

## Source-specific notes

- The **NVIDIA technical blog** explains the six capabilities, memory design, benchmark claims, and practical framing.
- The **arXiv technical report** provides the formal programming model, loop and context design, framework comparison, capability tests, limitations, and evaluation methodology.
- **MarkTechPost** provides an independent secondary overview and emphasizes installation/deployment details, including the alpha/research-preview status and the need for OS-level isolation. Treat its benchmark and package-version claims as secondary reporting and verify them against the project release artifacts.

## Related Concepts

- [[concepts/ai-agents/harness-engineering-hub.md|Harness Engineering Hub]]
- [[concepts/ai-agents/ai-agents-lesson-02-harness-implementing-an-agent.md|AI Agents Lesson 2: The Harness: Implementing an Agent]]
- [[concepts/ai-agents/ai-agents-lesson-03-planning-memory-and-state.md|AI Agents Lesson 4: Planning, Memory, and State]]
- [[concepts/ai-agents/ai-agents-lesson-05-guardrails-evaluation-and-reliability.md|AI Agents Lesson 6: Guardrails, Evaluation, and Reliability]]
- [[concepts/self-improving-ai-loops/2026-06-10_Lesson7_Orchestration.md|Lesson 7: Orchestration and UI]]
- [[concepts/ai-benchmarks/AIBenchmarks.md|AI Benchmarks]]

## Processed URLs

- https://developer.nvidia.com/blog/six-agent-harness-capabilities-for-higher-model-performance/
- https://arxiv.org/html/2607.20709v1
- https://www.marktechpost.com/2026/08/07/nvidia-ai-releases-nooa-an-object-oriented-python-framework/
- https://github.com/NVIDIA-NeMo/labs-OO-Agents
- https://arxiv.org/abs/2607.20709
