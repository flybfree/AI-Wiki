---
title: ComputerSD: Online Self-Distillation from Real-Time Feedback for Computer-Use Agents
url: http://arxiv.org/abs/2609.40253v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_17-40-09Z_ComputerSD_OnlineSelf_DistillationfromReal_TimeFee.md
generated_at: 2026-09-30 22:06
model: qwen3.6-35b-a3b
---

## Summary
ComputerSD introduces an online self-distillation framework for computer-use agents that leverages real-time feedback from executed GUI transitions to enhance policy learning beyond sparse outcome rewards. By employing a fine-tuned GUI analyzer to generate dynamic guidance and step-level value scores, the method resolves alignment issues inherent in fixed guidance while jointly optimizing token-level on-policy self-distillation with trajectory-level GRPO. Experiments demonstrate significant performance improvements over outcome-only baselines on OSWorld-Verified, validating the efficacy of learning from immediate environmental feedback across diverse backbones.

## Key Takeaways
- Existing computer-use agents suffer from sparse outcome rewards that lack supervision for intermediate actions; ComputerSD addresses this by converting real-time feedback from GUI transitions into continuous guidance signals via a fine-tuned GUI analyzer, which provides privileged context and regulates learning through step-level value scores.
- Direct application of on-policy self-distillation to computer-use agents faces challenges regarding fixed guidance misalignment with the student's state and probability shifts conflicting with correctness; ComputerSD mitigates these by dynamically updating guidance based on executed transitions, ensuring the distillation signals remain relevant and aligned with the agent's current trajectory.
- The method operates within a fully asynchronous training framework that jointly optimizes token-level OPSD and trajectory-level GRPO, achieving superior results over outcome-only GRPO by 1.9 and 4.1 percentage points on OSWorld-Verified using Qwen3-VL-8B-Thinking and EvoCUA-8B backbones, with further evidence of generalizability in out-of-distribution settings.

## Context
The development of autonomous computer-use agents relies heavily on the ability to learn effectively from interaction traces within executable environments. While online training offers a pathway for continuous improvement, the scarcity of dense reward signals has historically constrained the refinement of intermediate decision-making steps. This work situates itself at the intersection of self-distillation techniques and reinforcement learning for GUI automation, proposing a mechanism to extract richer supervisory signals directly from execution dynamics rather than relying solely on final task completion status.

## Implications
The ability to learn continuously from real-time feedback enables more robust and adaptable agents capable of mastering complex software interactions without extensive manual reward engineering or static datasets. Practitioners building GUI automation tools can leverage this approach to accelerate agent convergence and improve success rates in dynamic digital environments, potentially reducing the cost of training specialized models for diverse operating systems and applications. Furthermore, the asynchronous framework design offers a scalable blueprint for deploying online learning systems where latency and resource utilization must be carefully managed during continuous model updates.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.40253v1)
