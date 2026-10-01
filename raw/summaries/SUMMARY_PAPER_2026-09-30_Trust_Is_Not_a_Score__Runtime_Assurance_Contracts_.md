---
title: Trust Is Not a Score: Runtime Assurance Contracts for High-Risk AI Agents
url: http://arxiv.org/abs/2609.39717v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_13-28-42Z_TrustIsNotaScore_RuntimeAssuranceContractsforHigh_.md
generated_at: 2026-09-30 22:02
model: qwen3.6-35b-a3b
---

## Summary
This paper addresses the "assurance-transition gap" by introducing Runtime Assurance Contracts (RAC), a formal policy schema that dynamically adjusts an AI agent's authority during execution based on real-time evidence rather than static performance scores. The authors demonstrate through deterministic failure-injection studies that score-based authorization rules frequently fail to block critical risks, whereas RAC enforces non-compensatory gates that mandate escalation or termination when mandatory conditions are unmet. Experimental results show RAC aligns with stateful baselines and human-labeled judgments in synthetic holdout tests, though the authors note these findings are limited to synthetic evaluations and do not yet confirm deployed safety

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.39717v1)
