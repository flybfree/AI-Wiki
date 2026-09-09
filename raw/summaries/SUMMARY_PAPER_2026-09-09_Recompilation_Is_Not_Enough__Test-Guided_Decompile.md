---
title: Recompilation Is Not Enough: Test-Guided Decompiled-C Repair
url: http://arxiv.org/abs/2609.07201v1
type: paper-summary
date: 2026-09-09
source_paper: 2026-09-07_08-24-53Z_RecompilationIsNotEnough_Test_GuidedDecompiled_CRe.md
generated_at: 2026-09-09 00:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper addresses a limitation of simple recompilation when fixing decompiled C code, showing that test-guided repair is needed to ensure behavior matches original binaries. On 104 Coreutils binaries, 91 passed the test gate after repair, while some failed or required extra effort.

## Key Takeaways
- Recompiling repaired C may still produce incorrect option parsing, wrong byte output, or different exit statuses, indicating that compiler feedback alone is insufficient. - Smoke checks and official tests expose behavioral discrepancies that guide semantic repairs beyond compile-time fixes. - The evaluation shows 87.5% of reparable binaries succeed in passing the test gate within repair budget, highlighting the value of test-gate feedback for LLM-assisted decompiled C repair.

## Context
Decompilation of compiled languages often yields syntactically correct but semantically flawed code, a challenge for automated repair systems that rely on compile-time checks. This work demonstrates how integrating official test suites into repair pipelines improves reliability and auditability in AI-driven code restoration tasks.

## Implications
For practitioners, this approach offers a framework to validate repaired binaries with minimal human intervention, reducing risk of subtle bugs. In industry, adopting test-gate feedback can make LLM-assisted decompilation more trustworthy for critical software components.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.07201v1)
