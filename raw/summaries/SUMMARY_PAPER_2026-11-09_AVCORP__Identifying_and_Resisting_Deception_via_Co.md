---
title: AVCORP: Identifying and Resisting Deception via Communication Theory and Theory of Mind
url: http://arxiv.org/abs/2611.10176v1
type: paper-summary
date: 2026-11-09
source_paper: 2026-11-06_19-57-06Z_AVCORP_IdentifyingandResistingDeceptionviaCommunic.md
generated_at: 2026-11-09 21:25
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces AVCORP, a corpus of 5,000 annotated utterances from 250 games of Avalon designed to train language models to detect deception in multi-agent communication. The authors train Qwen3-8B on this corpus and demonstrate that the fine-tuned model outperforms its untrained baseline and several frontier models on held-out games, while consistently exceeding the untrained model's F1 score across all rounds when evaluated on games played by humans.

## Key Takeaways
- AVCORP encodes deception detection as a structured reasoning task by mapping 37 distinct communication tactics onto a 4x4 behavior matrix, and by including reasoning traces that capture abductive hypotheses, graduated suspicion levels, and nested Theory of Mind beliefs about other players' intentions and knowledge states. This structured annotation goes beyond simple label-based classification and instead teaches models the inferential process behind identifying deceptive behavior.
- The trained Qwen3-8B detector outperforms frontier models including GPT-5.6 Sol, Gemini 3.1 Pro, and DeepSeek-V4-Pro on held-out Avalon games, matching the performance of Claude Opus 5.5. This demonstrates that targeted fine-tuning on a deception-specific corpus can close or exceed the gap between a small open-source model and much larger proprietary systems on a specific reasoning task.
- On games played by human opponents, every trained detector variant exceeds the untrained baseline in F1 score across all game rounds, indicating that the learned deception-detection capability generalizes beyond the synthetic game setting to interactions with real human players, which is critical for practical deployment.

## Context
As LLM-based agents increasingly interact with humans and other agents in open environments, vulnerability to deception becomes a fundamental safety and reliability concern. Existing approaches to deception detection often rely on prompt engineering or general-purpose reasoning without grounding in communication theory or explicit Theory of Mind modeling. This paper bridges that gap by formalizing deception tactics through communication theory and by providing a scalable training resource that encodes multi-level belief reasoning, addressing a recognized gap in the literature on agent robustness.

## Implications
For practitioners building multi-agent systems, autonomous negotiation agents, or AI assistants that must operate in adversarial or trust-sensitive environments, AVCORP offers a concrete pathway to fine-tune smaller, deployable models for deception detection without relying on expensive frontier-model APIs. The structured annotation schema—combining a behavior matrix with nested ToM reasoning traces—also provides a reusable template for constructing similar corpora in other domains where agents must reason about others' beliefs and strategic intent, potentially informing future work on AI safety, adversarial robustness, and human-AI interaction design.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.10176v1)
