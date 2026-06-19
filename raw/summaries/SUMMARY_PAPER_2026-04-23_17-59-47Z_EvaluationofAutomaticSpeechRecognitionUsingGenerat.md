---

title: Evaluation of Automatic Speech Recognition Using Generative Large Language Models
url: http://arxiv.org/abs/2604.21928v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-04-23_17-59-47Z_EvaluationofAutomaticSpeechRecognitionUsingGenerat.md
generated_at: "2026-06-11 10:27"
model: nvidia/nemotron-3-nano-4b

---


## Summary
The paper investigates how generative large language models can improve Automatic Speech Recognition evaluation beyond traditional Word Error Rate. It tests three methods on the HATS dataset and finds that decoder‑based LLMs outperform semantic metrics in agreement with human annotators.

## Key Takeaways
- The best decoder‑based LLMs reach 92–94 % agreement for hypothesis selection, far above the 63 % achieved by WER.  
- Semantic embeddings generated from these models perform as well as encoder‑only approaches.  
- Human evaluation shows that semantic metrics still lag behind LLM‑based agreement.

## Context
Traditional ASR evaluation relies on Word Error Rate, which ignores meaning and is often misaligned with human perception. Recent work explores embedding‑based or neural metrics to capture semantics more accurately.

## Implications
LLMs provide a scalable way to produce interpretable, meaning‑aware error assessments for ASR systems. Practitioners can leverage these models to refine training data and improve diagnostic feedback without costly manual annotation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2604.21928v1)
