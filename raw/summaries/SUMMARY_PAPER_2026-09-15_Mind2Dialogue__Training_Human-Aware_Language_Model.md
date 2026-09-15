---
title: Mind2Dialogue: Training Human-Aware Language Models by Simulating User Mental States
url: http://arxiv.org/abs/2609.15972v1
type: paper-summary
date: 2026-09-15
source_paper: 2026-09-14_17-55-58Z_Mind2Dialogue_TrainingHuman_AwareLanguageModelsbyS.md
generated_at: 2026-09-15 00:24
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
The paper introduces Mind2Dialogue, a novel framework designed to train human-aware language models by simulating unspoken user mental states and converting them into privileged supervision. By employing a psychology-guided simulator that dynamically updates shared mental states during interactions, the authors generate coherent dialogues where an Oracle assistant provides well-informed responses grounded in hidden user beliefs and goals. Training on this simulated corpus significantly outperforms existing instruction-tuned baselines across personalization and theory of mind metrics, demonstrating substantial gains in preference-following and belief reasoning.

## Key Takeaways
- The authors address a critical supervision gap in LLM training by simulating users' unspoken beliefs and goals through a psychology-guided simulator that maintains consistent personal characteristics while dynamically evolving mental states during conversational interactions.
- A privileged distillation process leverages the Oracle assistant's well-informed responses to train deployable models, enabling them to assist effectively without direct access to hidden user mental states at inference time.
- Empirical evaluations combining personalization and theory of mind benchmarks reveal that Mind2Dialogue-trained models surpass Qwen, Llama, and OLMo baselines by 26.6 to 40.9 percentage points in preference-following generation, with notable improvements also extending to belief and action reasoning tasks.

## Context
As large language models advance toward long-term collaborative roles in education, healthcare, and professional environments, their ability to understand implicit user intentions has become a critical bottleneck. Current training datasets predominantly rely on explicit instructions or observable interactions, leaving a significant gap in modeling the unspoken cognitive and emotional states that drive real-world human behavior. This research directly addresses that limitation by bridging simulation-based data generation with practical model deployment.

## Implications
The Mind2Dialogue framework establishes a scalable pathway for developing AI collaborators capable of nuanced theory-of-mind reasoning, which could transform personalized tutoring, mental health support, and adaptive workplace assistance. By demonstrating that simulated mental state supervision significantly boosts preference alignment and contextual understanding,

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.15972v1)
