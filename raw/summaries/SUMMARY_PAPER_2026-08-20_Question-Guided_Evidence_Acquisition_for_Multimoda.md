---
title: Question-Guided Evidence Acquisition for Multimodal Visual Question Answering
url: http://arxiv.org/abs/2608.19739v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_07-37-45Z_Question_GuidedEvidenceAcquisitionforMultimodalVis.md
generated_at: 2026-08-20 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Q‑Guide, a query‑guided agent that improves multimodal visual question answering by allocating extra inference compute to locate missing evidence. On benchmark datasets DocVQA2026 and Manga109 the method raises accuracy from 40 % to 65 % compared with direct prompting and recent multi‑agent approaches, showing gains across three Claude backbones.

## Key Takeaways
- Q‑Guide adds a small agent that reads the question and decides which evidence is still missing, then calls targeted tools such as text extraction or zooming.  
- Accuracy improves significantly within two to three deliberate perception rounds, indicating limited need for complex planning.  
- The improvement stems from directing attention to the right location rather than from sophisticated multi‑agent coordination.

## Context
Current document VQA systems treat visual input as a single fixed encoding, which often fails on small text or tables. This work demonstrates that a modest increase in computational effort can yield large gains by making perception more deliberate and context‑aware.

## Implications
For industry practitioners, Q‑Guide offers a practical way to boost accuracy without overhauling model architectures. Practitioners can integrate a lightweight agent into existing VQA pipelines to handle edge cases where direct inference falters.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.19739v1)
