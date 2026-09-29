---
title: Fewer Assumptions by Design: A Reusable Skill for LLM-Assisted Verus Verification
published: 2026-09-28T10:58:41Z
authors: Andrada-Livia Antoneac, Dorel Lucanu, Dragoş Teodor Gavriluţ
url: http://arxiv.org/abs/2609.34886v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fewer Assumptions by Design: A Reusable Skill for LLM-Assisted Verus Verification

## Abstract
LLM-assisted Verus verification is a less tedious method to verify Rust implementations, but paired with self-referential structures, e.g., Doubly Linked Lists (DLLs)ânotoriously difficult to formalise for verificationâit becomes a substantially more demanding verification task.    Moreover, a specification weakness can arise when verification relies on unproven or invalidated assumptions, such as axiomatic lemmas and assume statements. We investigate whether LLM agents can synthesize strong DLL specifications while minimizing these trusted base. The analysis follows three different approaches: manual verification, property-specific verification, and a defined skill for the specific case of DLLs and certain properties of this type of data structure. The skill encodes domain knowledge and a task-decomposition strategy. We show that an LLM agent equipped with a carefully designed verification skill can generate strong, low-trust specifications for DLLs in Verus.

## Metadata
- **Published**: 2026-09-28T10:58:41Z
- **Authors**: Andrada-Livia Antoneac, Dorel Lucanu, Dragoş Teodor Gavriluţ
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.34886v1)