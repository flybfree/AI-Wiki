---
title: When Does Muon Help Agentic Reinforcement Learning?
url: http://arxiv.org/abs/2607.16169v1
type: paper-summary
date: 2026-07-19
source_paper: 2026-07-17_17-49-05Z_WhenDoesMuonHelpAgenticReinforcementLearning.md
generated_at: 2026-07-19 21:00
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates the impact of Muon optimizer on agentic reinforcement learning using Qwen2.5-0.5B-Instruct on ALFWorld with Group-in-Group Policy Optimization. It finds that applying Muon to hidden weight matrices improves final-window validation success from 0.290 to 0.546, while AdamW yields no improvement at high rates.

## Key Takeaways
- Applying Muon only to hidden weight matrices raises final-window validation success from 0.290 to 0.546 in sparse-reward agentic RL on ALFWorld.
- The effect of Muon depends on the advantage estimator and learning rate; at 3e-5 it improves GRPO from 0.161 to 0.268, whereas GraphGPO's gap narrows near saturation.
- At 1e-5, GraphGPO with Muon reaches 0.901 success, raising normalized validation AUC from 0.399 to 0.556 and achieving 0.5/0.75 thresholds earlier.

## Context
Agentic reinforcement learning requires efficient optimization of policy parameters in large language models, where traditional optimizers like AdamW may not capture fine-grained updates needed for sparse rewards. This study highlights how optimizer choice interacts with RL algorithms to affect performance metrics such as validation success and AUC.

## Implications
Practitioners should consider integrating Muon into their RL pipelines rather than relying solely on standard optimizers to maximize reward efficiency in large models. The findings suggest that joint optimization of optimizer, advantage estimator, and learning rate is crucial for reliable agentic behavior.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.16169v1)
