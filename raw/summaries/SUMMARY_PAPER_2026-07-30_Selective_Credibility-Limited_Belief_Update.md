---
title: Selective Credibility-Limited Belief Update
url: http://arxiv.org/abs/2607.28523v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_17-00-38Z_SelectiveCredibility_LimitedBeliefUpdate.md
generated_at: 2026-07-30 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a new mechanism called selective credibility‑limited belief update that refines how an agent incorporates epistemic inputs when only part of the input can be realized from each source world. By transforming the full input into a weaker proxy before applying credibility restrictions, the framework captures cases where only a subset of possible outcomes is credible. The authors provide both semantic and axiomatic characterizations, identify two well‑behaved sub‑classes, and show that existing approaches are special cases of this unified model.

## Key Takeaways
- Selective credibility‑limited belief update replaces an indivisible epistemic input with a source‑dependent proxy before applying credibility restrictions.  
- The framework is characterized axiomatically: consistency‑preserving operators require transformed inputs to be credible whenever the original input is consistent, and maximal consistency‑preserving operators also demand the proxy be maximally informative among credible consequences.  
- The model encompasses both Katsuno‑Mendelzon belief update (when credibility restrictions are removed) and credibility‑limited belief update (as a special case), demonstrating its generality.

## Context
In AI reasoning, belief updates must handle complex epistemic inputs that may not be fully realizable from every source world. Traditional models assume full applicability or treat the input as a single unit, limiting their ability to model partial information. This paper addresses that gap by allowing selective acceptance of only relevant parts of an input, aligning with real‑world scenarios where sources provide heterogeneous but potentially useful data.

## Implications
For practitioners developing autonomous agents, this framework enables more realistic belief propagation that respects source reliability and information relevance. It can improve decision quality in environments where not all epistemic inputs are trustworthy or fully applicable, offering a principled way to balance flexibility with credibility constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28523v1)
