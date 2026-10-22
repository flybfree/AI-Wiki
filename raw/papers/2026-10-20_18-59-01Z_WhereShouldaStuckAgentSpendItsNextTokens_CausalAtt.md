---
title: Where Should a Stuck Agent Spend Its Next Tokens? Causal Attribution of Inference-Time Resources
published: 2026-10-20T18:59:01Z
authors: Saiyue Lyu, Jerrold Huang, Yunbei Zhang, Janet Wang, Zhenting Wang, Yingqiang Ge, Haibo Zhang
url: http://arxiv.org/abs/2610.28834v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Where Should a Stuck Agent Spend Its Next Tokens? Causal Attribution of Inference-Time Resources

## Abstract
Inference-time scaling is often treated as a token-budget problem, but a failed coding agent can seek qualitatively different resources: computation, information, or feedback. We introduce Banzhaf Resource Attribution (BRA), a controlled factorial framework that measures each resource's marginal contribution to repair and its interactions while holding the failed state and revision protocol fixed. We evaluate six models on 194 function-level failures from MBPP+ and HumanEval+ and 126 repository-level failures from SWE-bench Verified. Task-relevant specifications consistently improve repair, whereas public-test feedback provides small gains and retrieved code little to none. The value of additional computation declines with model capability, while information remains useful; resource channels largely exhibit diminishing returns, although complementary information can reinforce itself. Yet three of four frontier models select feedback in 95-100% of cases and obtain lower gains than uniform random resource selection. BRA thus exposes a gap between the resources agents prefer and those that measurably improve repair.

## Metadata
- **Published**: 2026-10-20T18:59:01Z
- **Authors**: Saiyue Lyu, Jerrold Huang, Yunbei Zhang, Janet Wang, Zhenting Wang, Yingqiang Ge, Haibo Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.28834v1)