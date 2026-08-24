---
title: Metag: A dataset to build agentic meta-reviewing capabilities
published: 2026-08-20T18:19:03Z
authors: Anirudh Sundar, Min Chen, Divya Tadimeti, Gemma Zhang, Alice Li, Nigel Boachie Kumankumah, Pavan Uttej Ravva, Sadid Hasan, Somya Chatterjee, Pruthvi Prakash Navada, Xiao Wang, Yue Kang, Sulaiman Vesal, Larry Heck
url: http://arxiv.org/abs/2608.20488v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Metag: A dataset to build agentic meta-reviewing capabilities

## Abstract
AI tools increasingly support tasks across the scientific research cycle, from experiment design and manuscript preparation to peer review. At the same time, the continuing growth in conference submissions has increased the burden on meta-reviewers, who must synthesize reviewer feedback, author rebuttals, and manuscript revisions. To address this concern, this paper introduces Metag, a dataset to accelerate the development of meta-reviewing agents, specifically to identify changes made to scientific articles during the review-rebuttal process. Each instance contains a reviewer concern, the author's proposed resolution, and the manuscript diffs implementing the stated change. Metag is collected by obtaining manuscript versions from before the review deadline and after acceptance, computing differences between the two documents, and asking human annotators to align these differences with action items from OpenReview discussions. The resulting dataset consists of 349 high-quality action items tied to paper differences and will enable building methods to empower meta reviewers to quickly identify whether authors have addressed reviewer statements and where in the paper those changes have been made, resulting in additional transparency and traceability throughout peer review. The dataset is publicly available at https://github.com/microsoft/Metag-dataset.

## Metadata
- **Published**: 2026-08-20T18:19:03Z
- **Authors**: Anirudh Sundar, Min Chen, Divya Tadimeti, Gemma Zhang, Alice Li, Nigel Boachie Kumankumah, Pavan Uttej Ravva, Sadid Hasan, Somya Chatterjee, Pruthvi Prakash Navada, Xiao Wang, Yue Kang, Sulaiman Vesal, Larry Heck
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20488v1)