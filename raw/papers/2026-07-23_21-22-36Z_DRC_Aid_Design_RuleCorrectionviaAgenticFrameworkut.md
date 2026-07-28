---
title: DRC-Aid: Design-Rule Correction via Agentic Framework utilizing Inference-Time Large Language Models
published: 2026-07-23T21:22:36Z
authors: Anushka Mukherjee, Kang He, Kaushik Roy
url: http://arxiv.org/abs/2607.22761v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DRC-Aid: Design-Rule Correction via Agentic Framework utilizing Inference-Time Large Language Models

## Abstract
Resolving Design Rule Violations (DRVs) in layouts entails an iterative loop of geometric edits and verification. We present DRC-Aid, a closed-loop agentic framework that automates local DRC repair by formulating it as verification-in-the-loop search. To constrain the combinatorial geometric repair space, a deterministic Rule Engine converts physical verification tool-reported violations into a bounded menu of geometric edits. An off-the-shelf Large Language Model (LLM) evaluates local geometric context to select edits from this menu, with budgeted depth-first search and backtracking. Immediate feedback from verification tools such as Calibre nmDRC/nmLVS enforces geometric compliance and guards against electrical-topology degradation, while a global Memory Bank prevents cyclic re-exploration. Evaluated on FreePDK45 layouts containing DRVs, DRC-Aid achieves DRC-clean, LVS-equivalent repairs in ~92.5% of cases with a ~98% total violation reduction, while residual cases yield partially repaired LVS-equivalent candidates. Under an identical search and verification infrastructure, LLM-based selection outperforms random (54.4%) and deterministic-heuristic (83.3%) policies, with the gap widening on cases with six or more violations.

## Metadata
- **Published**: 2026-07-23T21:22:36Z
- **Authors**: Anushka Mukherjee, Kang He, Kaushik Roy
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22761v1)