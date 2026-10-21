---
title: Evaluating Context Compaction on the Questions That Come Later
url: http://arxiv.org/abs/2610.27301v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-19_21-15-56Z_EvaluatingContextCompactionontheQuestionsThatComeL.md
generated_at: 2026-10-20 21:00
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper evaluates how context compaction methods used by language-model agents perform not only on the question they were designed for, but also on subsequent questions that rely on the same compacted context. Using four corpora with annotated evidence and recorded agent trajectories, the authors find that sentence-selection methods tuned for a current question provide no detectable advantage over random deletion when evaluated on later questions, while question-agnostic word-level compaction (LLMLingua-2) significantly outperforms random sentence deletion. The study demonstrates that compaction quality metrics tied to a single question are unreliable predictors of downstream utility.

## Key Takeaways
- Sentence-selection methods optimized for the current question (e.g., using gpt-6-luna via the OpenAI Decisions API) boost accuracy on that question by 11.4 points at 25% token retention on MultiRC, but on later questions no such method outperforms random sentence deletion, revealing a fundamental misalignment between per-question optimization and multi-question utility.
- LLMLingua-2, which performs word-level deletion without conditioning on the question, beats random sentence deletion by 12.5 points on later MultiRC questions at the same token budget. It retains roughly twice the share of evidence content words compared to random deletion, and when content-word retention is equalized, its advantage narrows to 7.3 points, suggesting much of its gain stems from preserving substantive content rather than structural coherence.
- Benchmark choice critically affects conclusions: on FEVER, label accuracy overstates what kept text actually supports, and sentence-selection gains vanish when answers are scored against the retained evidence. On Evidence Inference, sentence selection beats LLMLingua-2, while on τ-bench trajectories requiring exact identifiers for later tool calls, sentence selection beats random deletion but LLMLingua-2 shows no detected gain. This confirms that no single compaction strategy dominates across settings.

## Context
Language-model agents increasingly operate over long documents and multi-turn interactions, where context compaction is essential to fit within token budgets. Prior work has evaluated compaction quality primarily against the immediate task, assuming that preserving information relevant to the current query suffices. This paper challenges that assumption by systematically measuring compaction fidelity against future, unanticipated questions, bridging a gap between single-task evaluation and the realistic multi-query workflows agents encounter in production.

## Implications
For practitioners deploying agentic systems, this work warns that compaction strategies tuned for a single prompt may silently degrade performance on downstream queries, tool calls, or retrieval steps that depend on the same context window. It suggests that question-agnostic, content-preserving compaction methods like LLMLingua-2 may be safer defaults for multi-question pipelines, while task-specific sentence selection should be reserved for single-shot evaluations. The findings also highlight the need for benchmark designs that score against retained evidence rather than surface labels, pushing the field toward more rigorous evaluation protocols for context management in agent architectures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.27301v1)
