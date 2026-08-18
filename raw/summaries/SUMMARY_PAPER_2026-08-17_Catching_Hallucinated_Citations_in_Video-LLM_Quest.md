---
title: Catching Hallucinated Citations in Video-LLM Question Answering: A Self-Verification Pipeline and Verifier Ablation Study
url: http://arxiv.org/abs/2608.15574v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_06-42-11Z_CatchingHallucinatedCitationsinVideo_LLMQuestionAn.md
generated_at: 2026-08-17 21:33
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the problem of deceptive timestamped claims in video-language question answering where models cite frames that do not support the answer. The authors introduce a self‑verification pipeline that re‑examines each cited frame and reports whether it truly backs up the claim, achieving 79 % detection on adversarial false‑premise questions while preserving true answers.

## Key Takeaways
- A retrieval‑augmented language model drafts answers with per‑claim timestamp citations, but the verification step is essential to prevent hallucinations.  
- Directly asking the vision model whether a frame supports a claim yields 0 % catch rate due to sycophancy bias.  
- Using a small natural language inference model as a verifier provides stable detection at 79 %, unlike unstable approaches that oscillate between 0 % and 100 %.

## Context
Video question answering systems rely on vision‑language models that generate timestamped citations to ground answers, but this design can mislead users by presenting false support. The field seeks methods that balance confidence with factual accuracy, especially as these models become integrated into consumer applications.

## Implications
Accurate verification is crucial for trustworthy AI products, preventing misinformation in educational and commercial settings. Practitioners can adopt lightweight NLI‑based checkers to improve reliability without heavy computational overhead, fostering safer deployment of multimodal systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15574v1)
