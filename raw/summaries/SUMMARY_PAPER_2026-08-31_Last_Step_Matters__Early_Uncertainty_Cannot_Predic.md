---
title: Last Step Matters: Early Uncertainty Cannot Predict Failure in Long-Horizon Agents
url: http://arxiv.org/abs/2608.29685v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-30_09-43-08Z_LastStepMatters_EarlyUncertaintyCannotPredictFailu.md
generated_at: 2026-08-31 21:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether early uncertainty signals can reliably predict failure in long‑horizon agents and finds that they do not. Verbal confidence is useful only at the end of a trajectory, while intermediate signals provide limited predictive power, highlighting a gap between early detection and successful completion.

## Key Takeaways
- Verbal confidence reaches peak discriminative ability near trajectory completion with an AUROC of 0.85 but offers no advantage before 50% progress where it stays below 0.60.  
- All uncertainty metrics—including perplexity and other measures—fail to predict failure earlier in the execution, indicating a breakdown in early warning signals.  
- The discrepancy is attributed to frequent path switching, which disrupts the continuity between early uncertainty readings and final outcomes.

## Context
Long‑horizon agents often require extensive computation and tool use, making failure prediction crucial for efficiency. Uncertainty quantification has been proposed as a low‑cost alternative to full inference, yet its practical utility remains uncertain due to the dynamic nature of agent behavior over time.

## Implications
Practitioners should rely on final‑step confidence rather than in‑trajectory interventions to decide whether to restart an agent, reducing unnecessary effort. This shift could lower resource consumption and improve overall performance in deep‑research environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29685v1)
