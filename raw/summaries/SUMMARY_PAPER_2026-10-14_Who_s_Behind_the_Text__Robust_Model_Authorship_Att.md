---
title: Who's Behind the Text? Robust Model Authorship Attribution
url: http://arxiv.org/abs/2610.19583v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_04-54-35Z_Who_sBehindtheText_RobustModelAuthorshipAttributio.md
generated_at: 2026-10-14 21:56
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces ATLAS (Authorship Tracing via Likelihood-based Attribution of Sources), a method for Model Authorship Attribution that identifies which large language model generated a given text by modeling source-conditioned text generation rather than directly predicting the source. The authors also present MAABench, a benchmark designed to evaluate attribution performance under out-of-distribution conditions such as unseen domains and future model versions. ATLAS consistently outperforms existing baselines, achieving 74.27% accuracy under combined domain and version shifts, and can additionally identify teacher models in distillation pipelines.

## Key Takeaways
- ATLAS reformulates MAA as a likelihood-based comparison problem: instead of training a classifier to directly predict which model produced a text, it learns how text from each source model family is generated and then attributes a query text by comparing its token-level likelihood under each learned source condition. This source-conditioned modeling approach is fundamentally more robust to distribution shifts than direct classification.
- The method aggregates likelihood evidence at the token level with clipping, ensuring that no single anomalous token dominates the attribution decision. This token-level aggregation with clipping provides stability against noisy or unusual tokens that could otherwise skew the attribution toward an incorrect source model.
- MAABench is introduced as a broad evaluation benchmark specifically targeting practical out-of-distribution scenarios, including shifts in generation domain and model version. Under combined domain and version shifts, ATLAS achieves 74.27% accuracy, surpassing the strongest existing baseline by 9.00 percentage points. Additionally, ATLAS successfully recovers the known teacher model for every distilled model evaluated, demonstrating its utility beyond simple attribution.

## Context
As LLMs proliferate across academic writing, software development, journalism, and cybersecurity, the ability to trace a text back to its generating model has become a critical component of AI governance and safety infrastructure. Existing attribution methods rely on direct source prediction, which degrades sharply when encountering text from unseen domains or newer model versions that were not part of the training distribution. This paper addresses a fundamental gap in the attribution literature by shifting the paradigm from discriminative classification to generative likelihood modeling, aligning MAA more closely with how language models actually produce text.

## Implications
For practitioners in academic integrity enforcement, AI safety auditing, and model provenance tracking, ATLAS offers a more reliable attribution tool that remains effective when model families evolve or when texts originate from domains not seen during training. For the broader AI research community, the ability to identify distillation teacher models through likelihood comparison provides a practical mechanism for auditing model lineage and ensuring transparency in model development pipelines. Industry stakeholders deploying LLMs at scale can leverage such attribution systems to detect unauthorized model usage, enforce licensing agreements, and strengthen accountability in AI-generated content pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.19583v1)
