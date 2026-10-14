---
title: Google Earth AI Geospatial Reasoning Agent: Capabilities and a Systematic Evaluation
published: 2026-10-11T16:31:29Z
authors: Noam Slonim, Aviv Slobodkin, Gil Fidel, Gal Moshitch, Mimi Sun, Lily Mihalkova, Joydeep Paul, Per Bjornsson, Sydney Lin, Jamie McPike, Samapriya Roy, Utkarsh Patel, Gia Jung, Zachary Luna, Allison Berman, William Cai, Xiao Wu, Mohit Agarwal, Mandar Sharma, Aliza Hoffman, Mark Young, Rama Pasumarthi, Roy Lee, Ruth Alcantara, Luke Barrington, Aaron Bell, Reuven Sayag, Avinatan Hassidim, Yossi Matias, Tyler McHenry, Ronald Ho, Christopher Haire, Oliver Guinan, Niv Efron, Tim Thelin, Gautam Prasad, Shravya Shetty
url: http://arxiv.org/abs/2610.15750v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Google Earth AI Geospatial Reasoning Agent: Capabilities and a Systematic Evaluation

## Abstract
Google Earth AI is a family of geospatial AI models, together with an agent that orchestrates them. We present this agent, Google Earth AI's Geospatial Reasoning agent (GRA), a Gemini-powered research system that combines geospatial data sources, foundation models, and tools to answer questions about our planet. GRA organizes these into modular domain skills and pairs them with upfront geospatial planning to decompose complex queries into multi-stage workflows. Evaluating such systems is hard: real-world problems admit multiple valid workflows, require data discovery across large catalogs, and rely on evolving ground truth. We introduce two benchmarks and release their development splits. GeoExpertQueries poses complex analytical problems grounded in practitioner use cases and refined by geospatial experts; each is paired with a consensus golden workflow from three independent experts and scored by a human-validated, tool-agnostic autorater. GeoKTools consists of templated queries with deterministic reference solvers that systematically vary the number of required tool types. We also use two external benchmarks, CBGB and UnivEARTH; the latter we find to be saturated. To isolate the contribution of GRA's tools and its agentic orchestration, we compare four configurations, each with Gemini 3.1 Pro and 3.8 Flash: a standalone LLM, the LLM with basic tools, the LLM with GRA's skills and tools but without its upfront planning and execution guidance, and GRA itself. With at most basic tools, an advanced model recovers much of the answer on templated queries but satisfies only a small fraction of the expert workflows on open-ended problems; GRA performs well on both. The largest step comes from GRA's skills and tools; on open-ended problems, its planning and execution guidance add a further gain with Gemini 3.8 Flash, letting Flash match or exceed Pro at lower cost.

## Metadata
- **Published**: 2026-10-11T16:31:29Z
- **Authors**: Noam Slonim, Aviv Slobodkin, Gil Fidel, Gal Moshitch, Mimi Sun, Lily Mihalkova, Joydeep Paul, Per Bjornsson, Sydney Lin, Jamie McPike, Samapriya Roy, Utkarsh Patel, Gia Jung, Zachary Luna, Allison Berman, William Cai, Xiao Wu, Mohit Agarwal, Mandar Sharma, Aliza Hoffman, Mark Young, Rama Pasumarthi, Roy Lee, Ruth Alcantara, Luke Barrington, Aaron Bell, Reuven Sayag, Avinatan Hassidim, Yossi Matias, Tyler McHenry, Ronald Ho, Christopher Haire, Oliver Guinan, Niv Efron, Tim Thelin, Gautam Prasad, Shravya Shetty
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.15750v1)