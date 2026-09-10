---
title: Why Is Video Still So Expensive? A Survey of Inference-Efficiency Mechanisms in Video and Audiovisual LLMs
url: http://arxiv.org/abs/2609.10355v1
type: paper-summary
date: 2026-09-09
source_paper: 2026-09-09_15-50-39Z_WhyIsVideoStillSoExpensive_ASurveyofInference_Effi.md
generated_at: 2026-09-09 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary  
This paper surveys inference-efficiency mechanisms for video and audiovisual large language models, focusing on how they reduce computation, memory, latency, or token count. It categorizes methods by pipeline stage and compares reported accuracy-cost trade-offs across studies. The authors highlight that these techniques collectively enable deployment in real-time and mobile settings.  

## Key Takeaways  
- Frame sampling reduces input length dramatically, cutting FLOPs and memory usage while preserving caption quality.  
- Modality encoding optimizations lower token count at the encoder level, decreasing LLM input size without accuracy loss.  
- Connector-level token reduction and LLM prefilling strategies improve decoding speed and latency for downstream tasks.  

## Context  
Video large language models have become central to multimodal AI research, yet their computational burden hampers practical deployment. This survey addresses that bottleneck by mapping existing efficiency techniques across the model pipeline.  

## Implications  
For practitioners, these insights guide hardware-aware design choices and resource allocation. For industry, they open pathways for affordable real-time video understanding on edge devices.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.10355v1)
