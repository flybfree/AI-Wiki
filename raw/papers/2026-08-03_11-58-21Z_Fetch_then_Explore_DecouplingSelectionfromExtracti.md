---
title: Fetch-then-Explore: Decoupling Selection from Extraction over a Persistent Workspace for Search Agents
published: 2026-08-03T11:58:21Z
authors: Qi Liu, Yiqun Chen, Zidan Chen, Yan Gao, Yi Wu, Yao Hu, Jiaxin Mao, Fengbin Zhu, Tat-Seng Chua
url: http://arxiv.org/abs/2608.02097v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fetch-then-Explore: Decoupling Selection from Extraction over a Persistent Workspace for Search Agents

## Abstract
Search agents now answer questions that take dozens of searches to settle, yet how such an agent reads a page has drawn far less attention than how it finds one. Nearly all of them use one of two document interfaces, and both tie a page to the moment it is opened. \emph{Visit-and-read} injects a reading of the page into the message history at fetch time, fixing that reading before the agent knows which fact it will need. Stateful \emph{browsing} instead extracts on demand from the page in hand, but holds one page at a time and releases it as soon as the agent opens another. Either way, a page that turns out to matter many turns later has to be fetched and rendered into context all over again. We propose \textbf{Fetch-then-Explore}, which separates page selection from evidence extraction and keeps what it selects: pages are recorded in a per-question workspace on the filesystem rather than the context window or a transient session, and evidence is pulled from them on demand later. Selection becomes almost free, extraction can wait until the agent knows what to look for and be repeated as its hypothesis sharpens, and pages are not released when the agent moves on, so evidence accumulates across the trajectory. In a unified ReAct harness with fixed search, we compare Fetch-then-Explore against snippet-only, visit-and-read, and browsing baselines on two open-web benchmarks, BrowseComp and WideSearch, across three agent backbones. It leads BrowseComp accuracy at every backbone and generally matches or exceeds the baselines on WideSearch, and a behavioral analysis traces the gains to the workspace's defining move: returning to a page after leaving it, which it does far more than any transient interface, so evidence missed on a first pass can still be recovered later.

## Metadata
- **Published**: 2026-08-03T11:58:21Z
- **Authors**: Qi Liu, Yiqun Chen, Zidan Chen, Yan Gao, Yi Wu, Yao Hu, Jiaxin Mao, Fengbin Zhu, Tat-Seng Chua
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02097v1)