---
title: $π\mathbf{R}^2$: Reactive Real-time Flow Policies
url: http://arxiv.org/abs/2607.26055v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_17-59-31Z_π_mathbf_R__2__ReactiveReal_timeFlowPolicies.md
generated_at: 2026-07-28 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces πR², a reactive real-time flow policy that enables large pretrained manipulation backbones to respond instantly to sensory input while maintaining multi‑action prediction. By splitting conditioning into fast proprioceptive channels and latency‑adaptive inpainting steps, the method reduces replanning frequency from ~25 Hz to ~40 ms per tick on a GPU A5000, achieving up to 30 % higher success rates than baselines in real‑world manipulation. The approach requires only minor architectural tweaks and can be finetuned directly from existing pretrained models.

## Key Takeaways
- The fast channel provides fresh proprioceptive data each tick, allowing immediate reaction within a chunk while vision features are updated asynchronously.
- Latency‑adaptive flow scheduling treats in‑flight actions as inpainting conditioning, emitting one action per denoising step to accommodate varying hardware delays.
- The method can be applied to existing architectures like GR00T‑N1.7 with minimal changes and yields a 4× faster replanning compared to the baseline.

## Context
Reactive control is essential for closed‑loop manipulation where environments change rapidly, yet current flow policies are limited by slow perception pipelines that cannot keep up with real‑time demands. This paper addresses the latency bottleneck in diffusion‑based backbones, which dominate modern AI agents but sacrifice responsiveness for expressiveness.

## Implications
The results demonstrate that large language vision models can be adapted to perform high‑frequency, low‑latency control without sacrificing performance. Practitioners can leverage this framework to build real‑world robotic manipulators with tighter feedback loops, opening new avenues for interactive and autonomous systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26055v1)
