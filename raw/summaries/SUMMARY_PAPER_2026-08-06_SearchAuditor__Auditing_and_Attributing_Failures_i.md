---
title: SearchAuditor: Auditing and Attributing Failures in Long-Horizon Search Agents
url: http://arxiv.org/abs/2608.05212v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-05_09-09-00Z_SearchAuditor_AuditingandAttributingFailuresinLong.md
generated_at: 2026-08-06 21:37
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces SearchAuditBench and SearchAuditor to address the challenge of diagnosing failures in long‑horizon search agents. The benchmark provides expertly annotated failure traces, while SearchAuditor demonstrates that even advanced models can only achieve modest success rates without a specialized auditing framework.

## Key Takeaways
- The benchmark contains 1,243 failed trajectories averaging 73 messages and 65 K tokens, each labeled with the exact error step, root cause, and repair solution.  
- SearchAuditor’s multi‑perspective approach localizes, attributes, and repairs errors using evidence‑grounded adjudication, outperforming baselines across frontier models.  
- When applied to GPT‑5.5, baseline performance drops to 26.6% pass rate, whereas SearchAuditor reaches 32.3% pass rate and improves recovery.

## Context
Long‑horizon search agents rely on sequential web interactions where small reasoning mistakes can cascade into incorrect answers. Existing diagnostic tools require manual inspection of long traces, limiting scalability and accuracy in AI research.

## Implications
Automated auditing reduces the human workload for error detection and enables more reliable deployment of complex search systems. Practitioners can integrate SearchAuditor to improve model robustness and maintain higher pass rates on challenging tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05212v1)
