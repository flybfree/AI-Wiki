---
title: When Text and Numbers Disagree: Evidence Arbitration in Large Language Models
url: http://arxiv.org/abs/2608.20116v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_14-48-30Z_WhenTextandNumbersDisagree_EvidenceArbitrationinLa.md
generated_at: 2026-08-20 21:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how large language models resolve conflicts between textual summaries and numerical data when they point to different conclusions. The authors create a synthetic benchmark that generates both types of evidence from the same latent risk trajectory, allowing precise control over modality, recency, reliability, and provenance. Their experiments reveal systematic biases: models often favor text over numbers, respond more strongly to recent information than to explicit reliability cues, and can incorrectly rely on external forecasts despite contradictory context.

## Key Takeaways
- Models show a consistent preference for textual evidence when it conflicts with numerical data, indicating a bias toward language rather than quantitative signals.  
- Temporal recency drives arbitration decisions more reliably than any stated reliability label attached to the source.  
- External forecast outputs can dominate model reasoning even when they clash with direct contextual information, revealing over‑reliance on auxiliary tools.

## Context
The study highlights a growing need for transparent evidence integration in AI systems that combine text and numbers, such as risk assessment or decision support tools. As LLMs become embedded in real‑world workflows, their heuristic arbitration can lead to systematic errors if not properly managed.

## Implications
For practitioners, the findings suggest that current open‑weight models must be evaluated for bias toward specific evidence modalities before deployment. Industry standards may need to incorporate explicit weighting mechanisms or debiasing strategies to ensure balanced reasoning across heterogeneous data sources.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20116v1)
