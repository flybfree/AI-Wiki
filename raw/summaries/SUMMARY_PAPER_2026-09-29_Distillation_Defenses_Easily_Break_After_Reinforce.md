---
title: Distillation Defenses Easily Break After Reinforcement Learning
url: http://arxiv.org/abs/2609.35699v1
type: paper-summary
date: 2026-09-29
source_paper: 2026-09-28_17-40-32Z_DistillationDefensesEasilyBreakAfterReinforcementL.md
generated_at: 2026-09-29 01:51
model: qwen3.6-35b-a3b
---

## Summary
This paper challenges the efficacy of current distillation defenses by introducing a more realistic threat model where attackers employ reinforcement learning after the initial distillation phase. The authors demonstrate that defenses which appear robust immediately post-distillation can be easily compromised once the distilled model undergoes further training, effectively breaking these security measures and creating a false sense of safety. Consequently, the study reveals that simple attacks using accessible API data can achieve reasoning improvements comparable to sophisticated full-trace extraction methods when combined with reinforcement learning, rendering many existing defenses ineffective against this enhanced threat vector.

## Key Takeaways
- Existing evaluations of distillation defenses are fundamentally flawed because they assume attackers stop training immediately after copying reasoning traces; however, the paper argues that a realistic threat model must account for subsequent reinforcement learning, which significantly undermines defense mechanisms and invalidates security claims based on static post-distillation assessments.
- Reinforcement learning dramatically lowers the barrier to entry for successful distillation attacks, as the authors demonstrate that attackers can leverage simple techniques using data readily available from current APIs to steal reasoning capabilities, yielding performance gains equivalent to much more complex attacks that require extracting full hidden reasoning traces.
- Any distillation defense that leaks sufficient information to allow the reconstruction of approximate reasoning traces is likely ineffective against this enhanced threat model, prompting the authors to conclude that batch-level distillation defenses may offer a more promising direction for protecting closed-source models from multi-stage extraction strategies.

## Context
As large language models

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.35699v1)
