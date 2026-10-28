---
title: kw-bench: Breaking Frontier Harnesses on Real-World Tasks
url: http://arxiv.org/abs/2610.36405v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-26_23-40-10Z_kw_bench_BreakingFrontierHarnessesonReal_WorldTask.md
generated_at: 2026-10-27 20:48
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces kw-bench, a benchmark designed to evaluate coding-agent harnesses on investigative knowledge work tasks—specifically, recovering and defending precise numerical answers from incomplete, inconsistent evidence spread across multiple systems. The first task family involves a five-year VAT reconstruction across three generations of SAP systems, graded deterministically without any LLM judge. The key finding is that below frontier-level models, the choice of harness dramatically determines performance (ranging from 0.00 to 0.542), while frontier models like Claude Opus 5.5 collapse the task to near-perfect scores in minutes.

## Key Takeaways
- kw-bench targets the "expensive part" of knowledge work—investigative tasks in audit, tax, due diligence, regulatory reporting, and claims—where the answer already exists but must be recovered from fragmented, inconsistent evidence across systems. Unlike most existing benchmarks that test generative tasks (building a memo or spreadsheet judged by rubric), kw-bench tests whether a harness can reconstruct a precise answer "to the cent" from raw, undocumented system extracts including page headers, local number formats, and partial link tables.
- The benchmark's first task is a five-year VAT reconstruction spanning legacy SAP ECC, a partial S/4HANA migration, and a consultant's redesign, delivered as raw system extracts with no documentation of how data connects. Grading is fully deterministic with no LLM judge, making results reproducible and objective.
- Running four harnesses (Claude Code, Codex, OpenCode, micro-cc) on the same mid-tier model (DeepSeek v4.1 Flash) for two hours revealed a stark split: independent model-agnostic harnesses achieved scores of 0.542 and 0.528, while lab-specific harnesses scored 0.00. The failure mode was "inertia"—the inability to keep many weak signals alive across a long session. However, on Claude Opus 5.5, micro-cc and Claude Code scored 0.9986 and 1.000 in 22–25 minutes, collapsing a weeks-long human engagement into minutes and a few dollars.

## Context
This paper sits at the intersection of two rapidly growing research threads: the repositioning of coding-agent harnesses as general-purpose infrastructure for knowledge work rather than software engineering tools, and the development of domain-specific benchmarks to stress-test those harnesses. Most existing agentic benchmarks are generative and evaluated by LLM judges, which introduces circularity and fails to capture the hardest real-world challenge—recovering a single correct answer from messy, multi-system evidence. kw-bench fills this gap with a deterministic, domain-grounded evaluation drawn from actual professional engagements, providing a more honest measure of whether current agent systems can handle the investigative work that dominates high-value knowledge labor.

## Implications
For practitioners in audit, tax, compliance, and consulting, the results suggest that frontier models paired with well-designed harnesses can already reduce weeks-long reconstruction engagements to minutes at negligible cost, fundamentally altering the economics of knowledge work. For the AI research community, the finding that harness architecture matters enormously below frontier capability but becomes irrelevant above it implies that benchmarking must be stratified by model capability, and that the design of agent scaffolding—how it maintains weak signals, manages long sessions, and handles incomplete documentation—remains a critical open problem for the large population of models that are not yet frontier-class.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.36405v1)
