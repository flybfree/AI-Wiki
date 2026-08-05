---
title: BAP-SQL: Budget-Aware Observation Planning for Agentic Text-to-SQL
published: 2026-08-03T20:55:58Z
authors: Chong Peng, Pin Qian, Su Wang, Yihang Chen, Varun Sah
url: http://arxiv.org/abs/2608.02876v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BAP-SQL: Budget-Aware Observation Planning for Agentic Text-to-SQL

## Abstract
Tool-using agents do not merely consume observations: their actions determine what arrives next. In agentic text-to-SQL, a broad query can spend context and database work before useful evidence appears, while post-hoc compression cannot recover omitted rows or expended work. We present BAP-SQL, which treats observation formation as a budget-control stage: it estimates query risk, rewrites SQL when useful, and delegates hard limits to an independent runtime shield. Across general 4B, specialized FINER-SQL 4B, and 7B backbones, BAP-SQL improves tight-budget success. On the primary BIRD-derived setting, it gains 3.4/3.6 percentage points over matched SFT while using 4.5/5.0% fewer tokens. Matched retraining and task-level transfer associate the gain with policy-visible planning and budget-sensitive rescue. The benefit attenuates as model capability and budget increase, reverses at the loosest setting, and does not reduce database work.

## Metadata
- **Published**: 2026-08-03T20:55:58Z
- **Authors**: Chong Peng, Pin Qian, Su Wang, Yihang Chen, Varun Sah
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02876v1)