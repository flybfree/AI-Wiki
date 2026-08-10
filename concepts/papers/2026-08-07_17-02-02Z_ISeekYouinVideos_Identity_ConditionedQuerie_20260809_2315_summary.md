# Summary: 2026-08-07_17-02-02Z_ISeekYouinVideos_Identity_ConditionedQueriesforPer.md
Saved: 2026-08-09 23:15
Source: 2026-08-07_17-02-02Z_ISeekYouinVideos_Identity_ConditionedQueriesforPer.md
Model: None

---

## Summary  
The paper introduces Identity‑Conditioned Queries (ICQ) for person‑centric video reasoning, a task that requires models to jointly associate an input video with a reference image of a person and answer questions about identity grounding, behavior understanding, and temporal relations. By extending beyond the simplified video‑text paradigm, ICQ enables richer multimodal, multi‑source interactions that are essential for real‑world video analysis.

## Key Contributions  
- Introduces the ICQ task definition, which couples video and reference image conditioning to answer person‑centric queries.  
- Builds ISYV‑Bench, a 1,377‑sample benchmark with six difficulty levels ranging from identity recognition to causal reasoning.  
- Develops ISYV‑Framework, including a large training set (ISYV‑75K) and an ICQ‑oriented model that extracts informative video shots without extra shot‑level annotations.

## Methodology  
The authors first designed the ICQ task as a unified framework requiring simultaneous grounding of identity and temporal reasoning. To create ISYV‑Bench, they performed automated annotation on 1,377 real‑world videos, followed by multi‑stage verification and manual review to ensure quality. The resulting ISYV‑75K dataset supplies 75 k high‑quality samples for training. Training employs a multimodal large language model (MLLM) that conditions on both video frames and the reference image; the ISYV‑Framework automatically selects informative shots, avoiding the need for per‑shot annotations.

## Results  
Experiments on ISYV‑Bench show that mainstream closed‑source and open‑source MLLMs struggle significantly, especially in cross‑domain identity matching and long‑horizon tracking. The proposed ISYV‑Model outperforms strong baselines and approaches closed‑source performance in several sub‑tasks, demonstrating the effectiveness of ICQ conditioning.

## Significance  
This work bridges a critical gap between video reasoning and person‑centric applications, providing a scalable benchmark and modeling insights that go beyond simple video‑text setups. By enabling identity grounding and long‑horizon tracking with multimodal conditioning, ISYV advances research in real‑world video analytics.

## Related Concepts  
Identity‑grounding, multimodal reasoning, video‑text integration, MLLM (multimodal large language models), shot‑level conditioning, long‑horizon tracking, cross‑domain matching.
