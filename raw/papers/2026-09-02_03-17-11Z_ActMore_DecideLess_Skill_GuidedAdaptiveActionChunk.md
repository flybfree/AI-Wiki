---
title: Act More, Decide Less: Skill-Guided Adaptive Action Chunking for Long-Horizon LLM Agents
published: 2026-09-02T03:17:11Z
authors: Yanting Yang, Can Jin, Jinman Zhao, Jiahao Wu, Yang Zhou, Zhepeng Wang, Zhendong Wang, Mu Zhou, Dimitris N. Metaxas
url: http://arxiv.org/abs/2609.02042v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Act More, Decide Less: Skill-Guided Adaptive Action Chunking for Long-Horizon LLM Agents

## Abstract
Large language model (LLM) agents for long-horizon interactive tasks typically follow a ReAct-style protocol, issuing one primitive action per LLM round. While this enables frequent replanning, it is inefficient for long-horizon tasks where many rounds are spent on routine action sequences. A natural alternative is to let the agent emit variable-length action chunks. However, naively training such policies with standard reinforcement learning fails: the agent either collapses to single-action behavior or over-commits to excessively long sequences. Both failures share a common root cause: the inability to learn chunk boundaries. We propose SPACE, which addresses this challenge by distilling chunk-boundary supervision from trajectory-induced programmatic skills. We induce two-level programmatic skills from successful trajectories, where subskill boundaries serve as direct chunk-boundary supervision. This temporal structure is then distilled into a primitive-chunk policy via hybrid on-/off-policy optimization with chunk-aware credit assignment. Experiments on ALFWorld and ScienceWorld show that SPACE improves success rates by 7.0%-31.3% over the strongest baseline in each setting while reducing average LLM decision rounds by up to 78.9%.

## Metadata
- **Published**: 2026-09-02T03:17:11Z
- **Authors**: Yanting Yang, Can Jin, Jinman Zhao, Jiahao Wu, Yang Zhou, Zhepeng Wang, Zhendong Wang, Mu Zhou, Dimitris N. Metaxas
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02042v1)