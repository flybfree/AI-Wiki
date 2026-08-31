---
title: FinExam-10K: When Retrieval Helps Financial Reasoning?
url: http://arxiv.org/abs/2608.28155v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_10-16-14Z_FinExam_10K_WhenRetrievalHelpsFinancialReasoning.md
generated_at: 2026-08-30 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces FinExam‑10K, the largest benchmark of English financial reasoning questions covering CFA Levels I–III and FRM Parts I–II, to evaluate how retrieval methods improve model performance. Across 17 models, the best accuracy is 85.29 % overall, but on the harder Full‑Coverage Track only 34.68 % is achieved; a gate that triggers FunctionGraph‑RAG improves recall from 70.83 % to 71.23 % (p = .0446).

## Key Takeaways
- The benchmark separates full coverage from context‑complete reasoning, revealing that many models fail on the latter despite high overall scores.  
- Function‑based retrieval methods such as FunctionRAG and FunctionGraph‑RAG reduce errors but also introduce new mistakes, yielding little net gain when used unconditionally.  
- A simple gate trained only on public data can selectively invoke FunctionGraph‑RAG for a minority of questions, boosting accuracy by 0.4 % with statistical significance.

## Context
Financial reasoning benchmarks are scarce because exams blend calculation, domain knowledge, and judgment in ways that standard language models cannot capture. This work fills that gap by providing a comprehensive dataset and leaderboard to guide research on retrieval‑augmented financial QA systems.

## Implications
For practitioners developing exam‑style AI assistants, the findings suggest that selective use of specialized retrieval tools can modestly improve performance without sacrificing overall correctness. The benchmark also offers a reliable metric for future progress, encouraging investment in domain‑specific grounding and conditional reasoning mechanisms.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28155v1)
