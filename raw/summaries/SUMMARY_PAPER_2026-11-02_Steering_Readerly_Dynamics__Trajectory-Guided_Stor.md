---
title: Steering Readerly Dynamics: Trajectory-Guided Story Generation with Large Language Models
url: http://arxiv.org/abs/2611.00469v1
type: paper-summary
date: 2026-11-02
source_paper: 2026-10-30_23-53-26Z_SteeringReaderlyDynamics_Trajectory_GuidedStoryGen.md
generated_at: 2026-11-02 21:37
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper proposes a novel framework for improving story generation by large language models through the explicit modeling of "readerly dynamics"—the evolving emotional and cognitive responses readers experience as a narrative unfolds. The authors train a small LLM to predict future reader responses as low-dimensional trajectories derived from high-quality human-written stories, then use these predicted trajectories to guide a larger, off-the-shelf writer LLM in generating coherent story segments. The approach yields a 12% to 35% improvement in trajectory-based fidelity to human-written narratives while largely preserving overall story coherence.

## Key Takeaways
- The core innovation is a two-model architecture: a small LLM learns to predict reader responses as low-dimensional trajectories rather than modeling high-dimensional story content directly, which sidesteps the difficulty of capturing nuanced narrative engagement in a single generative model. This decomposition makes the problem tractable while preserving the richness of reader experience.
- The framework leverages the strong instruction-following capability of a larger, off-the-shelf writer LLM to generate story segments that adhere to the predicted reader-response trajectories within a given story setting, effectively separating the "what readers will feel" prediction task from the "what text to write" generation task.
- Quantitative results demonstrate a 12% to 35% improvement in trajectory-based fidelity compared to baselines, indicating that explicitly guiding generation through predicted reader dynamics produces narratives that more closely mirror the engagement patterns found in human-authored stories, without sacrificing coherence.

## Context
This work sits at the intersection of narrative generation, affective computing, and instruction-following LLM research. While prior work on LLM-based story generation has focused on plot structure, character consistency, or stylistic mimicry, this paper addresses a subtler and more human-centered dimension: the temporal evolution of reader engagement. By framing readerly dynamics as a learnable, low-dimensional signal, the authors connect computational narrative generation to established literary theory and reader-response criticism, offering a principled bridge between AI-generated text and the qualities that make stories genuinely compelling to human audiences.

## Implications
For practitioners in creative AI, interactive fiction, and game narrative design, this framework offers a practical pathway to generate stories that feel emotionally engaging rather than merely structurally coherent, potentially improving user retention in AI-driven storytelling products. For the broader field, the small-model-predicts-trajectories-plus-large-model-writes paradigm suggests a reusable architectural pattern for steering generative outputs toward complex, multi-dimensional human experiences without requiring prohibitively large or fine-tuned models, opening avenues for more nuanced and reader-aware AI-generated content across entertainment, education, and therapeutic narrative applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.00469v1)
