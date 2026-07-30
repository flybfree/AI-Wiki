---
title: The Confounder Trap: Treatment-Encoding Representations in Causal Inference with Text
published: 2026-07-28T22:10:43Z
authors: Marie Neubrander, Graham Tierney, Alexander Volfovsky
url: http://arxiv.org/abs/2607.26309v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Confounder Trap: Treatment-Encoding Representations in Causal Inference with Text

## Abstract
Estimating causal effects of linguistic properties from observational text is difficult because the same document can contain both the treatment of interest and the non-treatment textual attributes needed for adjustment. Existing approaches often learn representations from the full text to capture latent confounding, but when treatment status is itself encoded by words in the text, these representations can directly encode treatment. This creates a confounder trap: richer representations can make treated and control documents separable, inducing overlap violations even when the underlying causal problem satisfies overlap. We study latent text treatments that are encoded through lexicons or other treatment-defining lexical information, and propose masking-based adjustment representations that remove this lexical treatment signal before representation learning. We formalize representation-induced overlap failure, prove that deletion masking preserves overlap for bag-of-words/topic-model representations, and characterize replacement masking as a natural relaxation for large language models that hides treatment-defining tokens while preserving word order and context. Across simulations, masking improves overlap diagnostics, stabilizes treatment effect estimates, and reduces bias relative to adjustment methods that learn from the unmasked text.

## Metadata
- **Published**: 2026-07-28T22:10:43Z
- **Authors**: Marie Neubrander, Graham Tierney, Alexander Volfovsky
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26309v1)