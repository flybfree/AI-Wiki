---
title: Vela: User Behavior as Supervision Sparks LLM Intelligence
url: http://arxiv.org/abs/2610.14709v1
type: paper-summary
date: 2026-10-13
source_paper: 2026-10-10_08-28-00Z_Vela_UserBehaviorasSupervisionSparksLLMIntelligenc.md
generated_at: 2026-10-13 21:42
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Vela, a framework that leverages real-world user behavior data as a supervisory signal for training large language models, addressing the gap between static training data and the dynamic nature of user behavior. By converting anonymized behavior records from 100,000 users into trainable tasks and trajectories across 91 real-world task templates, the authors demonstrate that fine-tuning Qwen3.6-35B-A3B on these trajectories yields up to 11.5-point improvements on user-related tasks and 4-point average gains on general benchmarks, suggesting user behavior is a scalable and effective source of supervision for LLM intelligence.

## Key Takeaways
- Vela converts real user behavior records into structured trainable tasks and trajectories, generating 100,000 tasks across 91 real-world task templates from 100,000 anonymized users, with difficulty-based filtering and trajectory acceptance criteria retaining approximately 75,000 high-quality tasks for training, demonstrating a systematic pipeline for turning behavioral data into supervision.
- Fine-tuning Qwen3.6-35B-A3B on Vela-generated trajectories improves performance by up to 11.5 points on user-related tasks and an average of 4 points on general benchmarks, while reinforcement learning applied after fine-tuning outperforms RL from the base model by up to 7.7 points, indicating that behavior-based supervision compounds with post-training optimization.
- Training on progressively more user behavior data yields further improvements in user-related performance, establishing a clear scaling relationship that positions real-world behavioral data as a scalable supervisory resource comparable in potential to traditional text-based training corpora.

## Context
Current LLM training pipelines rely heavily on static text corpora or synthetic data generation, which fail to capture how user preferences, intents, and behavioral patterns evolve over weeks to years. This limitation is particularly acute for applications like personal assistants, recommendation engines, and advertising systems that must reason about long-term user behavior. Vela addresses this gap by proposing a novel paradigm where naturally occurring behavioral logs from content platforms and agent systems serve as a training signal, bridging the disconnect between model training objectives and deployment-time user modeling requirements.

## Implications
For industry practitioners deploying LLMs in user-facing applications, Vela offers a practical pathway to improve user modeling capabilities without requiring entirely new data collection infrastructure, since behavior records already exist at scale on platforms. The finding that behavior-based supervision also improves general benchmark performance suggests this approach could strengthen broader model intelligence, not just domain-specific user inference. For the research community, this work opens a new axis for scalable supervision beyond text and synthetic data, potentially reshaping how future foundation models are trained and evaluated on user-centric capabilities.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.14709v1)
