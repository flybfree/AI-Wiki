---
title: Scoring Both Directions: LLMs realize the MRS they cannot reliably parse
url: http://arxiv.org/abs/2609.30071v1
type: paper-summary
date: 2026-09-27
source_paper: 2026-09-24_16-27-54Z_ScoringBothDirections_LLMsrealizetheMRStheycannotr.md
generated_at: 2026-09-27 16:16
model: qwen3.6-35b-a3b
---

## Summary
This study evaluates the bidirectional capabilities of large language models on Minimal Recursion Semantics (MRS), a formal graph-based representation of English sentence meaning. While Claude Opus and Sonnet demonstrate strong few-shot performance in generating natural text from MRS graphs, they significantly underperform traditional parsers when tasked with deriving MRS from text. The findings reveal a critical asymmetry between surface-level generation fluency and structural semantic understanding.

## Key Takeaways
- When provided with three examples, Claude Opus achieves a 76.3 BLEU score in the MRS-to-text direction, outperforming sequence-to-sequence models trained on tens of thousands of pairs and matching systems trained on nearly a million additional examples without any task-specific fine-tuning.
- In the reverse parsing direction (text to MRS), both LLMs struggle considerably, achieving F1 scores of 65.5 and 57.2 respectively, compared to the traditional ACE parser’s 91.0, with exact matches occurring on only about

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.30071v1)
