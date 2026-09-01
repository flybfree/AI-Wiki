---
title: TRACER: Per-Tool Context Retention for LLM Agents via Consequence-Attributed Reinforcement Learning
published: 2026-08-29T16:50:44Z
authors: Ziqi Lin, Ye Wu, Mengying Yang, Xu Liu, Yizhou Liu, Qiang Ke, Qin Guo
url: http://arxiv.org/abs/2608.29363v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TRACER: Per-Tool Context Retention for LLM Agents via Consequence-Attributed Reinforcement Learning

## Abstract
Enterprise data agents answer business queries by chaining many tool calls over multiple reasoning steps, routinely accumulating hundreds of thousands of context tokens per session. Existing compression strategies typically allocate retention budgets without accounting for the downstream consequences of removing individual tool outputs. Aggressive compression may therefore trigger costly tool re-invocations that offset the initial savings. We call this the compression--consequence gap. To close it, we propose TRACER, which formulates compression as a sequential per-tool decision problem. A lightweight REINFORCE policy assigns query-conditioned retention ratios using only information available at each compression event. Its consequence-aware objective jointly accounts for task success, total token consumption, and post-compression tool re-invocations. To improve credit assignment, TRACER uses a learned outcome model to compare the predicted consequences of the selected retention ratio with those of fully retaining each tool output. On held-out production queries across three compressor backends, TRACER reduces total token consumption by 29--46% relative to keeping all context while maintaining comparable or higher task success. Compared with a tool-type-conditional static policy, TRACER provides an additional 15--18% of token savings. Interventional rollouts show that the learned per-tool credit scores correlate with measured single-tool consequences. The learned policy also yields positive savings when transferred across agent backbones and compressor architectures, and reduces token consumption by 18--25% on five held-out LOCA-bench environments. These results demonstrate the value of consequence-aware, per-tool context retention for improving the efficiency of long-horizon language agents.

## Metadata
- **Published**: 2026-08-29T16:50:44Z
- **Authors**: Ziqi Lin, Ye Wu, Mengying Yang, Xu Liu, Yizhou Liu, Qiang Ke, Qin Guo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29363v1)