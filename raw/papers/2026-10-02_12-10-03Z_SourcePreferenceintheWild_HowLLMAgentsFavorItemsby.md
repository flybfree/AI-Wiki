---
title: Source Preference in the Wild: How LLM Agents Favor Items by Source, and How to Reduce It
published: 2026-10-02T12:10:03Z
authors: Jonghyun Song, Haewon Park, Jeonghoon Shim, Woojung Song, Yohan Jo
url: http://arxiv.org/abs/2610.03195v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Source Preference in the Wild: How LLM Agents Favor Items by Source, and How to Reduce It

## Abstract
As LLM agents decide on users' behalf which product to buy, which hotel to book, or which paper to cite, a preference for items from certain sources (the sites or services they come from) shapes what users receive and which sources are selected. We study source preference in end-to-end search with 12 agent models across three domains. Comparing items from different sources that satisfy the same requirements at the same position, we find that each model prefers some sources and avoids others in every domain, largely agreeing on which. This preference can outweigh how well items satisfy the request: an item satisfying one requirement fewer is selected about two-thirds of the time when it comes from a preferred source and the better one from a dispreferred source, but almost never in the reverse case. The information identifying an item's source affects selection by itself: hiding it weakens the preference, and relabeling an item with a preferred source raises its selection rate. We test two routes to this preference: training that rewards better items can make a source a shortcut for requirement satisfaction, and missing information can trigger preconceptions about the source. Supplying missing information or a prompt countering these preconceptions reduces source preference.

## Metadata
- **Published**: 2026-10-02T12:10:03Z
- **Authors**: Jonghyun Song, Haewon Park, Jeonghoon Shim, Woojung Song, Yohan Jo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.03195v1)