---
title: FACT: A Forensic Agent with Compiled Tool-Use Trajectories for AI-Generated Image Detection
published: 2026-09-05T04:39:49Z
authors: Jiaoyang Chen, Bin Hu, Jingyu Hu, Kun Zhou, Qin Zhang, Zhengzhe Liu
url: http://arxiv.org/abs/2609.05876v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FACT: A Forensic Agent with Compiled Tool-Use Trajectories for AI-Generated Image Detection

## Abstract
AI-generated image detection is increasingly open-world: new image generators produce highly realistic images that make visual artifacts harder to identify. Existing detectors usually rely on a fixed set of forensic cues, so a detector that works well for one generator family may fail on another. We introduce FACT (Forensic Agent with Compiled Tool-use Trajectories), which learns an image-conditioned tool-use policy for forensic analysis. Instead of applying a fixed detector, FACT decides which forensic tools to call, interprets the returned evidence, and stops when sufficient evidence has been collected. FACT follows an Evolve--Distill--Refine pipeline: it evolves an execution-verified forensic skill, compiles the skill into action--observation tool-use trajectories, distills them into a compact agent, and refines the policy with cost-aware GRPO. Across two internal and four public benchmarks, FACT achieves the best performance among all compared methods, including on recent unseen generators, deepfakes, and manipulated images.

## Metadata
- **Published**: 2026-09-05T04:39:49Z
- **Authors**: Jiaoyang Chen, Bin Hu, Jingyu Hu, Kun Zhou, Qin Zhang, Zhengzhe Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05876v1)