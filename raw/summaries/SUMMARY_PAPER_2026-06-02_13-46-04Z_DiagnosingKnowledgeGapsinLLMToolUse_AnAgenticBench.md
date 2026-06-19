---

title: "Diagnosing Knowledge Gaps in LLM Tool Use: An Agentic Benchmark for Novel API Acquisition"
url: http://arxiv.org/abs/2606.03657v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-02_13-46-04Z_DiagnosingKnowledgeGapsinLLMToolUse_AnAgenticBench.md
generated_at: "2026-06-11 10:51"
model: nvidia/nemotron-3-nano-4b

---


## Summary
This paper introduces NovelAPIBench, a dynamic benchmark that automatically discovers novel APIs for large language models and evaluates their ability to use these functions. The study compares knowledge injection via retrieval with parametric adaptation across multiple models, tasks, and domains, revealing that the two methods are complementary rather than interchangeable.

## Key Takeaways
- Usage examples emerge as the strongest standalone signal for API usage, outperforming other diagnostic components in most cases.
- The optimal pairing of signature information with either retrieval or fine‑tuning depends on both domain type and model backbone, showing no one‑size‑fits‑all solution.
- Adding extra context such as source code can increase import‑path errors, indicating that over‑context may hinder performance.

## Context
Current AI systems often rely on static APIs that do not reflect real‑world library evolution, limiting their usefulness. Evaluating how models acquire and integrate new API knowledge is therefore crucial for advancing practical deployment of language models.

## Implications
For practitioners, the findings suggest a hybrid approach: use retrieval to supply up‑to‑date API content while fine‑tuning refines procedural integration. This complementary strategy can improve robustness across diverse codebases and reduce errors in real applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.03657v1)
