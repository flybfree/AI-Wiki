---
title: Prune the Summary, Not the History: Source-Judged Compaction for Long-Horizon Agents
url: http://arxiv.org/abs/2610.20927v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-14_20-57-32Z_PrunetheSummary_NottheHistory_Source_JudgedCompact.md
generated_at: 2026-10-15 22:28
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper identifies a critical failure mode in long-horizon LLM agents that rely on context compaction: when interaction histories exceed the context window, natural-language summaries replace them, but these summaries conflate environment-verified facts with the compressor's own speculative reasoning, creating hallucinated "facts" the agent later acts upon. The authors propose Source-Judged Compaction (SJC), a training-free post-processing step that uses a non-generative decision model (Jev) to score each summary entry for whether it traces back to actual environment outputs or a prior summary, pruning entries that lack such grounding. SJC yields 2.1%–8.9% reliability improvements on AppWorld and OfficeBench benchmarks without altering the agent, the compressor, or token budgets.

## Key Takeaways
- The paper demonstrates that 83% of failed agent runs in a widely used structured compressor trace back to actions executing specific summary entries that no environment output actually supports, revealing that compaction prompts requesting "decisions and next steps" systematically inject unverifiable reasoning into what the agent treats as factual history.
- SJC operates as a training-free, model-agnostic post-processing layer: it adds a single inexpensive judge request per compaction cycle, scores each summary entry with a calibrated probability of having a verifiable source in environment outputs or the previous summary, and removes entries falling below threshold, requiring no retraining of either the agent or the compressor.
- The judge component, Jev, is a non-generative decision model that outputs calibrated probabilities rather than free-form text, making the verification step computationally cheap and deterministic in its scoring behavior, while the method was validated across two different agent models on two distinct benchmark suites (AppWorld and OfficeBench).

## Context
Long-horizon autonomous agents—those performing multi-step tool use, code execution, or office automation tasks—inevitably exceed their context windows and depend on compaction mechanisms to maintain operational continuity. This paper addresses a previously underexplored failure mode within that pipeline: the epistemic contamination introduced when summarization prompts ask for forward-looking reasoning alongside factual recording. By framing the problem as one of source attribution rather than compression quality, the work connects to broader research on hallucination detection, retrieval-grounded generation, and agent reliability engineering, offering a lightweight intervention that complements existing approaches like retrieval-augmented generation or self-critique loops.

## Implications
For practitioners deploying production agents in software engineering, office automation, or multi-tool orchestration, SJC provides a drop-in reliability improvement that requires no model fine-tuning, no architectural changes, and negligible additional token cost, making it immediately applicable to existing agent stacks. For the research community, the finding that the majority of agent failures stem from unverifiable summary entries rather than from poor planning or tool-use errors redirects attention toward auditing and grounding intermediate representations, suggesting that future agent frameworks should treat compaction as a verification-sensitive operation rather than a purely lossy compression step.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.20927v1)
