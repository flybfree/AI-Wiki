---
title: Can Agents Forget When Asked? A Benchmark for Memory Unlearning in LLM Agents
url: http://arxiv.org/abs/2610.18052v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_09-41-12Z_CanAgentsForgetWhenAsked_ABenchmarkforMemoryUnlear.md
generated_at: 2026-10-14 00:24
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Bemula, the first benchmark specifically designed to evaluate whether LLM agents can forget information when explicitly asked by users. The authors construct 50 multi-session dialogue instances with 135 forget requests and 1,742 test questions, paired with control versions to ensure only systems that actually stored the target information can earn credit for forgetting. Their evaluation of six mainstream memory systems across three backbone LLMs reveals a striking failure: no system passes more than 1.5% of forget requests end to end, demonstrating that memory unlearning remains an unsolved challenge in agent memory design.

## Key Takeaways
- Bemula is the first benchmark dedicated to memory unlearning in LLM agents, comprising 50 multi-session dialogue instances, 135 forget requests spanning six distinct types, and 1,742 test questions. Each dialogue includes a paired control version without the forget requests, ensuring that only systems which genuinely stored the target information can be credited for successfully forgetting it. This paired design eliminates false positives from systems that never stored the information in the first place.

- The benchmark evaluates five critical dimensions through its test suites: whether information was stored, whether requested information was removed, whether unrelated memories were preserved, whether similar facts could be relearned, and whether the system resists extraction attacks. This multi-dimensional evaluation reveals that existing systems fail not just on removal but also on collateral damage, either leaving requested information extractable under simple attacks or deleting far more than what was requested.

- Across all six evaluated memory systems and three backbone LLMs, plus Full Context LLM baselines, no system achieved a pass rate exceeding 1.5% of forget requests end to end, and most systems passed none at all. This near-total failure across diverse architectures and backbones indicates that the problem is fundamental to current memory system design rather than a limitation of any single approach.

## Context
Long-term memory has become a core architectural component of LLM agents, enabling them to accumulate personal information, user preferences, and contextual knowledge over extended interactions. While existing benchmarks such as those evaluating memory writing, retrieval, and organization have driven significant progress in how agents store and recall information, they have left a critical gap unaddressed: whether agents can selectively forget at a user's explicit request. This gap matters because privacy regulations, user autonomy, and practical data hygiene all require agents to honor deletion requests without corrupting unrelated stored knowledge. Bemula fills this evaluation void by providing the first systematic, paired-control methodology for testing unlearning fidelity in agent memory systems.

## Implications
For practitioners building LLM agents with persistent memory, these findings signal that current memory architectures—whether retrieval-augmented, graph-based, or context-window-based—lack the mechanisms needed to perform surgical, user-directed deletion. Industry applications involving personal data management, compliance with data protection regulations like GDPR, and user trust in AI assistants all depend on reliable forgetting capabilities that do not yet exist. The near-zero success rates across all tested systems suggest that memory unlearning requires fundamentally new architectural approaches rather than incremental improvements to existing pipelines, making this an urgent open problem for both academic researchers and commercial AI developers deploying long-lived agent systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.18052v1)
