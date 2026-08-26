---
title: PinSieve: Production Selective VLM Serving and a Governed Memory Flywheel for Enterprise Content-Quality Triage
published: 2026-08-25T03:57:56Z
authors: Chuqing Gao, Yuanfang Song, Jonathan Zhang, Yifan Wu, Vishwakarma Singh, Qinglong Zeng, Andrey Gusev
url: http://arxiv.org/abs/2608.24040v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PinSieve: Production Selective VLM Serving and a Governed Memory Flywheel for Enterprise Content-Quality Triage

## Abstract
Enterprise AI agents in production often need to be bounded, stateful, observable, and governable rather than fully autonomous. We present PinSieve, a production case study in a large-scale content-quality pipeline. Its deployed component is a selective vision-language-model (VLM) Serving Agent that operates only on the grey-zone slice left unresolved by lightweight upstream models, exposes a scalar routing score online, and preserves controlled human escalation. On this slice, the deployed system filters 2.05x more non-actionable items than the previous production module while slightly reducing estimated miss rate; after promotion, it improves review productivity by 25.7%, reduces normalized operating cost by 16.2%, and moves signal delivery from next-day to same-day. We then study maintenance through a governed memory flywheel under selective feedback, where escalated items are reviewed by default and auto-passed items are labeled mainly through audit sampling. Feedback Memory records routing traces, observation paths, audit propensities, and replay metadata for evaluation and debugging. The Data Curation Agent uses a bounded proposal-verifier loop over representative, uncertainty, recency, and fresh-review replay, with positive-rate and score-bin guardrails before batch acceptance. In chained monthly refresh over six months of production data, this design reduces average FNR@50% from 17.73% under representative random replay to 13.29%. A Reasoning Review Agent audits teacher-generated rationales and supports keep/repair/drop decisions. Production claims are attributed only to the deployed Serving Agent; replay and rationale-review results are offline or sampled-governance evidence. The same serving-agent recipe has been adopted to several additional internal signals, suggesting transferability beyond one task.

## Metadata
- **Published**: 2026-08-25T03:57:56Z
- **Authors**: Chuqing Gao, Yuanfang Song, Jonathan Zhang, Yifan Wu, Vishwakarma Singh, Qinglong Zeng, Andrey Gusev
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24040v1)