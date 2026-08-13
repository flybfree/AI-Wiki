---
title: Towards Understanding On-Policy Distillation through the Lens of Test-Time Scaling
url: http://arxiv.org/abs/2608.11829v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_09-13-35Z_TowardsUnderstandingOn_PolicyDistillationthroughth.md
generated_at: 2026-08-12 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates on-policy distillation (OPD) as a post-training method for LLMs and finds that while OPD improves average performance across sampling budgets, its benefit in pass@K diminishes with larger K. It also shows an asymmetry where previously solvable problems become unsolvable under OPD, suggesting the gains are largely due to better sampling efficiency rather than new reasoning capabilities.

## Key Takeaways
- OPD-trained models keep higher avg@K performance across all sampling budgets, indicating improved sample utilization.
- The pass@K advantage shifts toward pre-OPD base models as K increases, revealing diminishing returns in raw answer correctness at large budgets.
- An asymmetry analysis using pass@1024 shows more solvable problems become unsolvable under OPD than the reverse, implying illusory distillation.

## Context
This work addresses a key challenge in LLM fine-tuning: whether post-training methods truly expand reasoning ability or merely optimize inference. By focusing on test-time scaling, it provides empirical insight into how model capabilities evolve with computational resources.

## Implications
For practitioners, OPD should be viewed as an efficiency boost rather than a capability upgrade, guiding resource allocation toward models that maintain performance at scale. The findings caution against overestimating the transformative impact of distillation techniques in real-world deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.11829v1)
