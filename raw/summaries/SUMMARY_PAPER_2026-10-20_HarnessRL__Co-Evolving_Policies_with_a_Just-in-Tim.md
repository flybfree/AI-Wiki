---
title: HarnessRL: Co-Evolving Policies with a Just-in-Time Training Harness for Open-Ended RL
url: http://arxiv.org/abs/2610.26426v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-19_13-53-38Z_HarnessRL_Co_EvolvingPolicieswithaJust_in_TimeTrai.md
generated_at: 2026-10-20 00:15
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
HarnessRL introduces a training-time harness that co-evolves with a reinforcement learning policy during open-ended generation training, addressing two failure modes in rubric-based RL: non-discriminative rewards where scores collapse uniformly, and spurious rewards where higher scores do not reflect genuinely better responses. The system dynamically adjusts task sampling, rollout guidance, and rubric criteria through a memory-augmented evolver and a just-in-time critic loop, outperforming the strongest baselines by 2.8 to 3.1 points on a new five-domain benchmark while nearly halving the training steps required to reach its best checkpoint.

## Key Takeaways
- HarnessRL identifies that fixed training configurations—static task sampling, fixed exploration strategies, and unchanging evaluation rubrics—cause reward signals to degrade as the policy improves, producing either uniformly low/high scores (non-discriminative rewards) or inflated scores disconnected from response quality (spurious rewards). The solution is a training-time harness with three adaptive interfaces that update in lockstep with the evolving policy.
- The harness evolver maintains a training-time memory capturing within-task history and cross-task evidence, attributing each reward failure to the specific interface (task sampling, rollout guidance, or rubric criteria) whose update can remedy it. A proposer generates candidate updates, and a just-in-time critic accepts a candidate only after empirically measuring its effect on the current frozen policy, returning rejected candidates for revision rather than applying unvalidated changes.
- The authors curate Rubric-Mix-10k, a five-domain evaluation suite spanning medical, science, writing, role-play, and instruction-following tasks, and demonstrate that HarnessRL outperforms the strongest baselines by 2.8 to 3.1 points across both 4B and 9B parameter model scales while requiring nearly half the training steps to reach its best checkpoint, indicating substantial efficiency gains.

## Context
Rubric-based reinforcement learning has emerged as a practical approach for training language models on open-ended generation tasks where scalar rewards are unavailable, relying instead on natural-language evaluation criteria. However, the field has largely treated the training configuration as static, assuming that a fixed set of tasks, exploration budgets, and rubric definitions remain adequate throughout training. HarnessRL challenges this assumption by demonstrating that reward signal quality is a moving target that must be actively maintained as the policy evolves, bridging the gap between curriculum learning, self-play, and adaptive evaluation in a unified framework.

## Implications
For practitioners deploying RL fine-tuning pipelines on open-ended tasks, HarnessRL offers a concrete recipe for preventing reward collapse and reward hacking without requiring manual intervention or additional human annotation, potentially reducing training compute by roughly half. For the broader research community, the co-evolving harness paradigm suggests that future RL systems for language generation should treat evaluation infrastructure as a first-class trainable component rather than a fixed scaffold, opening directions for automated curriculum design and self-correcting reward pipelines in model training at scale.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.26426v1)
