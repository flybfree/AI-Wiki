---
title: SkillHEX: Improving Agent Skills via Hypothesis-Driven Autonomous Exploration and Exploitation
published: 2026-08-06T05:51:02Z
authors: Yuru Feng, Yaoqi Chen, Beidi Zhao, Qianxi Zhang, Xinjiang Wang, Jianan Lu, Zhirui Wang, Shusen Xu, Zengzhong Li, Qi Chen
url: http://arxiv.org/abs/2608.05628v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkillHEX: Improving Agent Skills via Hypothesis-Driven Autonomous Exploration and Exploitation

## Abstract
Although agent skills equip LLMs with reusable procedural knowledge, manual maintenance suffers from high costs, unscalability, and misalignment. Real-world deployments thus require autonomous, on-demand skill evolution at test time, constrained by limited interaction budgets and a lack of training or validation sets. This setting introduces a severe sparse reward challenge, where outcomes conflate multiple latent failure causes. Under such ambiguity, existing methods that greedily refine a single incumbent skill are particularly vulnerable to an exploitation trap, allowing early misdiagnoses to exhaust limited trials along unproductive trajectories. To address this, we introduce SkillHEX, a closed-loop framework coupling hypothesis-driven self-verification with evidence-guided tree search. SkillHEX translates falsifiable failure hypotheses into executable tests, producing diagnostic evidence as dense reward without additional environment attempts. This evidence guides a search over persistent skill-revision branches, dynamically balancing the exploitation of supported edits with the exploration of plausible alternatives. Evaluated on 87 tasks from SkillsBench, SkillHEX outperforms existing self-evolving methods and achieves an average pass rate of 55.9% and 57.9% using GPT-5.3-Codex and Claude Opus 4.7 under a five-iteration budget, respectively.

## Metadata
- **Published**: 2026-08-06T05:51:02Z
- **Authors**: Yuru Feng, Yaoqi Chen, Beidi Zhao, Qianxi Zhang, Xinjiang Wang, Jianan Lu, Zhirui Wang, Shusen Xu, Zengzhong Li, Qi Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05628v1)