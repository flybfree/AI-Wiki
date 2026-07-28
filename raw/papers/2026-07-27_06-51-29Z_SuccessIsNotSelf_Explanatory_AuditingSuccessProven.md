---
title: Success Is Not Self-Explanatory: Auditing Success Provenance in Agent Evaluation
published: 2026-07-27T06:51:29Z
authors: Jingkun Luo, Da-Tian Peng
url: http://arxiv.org/abs/2607.24054v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Success Is Not Self-Explanatory: Auditing Success Provenance in Agent Evaluation

## Abstract
A correct answer can conceal why an agent succeeded. Once agents change their information state during evaluation, correctness no longer distinguishes intended reasoning from answer acquisition. Outcome evidence and exposure detection do not establish whether success depended on an acquired target; we call this missing evaluation object success provenance. AcquaBench audits it through matched CLEAN, GOLD, and SHAM value substitution on four standardized surfaces with joint qid-clustered analysis. CLEAN retains benchmark-authorized information. GOLD makes the correct target available. SHAM preserves source structure and exposure opportunity but substitutes a matched incorrect value. GOLD minus CLEAN measures the total score response to correct-target availability; GOLD minus SHAM tests whether that response tracks target correctness beyond matched source exposure. In D0, GOLD exceeds SHAM by 19.1 to 25.9 percentage points, showing that success follows the correct value. In D2, GOLD still exceeds SHAM under distributed sufficiency while coloc no longer transfers as a high-score marker, with AUROC 0.376 and 0.142. Behavioral dependence can thus persist beyond this probe's intended observation unit. In model comparison, a supported 5.0-point CLEAN score gap compresses to a raw GOLD difference of -0.6 points without establishing rank inversion. Agent benchmarks should report success together with whether the evaluated information state supported it.

## Metadata
- **Published**: 2026-07-27T06:51:29Z
- **Authors**: Jingkun Luo, Da-Tian Peng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24054v1)