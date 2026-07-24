---
title: Best-of-Evidence: Best-of-N Selection under Partial Verification
url: http://arxiv.org/abs/2607.20950v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_06-03-59Z_Best_of_Evidence_Best_of_NSelectionunderPartialVer.md
generated_at: 2026-07-23 23:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Best-of-Evidence (BoE), a framework that improves model selection under partial verification where only parts of a response can be verified. BoE keeps the candidate pool fixed and uses evidence actions to allocate a limited budget, recovering the underlying BoN decision when no budget is spent.

## Key Takeaways
- The framework represents reusable claims with signed candidate--factor graph allowing shared queries across candidates.
- Evidence capacity limits improvement; shared factor queries can achieve O(log K) versus Θ(K) query separation in a factor-code model.
- Experiments show BoE improves fixed-pool selection and rescues some BoN failures when evidence is reliable, contrastive, and decision-relevant.

## Context
Vision-language tasks often provide only partial verification, limiting traditional BoN that needs full responses. This work addresses the gap by allowing selective evidence use without re-evaluating whole candidates.

## Implications
Practitioners can deploy BoE to enhance VQA systems where reliable evidence is scarce, though gains are bounded by channel quality and candidate generation limits. The O(log K) query separation suggests scalable solutions for large pools.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20950v1)
