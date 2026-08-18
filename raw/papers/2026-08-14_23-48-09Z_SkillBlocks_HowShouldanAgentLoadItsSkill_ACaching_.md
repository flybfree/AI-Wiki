---
title: Skill Blocks: How Should an Agent Load Its Skill? A Caching-Correct Comparison of Pre-load, On-Demand Tool-Loading, Progressive Disclosure, and Hybrid
published: 2026-08-14T23:48:09Z
authors: Hironobu Nakasuji
url: http://arxiv.org/abs/2608.14943v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Skill Blocks: How Should an Agent Load Its Skill? A Caching-Correct Comparison of Pre-load, On-Demand Tool-Loading, Progressive Disclosure, and Hybrid

## Abstract
Agent skills are often injected in full on every request, increasing token cost. We compare four content-preserving loading methods: Full, Skill Block, Reference, and Hybrid. Across SearchQA, SpreadsheetBench, ALFWorld, ScienceWorld, and SynthProc, we measure token usage using raw input for single-turn tasks and cache-correct effective input for multi-turn tasks. Results show no universal winner. Hybrid reduces input by 27.4% on SearchQA and 39.8% on SpreadsheetBench. On large multi-turn skills, Skill Block and Hybrid achieve substantial reductions, reaching 62.5% and 52.8% on ScienceWorld and 73.0% and 66.6% on SynthProc. ALFWorld shows smaller gains because procedures are short and repeatedly needed. Paired outcome tests detect no quality differences, though they do not establish equivalence. Overall, conditional loading is most beneficial when large portions of a skill are not needed on every turn.

## Metadata
- **Published**: 2026-08-14T23:48:09Z
- **Authors**: Hironobu Nakasuji
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14943v1)