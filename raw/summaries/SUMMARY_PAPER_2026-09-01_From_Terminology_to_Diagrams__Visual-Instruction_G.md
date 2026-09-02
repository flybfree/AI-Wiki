---
title: From Terminology to Diagrams: Visual-Instruction Generation for Scientific Diagram Understanding
url: http://arxiv.org/abs/2609.00948v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_09-07-31Z_FromTerminologytoDiagrams_Visual_InstructionGenera.md
generated_at: 2026-09-01 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SciGram, a dataset of scientific diagrams paired with multimodal instruction data generated from curriculum terminology. Fine‑tuning vision‑language models on this data improves performance on diagram‑centric benchmarks and enables new state‑of‑the‑art results when combined with LLaVA OneVision.

## Key Takeaways
- The framework extracts domain concepts, creates atomic facts, retrieves web diagrams, and produces captions plus multiple‑choice questions to generate large‑scale instruction data.  
- SciGram contains 194K diagrams and 1.4M visual instructions across life, earth, and physical sciences, enabling strong performance with fewer training instances than existing methods.  
- Fine‑tuned models on SciGram match or surpass state‑of‑the‑art VQA systems while using less data.

## Context
Scientific diagram understanding remains a bottleneck for vision‑language models that excel on natural images. Most datasets lack functional meaning and are not aligned with curricula, limiting progress in STEM reasoning tasks.

## Implications
The approach shows that terminology‑driven instruction generation can boost scientific VQA without massive labeled data, offering a scalable path for researchers and developers seeking reliable diagram comprehension tools.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00948v1)
