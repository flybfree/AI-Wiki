---
title: Calibrating Conservatism for Scalable Oversight
published: 2026-05-27T17:56:47Z
authors: William Overman, Mohsen Bayati
url: http://arxiv.org/abs/2605.28807v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Calibrating Conservatism for Scalable Oversight

## Abstract
Agentic AI systems capable of autonomous planning and extended environmental interaction pose a fundamental control problem: how can humans maintain meaningful oversight of systems that may exceed their own capabilities? Existing approaches to scalable oversight rely on complex assumptions, remain largely heuristic, or lack practical methods for sequential settings with statistical guarantees. We introduce Calibrated Collective Oversight (CCO), which aggregates diverse auxiliary scoring functions into a penalty measuring deviation from a conservative baseline. Inspired by Attainable Utility Preservation, CCO enables collective conservatism: actions face a penalty proportional to overseer concern, so high-utility actions are still selected when overseers find them unobjectionable and overridden only when concern accumulates. CCO calibrates this conservatism online using Conformal Decision Theory, ensuring that undesirable outcomes remain below a user-specified target threshold with finite-time bounds and no distributional assumptions. On a modified version of SWE-bench, weaker overseers successfully constrain an adversarially misaligned stronger agent; on MACHIAVELLI, CCO substantially reduces ethical violations while preserving reward. In both settings, empirical violation rates closely match the specified targets, as predicted by the theory.

## Metadata
- **Published**: 2026-05-27T17:56:47Z
- **Authors**: William Overman, Mohsen Bayati
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.28807v1)