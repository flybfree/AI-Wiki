---
title: Wrong Design Intent Is Worse Than None: A Derangement-Control Diagnosis of Header Conditioning in CAD Program Completion
url: http://arxiv.org/abs/2607.23191v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-25_13-11-23Z_WrongDesignIntentIsWorseThanNone_ADerangement_Cont.md
generated_at: 2026-07-27 22:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CADCON, a study of how fine‑tuned code language models respond to design‑intent headers in CAD program completion. Experiments show that a semantically wrong header harms generation quality and that the effect depends on whether the model has learned a mapping between header content and program behavior.

## Key Takeaways
- A correct 40% prefix header improves textual adherence but degrades geometric correctness, especially for polygonal and thin geometries, indicating the model can render unconditioned designs poorly.  
- The harm persists even when the header marginal distribution is unchanged by shuffling ground‑truth headers (derangement control), proving that a wrong intent actively misdirects generation rather than being noise.  
- Independent geometric scoring reduces the apparent benefit of correct headers, revealing metric circularity, and the effect only appears with a conditional prefix.

## Context
The work addresses a gap in AI research where conditioning on textual design intents is assumed to be benign, yet real‑world CAD systems require precise geometric fidelity. By isolating header content from program generation, CADCON reveals that language models can propagate incorrect specifications into executable outputs.

## Implications
For practitioners, this study warns against relying solely on token‑level metrics when evaluating conditional code generation and underscores the need for domain‑specific validation. In industry, it suggests that fine‑tuned LLMs must be paired with rigorous geometric checks to prevent misdirected design intent from producing unsafe or non‑functional CAD models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23191v1)
