---
title: Can MLLMs Decode the Creative Leap? Introducing C4 for Cross-Concept Understanding
url: http://arxiv.org/abs/2608.06501v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-06_18-38-14Z_CanMLLMsDecodetheCreativeLeap_IntroducingC4forCros.md
generated_at: 2026-08-09 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes C4, a framework for evaluating cross‑concept creativity using Chinese idioms, and finds that current MLLMs perform poorly on decoding creative meaning across concept bridges. The strongest models achieve around 50% primary accuracy while open‑source ones lag significantly.

## Key Takeaways
- C4 operationalizes cross‑concept understanding as encoding and decoding with explicit bridge paths and exact answers.
- Evaluation set includes 184 synthetic items and 37 human‑created chengyu figures, generating 884 answer‑recovery cases across ten models.
- Adding candidate constraints boosts accuracy sharply, whereas bridge hints or explanation requests only modestly improve performance.

## Context
Assessing creative abilities of large language models remains challenging because traditional metrics focus on factual correctness rather than conceptual insight. This work introduces a cognition‑inspired benchmark that mirrors how humans recover meaning from non‑obvious conceptual links, offering a more realistic test for MLLMs in design and collaboration tasks.

## Implications
For researchers, C4 provides a standardized way to measure cross‑concept reasoning beyond accuracy. For industry practitioners, it highlights the need for models that can navigate complex mental bridges, informing future AI systems aimed at human‑centric creativity.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06501v1)
