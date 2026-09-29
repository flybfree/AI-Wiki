---
title: Maat: Independent Deterministic Contract-Based Governance for Multi-Agent LLM Workflows
url: http://arxiv.org/abs/2609.34017v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-27_23-23-52Z_Maat_IndependentDeterministicContract_BasedGoverna.md
generated_at: 2026-09-28 21:42
model: qwen3.6-35b-a3b
---

## Summary
Maat introduces a deterministic runtime governance layer for multi-agent LLM workflows that validates agent-to-agent handoffs against versioned workflow contracts without employing language models in the validation path. While initial evaluations suggested performance improvements, a rigorous post-publication audit revealed that 37% of governance halts were false alarms caused by validator defects rather than model errors. When these false positives are accounted for, Maat demonstrates mixed results: it reduces costs and improves scores in specific workflows but underperforms compared to ungoverned baselines when validator configuration issues are penalized, confirming its utility is limited to contract-expressible defects.

## Key Takeaways
- Maat enforces deterministic validation of handoffs against a versioned workflow anchor, eliminating probabilistic LLM judges from the scoring loop; this approach reduces model-call costs by 17-53% in scenarios where verified defects trigger early halts.
- Corrected analysis shows that on paired trials with confirmed defects, Maat improves rubric scores by +

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34017v1)
