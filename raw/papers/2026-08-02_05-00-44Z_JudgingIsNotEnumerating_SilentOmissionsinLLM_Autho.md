---
title: Judging Is Not Enumerating: Silent Omissions in LLM-Authored Acceptable Sets
published: 2026-08-02T05:00:44Z
authors: Wenhui Chen, Jianlin Chen, Ziyao Lin, Peiji Long, Chi Man Vong
url: http://arxiv.org/abs/2608.01000v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Judging Is Not Enumerating: Silent Omissions in LLM-Authored Acceptable Sets

## Abstract
Language models are increasingly promoted from examinees to examiners: they write the test suites, answer keys, rubrics, and reward functions that define correctness for other systems. We measure the capability that role assumes and find it lacking under the protocol the role is usually deployed with, one-shot greedy authoring with no test-time reasoning. Across four reference constructions - two with complete finite truth, one with a hardened executable reference (HumanEval+/MBPP+), one with an explicitly incomplete lexical reference (WordNet) - models judge whether a candidate belongs far better than they author the set itself. On the incompleteness-proof algorithmic construction the gap is +0.34 to +0.29 F1 over a 24x parameter range and does not close; on executable code, models judging at F1 0.74-0.90 author suites admitting only 19-42% of oracle-correct solutions. A control locates the deficit: asked to emit the predicate rather than its extension, the same models reach F1 about 0.99. The failure is not missing knowledge or an inability to specify, but an inability to materialise the region a specification induces. The dominant error is omission, which resists audit: an over-inclusion is a token a reviewer can challenge, a missing member an absence whose discovery is the authoring problem itself. Models detect planted over-inclusions 6-7x more often than planted omissions, and a production deployment of 43,227 items fails omission-first at 10:1. Wired into RLVR, an authored key costs 1.9 points of accuracy against an exact oracle and 18.5 WordNet-relative (six paired seeds, p=0.031). Gating authored verifiers on a known-correct probe cuts false rejection from 58-92% to at most 5%, but keeps only 5-39% of suites. Repairing them instead, by rewriting each wrong expected value to what a reference execution returns, raises yield 3.3-10.6x across four author families.

## Metadata
- **Published**: 2026-08-02T05:00:44Z
- **Authors**: Wenhui Chen, Jianlin Chen, Ziyao Lin, Peiji Long, Chi Man Vong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01000v1)