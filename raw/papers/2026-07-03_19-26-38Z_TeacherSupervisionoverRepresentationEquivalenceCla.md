---
title: Teacher Supervision over Representation Equivalence Classes
published: 2026-07-03T19:26:38Z
authors: Sang Il Han
url: http://arxiv.org/abs/2607.03572v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Teacher Supervision over Representation Equivalence Classes

## Abstract
Knowledge distillation is usually framed as a choice of what to match in the teacher - its logits, hidden features, or sample relations - which presupposes that the teacher's representation has absolute coordinates to match. It does not: a pretrained representation is identifiable only up to an orthogonal-and-isotropic-scaling equivalence class, so a student should learn the teacher's equivalence class, not its features. The organizing fact is that capability is the teacher's output function, a class invariant that factors through the quotient by the class action, so an objective recovers capability exactly when it is defined there. This makes absolute feature matching ill-posed, and admissible supervision a matter of targeting class invariants (Gram structure, CKA, principal subspaces) or aligning coordinates first, unifying feature matching, relational distillation, alignment, and grafting in one geometric account. We validate our framework on Qwen2.5 and Llama-3.1. A restoration study recovers a corrupted model's representation (CKA ~ 0.99) but not its capability, and an ablation isolates the cause: output-function (logit) matching drives capability, while matching hidden representations aligns geometry without restoring function. Recovery is confined to the corpus-covered region, and a graft study confirms that boundary overlap predicts transplant success but is necessary, not sufficient.

## Metadata
- **Published**: 2026-07-03T19:26:38Z
- **Authors**: Sang Il Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.03572v1)