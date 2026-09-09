---
title: SCAFFOLD: Self-Improving Web Agents via Recursive Parametric Skill Abstraction
published: 2026-08-31T08:16:56Z
authors: Bowei He, Xiaokun Zhang, Meng Ding, Xue Liu
url: http://arxiv.org/abs/2609.05511v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SCAFFOLD: Self-Improving Web Agents via Recursive Parametric Skill Abstraction

## Abstract
Web agents need to navigate visually rich, long-horizon interfaces that change across sites, yet most previous agents still learn each task in isolation and discard the procedural knowledge they accumulate. Recent skill-augmented frameworks take an important first step, but they treat the skill library as a flat or two-tier prompt-side cache and offer no principled mechanism for compressing redundancy or composing skills recursively. We introduce \textsc{Scaffold}, a self-improving framework for visual web agents that (i) induces parametric, executable skills from successful trajectories under a multi-instance abstraction constraint, (ii) maintains a recursively composed hierarchy in which higher-level skills invoke lower-level ones, (iii) compacts the library via a minimum-description-length (MDL) criterion and behavioral equivalence checking, and (iv) periodically distills skill-augmented trajectories back into model weights to internalize the abstractions. Across WebArena, VisualWebArena, and a held-out split of Online-Mind2Web, \textsc{Scaffold} improves success rate by $11.1$--$17.2$ absolute points over the strongest skill-augmented baseline and shows monotonic gains across five self-improvement iterations without library collapse. We release the code and documents in the Github \href{https://github.com/BokwaiHo/SCAFFOLD}{repository}.

## Metadata
- **Published**: 2026-08-31T08:16:56Z
- **Authors**: Bowei He, Xiaokun Zhang, Meng Ding, Xue Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05511v1)