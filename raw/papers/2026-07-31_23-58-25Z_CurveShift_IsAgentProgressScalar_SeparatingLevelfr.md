---
title: CurveShift: Is Agent Progress Scalar? Separating Level from Shape
published: 2026-07-31T23:58:25Z
authors: Hanwen Xing, Pengyun Wang, BingXu Meng, Kumail Alhamoud, Xiang Li, Jicheng Wang, Xin Yu, Xinyang Han, Xiaomin Li, Philip Torr, Yuexing Hao
url: http://arxiv.org/abs/2608.00355v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CurveShift: Is Agent Progress Scalar? Separating Level from Shape

## Abstract
Progress in large language models is often summarized using a single scalar measure, such as a time horizon, a latent ability estimate, or an aggregate benchmark score. These summaries capture the overall performance, but they do not test whether progress is distributed differently across task difficulty. We find that most of the apparent shift in gains toward harder tasks does not reflect a change in the shape of the difficulty-response curve. On METR time-horizon data, a single Rasch model with rising ability reproduces this pattern, so it is largely explained by ceiling effects rather than a qualitative change in capability. This echoes how the choice of metric can make claimed emergent abilities look like a property of the models themselves. We then identify a smaller hard-task effect that survives this control. Isolating it is difficult on agentic benchmarks, because newer models are usually run with newer agentic harnesses, so a gain on hard tasks cannot be assigned to the model or its scaffold. We break the confound with LiveCodeBench, a public competitive programming benchmark that runs no agentic scaffold while pairing dated models with an exogenous difficulty ordering. After accounting for the rise in overall ability, models released after September 2024 still gain on the hardest problems beyond what their easy and medium performance predicts, by about +0.40 logits under our most conservative assumption, raising the hard-problem solve rate from roughly 18% to 25%. The effect is led by the strongest reasoning models and holds for hard tasks that need only short reasoning, not autonomy over long horizons. We present this as a result specific to competitive programming, since our clean identification rests on a single coding benchmark. We release the LiveCodeBench Difficulty Panel (66 dated models x 1,055 problems) and our analysis code.

## Metadata
- **Published**: 2026-07-31T23:58:25Z
- **Authors**: Hanwen Xing, Pengyun Wang, BingXu Meng, Kumail Alhamoud, Xiang Li, Jicheng Wang, Xin Yu, Xinyang Han, Xiaomin Li, Philip Torr, Yuexing Hao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00355v1)