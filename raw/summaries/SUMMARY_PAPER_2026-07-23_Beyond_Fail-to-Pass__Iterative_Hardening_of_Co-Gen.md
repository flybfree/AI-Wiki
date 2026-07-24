---
title: Beyond Fail-to-Pass: Iterative Hardening of Co-Generated Bug Reproduction Tests and Fixes
url: http://arxiv.org/abs/2607.19843v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_07-30-07Z_BeyondFail_to_Pass_IterativeHardeningofCo_Generate.md
generated_at: 2026-07-23 23:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses a limitation in automated program repair where bug reproduction tests (BRTs) are evaluated only by the fail‑to‑pass criterion, which can miss quality issues that affect downstream fixes. The authors demonstrate that lax BRTs generate plausible but incorrect patches and that co‑generation creates error coupling between test and fix. Their solution, CoHarden, uses a Lax signal as an in‑loop convergence metric to iteratively harden both the test and the repair until no Lax regressions survive.

## Key Takeaways
- F->P BRTs are split into rigorous and lax types; only rigorous ones consistently improve repair success.  
- Co‑generation can produce a failing test that still admits incorrect patches, leading to error coupling between test and fix.  
- CoHarden’s iterative hardening using the Lax signal raises Resolved rate to 69.4% and F->P rate to 78.9% on SWE-bench Verified.

## Context
Automated program repair leverages LLMs to generate fixes from bug reports, but the quality of generated reproduction tests is crucial for reliable repairs. Existing methods rely solely on fail‑to‑pass evaluation, which does not capture subtle regressions that degrade fix correctness. This gap limits the practical impact of APR in real‑world codebases.

## Implications
Practitioners can adopt CoHarden to obtain more robust BRTs and fixes, reducing false repairs and improving overall repair reliability across different LLM backbones. The framework’s emphasis on iterative hardening offers a path toward higher-quality automated repair pipelines in industry and research.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19843v1)
