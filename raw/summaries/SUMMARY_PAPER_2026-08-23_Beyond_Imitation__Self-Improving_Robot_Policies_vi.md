---
title: Beyond Imitation: Self-Improving Robot Policies via Off-Policy Q-Planning
url: http://arxiv.org/abs/2608.21204v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_15-18-37Z_BeyondImitation_Self_ImprovingRobotPoliciesviaOff_.md
generated_at: 2026-08-23 21:10
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper introduces Q‑Planning, a method that augments a large behavior cloning policy with an off‑policy Q‑function to enable self‑improving robot policies. By training the Q‑function on both successful and failed rollouts, it can guide action selection without retraining the BC weights, achieving significant gains across benchmark tasks.

## Key Takeaways  
- The off‑policy Q‑function is trained from deployment rollouts, allowing value estimation that captures failures which behavior cloning cannot.  
- Self‑improvement proceeds by fine‑tuning only the Q‑function while keeping the BC policy frozen, leading to rapid score improvements on LIBERO and RoboTwin benchmarks.  
- The approach improves purely from its own data without human intervention, outperforming supervised fine‑tuning methods that stall at low performance.

## Context  
Modern robotics relies on large language‑like models for manipulation, but self‑learning remains limited by the need for fresh demonstrations. This work demonstrates a scalable way to close the loop between imitation and reinforcement learning using lightweight off‑policy Q‑functions.

## Implications  
The method offers a practical path toward autonomous policy refinement in real robots, reducing reliance on human feedback and enabling continuous improvement without retraining massive models, which is crucial for industry adoption of advanced manipulation systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.21204v1)
