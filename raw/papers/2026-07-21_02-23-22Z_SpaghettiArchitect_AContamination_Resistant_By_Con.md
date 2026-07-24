---
title: Spaghetti Architect: A Contamination-Resistant, By-Construction-Labelled, Multi-Language Code Dataset Generator
published: 2026-07-21T02:23:22Z
authors: Yuxiang Ji
url: http://arxiv.org/abs/2607.18642v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Spaghetti Architect: A Contamination-Resistant, By-Construction-Labelled, Multi-Language Code Dataset Generator

## Abstract
Mined code corpora are abundant but uncontrolled: a snippet's semantics, surface "messiness," and difficulty are whatever the wild contained; there is no known-optimal reference to grade against; and any public sample may already sit in a model's training set. We present Spaghetti Architect, a tool that mints code datasets with the control such corpora lack. An anti-optimization transpiler maps a clean, language-agnostic JSON intermediate representation to deliberately redundant, fully-flattened programs in five languages (Python, JavaScript, Go, Java, C++); every program is compiled, run, and checked against a reference oracle, so each instance is correct by construction. The clean IR is a known-optimal reference, messiness is dialed by strictly-nested anti-pattern profiles, each instance is labelled along two orthogonal difficulty axes, intrinsic (problem size) and incidental (presentation at fixed semantics), and contamination is resisted by minting fresh variants from a private held-out seed. We give construct-validity evidence that the quality order moves established complexity and readability metrics, and report baselines on a four-model open ladder: exact match rises with scale, and the intrinsic knob collapses arithmetic-aggregation accuracy of even the strongest model to zero. Further, development-set scores equal freshly re-minted held-out counterparts within $|Δ|\le 0.012$ (comprehension) and $\le 0.011$ (refactoring); on identical programs, refactoring equivalence ($0.73 \rightarrow 0.99$) is scale-invariant while output prediction collapses; and ablating the generator's self-annotations shows they inflate the weakest model an order of magnitude more than the strongest ($-0.173$ vs $-0.017$): the annotated ladder resolves one of three adjacent pairs where the unannotated resolves all three. Open source (MIT), dependency-free, archived under a persistent DOI.

## Metadata
- **Published**: 2026-07-21T02:23:22Z
- **Authors**: Yuxiang Ji
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18642v1)