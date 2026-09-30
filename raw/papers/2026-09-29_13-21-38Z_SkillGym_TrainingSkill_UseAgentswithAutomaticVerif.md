---
title: SkillGym: Training Skill-Use Agents with Automatic Verifiable Environment Generation
published: 2026-09-29T13:21:38Z
authors: Renxi Wang, Mingshan Hee, Fajri Koto, Timothy Baldwin, Haonan Li
url: http://arxiv.org/abs/2609.37539v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkillGym: Training Skill-Use Agents with Automatic Verifiable Environment Generation

## Abstract
Skills equip LLM agents with professional knowledge and guidance to complete long-horizon and complex tasks. Although skills have been widely adopted in recent agent paradigms and harnesses, how to synthesize reliable training data and how to train agents for skill use remain underexplored. In this work, we propose SkillGym, an automatic pipeline to build verifiable environments, collect trajectories, and train skill-use agents. SkillGym first crawls a large volume of skills from the internet, then keeps those whose workflows can run reproducibly offline. A builder-reviewer pipeline is used to construct difficulty-controlled tasks, spanning four task types, each with a reference solution and an executable verifier. With this pipeline, we build 6.8k environments and collect 19k verified successful trajectories for supervised finetuning. Finetuning on these trajectories improves LLMs of different families and sizes, from 2B to 122B parameters across four skill-use benchmarks; Our Qwen3.5-9B SFT model outperforms the 397B untrained model on two of them. Further analysis shows that training teaches agents to invoke skills, raising the rate of reading the relevant skill from 28% to 96%, and that the gains hold across reasoning structures, extending to task types that form a minority of the training data and to skills held out from training

## Metadata
- **Published**: 2026-09-29T13:21:38Z
- **Authors**: Renxi Wang, Mingshan Hee, Fajri Koto, Timothy Baldwin, Haonan Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.37539v1)