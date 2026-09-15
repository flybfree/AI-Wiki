---
title: Validating Hybrid-State Cache Recovery for GLM-5.3-Flash with vLLM and LMCache
published: 2026-09-14T04:46:09Z
authors: Frank Li
url: http://arxiv.org/abs/2609.15030v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Validating Hybrid-State Cache Recovery for GLM-5.3-Flash with vLLM and LMCache

## Abstract
External cache transfers can succeed while a hybrid language model resumes from an inconsistent state. We examine the full 45-layer GLM-5.3-Flash model, using the RedHatAI/ GLM-5.3-Flash-NVFP4 quantized checkpoint with vLLM and LMCache under four-way tensor parallelism. A complete-hit recovery mismatch restored state for the full prompt while the scheduler credited one fewer token. We aligned recovery through strict-prefix lookup and established a numerical comparison using shared computation corrections, matched checkpoint scheduling, and fixed per-rank kernel configurations. In a nine-length serial workload, agreement with the modified recomputation control improved from 34/36 to 36/36 generations, each containing 64 token IDs. A separate instrumented run passed recorded transfer-page, effective-tail, and delayed-save checks. Three additional synthetic templates passed 72 paired 256-token continuations across two fresh-container runs. A subsequent serial performance study preserved output equality across 120 requests; among the measured trials, CPU reload reduced time to first token by 46-64% and total request time by 1.9-7.0% relative to modified cold recomputation. The contribution is an experimentally validated integration repair applying an existing checkpoint-alignment principle. The evidence is confined to one model revision and controlled configuration; it does not establish general determinism, task-quality equivalence, concurrent-serving gains, or capacity beyond GPU memory.

## Metadata
- **Published**: 2026-09-14T04:46:09Z
- **Authors**: Frank Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.15030v1)