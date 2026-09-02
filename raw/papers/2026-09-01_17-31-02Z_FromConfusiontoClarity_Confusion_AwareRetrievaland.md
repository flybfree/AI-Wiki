---
title: From Confusion to Clarity: Confusion-Aware Retrieval and Knowledge Injection for Text Classification
published: 2026-09-01T17:31:02Z
authors: Manish Gupta, Chaitanya Giri, Jayasimha Talur
url: http://arxiv.org/abs/2609.01564v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Confusion to Clarity: Confusion-Aware Retrieval and Knowledge Injection for Text Classification

## Abstract
Large language models (LLMs) struggle to classify text into taxonomies with many semantically similar labels, as the distinctions are domain-specific and not captured by pre-training. To handle large label spaces, a common approach retrieves top-$K$ candidate labels by embedding similarity and prompt the LLM to choose among them. However, top-$K$ retrieval reduces the number of candidates but does not help the model tell similar ones apart. When two similar labels both appear as candidates, the model lacks the signal to choose correctly between them. We propose a framework that (1) identifies which label pairs the model struggles to distinguish, (2) expands the candidate set to include confusable labels, and (3) generates targeted rules to differentiate between similar candidates. The framework requires no fine-tuning, and the generated rules transfer to smaller, cheaper models. On three benchmarks (WOS, Flipkart, LEDGAR), our approach improves Macro F1 by up to 10.0pp over retrieval baselines, with smaller models (2B--20B) gaining up to 11.5pp via cross-model transfer.

## Metadata
- **Published**: 2026-09-01T17:31:02Z
- **Authors**: Manish Gupta, Chaitanya Giri, Jayasimha Talur
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01564v1)