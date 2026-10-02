---
title: OverAct: Measuring and Mitigating Proactive Over-Authorization in LLM Tool-Calling Agents
published: 2026-10-01T11:44:45Z
authors: Taolin Zhang, Jiuheng Wan, Hanyu Wang, Tingyuan Hu, Chengyu Wang
url: http://arxiv.org/abs/2610.01508v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# OverAct: Measuring and Mitigating Proactive Over-Authorization in LLM Tool-Calling Agents

## Abstract
LLM agents with tool-calling capabilities can access external services and private user data, but they may retrieve more information than a user's request explicitly requires. We study this behavior in structured tool-calling agents and term it proactive over-authorization. This setting differs from filesystem-level coding agents because the main risk is unnecessary access to private data. We introduce OverAct, a controlled benchmark spanning eight privacy-sensitive domains with deterministic, judge-free scoring, together with an interpretive decision-theoretic framework that yields three testable predictions. Across seven models from four families, all models significantly exceed authorized scope. Request specificity is the strongest predictor of severity, over-authorization grows sublinearly with tool-pool size, and decoding temperature has little effect. These patterns are consistent with a cost-asymmetry account, suggesting that over-authorization arises more from structural decision tendencies than from decoding randomness. We also propose SelfAudit, a zero-shot inference-time method that generates request-grounded justifications and filters unjustified calls before execution. Ablation shows that explicit filtering is the main driver of scope reduction. SelfAudit reduces privacy-oriented excess by 43% without oracle knowledge.

## Metadata
- **Published**: 2026-10-01T11:44:45Z
- **Authors**: Taolin Zhang, Jiuheng Wan, Hanyu Wang, Tingyuan Hu, Chengyu Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.01508v1)