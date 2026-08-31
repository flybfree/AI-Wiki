---
title: CNeo-Bench: Diagnosing Large Language Models on Chinese Neologisms
url: http://arxiv.org/abs/2608.28053v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_08-17-30Z_CNeo_Bench_DiagnosingLargeLanguageModelsonChineseN.md
generated_at: 2026-08-30 20:07
model: nvidia/nemotron-3-nano-4b
---

## Summary  
This paper introduces CNeo‑Bench, a benchmark of 4,759 Chinese neologisms that exploit phonetic substitution and visual character decomposition. Evaluating 18 large language models on definition generation and source‑form restoration tasks reveals that most models achieve below 40 % accuracy, highlighting a persistent gap in handling these unique linguistic forms.

## Key Takeaways  
- Models can produce correct definitions for many neologisms but often replace the original source form with a paraphrased equivalent during restoration tasks.  
- A systematic recognition‑manipulation gap appears across several subcategories where the model’s output is semantically accurate yet not syntactically faithful to the input.  
- Few‑shot prompting improves performance on 1,058 difficult items but does not eliminate a substantial portion of errors, indicating that prompting alone cannot fully resolve the challenge.

## Context  
Chinese neologisms represent a distinct linguistic phenomenon that is rarely mirrored in other language datasets, making them valuable for testing the robustness of multilingual models. This work contributes to the growing effort to create linguistically rich benchmarks that reflect real‑world usage patterns beyond standard corpora.

## Implications  
For developers, the findings suggest that current LLMs need more targeted training on phonetic and visual character manipulation rather than relying solely on general language exposure. Practitioners should consider integrating specialized data augmentation or fine‑tuning strategies to address the recognition‑manipulation gap in Chinese neologisms.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28053v1)
