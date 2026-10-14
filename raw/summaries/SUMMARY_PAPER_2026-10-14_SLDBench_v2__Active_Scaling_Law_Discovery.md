---
title: SLDBench v2: Active Scaling Law Discovery
url: http://arxiv.org/abs/2610.16297v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-12_07-23-23Z_SLDBenchv2_ActiveScalingLawDiscovery.md
generated_at: 2026-10-14 00:59
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
SLDBench v2 extends a benchmark for evaluating whether language-model agents can autonomously discover scaling laws that predict large-model performance from small-scale experiments. The paper introduces two major extensions: a vastly expanded corpus of 127 scenarios covering language-model pretraining, downstream performance, and vision-language transfer, and a new "active" evaluation mode in which agents must strategically choose which experiments to run under a budget constraint. Across eight frontier agent systems, performance degrades substantially in the active setting, with median R² dropping from 0.72–0.75 in the passive setting to 0.24–0.57 in the active setting, revealing that experimental planning remains a critical unsolved challenge for AI-assisted model development.

## Key Takeaways
- The benchmark corpus was expanded from 8 to 127 scenarios, with 30 deliberately selected challenging cases where a reference power-law fit achieves R² ≤ 0.8, collectively representing at least 1.09 × 10²³ FLOPs of source-reported training compute. This ensures the benchmark tests agents on genuinely difficult, non-trivial scaling relationships rather than easily fittable patterns.
- In the newly introduced active discovery setting, agents must select which experiments to run, pay each experiment's recorded cost (such as training FLOPs), and iteratively revise their hypothesized scaling law as outcomes arrive. Performance drops dramatically compared to the passive setting where all data is provided upfront: prediction error increases by 1.5 to 4.7 times depending on the agent system, and median R² falls to as low as 0.24.
- Agents exhibit a strong bias toward cheap experiments, spending only 8–44% of the full experimental pool's cost on average. While low-cost acquisitions can sometimes yield strong predictions, the paper finds that cheap purchases systematically leave critical experimental conditions unobserved, undermining the agent's ability to extrapolate to the hidden targets used for scoring.

## Context
Scaling laws are foundational to modern AI development, guiding how practitioners allocate compute budgets for training large language models and multimodal systems. The ability to automate the discovery of these laws through AI agents—so-called "AI-for-AI" research—represents a promising frontier for reducing the human cost of model development. SLDBench v2 addresses a critical gap in this area: prior evaluations assumed agents received all experimental data passively, which does not reflect the real-world constraint that experiments are expensive and must be strategically planned. By introducing budget-constrained active discovery, the benchmark moves closer to the actual workflow of researchers who must decide what to train and measure under finite resources.

## Implications
For practitioners and AI labs, these findings signal that current frontier agent systems are not yet capable of replacing human judgment in experimental design for scaling law discovery. The strong bias toward cheap experiments and the resulting failure to observe conditions necessary for extrapolation suggest that future agent architectures need explicit planning and exploration strategies rather than greedy cost-minimizing behavior. For the broader AI-for-AI research community, SLDBench v2 establishes a more rigorous and realistic evaluation standard, highlighting that experimental planning—not just pattern fitting—is the key bottleneck that must be solved before autonomous agents can meaningfully assist in large-scale model development.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.16297v1)
