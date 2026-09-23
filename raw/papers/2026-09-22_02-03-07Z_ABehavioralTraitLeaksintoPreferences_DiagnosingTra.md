---
title: A Behavioral Trait Leaks into Preferences: Diagnosing Trait Interference in LLM User Simulators
published: 2026-09-22T02:03:07Z
authors: Chaehyun Kim, Sein Kim, Hongseok Kang, Chanyoung Park
url: http://arxiv.org/abs/2609.25572v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Behavioral Trait Leaks into Preferences: Diagnosing Trait Interference in LLM User Simulators

## Abstract
LLM-based user simulators aim to bridge the offline-online gap in recommender evaluation by emulating users through injected traits, where preference attributes determine what a user engages with and a behavioral activity trait governs how long they browse. However, we show this intended trait independence collapses during simulation, causing two failures: (i) Trait Interference, where amplified activity distorts preference boundaries and forces interactions with mismatched items to sustain browsing, and (ii) Evaluation Invalidity, where satisfaction scores inflate with activity-driven page counts despite taste mismatches, biasing evaluation toward trait distributions rather than recommender performance. To resolve this, we propose PQA, a page-level quality anchoring method that guides simulators using a personalized anchor reflecting each user's intrinsic preference standard. By assessing whether a page meets this standard before further browsing, PQA enables proactive exits from low-quality pages, letting the activity trait retain its intended role of modulating browsing depth within preference-conforming pages. Experiments show PQA mitigates trait interference and improves the reliability of LLM-based simulator evaluation under activity shifts. Our code is available at https://github.com/chaehyun1/PQA

## Metadata
- **Published**: 2026-09-22T02:03:07Z
- **Authors**: Chaehyun Kim, Sein Kim, Hongseok Kang, Chanyoung Park
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.25572v1)