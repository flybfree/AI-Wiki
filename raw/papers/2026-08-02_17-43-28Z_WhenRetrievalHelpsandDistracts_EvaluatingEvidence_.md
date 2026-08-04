---
title: When Retrieval Helps and Distracts: Evaluating Evidence-Generating LLMs for Biomedical Claim Verification
published: 2026-08-02T17:43:28Z
authors: Pritam Deka, Prabhjot Singh
url: http://arxiv.org/abs/2608.01409v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Retrieval Helps and Distracts: Evaluating Evidence-Generating LLMs for Biomedical Claim Verification

## Abstract
Biomedical fact-checking systems must do more than predict whether a claim is supported, contradicted, or unaddressed: they should also produce evidence that is faithful, complete, and useful for verification. We study this evidence-generation setting on CARE-XAI, a unified benchmark spanning five biomedical and health fact-checking sources. We compare base instruction LLMs, PubMed retrieval-augmented LLMs, fine-tuned LLMs, label-only LLMs, and biomedical encoder classifiers under a shared evaluation protocol. Biomedical classifiers remain strongest for verdict-only prediction, while fine-tuned LLMs are the strongest evidence-generating systems. PubMed retrieval is mixed: it helps PubMed-aligned sources such as PubMedQA and SciFact, but can distract models on broader public-health claims. We introduce Bio-GRACE, a gold-reference-normalized diagnostic for measuring whether retrieved evidence recovers the decision benefit of reference evidence. Bio-GRACE shows that retrieval utility is source-dependent, motivates selective retrieval, and exposes why retrieval recall and lexical evidence overlap are insufficient for biomedical fact-checking.

## Metadata
- **Published**: 2026-08-02T17:43:28Z
- **Authors**: Pritam Deka, Prabhjot Singh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01409v1)