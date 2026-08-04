---
title: Beyond Solution-Centric Search: Adaptive Inquiry and Knowledge Revision for Autonomous ML Engineering
published: 2026-08-03T12:28:52Z
authors: Shaokang Fu, Yulong Tao, Linbo Jin, Jiarong Zhao, Qiming Shi, Tianjun Pan, Haonan Li, Chengyu Wang, Jia Wu, Chengfu Huo
url: http://arxiv.org/abs/2608.02143v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Solution-Centric Search: Adaptive Inquiry and Knowledge Revision for Autonomous ML Engineering

## Abstract
Long-horizon autonomous research tasks such as machine learning engineering require systems to make interdependent decisions under a limited budget. Existing LLM-based agents typically organize candidate-solution improvement through tree, graph, or chain structures, meaning that the search process determines how information is acquired and managed. We call this design solution-centric search and propose instead the information paradigm, in which an evolving information state represents the system's understanding of the task and guides solution improvement. We instantiate this paradigm in Iris, an inquiry-revision loop. For information acquisition, Iris generates local action plans from the current information state and uses epistemic actions to probe decision-critical unknowns without modifying the retained solution. For information management, Iris synthesizes observations across experiments into task knowledge composed of revisable claims with explicit scope and status. It updates this knowledge as new evidence arrives and constructs each decision context from raw evidence, structured summaries, or task knowledge at the required level of detail. On MLE-Bench, Iris attains a 64.9% any-medal rate under a 12-hour budget, the highest among compared systems. Across four tasks spanning harness engineering and model post-training, Iris also demonstrates cross-domain generalization.

## Metadata
- **Published**: 2026-08-03T12:28:52Z
- **Authors**: Shaokang Fu, Yulong Tao, Linbo Jin, Jiarong Zhao, Qiming Shi, Tianjun Pan, Haonan Li, Chengyu Wang, Jia Wu, Chengfu Huo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02143v1)