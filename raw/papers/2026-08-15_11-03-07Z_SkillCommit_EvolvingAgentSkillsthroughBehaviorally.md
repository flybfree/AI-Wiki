---
title: SkillCommit: Evolving Agent Skills through Behaviorally Validated Scope Expansion
published: 2026-08-15T11:03:07Z
authors: Yu He, Weikai Yang
url: http://arxiv.org/abs/2608.15165v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SkillCommit: Evolving Agent Skills through Behaviorally Validated Scope Expansion

## Abstract
Large language model (LLM) agents can continually improve without parameter updates by converting historical experience into reusable procedural knowledge. However, existing methods often consolidate experience based on semantic similarity or LLM judgments, which may merge superficially related but behaviorally incompatible strategies and thereby degrade performance. To address the issue, we propose SkillCommit, an online skill evolution framework that continuously transforms experience into a hierarchical library of reusable skills. Each new experience is initially preserved as an instance-specific patch, retaining the behavior validated in its local context. As related skills accumulate, SkillCommit abstracts those sharing a common behavioral mechanism into higher-level skills. Specifically, for each incoming skill, embedding-based retrieval first identifies candidate related skills. Cross-instance replay and an LLM-based mechanism check determine whether these skills transfer across cases and share a common underlying mechanism. Candidates that pass both checks are abstracted into a higher-level skill and committed only if it preserves the validated behavior of all constituent skills. Experiments on RuleArena, OpenExempt and KOR-Bench demonstrate that SkillCommit consistently improves agent performance across diverse domains. Moreover, the learned skills transfer across model scales and families, enabling cross-model experience transfer.

## Metadata
- **Published**: 2026-08-15T11:03:07Z
- **Authors**: Yu He, Weikai Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15165v1)