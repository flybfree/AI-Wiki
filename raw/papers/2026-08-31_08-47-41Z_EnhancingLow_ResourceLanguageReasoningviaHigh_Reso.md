---
title: Enhancing Low-Resource Language Reasoning via High-Resource Language Feature Transfer
published: 2026-08-31T08:47:41Z
authors: Minju Song, Hyeon Hwang, Junhyun Lee, Jaewoo Kang
url: http://arxiv.org/abs/2608.30462v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Enhancing Low-Resource Language Reasoning via High-Resource Language Feature Transfer

## Abstract
Large language models exhibit substantial performance variation across languages, even when solving semantically equivalent tasks. Existing analyses often treat this phenomenon as an observational disparity caused by differences in pretraining data, tokenization, or benchmark coverage. We study a complementary hypothesis: high-resource languages (HRLs) may more reliably elicit latent computations useful for task-specific (i.e. mathematical) reasoning, while lower-resource languages (LRLs) may under-activate those computations despite expressing the same task. To test this hypothesis, we introduce a mechanistic intervention framework for identifying and transferring task-relevant sparse latent features across languages. Using sparse autoencoders over residual-stream activations, we isolate features enriched in successful HRL task-specific reasoning while filtering out source-language and generic-generation features. We then construct steering directions from these features and inject them during LRL inference. The resulting interventions test whether the selected features are functionally involved in the observed reasoning gap: suppressing them should impair source-language reasoning, while activating them should partially recover target-language reasoning beyond random and non-task controls. Our framework reframes some cross-lingual reasoning gaps as failures of mechanism elicitation rather than capability absence, and offers a causally testable route to feature-mediated transfer without translation, fine-tuning, or changing the user-facing language.

## Metadata
- **Published**: 2026-08-31T08:47:41Z
- **Authors**: Minju Song, Hyeon Hwang, Junhyun Lee, Jaewoo Kang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30462v1)