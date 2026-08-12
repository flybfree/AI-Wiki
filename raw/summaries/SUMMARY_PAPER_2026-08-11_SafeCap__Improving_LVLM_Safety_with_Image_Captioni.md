---
title: SafeCap: Improving LVLM Safety with Image Captioning Reinforcement Learning
url: http://arxiv.org/abs/2608.10513v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_05-37-59Z_SafeCap_ImprovingLVLMSafetywithImageCaptioningRein.md
generated_at: 2026-08-11 22:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SafeCap, a reinforcement‑learning framework that aligns large vision‑language models by having them generate safety‑relevant image captions before answering questions. The approach improves aggregate safety scores across multiple benchmarks while preserving or enhancing vision utility. Experiments show gains of 3.7–19.0 points in safety average compared with existing methods.

## Key Takeaways
- SafeCap trains a policy model to first produce a caption that highlights safety‑relevant visual cues and then generate an answer, optimizing the caption based on whether a frozen LLM reaches a safety‑aligned decision.  
- Across five multimodal safety benchmarks and six vision‑utility benchmarks, SafeCap raises safety performance by 3.7–19.0 points across four model settings while keeping vision utility comparable or better.  
- In controlled comparisons on matched backbones and data, SafeCap outperforms safety SFT, DPO, and SafeGRPO.

## Context
Multimodal models are increasingly deployed in real‑world applications where safety is paramount, yet they remain vulnerable to jailbreak attacks that exploit visual inputs. Traditional alignment techniques rely solely on textual supervision, which can miss important visual cues; thus, a method that leverages the model’s own caption generation offers a more holistic solution.

## Implications
Caption‑mediated reinforcement learning provides a scalable way to embed safety into vision‑language systems without sacrificing performance, encouraging broader adoption in industry and research. Practitioners can leverage this technique to build robust models that understand both text and images, reducing the risk of harmful outputs while maintaining utility.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10513v1)
