---
title: When Policies Change Probabilities: Modular Decision-Making for LLM Code Review
url: http://arxiv.org/abs/2608.02677v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-02_20-09-02Z_WhenPoliciesChangeProbabilities_ModularDecision_Ma.md
generated_at: 2026-08-05 01:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how LLM‑based code reviewers combine risk estimates with approval policies and whether separating these components improves decision quality. Using a large dataset of 15,792 reviewer responses to 720 patches across 360 repository issues, the authors find that high‑cost policies can inflate failure probabilities and increase loss compared with rejecting all patches.

## Key Takeaways
- Replacing an equal‑cost policy with a 10:1 false‑accept rule raises reported failure probabilities by 13.6 to 16.9 percentage points on average, indicating that cost weighting directly influences perceived risk.
- For every reviewer, applying the high‑cost “approve all” rule under equal costs yields worse outcomes than outright rejection, showing that probability elicitation itself adds excess loss.
- A modular pipeline that separates risk estimation from policy and combines it with an independent monitor score reduces mean loss by 0.073 per issue while maintaining a 58–68% acceptance rate.

## Context
The study addresses a core challenge in AI‑assisted software engineering: ensuring that model outputs reflect the true probability of failure rather than being distorted by downstream cost functions. By decoupling risk estimation from policy decisions, researchers can design more transparent and reliable review systems.

## Implications
Separating risk from action encourages developers to evaluate models without bias toward costly approvals, leading to better calibrated probabilities and reduced overall loss in code quality management. This approach could be adopted across AI‑driven development pipelines to improve trust and efficiency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02677v1)
