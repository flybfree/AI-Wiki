---
title: AI-Based Thesis Assessment: An Empirical Study of Human Evaluation Priorities and Their Impact on Automated Assessment
url: http://arxiv.org/abs/2608.00717v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-01_15-35-56Z_AI_BasedThesisAssessment_AnEmpiricalStudyofHumanEv.md
generated_at: 2026-08-03 21:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
This study surveys 84 thesis supervisors from four disciplines to capture how they weight 35 evaluation criteria, then compares those weights with the default settings of the RubiSCoT AI system. The analysis shows that integrating supervisor‑derived weights modestly reduces average error between human and machine assessments but does not achieve statistically significant improvement.

## Key Takeaways
- Supervisor‑generated criterion weights differ markedly from the AI’s default weights, indicating a gap in how humans prioritize evaluation factors.  
- When these weights are used to calibrate RubiSCoT, the mean relative deviation between AI and human scores drops only slightly from 11.18% to 10.85%, with no statistically significant gain.  
- Human supervisors themselves exhibit lower inter‑supervisor disagreement (mean relative deviation of 4.44%), suggesting that the primary source of variance is not the AI’s weighting scheme.

## Context
AI‑driven thesis assessment aims to automate grading while preserving human standards, yet most systems rely on expert‑set criteria without empirical validation. This paper fills a gap by empirically measuring how real supervisors actually weight their rubrics and testing whether those adjustments translate into better AI performance.

## Implications
For educators and developers, the findings suggest that simply swapping weights may not be enough to align automated grading with human judgment; deeper alignment mechanisms are needed. Practitioners should consider hybrid approaches that combine calibrated AI with targeted feedback to reduce assessment discrepancies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00717v1)
