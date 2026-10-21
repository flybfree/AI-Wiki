---
title: DuplexLedger: Benchmarking Transactional Memory in Full-Duplex Speech Agents
url: http://arxiv.org/abs/2610.27581v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-20_03-47-06Z_DuplexLedger_BenchmarkingTransactionalMemoryinFull.md
generated_at: 2026-10-20 22:10
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
DuplexLedger is a bilingual benchmark of 1,094 persistent sessions designed to evaluate how full-duplex speech agents manage transactional memory—deciding which events to write, update, ignore, or retain—while simultaneously listening and speaking. The paper reveals a critical interaction-memory gap across five evaluated full-duplex models, where no system achieves both strong boundary control and coherent final-state memory, with the best fact coverage reaching only 2.01%. The authors then propose ACT-Mem, a lightweight 8.92M-parameter sidecar that improves latest-value accuracy from 4.11% to 8.68% on held-out sessions while reducing stale assertions and distractor adoption.

## Key Takeaways
- Existing benchmarks fail to connect interaction timing with memory outcomes, obscuring the state transitions that underlie correct answers. DuplexLedger addresses this by providing event-level Write/Update/Ignore/Retain supervision, explicit pre- and post-memory states, and 6,564 same-session questions and checks across four full-duplex scenarios, creating a granular evaluation framework that isolates memory behavior from conversational fluency.
- The evaluation of five full-duplex models exposes a fundamental interaction-memory gap: no system combines strong boundary control with coherent final-state memory. The best final-state fact coverage is a mere 2.01%, demonstrating that current full-duplex agents overwhelmingly fail to maintain accurate persistent memory across sessions, treating memory as an afterthought rather than a core architectural concern.
- ACT-Mem, composed of an event controller, a versioned transactional ledger, and a typed retriever coupled with a frozen MiniCPM-o 4.5 backbone, demonstrates that selective, auditable memory management is feasible. It nearly doubles latest-value accuracy (4.11% to 8.68%) and reduces stale assertions and distractor adoption, though it introduces a tradeoff by slowing interruption stopping, highlighting that memory governance and interaction responsiveness remain in tension.

## Context
Full-duplex speech agents represent the frontier of conversational AI, enabling simultaneous listening and speaking to mimic natural human dialogue. However, the field has largely focused on turn-taking latency, interruption handling, and fluency while neglecting persistent memory integrity across sessions. DuplexLedger fills a critical evaluation gap by formalizing memory state transitions as first-class benchmark targets, shifting the research conversation from "can the agent respond quickly?" to "does the agent remember correctly and selectively?" This aligns with broader trends in AI safety and reliability, where auditable state management is increasingly recognized as essential for deploying agents in real-world, multi-session environments.

## Implications
For practitioners building production speech agents, this work argues against indiscriminate transcript retention and in favor of selective, auditable memory architectures that explicitly track what should be stored, revised, or excluded. The interaction-memory gap identified across all five evaluated models signals that current full-duplex systems are not yet reliable for applications requiring persistent user context, such as customer service, healthcare consultations, or long-running personal assistants. The ACT-Mem sidecar approach suggests a practical path forward: augmenting frozen backbone models with lightweight transactional memory modules, though the interruption-stopping tradeoff indicates that further engineering is needed before these systems can be deployed at scale without degrading conversational responsiveness.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.27581v1)
