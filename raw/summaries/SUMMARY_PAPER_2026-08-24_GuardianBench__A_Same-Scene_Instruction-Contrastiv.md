---
title: GuardianBench: A Same-Scene Instruction-Contrastive Benchmark for Latent Contextual Risk in Embodied AI
url: http://arxiv.org/abs/2608.21928v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-22_11-40-27Z_GuardianBench_ASame_SceneInstruction_ContrastiveBe.md
generated_at: 2026-08-24 21:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces GuardianBench, a benchmark that isolates latent contextual risk by pairing safe and unsafe instructions within the same scene across 3,024 examples. Evaluations show state‑of‑the‑art vision‑language models approve both instructions under a given scene with only 24.1% pair accuracy, indicating they fail to bind instruction‑relevant cues.

## Key Takeaways
- The benchmark demonstrates that many VLMs are insensitive to the instruction component when paired with a fixed scene, revealing latent safety risk.
- Failure analysis shows models neglect instruction‑specific visual cues that differentiate safe from unsafe compositions.
- A post‑training Verdict Log‑Odds Supervision (VLOS) objective improves performance on open‑weight backbones, highlighting the value of verdict‑level supervision.

## Context
GuardianBench addresses a gap in embodied AI safety research where only scene variation is tested while instruction composition remains constant. This limitation hampers progress toward robust, instruction‑aware safety systems that align with international standards.

## Implications
For practitioners, GuardianBench provides a standardized tool to detect and mitigate instruction‑scene interactions that could create hidden hazards. Industry adoption will drive safer AI deployments by ensuring models respect both visual context and textual intent.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21928v1)
