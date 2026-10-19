---
title: Distill Until Divergence: Error-Truncated Hindsight Distillation for Agentic RL
published: 2026-10-16T07:28:05Z
authors: Yibin Huang, Conghui Zhu
url: http://arxiv.org/abs/2610.23048v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Distill Until Divergence: Error-Truncated Hindsight Distillation for Agentic RL

## Abstract
Long-horizon interaction requires agents to make multiple decisions in a changing environment. Outcome-based GRPO lacks fine-grained guidance for intermediate decisions. Recent methods distill completed trajectories into reusable skills and use hindsight-conditioned OPD to provide dense token-level credit. However, skill-induced probability shifts do not necessarily represent reward-aligned credit; especially after an erroneous action changes subsequent interaction states, skill-conditioned supervision may become mismatched with the current state. To address this mismatch, we propose \methodname{}, which routes two complementary hindsight skills according to trajectory outcomes and error boundaries: Positive skills capture successful workflows to reinforce successful trajectories and pre-error decisions, while Negative skills capture failure-specific corrections to target decisive errors. The post-error suffix is optimized exclusively by GRPO, retaining outcome-based learning without extending potentially mismatched hindsight supervision. Extensive experiments demonstrate competitive task performance and support effective fine-grained credit allocation.

## Metadata
- **Published**: 2026-10-16T07:28:05Z
- **Authors**: Yibin Huang, Conghui Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.23048v1)