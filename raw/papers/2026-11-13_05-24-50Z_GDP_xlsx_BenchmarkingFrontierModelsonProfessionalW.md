---
title: GDP.xlsx: Benchmarking Frontier Models on Professional Workbooks
published: 2026-11-13T05:24:50Z
authors: Suhaas Garre, Sushant Mehta, Edwin Chen
url: http://arxiv.org/abs/2611.17766v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GDP.xlsx: Benchmarking Frontier Models on Professional Workbooks

## Abstract
We introduce GDP_xlsx, a benchmark of 70 realistic workplace requests written by professionals in 13 domains, each paired with an expert rubric of binary criteria and with the complete workbook or CSV file it refers to. Together the files hold 2.18 million populated cells, and the rubrics 791 criteria. Agents work in a container with spreadsheet tools, and an agentic judge that can open the file applies the rubric. Completeness and exclusivity criteria require set-valued answers to be found in full and with nothing extra. We rank models by strict pass@1, the share of attempts that meet every criterion. Across 20 model configurations, including frontier models from Google, Anthropic, and OpenAI, the top-scoring one, Gemini 4 Argon, passes only 38.3% of attempts, and the median score is 19.3%, leaving wide headroom. We release the evaluation harness and three public tasks; the other 67 are held out to protect the leaderboard from contamination.

## Metadata
- **Published**: 2026-11-13T05:24:50Z
- **Authors**: Suhaas Garre, Sushant Mehta, Edwin Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.17766v1)