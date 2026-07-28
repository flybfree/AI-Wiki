---
title: Outcome-Confounded Local Supervision in On-Policy Distillation
url: http://arxiv.org/abs/2607.23731v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-26_16-03-33Z_Outcome_ConfoundedLocalSupervisioninOn_PolicyDisti.md
generated_at: 2026-07-27 20:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how on-policy distillation can be misled by outcome-confounded local supervision, introducing an outcome-resolved diagnostic that distinguishes safe imitation from harmful divergence based on final answer correctness. Experiments reveal that agreement-on-failure accounts for a large portion of token mass, indicating a significant flaw in current training practices.

## Key Takeaways
- Agreement-on-failure constitutes 67.84% of pooled response-token mass across two model pairs.
- Even when student accuracy improves to 86.91%, agreement-on-failure remains high at 14.76% on prompts solved by teacher.
- Matched training probes that use available signals do not consistently reduce agreement-on-failure.

## Context
This work highlights a pervasive issue in local supervision methods where divergence is interpreted as error without considering the overall outcome, affecting model reliability and training efficiency.

## Implications
Practitioners must move beyond pointwise metrics to incorporate trajectory-level outcomes for robust evaluation. Future research should explore positional cues or token alignment to resolve this limitation.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23731v1)
