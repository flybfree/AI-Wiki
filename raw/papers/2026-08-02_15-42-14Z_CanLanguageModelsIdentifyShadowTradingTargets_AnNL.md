---
title: Can Language Models Identify Shadow Trading Targets? An NLP Evaluation of SEC Enforcement Theory
published: 2026-08-02T15:42:14Z
authors: Sarah Wilson, Michael MacKay, Anthony Marello, Trinav Bhattacharyya
url: http://arxiv.org/abs/2608.01322v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can Language Models Identify Shadow Trading Targets? An NLP Evaluation of SEC Enforcement Theory

## Abstract
Shadow trading -- trading in a peer firm's securities on the basis of material nonpublic information (MNPI) about an "economically linked" company -- is a novel and contested theory of insider trading liability, first prosecuted in SEC v. Panuwat (2023). Enforcing it requires identifying economically linked firms ex ante, a determination the SEC makes only after the fact using mass market surveillance infrastructure. We ask whether NLP can do what the SEC's theory presumes insiders already know: identify peer firms ex ante from publicly mandated disclosures. Using a two-stage LLM pipeline applied to Item 7 (Management's Discussion and Analysis) sections of SEC 10-K filings, we score semantic similarity across 30 M&A events spanning five industries and relate similarity to announcement-day abnormal stock returns. On the Panuwat fact pattern itself the pipeline recovers Incyte among the closest peers, a sanity check on the one case with a known outcome. Across the full dataset, however, we find no association: pooling 217 peer observations, the within-event rank correlation between similarity and abnormal return is +0.07 (permutation p = 0.37), and the mean per-event Spearman correlation is +0.05 with a 95% confidence interval of [-0.08, +0.18] -- narrow enough to exclude any moderate relationship rather than merely failing to detect one. A case-level reading agrees: 14 of 30 events support the hypothesis, 12 contradict it, and 4 are ambiguous. We also find that Incyte fell outside the standard \$2B-\$10B mid-cap band on the day before the announcement, complicating the "mid-cap oncology" category the SEC invoked. These results are exploratory and bound to this pipeline, corpus, and return measure, but they put pressure on the empirical premise of shadow trading enforcement and bear on constitutional questions surrounding the SEC's financial surveillance infrastructure.

## Metadata
- **Published**: 2026-08-02T15:42:14Z
- **Authors**: Sarah Wilson, Michael MacKay, Anthony Marello, Trinav Bhattacharyya
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01322v1)