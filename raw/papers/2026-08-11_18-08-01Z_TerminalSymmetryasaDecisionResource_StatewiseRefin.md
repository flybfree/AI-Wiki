---
title: Terminal Symmetry as a Decision Resource: Statewise Refinement for Anytime Verified Construction
published: 2026-08-11T18:08:01Z
authors: Yi Liu
url: http://arxiv.org/abs/2608.11318v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Terminal Symmetry as a Decision Resource: Statewise Refinement for Anytime Verified Construction

## Abstract
Many sequential construction tasks exhibit exact symmetry at completion while their execution remains directed and history-dependent. We develop a decision-resource view of terminal symmetry: process evidence supplies directionality, terminal correspondence transports that structure across equivalent outcomes, realized-state evidence refines its current decision relevance after transitions, and a fixed verifier certifies execution. This decomposition yields transport--refine--certify. \method{} instantiates the principle with an episode-fixed transported process structure, its state-restricted process rank, a state-dependent residual rank refreshed after accepted transitions, and an ordinal rank meet whose top-$k$ set is exactly the union of the two proposal prefixes. The meet provides a completion guarantee under prefix coverage and attains the tight worst-case verifier-query bound under the corresponding prefix information model; a two-state construction predicts a strict post-transition dynamic--static separation. Across CAD assembly, Mini-Programs, and exact-fill packing, statewise refresh improves anytime AUC by up to $6.77$, $21.75$, and $8.68$ points, respectively. On 1,135 target-removal episodes from the official GRN OOD scenes, \method{} attains the lowest mean capped verifier cost at all three scales among the compared GRN and CDGS-style planners. The statewise signal also transfers across aggregation and scheduler organizations. Terminal symmetry thereby becomes a reusable decision resource for directed construction.

## Metadata
- **Published**: 2026-08-11T18:08:01Z
- **Authors**: Yi Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11318v1)