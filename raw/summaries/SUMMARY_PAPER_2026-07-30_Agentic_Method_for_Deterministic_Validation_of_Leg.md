---
title: Agentic Method for Deterministic Validation of Legacy Code Migration
url: http://arxiv.org/abs/2607.28271v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_14-25-23Z_AgenticMethodforDeterministicValidationofLegacyCod.md
generated_at: 2026-07-30 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Locksmith Loop, an agentic test-synthesis method for deterministic validation of COBOL to Java migrations. It achieves high branch coverage and parity-preserving matching across case studies.

## Key Takeaways
- The iterative Witness Search over input mocks breaks plateaus in traditional input search.
- Parity-preserving mutations ensure generated Java matches original behavior under deterministic checks.
- Locksmith reaches near complete coverage on open-source programs and 91.90% branch coverage on a production-like program.

## Context
Legacy code migration to modern languages often lacks sufficient test data, leading to undetected defects. This work addresses the gap by providing an automated agentic framework that systematically explores execution paths without relying on exhaustive manual testing.

## Implications
The deterministic validation approach can be applied beyond COBOL to other legacy systems, offering a scalable method for quality assurance in high‑risk migrations and supporting confidence in AI‑generated code outputs.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28271v1)
