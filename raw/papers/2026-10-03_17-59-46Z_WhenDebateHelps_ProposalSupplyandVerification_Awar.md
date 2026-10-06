---
title: When Debate Helps: Proposal Supply and Verification-Aware Readout in Multi-Agent Reasoning
published: 2026-10-03T17:59:46Z
authors: Zihao Zhao, Tunyu Zhang, Haizhou Shi, Yusong Zhao, Xinxi Zhang, Hao Wang
url: http://arxiv.org/abs/2610.04686v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Debate Helps: Proposal Supply and Verification-Aware Readout in Multi-Agent Reasoning

## Abstract
Multi-agent debate can improve reasoning, yet often fails to beat simple majority voting. We argue that successful debate requires two distinct mechanisms: proposal supply must surface a correct answer, and readout must identify that answer when voting misses it. We formalize the first requirement through recoverable headroom, which measures cases where a correct proposal is available but the majority answer is wrong. For the second, we develop Latent Verification Debate (LVD), an accounting model in which candidate proposals receive answer-specific verification evidence before final generation. Controlled fixed-proposal interventions estimate this latent effect in equivalent peer-support units and show that correct evidence changes answer probabilities and generated decisions while proposal supply remains fixed. To improve proposal supply, we construct societies from neural-thicket agents using labeled and label-free coverage objectives. Across two backbones and matched-budget reasoning benchmarks, coverage-selected societies increase complementary proposal supply and improve aggregate accuracy in repeated stochastic evaluations. Round-level controls further show that interaction provides gains beyond applying the same finalizer directly to the initial proposals. These results identify proposal coverage and truth-sensitive evidence use as complementary conditions for debate to outperform voting. Code is available at https://github.com/Wang-ML-Lab/when-debate-helps.

## Metadata
- **Published**: 2026-10-03T17:59:46Z
- **Authors**: Zihao Zhao, Tunyu Zhang, Haizhou Shi, Yusong Zhao, Xinxi Zhang, Hao Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04686v1)