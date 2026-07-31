---
title: ARES: Adaptive Reasoning-Effort Steering for PPA- and Cost-Aware RTL Optimization with LLM Agents
published: 2026-07-30T08:53:32Z
authors: Stef Cuyckens, Mihaela Jivanescu, Jun Yin, Chao Fang, Marian Verhelst
url: http://arxiv.org/abs/2607.27879v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ARES: Adaptive Reasoning-Effort Steering for PPA- and Cost-Aware RTL Optimization with LLM Agents

## Abstract
Large language model (LLM) agents optimize the power, performance, and area (PPA) of register-transfer-level (RTL) designs by iterating over edits, synthesis, and PPA analysis, paying a dollar cost for every LLM call. Prior agents report the quality reached without its normalized cost, attribute that quality to an engineered cross-design memory, and hold the reasoning effort of every call fixed. We propose Ares with three corresponding innovations. (1) We introduce a normalized dollar cost per LLM call reported alongside the figure of merit (FoM), enabling fair comparison across effort levels and optimizers. (2) Using this accounting, we find the construction of the long-term memory matters little. An engineered memory brings no dependable gain over a plain concatenation of the same experience. (3) We instead adapt the per-call reasoning effort by escalating to deeper reasoning only once progress at a lower effort stalls, via a patience counter fit on 21 training designs, allocating reasoning where it pays rather than uniformly across all iterations. On three test designs unseen during training, the effort policy lowers the FoM by 23-27% where the best fixed effort reaches 16-23%, at equal normalized cost. Ares closes up to 83% of the gap from an LLM-drafted multiply-accumulate unit to its highly hand-optimized counterpart, and reaches a 25% deeper FoM than state-of-the-art Dr. RTL at 12% of its tokens.

## Metadata
- **Published**: 2026-07-30T08:53:32Z
- **Authors**: Stef Cuyckens, Mihaela Jivanescu, Jun Yin, Chao Fang, Marian Verhelst
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27879v1)