---
title: DIVE: Unlocking Self-Improvement in Frozen Language Models Through Diversity-Driven Skill Evolution
published: 2026-08-12T18:06:41Z
authors: Siheng Xiong, Ali Payani, Oguzhan Gungordu, Faramarz Fekri
url: http://arxiv.org/abs/2608.12486v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DIVE: Unlocking Self-Improvement in Frozen Language Models Through Diversity-Driven Skill Evolution

## Abstract
Large language models (LLMs) cannot retain post-deployment experience without parameter updates. We introduce DIVE, a diversity-driven framework that enables frozen LLMs to improve by evolving persistent natural-language skills from task experience and verifier feedback. These skills encode reusable reasoning procedures, verification strategies, common failure modes, and output constraints and are both executed and revised by the same underlying model without access to a teacher model. Since natural-language skill evolution is a stochastic, non-convex search process, optimizing a single skill trajectory can overfit to sampled experience or converge to a suboptimal solution. DIVE mitigates this optimization variance by independently evolving multiple skill populations from bootstrapped experience, adaptively refining them through diverse transformations, and jointly selecting a complementary set of skills. Across six mathematical and logical reasoning tasks and multiple model families, DIVE consistently outperforms existing reasoning methods, prompt-optimization approaches, skill-development frameworks, and memory-based baselines. It achieves rapid self-improvement from accumulated experience, obtaining substantially larger performance gains with fewer rollouts than parameter-based methods such as SFT and GRPO, and prompt optimization with GEPA. Further, the resulting skills transfer across model scales and families, enabling smaller models such as GPT-5-nano to match or outperform larger counterparts, i.e., GPT-5, under conventional prompting. These results establish diversity-driven skill evolution as an effective, interpretable, and parameter-free approach to LLM self-improvement.

## Metadata
- **Published**: 2026-08-12T18:06:41Z
- **Authors**: Siheng Xiong, Ali Payani, Oguzhan Gungordu, Faramarz Fekri
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12486v1)