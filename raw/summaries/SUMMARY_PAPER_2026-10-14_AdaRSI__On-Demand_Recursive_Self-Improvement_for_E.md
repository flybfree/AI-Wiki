---
title: AdaRSI: On-Demand Recursive Self-Improvement for Embodied Agents
url: http://arxiv.org/abs/2610.20474v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_16-51-09Z_AdaRSI_On_DemandRecursiveSelf_ImprovementforEmbodi.md
generated_at: 2026-10-14 21:51
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
AdaRSI introduces an on-demand recursive self-improvement framework for embodied agents that determines when and how to update the weights of a vision-language-action (VLA) executor rather than blindly fine-tuning all components. The framework operates in three stages—harness and skill refinement, failure attribution via state-replay retries, and selective fine-tuning of only persistently unreliable sub-steps—and demonstrates on RoboCasa365 that it raises success on unseen composite tasks from 4.6% to 13.8% while consuming only 28% of the GPU time and 22% of the self-collected demonstrations required by blanket fine-tuning.

## Key Takeaways
- AdaRSI reframes the central question of embodied self-improvement from "how do we improve?" to "when should we change the executor's weights?" Existing RSI methods either keep the executor frozen and only refine the surrounding harness (which cannot introduce a missing motion primitive) or fine-tune the executor on every persistent failure without diagnosing whether the failure stems from incorrect invocation or a genuine capability gap. AdaRSI explicitly attributes each failure before deciding whether to act.
- The three-stage pipeline first lets a coding agent improve its own skills and harness, then replays failing sub-steps from saved intermediate states to isolate which sub-steps remain unreliable after harness improvements, and finally fine-tunes only those sub-steps using demonstrations the agent collects itself and experience transferred from earlier tasks. This selective strategy means the system avoids wasting compute on sub-steps that were already fixed by harness changes.
- On all 50 target tasks of RoboCasa365 using GR00T N1.5 as the executor with zero human demonstrations, AdaRSI improves performance across all three evaluation suites. Compared with fine-tuning every sub-step indiscriminately, AdaRSI achieves slightly higher success while using only 28% of the GPU time and 22% of the self-collected demonstrations, and the ablation shows that fine-tuning without first improving the harness trains more yet gains far less, underscoring that harness refinement is a prerequisite for effective weight updates.

## Context
Recursive self-improvement has emerged as a promising paradigm for closing the gap between pretrained foundation models and the demands of long-horizon, open-world tasks. In embodied AI, however, the problem is compounded: failures can originate in the planning harness, the executor's learned representations, or the interface between the two. Prior embodied RSI work has treated these failure modes as interchangeable, leading to either brittle harness-only improvements or wasteful, undifferentiated fine-tuning. AdaRSI addresses this gap by introducing a principled attribution step that separates harness-level bugs from executor-level capability gaps, a distinction that is essential for any system expected to autonomously improve without human supervision.

## Implications
For robotics and embodied-AI practitioners, AdaRSI offers a blueprint for building self-improving agents that can operate in deployment settings where human demonstrations are unavailable and compute budgets are constrained. The finding that selective fine-tuning outperforms blanket fine-tuning while using a fraction of the resources suggests that future embodied-agent pipelines should invest heavily in failure-attribution and harness-refinement stages before ever touching model weights. More broadly, the framework signals a shift in the self-improvement literature from "improve everything" to "improve what is actually broken," a principle that could inform the design of autonomous learning systems across domains beyond robotics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.20474v1)
