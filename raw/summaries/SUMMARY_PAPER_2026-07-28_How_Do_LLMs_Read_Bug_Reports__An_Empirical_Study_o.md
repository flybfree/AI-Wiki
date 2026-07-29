---
title: How Do LLMs Read Bug Reports? An Empirical Study of Attention in LLMs for Automated Program Repair
url: http://arxiv.org/abs/2607.25873v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-28_15-38-12Z_HowDoLLMsReadBugReports_AnEmpiricalStudyofAttentio.md
generated_at: 2026-07-28 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how large language models allocate attention when repairing software bugs from real‑world reports. By analyzing 319 verified Python and Java bugs, the authors show that successful repairs tend to draw diffuse attention across multiple sections such as descriptions, stack traces, and test cases, whereas failed repairs often focus narrowly on metadata like version numbers. The study also links higher repair success with stronger alignment between model attention and developer‑identified key phrases.

## Key Takeaways
- Successful repairs are characterized by diffused attention that spans several diagnostic components rather than concentrating on a single area.  
- Unsuccessful repairs frequently exhibit over‑localized attention, especially toward metadata such as version information which may be less relevant to the actual bug.  
- The degree of alignment between model attention and developer‑identified key sections or phrases correlates with repair success.

## Context
Understanding attention mechanisms in language models is crucial for building transparent AI systems that can explain their decisions. This work provides empirical evidence that attention misallocation contributes to failures in automated program repair, a field where reliability directly impacts software quality and maintenance costs.

## Implications
For practitioners developing APR tools, monitoring attention patterns could serve as an early warning of potential errors. Designing models that attend more broadly across relevant sections may improve repair accuracy and make the system’s reasoning more interpretable for developers.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.25873v1)
