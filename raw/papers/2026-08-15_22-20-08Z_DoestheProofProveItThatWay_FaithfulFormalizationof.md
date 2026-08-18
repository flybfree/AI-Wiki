---
title: Does the Proof Prove It That Way? Faithful Formalization of Elements Proofs
published: 2026-08-15T22:20:08Z
authors: Tadd Mao, Tianjun Zhong, Dhruva Arekar, Yuming Feng, One An, Jiani Huang, Xujie Si, Ziyang Li
url: http://arxiv.org/abs/2608.15432v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Does the Proof Prove It That Way? Faithful Formalization of Elements Proofs

## Abstract
In formal verification, both the autoformalization of statements and automated proof search have been studied extensively. While automated proof search can produce a formal proof that compiles, the generated proof does not necessarily reflect how the natural-language argument arrives at its conclusion--a property we refer to as faithfulness. With faithfully formalized proofs, one can check the reasoning behind a human- or AI-written argument, and assist mathematicians in formalizing their proof sketches. However, it is particularly challenging due to misalignment of formal proof tactics and natural language reasoning. In this work, we rigorously describe a set of five necessary conditions a faithful formal proof must satisfy, and introduce Pistis, an agentic, oracle-guided proof search that produces formal Lean proofs that satisfy them. At its core is a novel faithfulness-preserving divide-and-conquer search, which we name OrderDecompose, that tracks citation dependencies and blocks unfaithful shortcuts, paired with a refutation search, that surfaces gaps and errors in the natural language proof source. OrderDecompose completes proofs that baselines cannot close even within a 12-hour budget, and its artifacts compile over 33$\times$ as fast as prior work's. We apply Pistis on the first three books of Euclid's Elements, producing high-quality artifacts containing faithful formal proofs. Under a blinded human study and an LLM-as-a-judge protocol on rigorous rubrics, Pistis-generated proofs are favored over prior works--2.89$\times$ and 5.2$\times$ as often by human reviewers and the LLM judge, respectively. It further uncovers gaps in Euclid's proofs and their translation, and can accept or refute natural language proofs written by humans or AI, demonstrating that faithful formalization is useful as a proof-checking tool.

## Metadata
- **Published**: 2026-08-15T22:20:08Z
- **Authors**: Tadd Mao, Tianjun Zhong, Dhruva Arekar, Yuming Feng, One An, Jiani Huang, Xujie Si, Ziyang Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15432v1)