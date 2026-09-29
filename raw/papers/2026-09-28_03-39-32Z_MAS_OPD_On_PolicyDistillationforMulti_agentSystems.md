---
title: MAS-OPD: On-Policy Distillation for Multi-agent Systems
published: 2026-09-28T03:39:32Z
authors: Qiyong Zhong, Mao Zheng, Mingyang Song, Houcheng Jiang, Jiajie Su, Huwei Ji, Li Zhang, Junfeng Fang
url: http://arxiv.org/abs/2609.34234v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MAS-OPD: On-Policy Distillation for Multi-agent Systems

## Abstract
Multi-agent systems (MAS) split a task across specialized roles and are promising on complex tasks, yet a prevailing approach relies on inference-time orchestration alone. General-purpose APIs are costly and hard to customize, while small models with role prompts rarely develop stable role competence or reliable collaboration, so post-training a MAS jointly is central. Most attempts use reinforcement learning, whose team-level reward leaves undetermined which step of which agent brought about the outcome, while local rewards need redesigning per task. On-policy distillation (OPD) gives token-level teacher supervision on trajectories the student samples, a denser signal needing no local reward, yet is underexplored for the interdependent agents of a MAS. Two difficulties arise: building complementary specialization from a judgement of which role a behavior belongs to while preserving the knowledge all roles need, and turning cross-agent collaborative information into supervision OPD can exploit. We present MAS-OPD, where Role-Advantage Specialization defines the role advantage as the difference between the teacher signals under target and non-target role conditions, and Privileged Attribution for Coordination attributes an interaction conflict to its source and supplies it to the teacher alone as privileged information. Extensive experiments on code and mathematics benchmarks show that MAS-OPD attains the highest mean score at both student scales and leads the agents to develop clearer role specialization and more effective collaborative behavior.

## Metadata
- **Published**: 2026-09-28T03:39:32Z
- **Authors**: Qiyong Zhong, Mao Zheng, Mingyang Song, Houcheng Jiang, Jiajie Su, Huwei Ji, Li Zhang, Junfeng Fang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34234v1)