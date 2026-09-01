---
title: Where Induction Runs Out: Description-Length Difficulty and the Memorisation Gap in Integer-Sequence Benchmarks
published: 2026-08-29T19:25:31Z
authors: Sabilashan Ganeshan
url: http://arxiv.org/abs/2608.29411v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Where Induction Runs Out: Description-Length Difficulty and the Memorisation Gap in Integer-Sequence Benchmarks

## Abstract
Integer sequences from the On-Line Encyclopedia of Integer Sequences (OEIS) are increasingly used to benchmark mathematical reasoning in language models. We ask what such benchmarks actually measure, using an exactly computable reference learner: two-part minimum description length (MDL) over the class of P-recursive (holonomic) recurrences, evaluated on every prefix of a sequence as terms arrive. Three findings follow. First, MDL difficulty is a parameter count. The discovery point nd, the first prefix length at which a symbolic hypothesis beats verbatim storage, is predicted almost exactly by a combinatorial identifiability bound on the selected operator's order and degree. It is invariant to term magnitude: scaling Fibonacci over twelve orders of magnitude leaves nd unchanged, because a hypothesis must encode its own initial conditions and the magnitude cancels. Second, at scale the learner exhibits a regime our curated corpus could not produce even once: across 20,000 OEIS sequences, 89.98% of those that fit a recurrence on some prefix fit none at full length. We call this the wilderness -- induction acquires a theory, loses it, and never recovers. Third, evaluating three language models on sequences stratified by these MDL regimes refuted our pre-registered hypothesis: models do not confabulate where MDL reports no theory, but hedge appropriately. Confident errors are inverted, concentrating on the easy stratum, where apparent competence tracks recognition of the sequence rather than induction of its rule. OEIS-derived benchmarks therefore substantially measure memorisation, and MDL supplies a cheap, contamination-free difficulty signal they currently lack. Code and data are released.

## Metadata
- **Published**: 2026-08-29T19:25:31Z
- **Authors**: Sabilashan Ganeshan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29411v1)