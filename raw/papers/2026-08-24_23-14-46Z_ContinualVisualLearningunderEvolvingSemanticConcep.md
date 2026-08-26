---
title: Continual Visual Learning under Evolving Semantic Concept Shift
published: 2026-08-24T23:14:46Z
authors: Ismail Lamaakal, Chaymae Yahyati, Yassine Maleh, Khalid El Makkaoui, Ibrahim Ouahbi
url: http://arxiv.org/abs/2608.23903v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Continual Visual Learning under Evolving Semantic Concept Shift

## Abstract
Visual foundation models are commonly adapted under the assumption that the appearance of incoming data may change while the semantic meaning of the prediction task remains fixed. In long-lived visual systems, however, taxonomies, policies, and concept definitions can themselves evolve, causing the same visual evidence to require a different interpretation. We study this setting as evolving semantic concept shift and introduce SemReWrite, a framework for selectively updating obsolete visual--semantic mappings while preserving knowledge that remains valid. SemReWrite represents changes between old and revised semantic specifications, combines semantic discrepancy with sparse revised supervision to localize affected visual regions, and uses an input-dependent low-rank rewriting mechanism together with structured semantic memory, preservation, and obsolete-decision suppression. We further introduce EvoShift-Bench, spanning ImageNet, iNaturalist, CUB-200-2011, and DomainNet, with semantic transitions including class split, merge, boundary revision, insertion, partial redefinition, recurrence, and mixed semantic--appearance shift. To explicitly evaluate selective semantic revision, we introduce Rewrite Accuracy (RA) and Preservation Accuracy (PA) for affected and unaffected regions, respectively, Obsolete Retention (OR) for measuring residual outdated semantic associations, and the Selective Revision Score (SRS), which jointly summarizes rewriting and preservation performance. Experiments show that SemReWrite achieves a stronger balance between learning revised semantics and retaining unaffected knowledge than prompt replacement, conventional fine-tuning, parameter-efficient adaptation, and continual-learning strategies.

## Metadata
- **Published**: 2026-08-24T23:14:46Z
- **Authors**: Ismail Lamaakal, Chaymae Yahyati, Yassine Maleh, Khalid El Makkaoui, Ibrahim Ouahbi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23903v1)