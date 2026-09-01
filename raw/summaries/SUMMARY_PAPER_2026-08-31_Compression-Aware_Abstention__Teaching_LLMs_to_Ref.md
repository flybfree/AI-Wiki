---
title: Compression-Aware Abstention: Teaching LLMs to Refuse When KV-Compression Masks Remove Answer Evidence
url: http://arxiv.org/abs/2608.29934v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_18-02-15Z_Compression_AwareAbstention_TeachingLLMstoRefuseWh.md
generated_at: 2026-08-31 21:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a method for teaching large language models to abstain from answering when key‑value compression removes the evidence needed for correct responses. By training a lightweight LoRA adapter on examples labeled as confident or abstain based on survival masks, the model learns to produce answers only when supporting spans remain after compression. Experiments show a 97% reduction in hallucinations under prompt truncation while maintaining correct answers.

## Key Takeaways
- The method treats compression‑aware abstention as a conditional learning problem where the adapter outputs an answer only if evidence tokens survive KV‑cache eviction.
- Training on ~2.6K MuSiQue 2‑hop QA examples with survival masks reduces hallucinations by 97% compared to unaided models under prompt‑style truncation.
- Multi‑compressor training yields a 6–22× relative lift in performance for evidence‑retaining examples, indicating the learned policy is driven by content rather than length alone.

## Context
LLMs increasingly rely on KV‑cache compression to fit within memory limits, but this can degrade factuality when essential context is discarded. Prior work has explored prompt‑style abstention, which often over‑abstrains or ignores evidence loss. This study bridges that gap by aligning model behavior with the actual content of compressed tokens.

## Implications
For developers deploying LLMs in resource‑constrained settings, this approach offers a principled way to avoid hallucinations without sacrificing useful answers. It can be integrated into inference pipelines as a lightweight adapter, improving reliability when memory is limited and context is aggressively trimmed.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29934v1)
