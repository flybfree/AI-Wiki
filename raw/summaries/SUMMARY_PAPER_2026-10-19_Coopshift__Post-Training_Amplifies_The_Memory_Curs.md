---
title: Coopshift: Post-Training Amplifies The Memory Curse In LLM Cooperation
url: http://arxiv.org/abs/2610.24086v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-16_18-11-16Z_Coopshift_Post_TrainingAmplifiesTheMemoryCurseInLL.md
generated_at: 2026-10-19 20:43
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates how post-training stages (supervised fine-tuning and preference/reward optimization) alter cooperative behavior in large language models during repeated social interactions. The authors compare Base, SFT, and Aligned checkpoints across seven model lineages in seven social dilemmas, revealing that post-training amplifies the "memory curse"—the phenomenon where agents cooperate less when they can observe more rounds of past interaction. The central finding is that both SFT and Aligned stages show steeper declines in cooperation as visible history expands, and these declines exceed those of the Base model in six of seven lineages.

## Key Takeaways
- Post-training amplifies the memory curse across binary-action games: expanding visible history from two to forty rounds reduces cooperation at every SFT and Aligned checkpoint, and these declines are steeper than Base's in six of seven model lineages. Most of this amplification is already introduced at the SFT stage, suggesting that supervised fine-tuning is the primary culprit rather than the subsequent alignment step.
- In symmetric binary games, post-trained models exhibit steeper fitted cooperation-rate declines as per-round cooperation costs rise, benefits fall, or noncooperation becomes more rewarding, indicating that post-training makes models more sensitive to payoff structures in ways that undermine sustained cooperation.
- The behavioral difference between Aligned and SFT checkpoints shifts depending on framing: when given identical past records, their choices depend on whether instructions describe a final round or possible future interaction, revealing that post-training introduces context-dependent cooperation strategies that are invisible in one-shot evaluations.

## Context
This work sits at the intersection of LLM alignment research and behavioral game theory, addressing a critical gap in how we evaluate post-trained models. Most alignment evaluations focus on isolated decisions—single-turn benchmarks measuring whether a model produces a cooperative or prosocial response. This paper demonstrates that such evaluations miss a fundamental dimension: how cooperation behaves dynamically over repeated interactions and how it degrades as agents gain access to longer histories. By systematically comparing Base, SFT, and Aligned checkpoints across multiple model families and game structures, the authors provide the first comprehensive evidence that the very training procedures designed to make models more helpful and cooperative can paradoxically make them worse at sustaining cooperation in multi-round settings.

## Implications
For practitioners deploying LLMs in multi-agent systems—negotiation platforms, collaborative coding environments, or simulated social ecosystems—this research warns that post-trained models may underperform their Base counterparts in sustained cooperative tasks, particularly when agents can reference longer interaction histories. Evaluation protocols for alignment should be expanded beyond one-shot benchmarks to include repeated-interaction games with varying payoff structures and history lengths, ensuring that post-training does not inadvertently erode the very cooperative behavior it aims to instill. Model developers and safety researchers should treat SFT as a critical intervention point for cooperation dynamics, not merely a precursor to alignment tuning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.24086v1)
