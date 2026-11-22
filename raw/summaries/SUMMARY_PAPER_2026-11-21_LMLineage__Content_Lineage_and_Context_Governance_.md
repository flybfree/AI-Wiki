---
title: LMLineage: Content Lineage and Context Governance for LLM Agents
url: http://arxiv.org/abs/2611.22511v1
type: paper-summary
date: 2026-11-21
source_paper: 2026-11-17_10-05-59Z_LMLineage_ContentLineageandContextGovernanceforLLM.md
generated_at: 2026-11-21 21:40
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
LMLineage introduces an out-of-band attribution system that traces every output sentence produced by an LLM agent back to its supporting input spans with calibrated confidence scores, without needing white-box model access or extra inference passes. The paper further proposes a concept-drift micro compaction mechanism that surgically removes previously referenced documents once they are no longer actively used, rather than waiting for context-length limits to trigger blanket summarization. Evaluation across annotated Chinese web-QA cases and multi-turn sessions spanning three generator models demonstrates that window-level embedding similarity outperforms whole-document or lexical matching, and that per-turn attribution completes in approximately one second on a single GPU even as context grows to 40 turns.

## Key Takeaways
- Window-level embedding similarity is significantly better aligned with how LLMs paraphrase source material than whole-document similarity or lexical matching approaches. The greedy-window fast path achieves both faster execution and higher average accuracy compared to exhaustive line-matching, which suffers from a multiple-comparisons bias that inflates web recall at the expense of overall precision. This finding has practical consequences for any system attempting to build provenance chains over retrieved documents.
- The concept-drift micro compaction design operates conservatively, achieving zero percent false compaction in evaluation. It detects when previously used input documents have stopped being referenced in subsequent turns and surgically compacts only those drifted documents while preserving user instructions verbatim. Recall of drifted documents is bounded by the accuracy of the underlying attribution system, meaning the compaction mechanism inherits the strengths and limitations of the lineage metadata it depends on.
- Per-turn attribution completes in roughly one second on a single GPU and remains stable as context accumulates up to 40 turns, demonstrating that the system scales practically for real-world agent sessions. The approach requires no white-box access to model weights and no additional inference passes, making it deployable as an out-of-band governance layer over any LLM agent pipeline regardless of the underlying model architecture.

## Context
Interpretability research in AI has predominantly focused on understanding internal model weights, attention patterns, or activation circuits, leaving the agent's reasoning over multi-source retrieved context largely opaque. As LLM agents increasingly orchestrate information from web search, document retrieval, and multi-turn conversation, the question of which specific input spans justified a given output sentence becomes a governance and safety concern rather than a purely academic one. LMLineage addresses this gap by treating provenance tracking as an infrastructure-level capability that operates independently of the model, complementing existing interpretability efforts that target the model itself.

## Implications
For practitioners building production LLM agent systems, LMLineage offers a practical path to auditability and context hygiene without modifying model internals or adding inference overhead, which is critical for regulated industries, legal compliance, and enterprise deployments where output traceability is mandatory. The concept-drift compaction strategy also suggests a more surgical approach to context management that could reduce token costs and hallucination risk in long-running agent sessions, potentially influencing how agent frameworks handle memory and context window governance in future architectures. The companion patent filing signals that the lineage construction method is being positioned as a protectable infrastructure technique for commercial agent platforms.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.22511v1)
