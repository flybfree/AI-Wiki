---
title: Towards Automatically Pruning Logging Code with Coding Agents: How Far Are We?
published: 2026-10-03T19:11:19Z
authors: He Yang Yuan, Haonan Zhang, Xin Wang, An Ran Chen, Kisub Kim, Zishuo Ding, Zhenhao Li
url: http://arxiv.org/abs/2610.04716v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards Automatically Pruning Logging Code with Coding Agents: How Far Are We?

## Abstract
Logging code supports debugging, monitoring, and software maintenance, but excessive logging can add noise, impose runtime overhead, and obscure diagnostic information. While prior research has extensively studied logging code generation and modification, logging removal remains comparatively underexplored. In this paper, we study developer logging removal practices and explore the use of coding agents for this task. We extract and manually validate logging removal cases from Python and Java repositories and derive 10 removal patterns and 11 removal reasons that characterize how and why logging code was removed in real-world software changes. We further construct LogRem, a dataset of 387 real-world cases covering direct logging statement removal, logging infrastructure removal, and logging replacement. We evaluate four coding agents with multiple model settings and compare their outputs with accepted real-world changes. Although 95.6% to 100.0% of outputs pass validity checks, only 11.1% to 19.6% remove the same logging code as the corresponding real-world change while preserving unrelated code. Agents differ through missed removals, extra removals, and unrelated code edits, with substantial variation across logging removal categories and trajectories. Execution cost varies widely, but higher cost does not consistently yield closer alignment. Commit messages and developer discussions provide the largest alignment gains, while taxonomy guidance consistently reduces runtime. Overall, our study establishes logging removal as a distinct software maintenance task and shows that reliable automation depends on accurately determining removal scope while preserving necessary code. To the best of our knowledge, this is the first study to examine logging code removal from this perspective.

## Metadata
- **Published**: 2026-10-03T19:11:19Z
- **Authors**: He Yang Yuan, Haonan Zhang, Xin Wang, An Ran Chen, Kisub Kim, Zishuo Ding, Zhenhao Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.04716v1)