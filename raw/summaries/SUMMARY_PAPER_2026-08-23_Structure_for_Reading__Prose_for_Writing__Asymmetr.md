---
title: Structure for Reading, Prose for Writing: Asymmetric Structural Conditioning in Multi-Agent Document Authoring
url: http://arxiv.org/abs/2608.20786v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_06-57-46Z_StructureforReading_ProseforWriting_AsymmetricStru.md
generated_at: 2026-08-23 21:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates a multi‑agent pipeline that must both read requester forms and write formal documents, evaluating an open‑weights language model against human submissions from the same organization. In blind comparisons the system matched or exceeded human quality on most sections, yet many gaps stemmed from missing knowledge rather than writing flaws, revealing an asymmetry where reading benefits do not transfer to conditioning.

## Key Takeaways
- The blind comparison showed the LLM judge rated the system’s answers at least as good as humans on 40 of 55 ground‑truth sections, with only one unsupported claim flagged.  
- Most adverse verdicts were due to information that was absent from the model’s sources, not from writing deficiencies, indicating a reading‑only problem.  
- Converting instruction material from prose to nested XML dropped answer quality sharply (74 % → 48 %), highlighting that structural markup aids reading but hinders conditioning for generation.

## Context
The work addresses a growing need for AI systems that can autonomously produce formal documents while respecting organizational knowledge constraints. It builds on prior research showing that document structure improves extraction tasks, yet few studies explore the downstream impact of such structural conditioning on writing quality in multi‑agent pipelines.

## Implications
For industry practitioners, this asymmetry suggests that designing reading‑focused structures may unintentionally degrade generation performance if not carefully balanced with writing‑oriented training. It calls for methodological shifts that separate reading and writing responsibilities to avoid hidden knowledge loss and improve overall document reliability.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20786v1)
