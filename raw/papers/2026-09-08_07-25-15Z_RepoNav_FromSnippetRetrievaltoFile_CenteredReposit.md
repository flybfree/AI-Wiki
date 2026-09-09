---
title: RepoNav: From Snippet Retrieval to File-Centered Repository Navigation for Code Agents
published: 2026-09-08T07:25:15Z
authors: Hongzheng Chai, Jiakun Li, Hongyue Yu, Yuan Yuan
url: http://arxiv.org/abs/2609.08355v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RepoNav: From Snippet Retrieval to File-Centered Repository Navigation for Code Agents

## Abstract
Solving repository-level code tasks requires LLM-based agents to use code search tools to navigate large codebases and identify a small set of relevant files and functions. However, current retrieval tools typically return flat lists of isolated code snippets: such lists can surface relevant files, but provide insufficient structure for agents to distinguish the target function from semantically similar alternatives in the same file. We introduce RepoNav, a lightweight post-retrieval interface that reorganizes retrieved snippets into a file-centered navigation scaffold. By presenting compact structural cues and candidate targets, this scaffold guides on-demand file-structure browsing, helping agents compare sibling symbols before selecting a target function. Across diverse models on LocBench, RepoNav improves function-level localization and narrows the file-to-function gap. Controlled ablations demonstrate that these gains come from structured evidence organization rather than simply exposing additional file structure, and the approach also improves performance on a repository-level question-answering benchmark.

## Metadata
- **Published**: 2026-09-08T07:25:15Z
- **Authors**: Hongzheng Chai, Jiakun Li, Hongyue Yu, Yuan Yuan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.08355v1)