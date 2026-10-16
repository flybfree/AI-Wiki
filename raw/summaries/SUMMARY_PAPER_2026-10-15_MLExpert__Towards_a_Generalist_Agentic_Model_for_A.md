---
title: MLExpert: Towards a Generalist Agentic Model for Autonomous Machine Learning Engineering
url: http://arxiv.org/abs/2610.22344v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_17-56-32Z_MLExpert_TowardsaGeneralistAgenticModelforAutonomo.md
generated_at: 2026-10-15 22:12
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
MLExpert introduces a 35-billion-parameter Mixture-of-Experts agentic model trained through a novel post-training pipeline designed for autonomous, long-horizon machine learning engineering tasks. The paper proposes a combination of hierarchical agentic supervised fine-tuning and Windowed Interaction RL (WIRL) to teach the model to autonomously plan, execute, and adapt optimization strategies across many sequential experiments. On MLE-Bench Lite, MLExpert raises the average medal rate from 37.9% to 72.7%, matching the performance of much larger frontier models, and demonstrates generalization to other benchmark tasks such as NatureBench Lite and algorithm optimization.

## Key Takeaways
- The paper introduces Windowed Interaction RL (WIRL), a reinforcement learning approach that groups the multi-turn decisions between successive experiment results into a single "execution window" and assigns a shared outcome-based reward. This addresses the core challenge that feedback from any single experiment reflects several preceding decisions, making credit assignment across long interaction trajectories extremely difficult. Asynchronous collection and policy correction further allow the model to update its policy before a full trajectory has finished, accelerating learning from intermediate outcomes.
- The training pipeline combines a Kaggle-MLE Factory for constructing executable, realistic ML engineering tasks with hierarchical agentic SFT that transfers general tool-use and coding capabilities into the MLE domain through outcome-guided supervision. This two-stage design ensures the model first acquires broad agentic competence before specializing in long-horizon experimentation workflows, rather than learning everything from scratch.
- Despite being a 35B Mixture-of-Experts model, MLExpert achieves performance comparable to significantly larger frontier models such as Kimi-K3 and GLM-5.3 on MLE-Bench Lite, and its learned optimization capability transfers to unrelated tasks including NatureBench Lite, agent scaffold optimization, and algorithm optimization. This suggests the post-training method captures generalizable strategic reasoning rather than task-specific memorization.

## Context
This work sits at the intersection of AI4AI (AI for AI) research and recursive self-improvement, where LLMs are expected to autonomously design, run, and refine machine learning experiments without human intervention. Prior MLE systems relied on rigid, workflow-driven orchestration, while newer approaches adopt model-directed interaction where the model itself plans experiments. MLExpert addresses the critical gap in training methodology: how to extract useful supervision signals from long, noisy interaction trajectories where each experiment's outcome is entangled with many prior decisions. By formalizing this as a windowed RL problem, the paper provides a concrete training recipe for the next generation of autonomous AI research agents.

## Implications
For practitioners, MLExpert demonstrates that a mid-scale (35B) agentic model can match frontier-scale systems on complex ML engineering benchmarks, potentially lowering the compute and cost barrier for deploying autonomous MLE agents in industry settings such as Kaggle competitions, internal model development pipelines, and automated hyperparameter search. The generalization to NatureBench Lite and algorithm optimization tasks suggests that the learned capability is not narrowly tied to one benchmark but represents a transferable skill in strategic experimentation, which could accelerate AI-assisted scientific discovery and software engineering workflows. For the broader research community, the WIRL framework and the Kaggle-MLE Factory provide reusable infrastructure and training methodology that other groups can adopt to build and evaluate autonomous research agents more efficiently.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22344v1)
