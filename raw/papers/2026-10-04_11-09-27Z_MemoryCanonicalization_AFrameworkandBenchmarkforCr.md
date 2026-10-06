---
title: Memory Canonicalization: A Framework and Benchmark for Cross-Model Drift in Persistent LLM Memory
published: 2026-10-04T11:09:27Z
authors: Amit Vadnere, Aishwarya Lonarkar
url: http://arxiv.org/abs/2610.05124v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Memory Canonicalization: A Framework and Benchmark for Cross-Model Drift in Persistent LLM Memory

## Abstract
Persistent memory for Large Language Models (LLMs) has matured rapidly: systems such as MemGPT/Letta, Mem0, and Zep now provide agents with tiered, temporally-aware, model-agnostic external storage, while the Model Context Protocol (MCP) standardizes access to memory servers. A less addressed problem is that an identical stored memory object, retrieved by two different LLMs under otherwise identical conditions, may not be interpreted the same way, factually or emotionally. This paper proposes memory canonicalization: a write-time pipeline that detects ambiguity, conditional structure, and emotional loading in a raw memory object and rewrites it into an explicit, structurally disambiguated canonical form, with emotional valence represented as a separate field rather than inferred from tone. We formalize the pipeline, define a companion Cross-Model Semantic Drift / Emotional Consistency Score benchmark (CMSC-E), and report results from a three-arm pilot using 176 synthetic memory objects and three downstream model families. We find an uncorrected improvement in cross-model emotional consistency for fully canonicalized memory relative to raw memory (+0.050, 95% bootstrap CI [0.013, 0.086], paired t-test p = 0.010), but this result does not survive Bonferroni, Holm, or Benjamini-Hochberg correction across the six comparisons tested. None of the factual-drift (CMSD) comparisons reach significance at any correction level. We report these results as exploratory rather than confirmatory and outline needed follow-up work, including larger samples, independent judge models, human-validated rendering, and preregistration.

## Metadata
- **Published**: 2026-10-04T11:09:27Z
- **Authors**: Amit Vadnere, Aishwarya Lonarkar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.05124v1)