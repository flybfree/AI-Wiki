---
title: Deep Agentic Search for Repository-Level Code Question Answering: An Empirical Study
url: http://arxiv.org/abs/2608.01507v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_21-36-59Z_DeepAgenticSearchforRepository_LevelCodeQuestionAn.md
generated_at: 2026-08-03 23:33
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates two code‑agent strategies for answering questions that refer to entire software repositories: a semantic search approach and deep agentic search where a sub‑agent performs the retrieval in an isolated context window. On the SWE‑QA benchmark, deep agentic search achieved 46.2 % correct answers while semantic search reached 65.2 %, but it required roughly twice as many tokens to produce each answer. The authors also catalog every failure into a taxonomy that reveals a new failure class: handoff errors between planner and sub‑agent account for 41.8 % of wrong outputs.

## Key Takeaways
- Deep agentic search outperforms semantic search in correctness but at a higher computational cost, indicating a trade‑off between accuracy and efficiency.
- The taxonomy shows that the majority of failures stem from handoff problems, not from retrieval errors, highlighting a specific design weakness.
- Despite its benefits, deep agentic search may introduce hidden inefficiencies such as silent wrong answers that increase token usage.

## Context
Code agents must balance precise answer generation with low latency and minimal resource consumption. The emergence of large language models has enabled complex reasoning tasks like repository‑level question answering, yet prior work rarely quantifies the cost versus accuracy trade‑off or systematically analyzes failure modes beyond retrieval quality.

## Implications
For developers deploying code assistants, choosing between retrieval‑heavy and planning‑heavy architectures requires careful evaluation of both performance and token usage. The findings suggest that while deep agentic search is now preferred for its robustness, practitioners should monitor handoff reliability to avoid costly silent failures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01507v1)
