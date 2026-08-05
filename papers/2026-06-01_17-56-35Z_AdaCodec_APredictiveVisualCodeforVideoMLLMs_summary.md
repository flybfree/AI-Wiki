---
title: "Summary: 2026-06-01_17-56-35Z_AdaCodec_APredictiveVisualCodeforVideoMLLMs.md"
date: 2026-06-01
tags: ['paper', 'research', 'ai']
---
# Summary: 2026-06-01_17-56-35Z_AdaCodec_APredictiveVisualCodeforVideoMLLMs.md


**Source**: [Original Paper](http://arxiv.org/abs/2606.02569v1)
Saved: 2026-06-01 23:01
Source: 2026-06-01_17-56-35Z_AdaCodec_APredictiveVisualCodeforVideoMLLMs.md
Model: None

---


## Summary  
Video multimodal large language models (video MLLMs) currently treat each sampled frame as an independent RGB image, leading to redundant visual tokens that repeat content already present in earlier frames. The authors propose a “predictive visual code” called AdaCodec that sends a full reference frame only when the scene cannot be predicted well from prior context and otherwise transmits compact P‑tokens describing inter‑frame changes such as motion and prediction residuals. This approach reduces token waste while preserving visual fidelity across long videos. Experiments show that AdaCodec achieves comparable or better performance than per‑frame RGB baselines under a fixed visual‑token budget.

## Semantic links
- [[concepts/papers/2026-06-17_17-51-50Z_Reference_DrivenMulti_SpeakerAudioSceneGene_summary.md|Summary: 2026-06-17_17-51-50Z_Reference_DrivenMulti_SpeakerAudioSceneGenerationf.md]] — 3 title terms overlap; shared tags: ai, paper, research; 9 summary/topic terms overlap
- [[concepts/papers/2026-06-11_17-56-35Z_EurekAgent_AgentEnvironmentEngineeringisAll_summary.md|Summary: 2026-06-11_17-56-35Z_EurekAgent_AgentEnvironmentEngineeringisAllYouNeed.md]] — 3 title terms overlap; shared tags: ai, paper, research; 9 summary/topic terms overlap
- [[concepts/papers/2026-06-10_17-59-54Z_Context_DrivenIncrementalCompressionforMult_summary.md|Summary: 2026-06-10_17-59-54Z_Context_DrivenIncrementalCompressionforMulti_TurnD.md]] — 3 title terms overlap; shared tags: ai, paper, research; 9 summary/topic terms overlap

## Key Contributions  
- [Finding 1] A predictive visual code can replace full RGB frames with compact inter‑frame descriptors when the scene is predictable, reducing token redundancy.  
- [Finding 2] AdaCodec dynamically decides whether to use a reference frame or encode changes as P‑tokens based on a conditional predictive cost.  
- [Finding 3] The method improves both accuracy and speed of video MLLMs across multiple benchmarks while using up to one‑seventh the visual token budget.

## Methodology  
The authors build AdaCodec by integrating it into existing video MLLM pipelines. For each frame, they compute a predictive cost that estimates how well the current scene can be inferred from earlier frames. If the cost is high, a full RGB reference frame is encoded as a visual token; otherwise, motion and residual information are compressed into P‑tokens. The resulting sequence of visual tokens replaces the original per‑frame RGB images while preserving the model’s ability to attend to relevant visual content.

## Results  
Across eleven benchmark datasets, AdaCodec outperforms the Qwen3‑VL‑8B per‑frame RGB baseline when using a matched visual‑token budget. Even at 1/7 of that budget, AdaCodec with 32k tokens surpasses the 224k‑token baseline on all long‑video benchmarks. On five general‑video datasets it raises average scores and cuts time‑to‑first‑token from 9.26 seconds to 1.62 seconds.

## Significance  
AdaCodec demonstrates that video MLLMs can achieve high visual quality with far fewer tokens, enabling more efficient inference for long videos. By eliminating unnecessary full‑frame encoding, the method reduces computational load and latency, making large‑scale video generation more practical and scalable.

## Related Concepts

- [[concepts/llm-models/llm-models-hub.md|LLM Models Hub]]
- [[concepts/evaluation-benchmarks/evaluation-benchmarks-hub.md|Evaluation Benchmarks Hub]]
- [[concepts/multimodal-ai/multimodal-ai-hub.md|Multimodal AI Hub]]
- [[concepts/training-optimization/training-optimization-hub.md|Training Optimization Hub]]
