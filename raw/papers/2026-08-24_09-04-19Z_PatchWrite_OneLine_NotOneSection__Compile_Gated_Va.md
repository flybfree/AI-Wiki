---
title: PatchWrite: One Line, Not One Section -- Compile-Gated, Validity-Preserving Editing for AI-Drafted Manuscripts
published: 2026-08-24T09:04:19Z
authors: Weiwei Yang
url: http://arxiv.org/abs/2608.23001v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PatchWrite: One Line, Not One Section -- Compile-Gated, Validity-Preserving Editing for AI-Drafted Manuscripts

## Abstract
Automated manuscript pipelines often regenerate an entire section to repair a local defect, allowing unrelated metrics and citations to change even when the resulting PDF still builds. PatchWrite instead constrains how candidate edits become committed manuscript states: it reuses bounded EDIT N M editing and rollback, but tightens compilation acceptance with fatal-log checks and adds evidence locks that require every cited key and experimental numeric token to be attested by a reference registry or experimental log. Candidates that fail either check are rejected and the previous HEAD is retained. On a 24-manuscript x 8-fault oracle stress test (768 jobs, evenly split between compile-breaking and content-only faults), whole-slot rewriting mutated an unrelated "12-layer" line in every case (0/192 preserved; numeric Jaccard 0.6667), whereas PatchWrite preserved it in 192/192 cases. Removing the compile gate reduced acceptance to 0, while removing the evidence gate allowed a hallucinated citation to pass. The same pattern held across all eight faults. To test the protocol with generation rather than oracle edits, we reran the 192 jobs with the writer model proposing the edits. The model's candidates were accepted in 75% of cases; nearly all rejections came from one reproducible failure mode in which the model attempted to delete a line using an empty replacement unsupported by the current grammar. Every accepted candidate passed both gates, and 93.75% fixed the injected fault; the remaining cases involved a technically valid but sentence-inappropriate citation and one markup-changing near-miss. In a blind evaluation of sixteen PDF pairs, both raters preferred PatchWrite for preserving lab-grounded facts (C1 Likert 5.0 vs. 2.0), while rating prose quality nearly identically. Logs from 193 in-product drafting tasks show the same classes of failures occurring in practice.

## Metadata
- **Published**: 2026-08-24T09:04:19Z
- **Authors**: Weiwei Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23001v1)