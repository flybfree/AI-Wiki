---
title: ProAS: A Progress-Aware Advantage Shaping Framework for Multi-Turn Agentic Reinforcement Learning
url: http://arxiv.org/abs/2610.18683v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_16-39-38Z_ProAS_AProgress_AwareAdvantageShapingFrameworkforM.md
generated_at: 2026-10-14 02:00
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces ProAS (Progress-Aware Advantage Shaping), a plug-and-play framework designed to solve the uniform credit assignment problem inherent in critic-free reinforcement learning algorithms like GRPO when training multi-turn LLM agents. By leveraging a dynamically evolving Agentic Reference Graph to perform fine-grained credit assignment through two novel mechanisms—Masking Unreasonable Incentives and Asymmetric Penalty Redistribution—ProAS achieves state-of-the-art success rates on ALFWorld (up to 94.3%) and WebShop (up to 70.8%) while accelerating training convergence by up to 2.44× without introducing critic model overhead.

## Key Takeaways
- The core problem identified is that existing critic-free group-based RL methods (e.g., GRPO) broadcast trajectory-level advantages uniformly across all actions in a trajectory, which structurally reinforces invalid or suboptimal actions embedded within otherwise successful trajectories and fails to account for the cascading downstream consequences of early pivotal deviations in failed trajectories. This uniformity fundamentally limits the agent's ability to learn from multi-turn interactions.
- ProAS addresses this through two complementary mechanisms: Masking Unreasonable Incentives (MUI) suppresses the reinforcement signal for structurally invalid actions within preferred trajectories, while Asymmetric Penalty Redistribution (APR) redistributes penalties in unpreferred trajectories to highlight the true causal origin of failure rather than penalizing all downstream actions equally. Both mechanisms are driven by a dynamically evolving Agentic Reference Graph (ARG) that encodes valid action sequences and progress states.
- The framework is validated on Qwen2.5-1.5B-Instruct and Qwen2.5-7B-Instruct models, demonstrating universal performance gains over mainstream group-based baselines. Critically, ProAS maintains strong robustness even when the ARG is imperfect or distilled from other sources, and it accelerates convergence by up to 2.44×, making it practical for resource-constrained training pipelines.

## Context
Multi-turn agentic tasks such as interactive game-playing (ALFWorld) and web navigation (WebShop) require LLMs to make sequential decisions where early errors cascade into later failures, making credit assignment fundamentally harder than single-step RL. The field has increasingly adopted critic-free group-based methods like GRPO to avoid the computational cost of training value networks, but these methods treat every action in a trajectory as equally responsible for the outcome. ProAS sits at the intersection of RL credit assignment research and practical LLM agent training, offering a principled solution that does not require architectural changes to existing training pipelines.

## Implications
For practitioners training LLM agents on interactive, multi-step tasks, ProAS provides a drop-in improvement to existing GRPO-style training pipelines that yields higher success rates and faster convergence without additional model parameters or critic networks, lowering the barrier to effective agent training. For the broader AI research community, the paper demonstrates that structured progress-aware signals derived from reference graphs can substitute for learned critics in credit assignment, opening a path toward more interpretable and efficient RL training for agentic systems. The robustness to imperfect ARGs further suggests that such frameworks can be deployed in settings where ground-truth action sequences are noisy or partially available, which is common in real-world deployment scenarios.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.18683v1)
