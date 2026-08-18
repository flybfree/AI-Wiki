---
title: Reconstruction: A Blind Benchmark for Recovering Research Ideas from Pre-Publication Bibliographies
published: 2026-08-17T14:44:30Z
authors: Shaolong Chen, Yanlin Fei, Nazhou Liu, Xinmiao Yu, Lei Li, Rahul Thapa, Madalina Ciobanu, Qingqing Mao, Ritankar Das
url: http://arxiv.org/abs/2608.16645v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reconstruction: A Blind Benchmark for Recovering Research Ideas from Pre-Publication Bibliographies

## Abstract
Can a language model recover the true research idea of a published paper when given only that paper's pre-publication bibliography? We introduce Reconstruction, a blind idea-recovery benchmark that withholds the seed paper and all contemporaneous or future literature, and asks models to propose hypotheses that an independent large language model judge matches against the held-out ground-truth idea. A strict anti-leakage protocol-temporal citation cutoff, anonymous reference IDs, and frozen per-paper bibliographies, which prevents prompt-time leakage of the seed idea. Across six scientific domains and 643 evaluated papers, seven frontier models achieve only modest Match rates (approx. 3-15%). We then evaluate a reference-only multi-agent (top 4) pipeline that combines cross-model review with a Swiss tournament over aligned hypothesis slots, without external web search. Cross-model review plus tournament selection raises Match rates to approx. 23-42% across all six domains, which is an observed approx. 2.4x lift over the best single-model baseline. This draft reports the protocol, anti-leakage design, and current results as an arXiv timestamp.

## Metadata
- **Published**: 2026-08-17T14:44:30Z
- **Authors**: Shaolong Chen, Yanlin Fei, Nazhou Liu, Xinmiao Yu, Lei Li, Rahul Thapa, Madalina Ciobanu, Qingqing Mao, Ritankar Das
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16645v1)