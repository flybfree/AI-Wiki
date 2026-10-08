---
title: GeoNatureAgent (GNA): A Framework and Benchmark for Pre-Production Evaluation of Tool-Using Agents on Geospatial and Environmental Tasks
published: 2026-10-06T21:03:04Z
authors: Gabriel Diaz-Ireland, Diego Prieto-Herráez, Mario García Peces, Javier Velázquez, Benjamin Zaitchik, Devika Jain
url: http://arxiv.org/abs/2610.09112v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GeoNatureAgent (GNA): A Framework and Benchmark for Pre-Production Evaluation of Tool-Using Agents on Geospatial and Environmental Tasks

## Abstract
Before tool-using LLM agents are deployed in environmental and geospatial workflows, teams need evidence that an agent reliably selects the right operations against real APIs. We introduce GeoNatureAgent (GNA), a framework for pre-production evaluation of tool-using agents: a fixed sixteen-tool geospatial interface published as a Model Context Protocol (MCP) server, so the agent under test is the only variable, scored against an identical tool layer, task suite, and deterministic scorer. Its flagship instance is a 103-task benchmark (a 93-task main suite across 18 categories plus a ten-task comparison expansion) evaluated against an open, self-hostable geospatial API serving three environmental indicators across Spain and Portugal. We evaluate nine LLMs under three temperature-1.0 seeds, reporting capability and per-case cost as orthogonal axes. (1) Claude Sonnet 4 achieves the highest capability (61.7% +/- 0.7% on all 103 tasks; 60.8% on the main suite), followed closely by DeepSeek V3.2 (57.9%), while no other model exceeds 53%; (2) the cost-accuracy Pareto frontier is mostly open-weight, with DeepSeek V3.2 offering 93% of Claude's capability at 11.3x lower list-price cost; (3) under strict all-checks scoring the best model sits 24-36 points below the 85-97% reported on general-purpose GIS benchmarks, whereas per-check partial credit for the top four models (86-90%) is comparable, so much of that gap reflects scoring strictness rather than task difficulty alone. The MCP server, evaluation harness, benchmark, and API are publicly available; swapping the tool executors and task suite instantiates an equivalent benchmark for any geospatial domain.

## Metadata
- **Published**: 2026-10-06T21:03:04Z
- **Authors**: Gabriel Diaz-Ireland, Diego Prieto-Herráez, Mario García Peces, Javier Velázquez, Benjamin Zaitchik, Devika Jain
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.09112v1)