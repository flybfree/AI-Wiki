---
title: StateWise: Teaching Language Models to Track and Obey Evolving Constraints in Multi-Turn Dialogue
url: http://arxiv.org/abs/2610.33766v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-24_16-17-56Z_StateWise_TeachingLanguageModelstoTrackandObeyEvol.md
generated_at: 2026-10-26 20:30
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
StateWise introduces a self-improving fine-tuning approach that teaches a single language model to maintain its own revisable constraint state during multi-turn conversations, addressing two critical failure modes in instruction-tuned LLMs: persistence failure (active constraints being ignored as dialogue lengthens) and relapse (withdrawn constraints being re-enacted). The method combines supervised fine-tuning on constraint-state summarization and conditioned response generation with self-training filtered by exact round-trip verification, followed by a preference optimization stage targeting relapse contrasts, ultimately enabling 7-8B models to outperform external compiled-ledger baselines without any inference-time scaffolding.

## Key Takeaways
- StateWise constructs a typed internal state representation with tombstones for revoked constraints, enabling executable checkers to measure persistence and relapse objectively and compile ground-truth states for free, eliminating the need for an external ledger system that re-injects a compiled specification every turn. The approach fine-tunes the model on two complementary skills: summarizing a dialogue into its constraint state and responding conditioned on that state, then self-trains on its own trajectories while keeping only turns that pass an exact round-trip check against the compiled state.
- A surprising finding is that supervised self-training alone roughly doubles relapse on Llama-3.1-8B, meaning the model learns to track state almost perfectly but fails to obey it. StateWise addresses this by adding a preference stage on self-generated relapse contrasts, where the rejected response enacts a revoked rule and the chosen one passes the round-trip check, cutting relapse by 8-22 points relative to supervised self-training alone.
- On two backbones evaluated with held-out constraint families and unseen phrasings, StateWise lifts conversation success by 8-19 points over the backbone and beats an oracle compiled-ledger baseline on relapse with no inference-time scaffolding. The authors also characterize the recipe's cost on general instruction-following benchmarks and study weight interpolation as a mitigation strategy to preserve general capabilities.

## Context
Conversational assistants in production increasingly handle multi-turn interactions where users incrementally add, amend, withdraw, and restate constraints, yet current instruction-tuned LLMs degrade in constraint adherence as dialogue length grows. The prevailing workaround—maintaining an external ledger that re-injects a compiled specification each turn—adds engineering complexity and inference overhead. StateWise represents a shift toward internalizing constraint tracking within the model itself, aligning with broader research trends in self-improving language models, preference optimization, and the growing recognition that multi-turn coherence is a distinct capability from single-turn instruction following.

## Implications
For practitioners building conversational AI products, StateWise demonstrates that smaller 7-8B models can achieve constraint-tracking performance comparable to or exceeding external scaffolding systems, potentially reducing inference costs and architectural complexity in production deployments. The finding that supervised training alone worsens relapse highlights a critical gap between state tracking and state obedience, suggesting that future model training pipelines must explicitly target behavioral compliance rather than mere representational accuracy. The study of weight interpolation as a mitigation also signals a practical tradeoff between specialized constraint-following ability and general instruction-following performance that product teams will need to navigate when deploying fine-tuned models in diverse conversational settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.33766v1)
