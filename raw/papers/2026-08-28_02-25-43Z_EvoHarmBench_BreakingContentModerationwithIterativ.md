---
title: EvoHarmBench: Breaking Content Moderation with Iterative Human-Like Evasion
published: 2026-08-28T02:25:43Z
authors: Ruijie Jian, Benlei Cui, Ting Ma, Haidong Ding, Kangwei Liu, Ziwen Xu, Longtao Huang, Hui Xue, Ziqiang Zhu, Junjie Li, Haiwen Hong
url: http://arxiv.org/abs/2608.27844v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EvoHarmBench: Breaking Content Moderation with Iterative Human-Like Evasion

## Abstract
Existing evaluations of harmful content detection rely predominantly on static benchmarks, which struggle to reflect the interactive adversarial ecosystem of real-world content platforms where users continuously revise their expressions in response to moderation feedback. This mismatch creates a significant performance gap between offline benchmark scores and online deployment effectiveness. To the best of our knowledge, we present EvoHarmBench, the first dynamic adversarial evaluation framework for content moderation systems. The framework employs an iterative optimization loop that evolves evasion strategies at the semantic-cluster level, while simultaneously optimizing for evasion success and human readability. We systematically evaluate LLM-based defense models which are widely used in real world moderation systems. The evaluation covers 229 semantic sub-clusters across five violation categories, derived from 5,002 real-world adversarial samples collected from content platforms. Our experiments reveal substantial vulnerabilities even in leading commercial systems: after twelve optimization iterations, the attack success rate under readability constraints reaches 80.3% within SOTA LLM moderators. We will release the full benchmark data, evaluation framework, and code to encourage a shift from static benchmarking toward dynamic adversarial evaluation in content safety research.

## Metadata
- **Published**: 2026-08-28T02:25:43Z
- **Authors**: Ruijie Jian, Benlei Cui, Ting Ma, Haidong Ding, Kangwei Liu, Ziwen Xu, Longtao Huang, Hui Xue, Ziqiang Zhu, Junjie Li, Haiwen Hong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27844v1)