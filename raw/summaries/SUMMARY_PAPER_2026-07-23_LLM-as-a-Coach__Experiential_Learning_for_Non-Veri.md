---
title: LLM-as-a-Coach: Experiential Learning for Non-Verifiable Tasks
url: http://arxiv.org/abs/2607.18110v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-20_16-08-49Z_LLM_as_a_Coach_ExperientialLearningforNon_Verifiab.md
generated_at: 2026-07-23 23:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Experiential Learning, a method that uses an LLM as a coach to provide rich textual feedback for reinforcement learning on open-ended tasks. By converting this feedback into experiential knowledge, the approach improves policy performance compared with scalar reward RL. The authors show that EL outperforms rubric-based methods and generalizes well beyond training data.

## Key Takeaways
- The coach distills each response’s assessment into transferable experiential knowledge rather than a single scalar reward.
- On-policy context distillation allows the teacher model to internalize this knowledge, which is then learned by the policy.
- EL consistently outperforms rubric-based RL on both held-out and unseen open-ended tasks and reduces reward hacking.

## Context
Open-ended reinforcement learning struggles because traditional reward signals are coarse and can misrepresent task quality. This work addresses that limitation by leveraging fine-grained LLM feedback, offering a higher‑bandwidth supervision channel for model improvement.

## Implications
Practitioners can adopt EL to train agents on complex, non-verifiable tasks where precise human judgment is unavailable. The method suggests that richer supervisory signals may lead to more robust and generalizable AI systems across various applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18110v1)
