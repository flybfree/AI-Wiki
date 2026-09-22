---
title: Judging a Review by its Cover: A Reliability Analysis of LLM-based Peer Review Evaluation Metrics
published: 2026-09-20T00:49:57Z
authors: Shakiba Amirshahi, Sajad Ebrahimi, Hai Son Le, Negar Arabzadeh, Ebrahim Bagheri
url: http://arxiv.org/abs/2609.23264v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Judging a Review by its Cover: A Reliability Analysis of LLM-based Peer Review Evaluation Metrics

## Abstract
Peer-review evaluation is increasingly being automated with LLM-as-a-judge metrics, but this creates a measurement risk. A review may receive a high score because it is fluent, organized, and polished, rather than because it provides a strong evaluation of the paper. This risk is especially important in AI-assisted reviewing, where reviewers may use LLMs to improve clarity or presentation while preserving the underlying judgments. We propose a statistical framework for testing whether peer-review evaluation metrics capture substantive review quality beyond surface-level linguistic form. The framework compares original human reviews with faithful LLM rewrites that preserve the same evaluative content while changing wording and presentation. Using a dataset comprising 4,044 meaning-preserving rewrites derived from 674 human reviews from ICLR and NeurIPS, we evaluate 29 content-oriented peer-review evaluation metrics drawn from four prior works through complementary tests of surface sensitivity and robustness. Although these metrics are intended to capture review properties beyond surface-level, writing-dependent characteristics, we find that sensitivity to rewriting is widespread. Under our primary analysis, 23 metrics assign significantly different scores to reviews whose evaluative content is preserved, while only six satisfy our robustness criterion. The patterns are largely consistent across two LLM judge models, suggesting that the issue is not specific to a single judge. These findings show that many peer-review evaluation metrics partially conflate review quality with linguistic presentation, and indicate that robustness to meaning-preserving rewriting should be validated before such metrics are used to compare human-written, AI-assisted, and AI-generated reviews.

## Metadata
- **Published**: 2026-09-20T00:49:57Z
- **Authors**: Shakiba Amirshahi, Sajad Ebrahimi, Hai Son Le, Negar Arabzadeh, Ebrahim Bagheri
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.23264v1)