---
title: Do Large Language Models Know Colombian Law? A Reliability Benchmark for the Colombian Legal System
url: http://arxiv.org/abs/2610.03639v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-02_17-27-41Z_DoLargeLanguageModelsKnowColombianLaw_AReliability.md
generated_at: 2026-10-04 21:38
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces the first expert-validated benchmark for evaluating large language model reliability specifically on the Colombian legal system, comprising 1,042 items across ten legal areas and three question formats. The authors evaluate 15 contemporary proprietary and open-weight models, finding that while some models achieve high accuracy on closed multiple-choice questions (up to 0.905), free-text legal correctness never exceeds 0.45 for any model, revealing a critical gap between apparent responsiveness and actual factual accuracy in legal reasoning.

## Key Takeaways
- There is a significant dissociation between answer relevancy and factual correctness (Spearman rho = -0.46), meaning models reliably sound responsive and well-structured while frequently being factually wrong. This pattern is particularly dangerous for non-expert users who may trust fluent-sounding legal answers without verifying their accuracy. Additionally, only about half of the legal norms models cite are correct, with the remainder being wrong or entirely non-existent, exposing a serious hallucination problem in legal citation.
- Closed-question accuracy and free-text correctness are strongly rank-correlated (rho = 0.94), meaning that cheap multiple-choice screening can predict model ranking but substantially overstates absolute reliability. This finding has practical implications for benchmark design: multiple-choice evaluations give a misleadingly optimistic picture of how well models perform on open-ended legal reasoning tasks where accuracy drops dramatically.
- Reliability varies systematically by legal area and follows an inverted-U pattern across question complexity, suggesting that neither the simplest nor the most complex questions yield the best model performance. An independent rubric-based LLM judge and blind human expert scoring both reproduce the free-text ranking (rho >= 0.88), validating the benchmark methodology and demonstrating that automated evaluation can reliably mirror expert judgment.

## Context
Most existing legal AI benchmarks focus on the United States legal system, leaving a substantial gap in understanding how LLMs perform in other national jurisdictions with distinct legal traditions, codes, and institutional frameworks. Colombia's civil-law system, with its own constitutional court jurisprudence, procedural codes, and regulatory frameworks, presents unique challenges that are not captured by US-centric evaluations. This paper addresses a broader concern in AI evaluation research: the assumption that model performance generalizes across legal systems, which this work demonstrates is not the case. The human-in-the-loop benchmark construction pipeline with multi-stage expert review also contributes a methodological template for building domain-specific legal benchmarks in other jurisdictions.

## Implications
For legal practitioners, educators, and policymakers in Colombia and similar jurisdictions, the findings indicate that current LLMs cannot be trusted for unsupervised legal tasks and require expert oversight before their outputs inform decisions, education, or research. For the AI industry, the results underscore the urgent need for retrieval-augmented generation and grounding in authoritative legal sources as a path toward higher reliability, rather than relying on parametric knowledge alone. For benchmark designers, the dissociation between closed-question performance and open-ended correctness warns against over-reliance on multiple-choice evaluations when assessing real-world legal utility, and the released construction pipeline offers a reproducible framework for extending similar evaluations to other national legal systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.03639v1)
