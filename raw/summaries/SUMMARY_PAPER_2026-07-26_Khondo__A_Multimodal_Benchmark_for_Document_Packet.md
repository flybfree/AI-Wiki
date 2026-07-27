---
title: Khondo: A Multimodal Benchmark for Document Packet Splitting of Bangla Forms
url: http://arxiv.org/abs/2607.21780v1
type: paper-summary
date: 2026-07-26
source_paper: 2026-07-23_19-52-58Z_Khondo_AMultimodalBenchmarkforDocumentPacketSplitt.md
generated_at: 2026-07-26 21:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Khondo, a multimodal benchmark for splitting concatenated Bangla government forms into their original documents. It focuses on vision-native models that process page images directly and evaluates zero-shot MLLMs across five concatenation schemes. The study finds that while clustering works well, ordering pages remains challenging, especially when packets are shuffled.

## Key Takeaways
- Khondo is the first bilingual Bangla‑English benchmark for document packet splitting where models work on raw page images rather than OCR text.
- Zero‑shot MLLMs can group pages into correct documents but often fail to restore the original sequence when concatenation order is shuffled, indicating ordering as a dominant difficulty.
- English packets are ordered more reliably than Bangla ones, suggesting language influences the task and that explicit page‑order instructions are necessary but not sufficient.

## Context
Vision‑based document understanding remains limited for low‑resource languages because most existing datasets rely on OCR text. Khondo addresses this gap by providing a vision‑native dataset that can be used to test multimodal models directly on images, which is crucial for real‑world forms where OCR accuracy varies.

## Implications
For practitioners developing automated form processing systems, Khondo highlights the need to prioritize page ordering in multimodal pipelines. The benchmark also offers a controlled way to measure progress toward solving this problem, guiding research and deployment efforts in low‑resource administrative contexts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21780v1)
