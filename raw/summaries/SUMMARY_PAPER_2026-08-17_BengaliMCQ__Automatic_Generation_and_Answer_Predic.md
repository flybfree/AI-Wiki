---
title: BengaliMCQ: Automatic Generation and Answer Prediction of Academic Multiple-Choice Questions in a Low-Resource Language
url: http://arxiv.org/abs/2608.15547v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_05-44-52Z_BengaliMCQ_AutomaticGenerationandAnswerPredictiono.md
generated_at: 2026-08-17 21:33
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a structure‑aware retrieval‑augmented generation (RAG) framework designed to generate and predict answers for academic multiple‑choice questions in Bengali, a low‑resource language. By modeling textbooks as hierarchical graphs and using a contrastively trained graph neural network, the system retrieves focused passages that improve topic‑specific MCQ generation and answer prediction.

## Key Takeaways
- The model treats Bengali textbooks as hierarchical graphs rather than flat documents, allowing it to capture the logical structure of content and retrieve only the most relevant sections.  
- A contrastively trained graph neural network is used to pull a small set of passages that serve as focused context for a large language model, enabling precise MCQ generation and answer prediction.  
- Experimental results show that the framework outperforms strong dense retrieval baselines on retrieval metrics, produces more relevant MCQs, and achieves higher answer‑prediction accuracy.

## Context
Current RAG approaches often ignore document hierarchy, leading to suboptimal performance in languages with limited training data such as Bengali. This work addresses that gap by integrating structural information into the retrieval process, which is crucial for low‑resource language AI systems seeking reliable question generation.

## Implications
For educators and developers working on multilingual educational tools, this framework offers a scalable way to produce high‑quality MCQs without extensive annotated data. It also demonstrates how graph‑based modeling can enhance LLM performance in resource‑constrained settings, encouraging broader adoption of hierarchical RAG techniques across low‑resource languages.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15547v1)
