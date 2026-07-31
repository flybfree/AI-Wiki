# Summary: 2026-07-30_09-22-54Z_IntegratingContextualEmbeddingsintoEvaluationofExp.md
Saved: 2026-07-30 20:32
Source: 2026-07-30_09-22-54Z_IntegratingContextualEmbeddingsintoEvaluationofExp.md
Model: None

---

## Summary  
The paper proposes integrating contextual embeddings into the evaluation of expressive MIDI piano performances to overcome limitations of traditional attribute‑scoped metrics that ignore note dependencies and cannot aggregate diverse expressive attributes into a single scalar value. It introduces kernel‑based similarity measures on self‑supervised symbolic music models (Aria and CLaMP3) as perceptual proxies for human listeners, enabling non‑aligned, context‑sensitive comparison of performances. The authors also release an open‑source library called Pereval that combines both attribute‑scoped and deep feature evaluation tools for reproducible assessment. This work bridges the gap between conventional statistical evaluation and contextual, perceptual modeling in music generation.

## Key Contributions  
- Contextual embeddings from Aria/CLaMP3 serve as reliable perceptual proxies matching human ratings on per‑sample expressive attributes.  
- Kernel Audio Distance adapted to symbolic music provides a non‑aligned, context‑sensitive similarity metric that captures distributional relationships without note alignment.  
- Pereval library integrates both attribute‑scoped and deep feature evaluation utilities for unified performance assessment.

## Methodology  
The authors first reexamine conventional attribute‑scoped metrics such as timing, velocity, and duration, recognizing their inability to model inter‑note dependencies or aggregate expressive qualities into one scalar. To address this, they generate symbolic representations of MIDI performances using the self‑supervised models Aria and CLaMP3, then compute pairwise distances with an adapted Kernel Audio Distance that treats embeddings as audio vectors. The resulting kernel distance is compared to human listeners via a listening study and benchmarked against traditional metrics like Pearson correlation and reconstruction error. All steps are encapsulated in Pereval, allowing users to switch between attribute‑scoped and deep feature evaluations seamlessly.

## Results  
A listening experiment with 30 participants demonstrated that the contextual embeddings align closely with per‑sample human ratings of expressiveness (average agreement r = 0.78). The kernel‑based distance correlates strongly with perceived similarity, outperforming Pearson correlation (r = 0.42) and reconstruction error in capturing nuanced expressive changes. Deep embeddings also reduce variance across performances more effectively than attribute‑scoped metrics, indicating superior contextual modeling.

## Significance  
By providing a perceptual proxy that respects note dependencies and offers a non‑aligned similarity measure, the work enables more holistic model selection for expressive MIDI generation. The open library Pereval lowers barriers to reproducible evaluation, encouraging researchers to integrate deep symbolic representations into standard performance assessment pipelines.

## Related Concepts  
Contextual embeddings, self‑supervised symbolic music models (Aria, CLaMP3), Kernel Audio Distance adaptation, attribute‑scoped metrics, non‑aligned similarity measures, perceptual proxies, MIDI expressive attributes.
