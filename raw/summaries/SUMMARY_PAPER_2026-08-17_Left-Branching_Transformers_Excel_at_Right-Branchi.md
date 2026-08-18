---
title: Left-Branching Transformers Excel at Right-Branching Languages: Data Shapes Word Order Preferences in Language Models
url: http://arxiv.org/abs/2608.15129v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_09-03-10Z_Left_BranchingTransformersExcelatRight_BranchingLa.md
generated_at: 2026-08-17 21:38
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how decoder‑only language models learn word order biases across a wide range of artificial and natural languages. It finds that models show a left‑branching preference in synthetic languages, which does not match any known linguistic universal or human learning pattern, while in natural languages they develop a right‑branching subject‑verb‑object (SVO) bias as data scale increases.

## Key Takeaways
- Artificial languages trigger a left‑branching word order preference that is unrelated to natural language typology or human acquisition processes.  
- In natural languages, monolingual models initially show no base order bias but later favor SVO over SOV even though SOV is the most common order globally.  
- The observed SVO advantage correlates with higher resource levels and data quality rather than inherent word‑order properties.

## Context
This study highlights that language model biases are not fixed by architecture or linguistic theory but emerge from the specific datasets used to train them. It underscores a growing concern about how large‑scale training can amplify certain syntactic preferences, potentially skewing the representation of multilingual corpora.

## Implications
For practitioners, the findings suggest that data curation and resource allocation should be considered when evaluating model behavior across languages. The paper warns that widespread adoption of LLMs may gradually diminish linguistic diversity by reinforcing SVO‑biased patterns, especially for languages that support multiple word orders.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15129v1)
