---
title: EmoRSS: Mitigating Emotion-Induced Over-Refusal in Large Language Models
url: http://arxiv.org/abs/2610.04998v1
type: paper-summary
date: 2026-10-05
source_paper: 2026-10-04_06-40-16Z_EmoRSS_MitigatingEmotion_InducedOver_RefusalinLarg.md
generated_at: 2026-10-05 22:19
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper identifies a previously overlooked phenomenon in large language models: emotional expressions in user prompts systematically increase refusal tendencies on benign requests, causing unnecessary over-refusal. The authors propose EmoRSS (emotion-guided refusal subspace steering), an activation-steering method that identifies refusal-sensitive layers via linear probes, constructs a refusal subspace from sparse autoencoder features, and applies a reverse-direction activation intervention at inference time to reduce over-refusal while preserving appropriate refusal behavior on genuinely harmful requests.

## Key Takeaways
- Emotional expressions in prompts trigger a measurable shift in model activations that increases refusal rates even on benign, harmless requests. Prior research focused on how emotions facilitate attacks under harmful queries, but this work reveals that the same emotional cues systematically inflate refusal behavior on safe queries, creating a significant usability problem for emotionally expressive users.
- EmoRSS operates through a three-stage pipeline: first, layer-wise linear probes identify which transformer layers are most sensitive to refusal decisions; second, sparse autoencoder (SAE) features aligned with the probe direction define a low-dimensional refusal subspace; third, paired regular and emotional prompts with identical queries are used to estimate the mean activation shift in those SAE features, which is then decoded into an intervention vector applied in the reverse refusal direction during inference without any backbone parameter updates.
- Experiments on two LLMs demonstrate that EmoRSS achieves a more favorable trade-off between refusing harmful requests and answering benign ones compared to prior over-refusal mitigation baselines, while better preserving general task performance, indicating that targeted activation steering can decouple emotional sensitivity from safety refusal without retraining.

## Context
Safety alignment in LLMs has become a central concern as these models are deployed in consumer-facing applications where users express themselves with varying emotional intensity. Existing alignment techniques such as RLHF and constitutional AI tend to produce models that are overly cautious, and prior over-refusal mitigation work has largely treated emotional expression as a factor that helps models detect harmful intent. This paper shifts the paradigm by showing that emotional cues are a double-edged sword: they can help flag harmful content but simultaneously trigger spurious refusals on safe content, revealing a gap in the safety alignment literature that directly affects user experience for emotionally expressive populations.

## Implications
For practitioners deploying LLMs in customer service, mental health support, creative writing assistance, and educational tutoring, emotion-induced over-refusal represents a practical failure mode that degrades trust and usability for users who naturally express frustration, sadness, or excitement in their prompts. EmoRSS offers a parameter-free, inference-time intervention that can be integrated into existing model serving pipelines without costly retraining, making it attractive for production systems where safety guardrails must remain intact while reducing false-positive refusals. More broadly, the work suggests that interpretability tools like sparse autoencoders can be leveraged not just for understanding model behavior but for surgically editing specific behavioral tendencies, opening a path toward more granular and controllable safety alignment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.04998v1)
