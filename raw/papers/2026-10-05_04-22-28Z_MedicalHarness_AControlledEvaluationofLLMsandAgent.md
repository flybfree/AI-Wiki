---
title: MedicalHarness: A Controlled Evaluation of LLMs and Agent Harnesses on Medical Tasks
published: 2026-10-05T04:22:28Z
authors: Ziqing Wang, Lili Zhao, Kaize Ding
url: http://arxiv.org/abs/2610.05778v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MedicalHarness: A Controlled Evaluation of LLMs and Agent Harnesses on Medical Tasks

## Abstract
LLM agents are increasingly built for medical work and scored on clinical benchmarks. Each such score, however, comes from a model running inside an agent harness, the system that controls the loop between the model and its environment. An agent's score is therefore a property of a model--harness pair. For medical agents, how much outcomes change with the harness has rarely been measured. Measuring this change, and explaining it, raises two challenges. First, a harness comparison must change nothing but the harness and be repeated across models and kinds of task. Second, comparing whole harnesses leaves their mechanisms bundled together, so it cannot show when an individual mechanism helps. To address these challenges, we present MedicalHarness, a controlled study of models and agent harnesses on medical tasks. We first build MedicalHarnessBench to evaluate agents on $107$ tasks across four domains that each test a different harness capability. Using this benchmark, we run five open-weight models under five agent harnesses, changing only the harness within a comparison, and analyze both outcomes and execution traces. To study individual mechanisms, we build MH-Lab, a controlled harness that switches off context management, planning or tool exposure one at a time within a shared execution loop. We find that the harness and its interaction with the model account for about a quarter of the outcome variance, and that no single harness is best across models and tasks. Code and data are available at https://github.com/REAL-Lab-NU/MedicalHarness.

## Metadata
- **Published**: 2026-10-05T04:22:28Z
- **Authors**: Ziqing Wang, Lili Zhao, Kaize Ding
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.05778v1)