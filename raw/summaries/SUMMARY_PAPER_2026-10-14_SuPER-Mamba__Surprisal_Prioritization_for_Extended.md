---
title: SuPER-Mamba: Surprisal Prioritization for Extended-Context Routing in Mamba
url: http://arxiv.org/abs/2610.16636v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_11-57-50Z_SuPER_Mamba_SurprisalPrioritizationforExtended_Con.md
generated_at: 2026-10-14 01:12
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
SuPER-Mamba introduces a training-free routing framework for pretrained Mamba state-space models that leverages Surprisal—a model-intrinsic information-theoretic signal derived from next-token predictions—to prioritize which global-channel state updates should be applied during extended-context processing. The framework addresses the well-documented performance degradation that state-space models suffer as input context length increases, achieving a 94.7% relative improvement over base models and a 13.1% gain over the prior state-of-the-art baseline on the LongBench-E benchmark without requiring any additional training or query-dependent scoring mechanisms.

## Key Takeaways
- SuPER-Mamba computes position-wise Surprisal scores directly from the pretrained model's own next-token prediction outputs, then aggregates these scores through a Local Pooling mechanism to produce routing priorities for Global-Channel updates. This means the routing signal is entirely model-intrinsic and requires no external supervision, fine-tuning, or query-dependent attention scoring, making the framework fully training-free and plug-and-play for existing Mamba architectures.
- The framework was evaluated across three distinct state-space model architectures on the LongBench-E benchmark, demonstrating consistent improvements: the average benchmark score rose from 8.06 to 15.69, a 94.7% relative gain over unmodified base models and a 13.1% improvement over the best previously reported baseline. Ablation studies and length-wise analyses confirmed that the gains are robust across varying context lengths and that each component of the routing pipeline contributes meaningfully to the final performance.
- By using Surprisal as a proxy for information content and uncertainty at each token position, SuPER-Mamba effectively identifies which segments of a long sequence carry the most novel or unpredictable information, allowing the model to allocate its limited state-update capacity toward the most informative regions rather than uniformly processing all tokens. This principled prioritization avoids the uniform dilution of state information that causes performance collapse in vanilla Mamba models at extended context lengths.

## Context
State-space models such as Mamba have emerged as compelling alternatives to transformer architectures for long-sequence processing due to their linear computational complexity and constant memory footprint. However, a persistent weakness is that their fixed-size hidden state becomes increasingly diluted and less discriminative as context length grows, causing retrieval and reasoning performance to degrade sharply beyond moderate sequence lengths. SuPER-Mamba sits at the intersection of information theory and efficient sequence modeling, proposing a principled, training-free mechanism to mitigate this degradation without altering model weights or introducing additional parameters, which positions it as a practical intervention for deploying existing pretrained Mamba models in long-context applications.

## Implications
For practitioners deploying Mamba-based models in production settings involving long documents, codebases, or multi-turn conversations, SuPER-Mamba offers a drop-in enhancement that requires no retraining, no additional GPU memory for scoring heads, and no architectural modifications, making it immediately applicable to existing model checkpoints. For the broader research community, the paper demonstrates that model-intrinsic uncertainty signals like Surprisal can serve as effective routing heuristics for state-space architectures, opening a pathway toward adaptive, information-aware state management that could be generalized beyond Mamba to other linear-complexity sequence models seeking to handle extended contexts without sacrificing efficiency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.16636v1)
