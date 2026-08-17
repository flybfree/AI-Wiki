---
title: More Correct Mass, Worse Answers: Why Power Sampling Can Fail and How to Fix It
url: http://arxiv.org/abs/2608.14420v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_16-01-10Z_MoreCorrectMass_WorseAnswers_WhyPowerSamplingCanFa.md
generated_at: 2026-08-16 20:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why Power Sampling, intended to improve reasoning by concentrating probability mass on correct generation paths, can paradoxically reduce accuracy. Experiments show up to an 18.5 percentage point drop in self‑consistency benchmarks despite higher mass on correct trajectories. The authors attribute this to two mismatches: a dose mismatch from a fixed exponent and a coverage mismatch where global sharpening narrows the supported set of paths.

## Key Takeaways
- Dose mismatch arises because a uniform trajectory exponent causes uneven distributional shifts across different reasoning problems, leading to excessive mass loss on some tasks.  
- Coverage mismatch occurs when Power Sampling concentrates probability into high‑pass@k paths, eliminating moderate‑probability alternatives needed for downstream search and selection.  
- The proposed deformation‑controlled, support‑preserving Power target calibrates sharpening across problems while limiting suppression of intermediate‑probability trajectories.

## Context
Power Sampling is a recent technique that refines the probability distribution over complete generation sequences without requiring external verification. Its promise lies in enabling more accurate inference by focusing on high‑quality paths, yet its behavior varies widely with problem characteristics, highlighting a gap between theoretical expectations and practical performance.

## Implications
For practitioners, this research underscores the need to tailor sampling strategies rather than applying uniform transformations across all tasks. It suggests that future work should incorporate problem‑specific calibration to balance sharpening with diversity preservation, ultimately leading to more robust and reliable AI inference systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14420v1)
