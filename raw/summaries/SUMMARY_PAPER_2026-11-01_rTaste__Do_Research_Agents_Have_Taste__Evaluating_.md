---
title: rTaste: Do Research Agents Have Taste? Evaluating Early Stage Research Judgment
url: http://arxiv.org/abs/2610.40488v1
type: paper-summary
date: 2026-11-01
source_paper: 2026-10-29_17-15-53Z_rTaste_DoResearchAgentsHaveTaste_EvaluatingEarlySt.md
generated_at: 2026-11-01 21:35
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces rTaste, an evaluation framework that tests whether frontier AI research agents possess "taste"—the ability to judge which experiments are worth running before their outcomes are known. By having six frontier models propose, forecast, and rank minimum viable experiments (MVEs) derived from seven recent NLP papers, then auditing all 415 proposed experiments, the study finds that while agents generate many worthwhile experiments, their rankings do not measurably improve the selection of which experiments to actually run compared to simpler baselines.

## Key Takeaways
- Of 415 minimum viable experiments proposed by six frontier models, 194 were judged sound, valuable, and new by auditors, but only 73 (fewer than half of those) were judged to go beyond the seed paper and be non-obvious, indicating that most agent-proposed experiments are incremental rather than genuinely novel contributions to research taste.
- The agents' top-ranked choices matched the auditors' most valued experiment more often than a random pick, but this advantage was not shown to exceed simply choosing the experiment written first in the paper, suggesting that ranking ability does not add meaningful selection value beyond trivial heuristics.
- Forecasting accuracy beat a naive base rate but was not measurably more accurate than a fresh instance of the same model given only the paper and registrations, and multi-agent teams increased cost without a clear overall improvement in proposal quality, undermining the case for team-based research agents.

## Context
As AI agents increasingly participate in scientific discovery pipelines—from hypothesis generation to experiment design—understanding whether they possess genuine research judgment (taste) versus mere pattern replication is critical for the field. This paper addresses a gap in the AI evaluation landscape by moving beyond outcome-based benchmarks to assess the quality of pre-experiment decision-making, a skill that human researchers consider central to effective science. The work sits at the intersection of AI agent evaluation, automated scientific discovery, and the growing debate over whether LLMs can truly reason about research value or merely reproduce surface-level patterns from training data.

## Implications
For practitioners building autonomous research agents, this work cautions against assuming that model-generated rankings or team-based proposals will meaningfully improve experimental selection over simpler strategies, suggesting that current frontier models lack the discriminative judgment needed to prioritize truly novel experiments. For the broader AI research community, the released evaluation harness and dataset of 415 audited MVEs provide a reproducible benchmark for measuring research taste, which could guide future model development toward genuine scientific judgment rather than superficial experiment generation. Industry stakeholders investing in AI-driven R&D pipelines should temper expectations about autonomous agent capabilities in early-stage research planning until stronger evidence of taste emerges.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.40488v1)
