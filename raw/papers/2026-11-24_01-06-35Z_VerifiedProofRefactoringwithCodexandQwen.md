---
title: Verified Proof Refactoring with Codex and Qwen
published: 2026-11-24T01:06:35Z
authors: Lazar Milikic, Gordan Đurić, Viktor Kunčak
url: http://arxiv.org/abs/2611.31762v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Verified Proof Refactoring with Codex and Qwen

## Abstract
We refactor existing Lean 4 proofs to reduce source length and checking cost while preserving theorem statements and compatibility across Lean versions. A locally served Qwen model uses the open-source Codex CLI to inspect source, retrieve declarations, and test proof replacements. The host keeps a replacement only if it improves the objective and Lean accepts it on every required version. A deterministic CPU pass then refines the verified proofs. On the 60 problems in Lean Refactor Arena, model search achieves a local mean combined score of 82.07, and cleanup raises it to 82.18. The final proofs pass all 127 required proof--version checks. Our system placed first in the open-source LLM track of Lean Refactor Arena at VeriCodeGen.

## Metadata
- **Published**: 2026-11-24T01:06:35Z
- **Authors**: Lazar Milikic, Gordan Đurić, Viktor Kunčak
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.31762v1)