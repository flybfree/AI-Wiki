---
title: Co-Design Bench: Multimodal Collaborative Coding Evaluation for Agentic Models
url: http://arxiv.org/abs/2610.35138v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-26_10-10-21Z_Co_DesignBench_MultimodalCollaborativeCodingEvalua.md
generated_at: 2026-10-27 00:08
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
Co-Design Bench introduces a reference-free benchmark of 273 tasks derived from over 26,000 real user coding sessions to evaluate whether agentic coding models can translate multimodal human requests into working application revisions. The benchmark spans two tracks—Multimodal Editing and Repository Editing—and reveals a significant gap between partial criterion satisfaction and full task completion, with the strongest tested model satisfying only 26.4% of tasks completely despite passing 69.9% of individual criteria on average.

## Key Takeaways
- The benchmark is constructed from 37,463 deduplicated queries across 26,314 real user coding sessions, making it grounded in authentic human-AI interaction patterns rather than synthetic or curated tasks. It covers three capability dimensions—Grounded Understanding, UI Transformation, and Functional Implementation—and accepts optional image, audio, video, or document inputs, reflecting the multimodal nature of real user requests.
- Evaluation uses a judge-then-refute protocol with 2,331 hidden expert-authored acceptance criteria, grading each criterion against source code and browser evidence, then challenging positive verdicts with a separate LLM verifier. This approach audits visual and interaction claims without relying on gold reference code or target screenshots, reducing evaluation bias.
- A critical finding is the performance degradation on complex repository edits: all ten tested model endpoints achieve lower criterion completion on tasks spanning three or four change types compared to those spanning one or two. The gap between passing 69.9% of individual criteria and fully satisfying only 26.4% of tasks highlights that partial requirement satisfaction does not translate into complete task success under agentic execution.

## Context
As agentic coding assistants increasingly handle multi-file, multi-modal editing tasks in production environments, existing benchmarks that rely on single-file code generation or static reference solutions fail to capture the coordination, visual fidelity, and multi-step reasoning required for real application revisions. Co-Design Bench addresses this gap by grounding evaluation in actual user workflows and introducing a hidden-criteria, evidence-based grading protocol that mirrors how practitioners assess whether a revision truly works.

## Implications
For AI developers and product teams building coding agents, the 26.4% full-task success rate signals that current models remain far from reliable autonomous application editing, particularly for multi-change repository tasks. Practitioners should treat partial criterion pass rates as insufficient proxies for deployment readiness and adopt multi-dimensional evaluation frameworks. The benchmark also provides a standardized testbed for tracking progress toward genuinely useful collaborative coding assistants across the industry.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.35138v1)
