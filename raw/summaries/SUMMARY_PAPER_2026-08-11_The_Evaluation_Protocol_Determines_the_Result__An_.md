---
title: The Evaluation Protocol Determines the Result: An Independent Reproduction of LeWorldModel on TwoRoom
url: http://arxiv.org/abs/2608.10145v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_19-00-51Z_TheEvaluationProtocolDeterminestheResult_AnIndepen.md
generated_at: 2026-08-11 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper reports an independent reproduction of LeWorldModel on the TwoRoom environment, achieving higher performance than the original claims when following a strict evaluation protocol. It shows that the reported 87% goal reach is not reproducible without specific conventions and that the evaluation method itself influences results.

## Key Takeaways
- The model reaches 94.0% at the repository's evaluation goal offset while the authors' own checkpoint yields only 84.0%, indicating sensitivity to goal construction.
- Changing how the goal is built across identical episodes shifts performance from 84.0% down to 8.0%, showing that protocol details matter more than model weights.
- A batch normalisation layer inflates validation loss by up to a factor of 300, masking training dynamics.

## Context
The work highlights how evaluation protocols can obscure true model capabilities in AI research, where reported metrics may depend on implementation choices rather than intrinsic performance. This echoes broader concerns about reproducibility and the need for transparent benchmarking practices.

## Implications
For researchers, this underscores that publishing only model weights without reproducible configurations risks misleading conclusions. Practitioners should adopt standardized evaluation pipelines to ensure fair comparison across studies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10145v1)
