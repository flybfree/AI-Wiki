---
title: Harness-Search: Guiding Long-Horizon Search through Multi-Agent Coordination
published: 2026-10-04T17:14:24Z
authors: Shanyong Wang, Zhenwen Ji, Lei Jin, Yining Zhao, Yicheng Qian, Chengqiang Lu, Yi Wu, Yao Hu, Lizhen Cui, Yanyu Xu
url: http://arxiv.org/abs/2610.05382v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Harness-Search: Guiding Long-Horizon Search through Multi-Agent Coordination

## Abstract
Long-horizon search requires agents to gather evidence across multiple steps and synthesize it into well-supported answers. The recent agent harnesses provide a natural and promising framework to support such long-running search processes. As interaction histories grow, one single agent in harnesses might get stuck and cause the policy to lose track of unresolved questions, overlook useful evidence, or terminate before sufficient support has been collected. One of promising way is to decouple three distinct responsibilities of proposing retrieval actions, updating persistent state, and deciding when to stop rather than concentrating them within a single policy. Targeted at it, we introduce Harness-Search, a multi-agent search harness to reduce the local errors propagating across subsequent exploration, evidence curation, and termination decisions. In particular, Harness-Search assigns these responsibilities to three permission-bounded authorities: a Retrieval Policy that proposes search operations, a Memory Operator that validates and commits persistent-state updates, and a Summary Auditor that accepts or rejects termination based on the sufficiency of the curated evidence. Together, these roles form a Propose-Commit-Audit loop in which actions are proposed, persistent evidence is selectively committed, and stopping decisions are subjected to an explicit sufficiency check. Across seven long-horizon search benchmarks, Harness-Search improves both retrieval and answer generation under the same policy backbone, increasing Recall by 4.60-27.92 points and Final-Answer Recall by 12.34-30.13 points over the strongest harness-based baseline on each evidence-retrieval benchmark. Moreover, trajectory-level analyses show that Harness-Search continues to accumulate useful evidence and expand evidence coverage with less redundant retrieval as the search history grows.

## Metadata
- **Published**: 2026-10-04T17:14:24Z
- **Authors**: Shanyong Wang, Zhenwen Ji, Lei Jin, Yining Zhao, Yicheng Qian, Chengqiang Lu, Yi Wu, Yao Hu, Lizhen Cui, Yanyu Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.05382v1)