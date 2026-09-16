---
title: RepoAtlas: Guiding Coding Agents via Evolving Multimodal Repository Views
published: 2026-09-15T10:11:51Z
authors: Yunxiang Zhang, Haiquan Wang, JiaWei Guo, Hanyang Xia, Yan Chen, Tong Chen, Zhang Zhiwei, Junchen Ye
url: http://arxiv.org/abs/2609.16936v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RepoAtlas: Guiding Coding Agents via Evolving Multimodal Repository Views

## Abstract
Large language model (LLM)-powered coding agents have made rapid progress in automating software engineering tasks, yet repository-level issue resolution remains challenging. Beyond generating a plausible patch, an agent must localize relevant code across interdependent files and maintain repository context that is both sufficient and focused. Code graphs expose non-local relations, but linear text interfaces obscure their topology; rendering the full repository graph yields visual representations that are too dense to perceive reliably, whereas a one-shot local view becomes stale as exploration proceeds. We present \textbf{RepoAtlas}, a training-free module that maintains evolving multimodal repository views through a \emph{select--project--refresh} loop over a repository code graph. RepoAtlas combines evidence from the issue with the agent's current exploration state to select a task-relevant region under a fixed budget, projects the selected structure into complementary visual and textual representations, and refreshes the view when changes in the exploration state render it outdated. We evaluate RepoAtlas on SWE-bench Verified, where it improves the resolve rate by 2.4 points while reducing input tokens and model calls by 5.8\% and 7.8\% on average, relative to the strongest multimodal graph baseline, with consistent gains across three models of different families and scales.

## Metadata
- **Published**: 2026-09-15T10:11:51Z
- **Authors**: Yunxiang Zhang, Haiquan Wang, JiaWei Guo, Hanyang Xia, Yan Chen, Tong Chen, Zhang Zhiwei, Junchen Ye
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.16936v1)