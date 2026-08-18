---
title: Defake-o3: From Speculative Rationales to Verifiable Evidence for Explainable AIGI Detection
published: 2026-08-17T08:30:32Z
authors: Bowen Deng, Jiahui Zhan, Yikun Ji, Haozhen Yan, Jianfu Zhang
url: http://arxiv.org/abs/2608.16259v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Defake-o3: From Speculative Rationales to Verifiable Evidence for Explainable AIGI Detection

## Abstract
The rapid progress of image generation models calls for AI-generated image (AIGI) detectors that are not only accurate but also explainable and reliable. While MLLM-based detectors can provide natural language explanations, existing methods often generate speculative rationales: they rely on vague or hallucinated artifacts, miss subtle localized flaws from the latest generators, and fail to provide evidence that can be visually verified. We present Defake-o3, an explainable AIGI detector that moves from speculative rationales to verifiable evidence. It combines interactive visual search with verifier-guided evidence alignment: the model iteratively zooms into suspicious regions to inspect fine-grained details, while an Evidence Verifier, trained from human verification annotations, provides reinforcement learning rewards that favor grounded evidence and penalize baseless claims. To support this objective, we construct GroundFake, a dataset designed for grounded explainable detection, with localized bounding-box evidence, human verification based on visual grounding and artifact specificity, corrected reasoning trajectories, and valid/invalid evidence supervision. We further introduce FakeFrontier, an out-of-distribution benchmark built from real images and outputs of 10 recent generators, together with an MLLM-based protocol for evaluating evidence quality and persuasiveness. Experiments on GroundFake, FakeFrontier, and additional out-of-distribution benchmarks show that Defake-o3 improves both detection accuracy and explanation quality, producing more localized, verifiable, and persuasive evidence.

## Metadata
- **Published**: 2026-08-17T08:30:32Z
- **Authors**: Bowen Deng, Jiahui Zhan, Yikun Ji, Haozhen Yan, Jianfu Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16259v1)