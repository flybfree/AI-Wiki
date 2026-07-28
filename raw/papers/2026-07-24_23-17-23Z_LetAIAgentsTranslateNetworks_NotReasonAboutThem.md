---
title: Let AI Agents Translate Networks, Not Reason About Them
published: 2026-07-24T23:17:23Z
authors: Hongyu Hè, Maria Apostolaki
url: http://arxiv.org/abs/2607.22947v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Let AI Agents Translate Networks, Not Reason About Them

## Abstract
A formal model enables verifying reachability, localizing an outage, or anticipating the blast radius of a change. Yet, virtually no production network has one, since writing a model by hand demands rare expertise and is hard to keep current as the network changes frequently. At its core, network modeling is a typographical exercise: it translates network artifacts (e.g., configurations, topology, and routing state) into rules in formal logic. Translation of this kind is what large language models (LLMs) nowadays do well. Unlike free-form AI reasoning, such translation can be formally verified.   Once modeling is no longer the bottleneck, trusting AI to reason over large, complex networks no longer makes sense. Our position therefore cuts against the prevailing race to put autonomous AI agents in charge end-to-end. We instead confine AI to translation and rely on a solver for reliable long-horizon reasoning, building a reusable formal model of general network behavior that can then be specialized to specific tasks, e.g., root-cause analysis (RCA). We build TypoNet that constructs and validates a symbolic model of an emulated production-scale WAN from the network's own artifacts. Our preliminary evaluation shows TypoNet helps in two ways. On its own, TypoNet answers operational questions (e.g., reachability verification and change-impact analysis) faster, more cheaply, and more reliably than an LLM. As a tool for an AI agent, TypoNet boosts fault localization at lower cost. The result makes the case for AI that builds verifiable network models and relies on a solver for reliable long-horizon reasoning.

## Metadata
- **Published**: 2026-07-24T23:17:23Z
- **Authors**: Hongyu Hè, Maria Apostolaki
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22947v1)