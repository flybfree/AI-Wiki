---
title: HarnessTTT: Learn to Optimize Harness at Test-Time for Scientific Discovery
published: 2026-10-12T20:27:32Z
authors: Yingzi Ma, Yulong Cao, Nanxi Li, Fang Wu, Yizhe Zhang, James Zou, Yejin Choi, Chaowei Xiao
url: http://arxiv.org/abs/2610.17370v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HarnessTTT: Learn to Optimize Harness at Test-Time for Scientific Discovery

## Abstract
Scientific discovery with language models requires finding the best valid solution within a finite computational budget. We study how feedback from this search can improve the procedure used to conduct it. We introduce HarnessTTT, a test-time learning framework that trains a harness proposer while keeping the executor frozen. The proposer generates executable harnesses comprising system prompts, reusable skills, tools, middleware, and execution controls. Each harness guides a budgeted discovery rollout, whose outcome provides feedback for updating the proposer. A discovery-oriented policy-gradient objective combines gap-normalized rewards, leave-one-out advantages (RLOO), and max-sharpening to favor high-performing proposals. Generated components are validated before execution, and the search retains the best valid solution and selected harnesses across rounds. Across fourteen discovery tasks in mathematics, systems, GPU kernels, heuristic programming, astrodynamics, and biology, HarnessTTT with a frozen 9B executor improves on OpenEvolve with the same executor on all eleven benchmark tasks (e.g., from 1.17 to 2.64 on circle packing), improves on the discovery-fine-tuned Finch-9B by up to 92%, holds the best open-weight sub-10B result on nine, and reaches 0.380919 on Erdős minimum overlap, better than the best human reference of 0.380927. Scaling the proposer and frozen executor to 27B improves on eleven of fourteen tasks, and transferring the learned harnesses to GPT-5.5 matches or exceeds the strongest reported system of any backbone on nine of fourteen tasks. Together, these results show that harness search can itself be learned at test time: a trained proposer lets a small frozen executor search effectively, and the harnesses it finds carry over to stronger executors.

## Metadata
- **Published**: 2026-10-12T20:27:32Z
- **Authors**: Yingzi Ma, Yulong Cao, Nanxi Li, Fang Wu, Yizhe Zhang, James Zou, Yejin Choi, Chaowei Xiao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.17370v1)