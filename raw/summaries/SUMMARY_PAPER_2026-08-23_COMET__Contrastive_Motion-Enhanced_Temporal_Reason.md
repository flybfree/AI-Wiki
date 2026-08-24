---
title: COMET: Contrastive Motion-Enhanced Temporal Reasoning for Video Multimodal Large Language Models
url: http://arxiv.org/abs/2608.21030v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_12-28-36Z_COMET_ContrastiveMotion_EnhancedTemporalReasoningf.md
generated_at: 2026-08-23 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces COMET, a framework that enhances video multimodal large language models by explicitly modeling frame‑to‑frame motion. It achieves consistent improvements on action and temporal reasoning tasks while keeping static perception performance stable across model families such as Qwen3-VL-8B and InternVL2.5-8B.

## Key Takeaways
- COMET builds a temporal motion branch using Taylor frame differences to capture change between consecutive frames, providing a direct representation of motion evidence.
- The motion evidence is injected into the appearance stream through attention bias‑enhanced cross‑attention, enabling interaction between visual content and temporal dynamics.
- A forward‑reverse TC‑GRPO optimization stage turns temporal order into a learning signal, strengthening direction‑aware motion pattern utilization.

## Context
Current video multimodal models often rely on sparse frame sampling, which limits their ability to understand fine‑grained motion. Without an explicit temporal modeling pipeline, the interaction between appearance and motion remains weak, hindering tasks that require precise timing or directional cues.

## Implications
COMET demonstrates that adding a dedicated temporal branch can yield measurable gains in video understanding without sacrificing static perception, offering a scalable approach for developers seeking better performance across diverse model architectures. This research points toward more robust multimodal systems that respect the sequential nature of video data.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21030v1)
