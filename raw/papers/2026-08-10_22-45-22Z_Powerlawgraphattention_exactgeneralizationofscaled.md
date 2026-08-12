---
title: Power law graph attention: exact generalization of scaled dot-product attention, empirical collapse at inference
published: 2026-08-10T22:45:22Z
authors: Burc Gokden
url: http://arxiv.org/abs/2608.10288v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Power law graph attention: exact generalization of scaled dot-product attention, empirical collapse at inference

## Abstract
The Large Language Model from Power Law Decoder Representations (PLDR-LLM) and its attention, Power Law Graph Attention (PLGA), replace the fixed bilinear form of scaled dot-product attention (SDPA) with a learned, input-generated bilinear operator $G_{LM}$, built from a positive tensor $A_{LM}$ by elementwise power laws. The architecture is fully specified, verified against pinned reference releases; claims are labeled theorem, conditional theorem, measurement, or conjecture. Unconditionally: PLGA contains SDPA exactly at $G_{LM}=I$; $A_{LM}$ and $A_P$ are strictly entrywise positive, with Perron-Frobenius structure on $A_{LM}$; the DAG regularizer has the NOTEARS walk-counting form and positivity obstructs exact acyclicity; and, under nonresonance (satisfied by standard rotary frequencies), a commutant criterion identifies which operators preserve relative-position dependence. An inference-collapse theorem: exact input invariance of deductive outputs collapses inference to generalized SDPA with a constant operator. Measured invariance: relative fluctuations of $10^{-6}$ and below; perturbation bounds quantify but do not certify cached inference; the assembled proxy misses the decoding margin. A conditional three-stage mechanism (rotary twirl, concentration, row-map contraction) is measured on a released checkpoint. Blockwise training and scoring under the global Gram are stated with explicit target exposure; on tested samples, block and sequential scoring select identical answers and agree on the published TruthfulQA probability-mass metric within $5\times 10^{-5}$ per item. Self-organized criticality enters as a phenomenological framework with an intrinsic order parameter; open claims become falsifiable conjectures. Selected proof cores are machine-checked in Lean 4.

## Metadata
- **Published**: 2026-08-10T22:45:22Z
- **Authors**: Burc Gokden
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10288v1)