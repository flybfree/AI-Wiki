---
title: Feyospace-v1: How the Cyber Mercury Seven Trained Frontier Cyber Models
url: http://arxiv.org/abs/2609.08418v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-08_08-26-43Z_Feyospace_v1_HowtheCyberMercurySevenTrainedFrontie.md
generated_at: 2026-09-08 22:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Feyospace-v1, a framework that trains open-weight cyber agents by addressing bottlenecks of model scale, execution cost, teacher sampling, API restrictions, and merged capabilities. It builds five complementary systems to create resettable environments and verifies trajectories with evidence auditing, achieving 23.76% improvement on CyberGym and 10.49% across CTF suites. The three checkpoints rank first among models at comparable scales.

## Key Takeaways
- Choulea analyzes hidden reasoning signatures to guide training, enabling the model to learn from internal traces.
- SkyReal reduces teacher-sampling cost by reusing existing environments, making supervision cheaper and faster.
- Hongzwang bypasses API restrictions on teacher execution, allowing direct use of vulnerable systems as teachers.

## Context
Training cyber agents traditionally relies on massive compute and strict sandboxed environments, which limit open-weight deployment. This work shows that data-centric design can overcome these constraints, opening the door to more accessible and reliable agentic AI.

## Implications
The methodology enables developers to train robust, open models without heavy infrastructure, potentially accelerating research in autonomous cyber systems. Practitioners can adopt similar frameworks to improve model performance while maintaining transparency and safety.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.08418v1)
