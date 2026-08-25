---
title: Enrich-Retrieve-Rank: Scaling Capability Discovery Beyond In-Context Routing
published: 2026-08-24T01:21:05Z
authors: Nazib Sorathiya, Daniel Zhang, Bardiya Akhbari
url: http://arxiv.org/abs/2608.22695v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Enrich-Retrieve-Rank: Scaling Capability Discovery Beyond In-Context Routing

## Abstract
Agent ecosystems now include thousands of MATS components (Models, Agents, Tools, and Skills), yet their discovery still relies on in-context routing. These systems read a registry (names, hints, or descriptions, as context budget permits), pick a candidate, invoke it, and retry on failure. This pattern degrades with scale, and registries are growing fast. We recast capability discovery as search over a registry by defining an offline enrichment step that turns sparse metadata into searchable profiles, and an online retrieve-then-rank pipeline that returns a ranked shortlist without invoking any candidates online. We show that from N=10 to 7,278 capabilities, in-context routing's top-1 accuracy (Match@1) collapses (0.85 to 0.12), while retrieve-then-rank degrades more gently (0.81 to 0.39) because its reranker still ranks the right capability first 0.70-0.87 of the time once retrieval finds it. In the Nova Micro sweep, the crossover is around N=500. We compare against two in-context baselines. Full-Ctx puts the whole registry in the prompt and asks the LLM to pick. Search&Pick gives the LLM a search tool to narrow candidates before it picks. At full scale the pipeline leads Search&Pick by 6.5 percentage points (pp) on Match@1 at about half the cost. It reduces cost 70x versus Full-Ctx. We use a fixed configuration (same enrichment, retriever, and scorer weights) across agent, tool, and skill registries. The pipeline runs in production as the default capability-discovery layer of a large-scale multi-agent platform.

## Metadata
- **Published**: 2026-08-24T01:21:05Z
- **Authors**: Nazib Sorathiya, Daniel Zhang, Bardiya Akhbari
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22695v1)