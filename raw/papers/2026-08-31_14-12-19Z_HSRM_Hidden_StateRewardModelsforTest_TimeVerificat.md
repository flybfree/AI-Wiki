---
title: HSRM: Hidden-State Reward Models for Test-Time Verification
published: 2026-08-31T14:12:19Z
authors: Xianzhi Li, Xiaodan Zhu
url: http://arxiv.org/abs/2608.30841v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HSRM: Hidden-State Reward Models for Test-Time Verification

## Abstract
Large language models can often generate plausible mathematical reasoning traces, but reliably identifying the correct solution among multiple candidates remains a key challenge. Existing test-time reasoning pipelines typically rely on text-based verifiers that re-read each generated solution, making verification an expensive component of inference. Prior work has shown, however, that LLMs often encode correctness-related signals in their internal representations, including awareness of when their own answers are likely to be wrong. Building on this observation, we introduce HSRM, a lightweight hidden-state reward model that verifies candidate solutions by directly reading the generator's internal representations rather than re-processing its text. HSRM extracts hidden states from a frozen generator at reasoning-step boundaries and uses a small Transformer encoder to rank candidates. It is trained from self-generated trajectories with outcome labels, requiring neither human-written process supervision nor a large pretrained verifier. Across four mathematical reasoning benchmarks, HSRM matches or outperforms a 55M-parameter text-only energy verifier in 15 of 16 generator--dataset settings while using only about 2M parameters, providing an efficient alternative to text-only verification by reusing representations already computed during generation.

## Metadata
- **Published**: 2026-08-31T14:12:19Z
- **Authors**: Xianzhi Li, Xiaodan Zhu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30841v1)