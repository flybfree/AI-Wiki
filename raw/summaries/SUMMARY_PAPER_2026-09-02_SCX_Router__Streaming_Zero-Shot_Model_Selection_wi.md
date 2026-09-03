---
title: SCX Router: Streaming Zero-Shot Model Selection with a Decoder-KV Classifier and a Real-World Task Ontology
url: http://arxiv.org/abs/2609.02292v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_08-40-07Z_SCXRouter_StreamingZero_ShotModelSelectionwithaDec.md
generated_at: 2026-09-02 20:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SCX Router, a lightweight GLiClass‑based system that selects the optimal large language model for inference without generating any autoregressive text. The router assigns suitability scores to model labels using a decoder‑KV classifier and leverages a real‑world task ontology to guide selection, achieving higher speed‑cost‑quality trade‑offs than fixed models across multiple benchmarks.

## Key Takeaways
- The SCX Router uses a 0.6B parameter checkpoint that combines Qwen3’s decoder with a shallow bidirectional scorer, preserving only new dialogue turn key‑value pairs while evaluating candidate labels without expanding the persistent cache.  
- It predicts task type, difficulty, reasoning mode, and output length from the same model, supporting custom zero‑shot labels through a 23‑family, 115‑type, 345‑subtype ontology built on 30 domains.  
- Training separates request prediction from per‑task policies (eligibility, cost, cache reuse, safety) and the router outperforms mean candidate models with an aggregate top‑1 score of 0.707 versus 0.696 for the strongest fixed model.

## Context
The proliferation of diverse LLMs creates a need for task‑specific selection mechanisms that balance performance with computational constraints. This work addresses the challenge by integrating a lightweight classifier and a structured ontology, enabling automated routing without costly per‑task fine‑tuning.

## Implications
For developers deploying LLM services, SCX Router offers a practical way to improve user experience while reducing costs, as it selects models dynamically based on real‑world task characteristics. Practitioners can adopt this approach to build scalable inference pipelines that adapt to varying latency and safety requirements.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02292v1)
