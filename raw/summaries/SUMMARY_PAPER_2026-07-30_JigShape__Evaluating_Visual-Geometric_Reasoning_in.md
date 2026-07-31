---
title: JigShape: Evaluating Visual-Geometric Reasoning in VLMs through Jigsaw Puzzles
url: http://arxiv.org/abs/2607.27670v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_04-34-27Z_JigShape_EvaluatingVisual_GeometricReasoninginVLMs.md
generated_at: 2026-07-30 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Jigshape, a benchmark that combines visual and geometric reasoning using tab-and-blank interlocking pieces with clear local compatibility constraints. Experiments on 95K puzzles at varying grid sizes reveal that zero-shot vision-language models perform poorly, especially as puzzle size grows, while supervised fine-tuning improves performance only up to small grids. The scaling cliff indicates current architectures cannot sustain geometric reasoning beyond tiny puzzles.

## Key Takeaways
- Zero‑shot VLMs lack geometric reasoning: only GPT‑5.5 exceeds chance on 4×4 puzzles, others are at random level.
- Supervised fine‑tuning reaches >97% accuracy on 4×4 but collapses on larger grids, dropping below 5% on 12×12.
- The scaling cliff shows current models cannot maintain consistent constraint satisfaction as the number of pieces increases.

## Context
Jigsaw puzzles have long been used to test visual‑geometric integration in AI. Existing benchmarks suffer from ambiguous ground truth due to repeated textures, limiting reliable evaluation. This work addresses that gap by providing a clear geometric interface and demonstrates a systematic failure mode across model sizes.

## Implications
The findings highlight a critical limitation of current vision‑language systems: they cannot reliably handle combinatorial spatial constraints beyond trivial cases. For industry practitioners, this suggests a need for specialized reasoning modules or architectural changes to support larger-scale geometric tasks. The benchmark opens research avenues toward scalable visual‑geometric AI.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27670v1)
