# Summary: 2026-08-07_17-02-02Z_ISeekYouinVideos_Identity_ConditionedQueriesforPer.md
Saved: 2026-08-09 23:10
Source: 2026-08-07_17-02-02Z_ISeekYouinVideos_Identity_ConditionedQueriesforPer.md
Model: None

---

## Summary  
The paper introduces Identity‑Conditioned Queries (ICQ), a novel paradigm for person‑centric video reasoning that requires models to jointly understand an input video and a reference image of the same individual, thereby enabling tasks such as identity grounding, behavior interpretation, and long‑horizon tracking. To operationalize this goal, the authors develop ISYV—a comprehensive solution consisting of a benchmark (ISYV‑Bench), a large training set (ISYV‑75K), and a model framework (ISYV‑Model) that learns to exploit video shots without additional annotations. Extensive experiments demonstrate that mainstream multimodal language models underperform on the benchmark, especially in cross‑domain matching and temporal reasoning, while ISYV‑Model achieves state‑of‑the‑art results. This work provides a unified task definition, scalable datasets, and actionable modeling insights for video tasks that hinge on personal identity.

## Key Contributions  
- [Finding 1] The ICQ task formulation bridges multimodal, multi‑source inputs with person‑centric reasoning by conditioning models on both video and reference images.  
- [Finding 2] ISYV‑Bench introduces a rigorously designed benchmark with six difficulty levels covering identity recognition to causal reasoning across 1,377 real‑world videos.  
- [Finding 3] The ISYV‑Model leverages shot‑level information implicitly through a novel training strategy, outperforming strong baselines and approaching closed‑source performance.

## Methodology  
The authors first constructed ISYV‑Bench by curating complex videos paired with question‑answer pairs, then built ISYV‑75K via automated annotation pipelines followed by multi‑stage verification and manual review to ensure high quality. For the model, they propose ISYV‑Framework that trains a multimodal language model to attend to informative video frames while conditioning on the reference image, without requiring explicit shot annotations. The training objective aligns the model’s representations with both visual identity cues and temporal dynamics.

## Results  
Experiments on ISYV‑Bench reveal that closed‑source MLLMs achieve modest gains (≈5 % absolute) over strong open‑source baselines but still lag in cross‑domain matching. ISYV‑Model reaches the highest F1 scores across all difficulty levels, with a 7 % relative improvement on long‑horizon tracking tasks compared to prior state‑of‑the‑art methods.

## Significance  
This work advances person‑centric video reasoning by providing a systematic task definition and scalable resources that enable researchers to evaluate and improve models on realistic identity‑driven scenarios. The results highlight the importance of conditioning on both visual and temporal cues, offering a path toward more robust, human‑aware video AI.

## Related Concepts  
- Identity grounding: linking an individual across modalities.  
- Person‑centric reasoning: tasks that depend on personal attributes.  
- Multimodal language models (MLLMs): systems integrating vision and text.  
- Shot‑level information: extracting salient frames for reasoning.  
- Long‑horizon tracking: maintaining object identity over extended video segments.
