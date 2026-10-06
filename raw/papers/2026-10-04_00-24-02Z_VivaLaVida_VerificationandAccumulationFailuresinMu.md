---
title: Viva La Vida: Verification and Accumulation Failures in Multi-Agent Proof Search
published: 2026-10-04T00:24:02Z
authors: Benji Xu, Ken Zheng, Noah Han
url: http://arxiv.org/abs/2610.04829v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Viva La Vida: Verification and Accumulation Failures in Multi-Agent Proof Search

## Abstract
When an agentic prover works on an open problem, there is no proof assistant to fall back on: its verifier and lemma library are ultimately language models judging model outputs. We instrumented such a system end to end and analyzed $51{,}754$ traced observations across three full runs ($186$ hours, \$$5{,}694$). We find three connected failure modes. First, the three-model verifier requires unanimity and treats parse or API failure as non-approval; in $10$ of $12$ verification events, one member returned no parseable output or an API error, making acceptance arithmetically impossible without surfacing an error. Second, when the ensemble did function, one verifier approved $3$ attempts that GPT rejected, each claiming to resolve the open problem; a single-verifier design would therefore have announced a solution three times. Third, because nothing could be approved, every review was a refutation, yet the lemma extractor mines reviews as well as proofs: $24$ of $93$ lemmas ($26\%$) were extracted from rejected arguments with their refutational context removed. Taken together, these findings show that without external verification, supervision is itself a critical trust boundary: systems must distinguish abstention from rejection, preserve useful disagreement, and preserve the provenance and polarity of information before it becomes future context.

## Metadata
- **Published**: 2026-10-04T00:24:02Z
- **Authors**: Benji Xu, Ken Zheng, Noah Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04829v1)