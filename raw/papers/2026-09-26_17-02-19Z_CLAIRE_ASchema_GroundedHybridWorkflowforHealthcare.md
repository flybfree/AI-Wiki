---
title: CLAIRE: A Schema-Grounded Hybrid Workflow for Healthcare Administrative Form Completion
published: 2026-09-26T17:02:19Z
authors: Garapati Keerthana, Manik Gupta
url: http://arxiv.org/abs/2609.32787v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CLAIRE: A Schema-Grounded Hybrid Workflow for Healthcare Administrative Form Completion

## Abstract
Healthcare administrative staff transfer structured information from electronic health records, referrals, claims systems, provider rosters, and work queues into dynamic forms. We developed and evaluated CLAIRE (Clinical Language and Agentic Intelligence for Reasoning and Entry), a hybrid workflow that separates field-state discovery, source-to-field mapping, deterministic validation, bounded correction, escalation, and audit tracing. We tested five synthetic healthcare administrative schemas, 1,000 source records, four interface variants, two data-quality suites, and six comparators, yielding 24,000 benchmark episodes. A separate strict-output audit evaluated direct mappings from Qwen2.5-1.5B and Qwen2.5-7B, and a trace-derived operational simulation covered 6,000 episodes. Under the evaluated synthetic benchmark conditions, full CLAIRE achieved 1.000 episode success, field accuracy, required-field completion, and dependency completion in both suites; removing validation reduced stress-suite success to 0.500. In the simulation, 100.0% of clean and validation-stress episodes reached a staff-reviewable draft, compared with 68.6% of escalation challenge episodes, unsupported cases were blocked. Scenario-based savings were 149.7-165.5 seconds per case, not observed staff times. The findings support schema-grounded, validation-first healthcare administrative automation in which language-model components assist mapping but do not authorize unsupported or consequential actions.

## Metadata
- **Published**: 2026-09-26T17:02:19Z
- **Authors**: Garapati Keerthana, Manik Gupta
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32787v1)