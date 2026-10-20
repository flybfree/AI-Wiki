---
title: Can Agents Keep Secrets They Were Never Told? Benchmarking Latent Privacy Risks Across Sessions with MemJoin
url: http://arxiv.org/abs/2610.24359v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-17_01-20-36Z_CanAgentsKeepSecretsTheyWereNeverTold_Benchmarking.md
generated_at: 2026-10-19 20:44
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces MemJoin, a privacy benchmark comprising 288 synthetic analysis cases designed to test whether AI agents with long-term memory inadvertently reveal sensitive personal relations that were never explicitly stated in any single session. The authors evaluate six memory systems and demonstrate that cross-session memory combination can expose complete, person-linked sensitive relations even when each individual session appears innocuous, revealing a critical gap in how privacy risks are currently assessed in agent memory systems.

## Key Takeaways
- MemJoin constructs 288 synthetic cases where the complete interaction history entails a sensitive relation, but every individual session is insufficient on its own to reveal it. This design isolates the risk that arises specifically from cross-session memory aggregation, a scenario that existing single-session privacy evaluations fail to capture.
- The evaluation framework separates two distinct checks: whether target attribute values appear in stored records and retrieved context, and whether the final answer states the complete, person-linked relation. A paired test on a prespecified subset shows that removing shared identifiers and connecting clues can prevent the complete-relation output while all checked attribute values remain visible, proving that attribute-level visibility checks are insufficient for evaluating what records from different sessions reveal together.
- Six memory systems were evaluated using the same answer-generating model alongside full-history and no-history controls, with each system writing and updating memories in session order and later retrieving context for an ordinary task. Target annotations remained with the evaluator, ensuring that the benchmark measures emergent privacy leakage rather than direct instruction-following.

## Context
As AI agents increasingly rely on long-term memory to deliver personalized, sustained interactions across multiple sessions, the privacy surface expands beyond what any single conversation contains. Existing privacy evaluations in the AI safety and agent-memory literature predominantly focus on whether sensitive data is stored or retrieved within a given session, leaving the combinatorial risk of cross-session inference largely unexamined. MemJoin addresses this gap by formalizing latent privacy risks that emerge only when multiple sessions are joined, a scenario that mirrors real-world deployments where agents accumulate user information over time.

## Implications
For practitioners building agent memory systems, this work demonstrates that current privacy auditing methods—which typically check whether individual attributes are visible in stored records—can miss the more consequential risk of reconstructing a complete sensitive relation from innocuous fragments across sessions. Industry teams deploying long-term memory in customer-facing assistants, healthcare agents, or enterprise copilots should adopt cross-session privacy stress-testing similar to MemJoin's design, ensuring that memory retrieval pipelines are evaluated not only for attribute leakage but for the emergent relational inferences they enable. This benchmark provides a concrete, reproducible methodology for such evaluation, setting a standard that future agent-memory systems will need to meet.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.24359v1)
