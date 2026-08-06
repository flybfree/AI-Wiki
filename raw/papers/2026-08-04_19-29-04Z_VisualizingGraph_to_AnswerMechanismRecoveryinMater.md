---
title: Visualizing Graph-to-Answer Mechanism Recovery in Materials-Science Hypothesis Generation
published: 2026-08-04T19:29:04Z
authors: Shashwat Sourav, Subhadeep Pal, Markus J. Buehler, Sanjay Das, Fiona Y. Wang, Dominik Soos, Tirthankar Ghosal
url: http://arxiv.org/abs/2608.04170v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Visualizing Graph-to-Answer Mechanism Recovery in Materials-Science Hypothesis Generation

## Abstract
AI co-scientists can generate fluent materials-science hypotheses, but fluency does not show that an answer preserves a scientifically meaningful mechanism. We present a graph-to-answer mechanism-tracing case study for Graph-PRefLexOR-8B, a Qwen3-8B model adapted to expose distinct stages for brainstorming, graph construction, pattern extraction, and synthesis. We organize semantic backtracking, graph corruption, activation-based recovery measurements, and layer-by-token-region grids into a visual diagnostic workflow for inspecting this pathway. Across 100 open-ended materials-science questions, final answers remain closest to the model's own structured stages, especially synthesis. Under graph corruption, a full sweep over 37 residual-stream checkpoints, the embedding output and 36 transformer blocks, shows little mechanism recovery in the earlier transition region at layers 7--10, recovery instead concentrates in late synthesis and answer-start regions around layers 30 and 36. The workflow is intended to help scientists and model developers identify where a generated hypothesis loses or regains mechanism support before it is passed to downstream experimental planning.

## Metadata
- **Published**: 2026-08-04T19:29:04Z
- **Authors**: Shashwat Sourav, Subhadeep Pal, Markus J. Buehler, Sanjay Das, Fiona Y. Wang, Dominik Soos, Tirthankar Ghosal
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04170v1)