---
title: AfterDeleteBench: Auditing Post-Deletion Information Persistence in LLM Agents
url: http://arxiv.org/abs/2610.31366v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-22_14-41-36Z_AfterDeleteBench_AuditingPost_DeletionInformationP.md
generated_at: 2026-10-22 22:14
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
AfterDeleteBench introduces a controlled behavioral audit framework for evaluating whether information persists in LLM agents after the original memory record is deleted. The paper demonstrates that deleting a source record does not eliminate information carried by derived descendants such as summaries, and that fixed-weight agents like Qwen2.5-7B-Instruct can recover deleted secrets in roughly two-thirds of cases even when no verbatim copy survives. The authors further show that reconstruction succeeds in 62–99% of cases across multiple model families when only component fragments remain under a public composition rule, establishing that source deletion must be evaluated behaviorally at the agent-and-memory-system level rather than as a mere storage operation.

## Key Takeaways
- A single query recovers a deleted secret from Qwen2.5-7B-Instruct in approximately two-thirds of trials, while matched never-exposed control agents achieve zero recovery, confirming that post-deletion leakage is attributable to the original exposure rather than model priors or coincidence.
- Recovery does not require a surviving verbatim copy of the secret; when the complete string is absent and only separately stored components remain under a publicly known composition rule, exact reconstruction succeeds in 62–99% of cases across Qwen, Mistral, and Phi-3 model families, revealing that compositional reasoning in the agent's reasoning chain can reassemble deleted information from fragments.
- The response interface itself is part of the measurement system: target-bearing replies can be misclassified as failures when the requested output format and the evaluation parser are misaligned, meaning that benchmark design choices can artificially suppress or inflate apparent recovery rates. Additionally, provenance-aware closure eliminates observed recovery in tested positive-baseline settings, while an exact-literal write filter blocks reinsertion but cannot erase information already present in the agent's derived state.

## Context
This work addresses a critical gap in the evaluation of LLM agent memory systems, where the prevailing assumption is that deleting a record from a vector store or database constitutes a complete information-removal operation. In practice, agents generate summaries, embeddings, and derived state from original inputs, creating a dependency graph in which the original node may be removed while its descendants persist. As LLM agents increasingly serve as personal assistants, legal advisors, and enterprise knowledge workers handling sensitive data, the distinction between storage-level deletion and behavioral-level information erasure becomes a matter of regulatory compliance, user trust, and system safety. AfterDeleteBench provides the first controlled, matched-pair experimental protocol for isolating post-deletion leakage from confounding factors such as model memorization or prompt leakage.

## Implications
For practitioners building agentic systems with persistent memory, this research demonstrates that conventional delete operations on a knowledge store are insufficient to guarantee information removal; developers must audit the full derived-state graph and implement provenance-aware closure mechanisms that prevent compositional reconstruction from surviving fragments. For the broader AI safety and governance community, the findings underscore that data-deletion compliance under regulations such as GDPR or the EU AI Act cannot be satisfied by storage-layer operations alone, and that behavioral auditing frameworks like AfterDeleteBench should become a standard component of agent deployment pipelines before agents handle personally identifiable or legally sensitive information.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.31366v1)
