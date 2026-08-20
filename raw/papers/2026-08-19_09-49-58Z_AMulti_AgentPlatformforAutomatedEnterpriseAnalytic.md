---
title: A Multi-Agent Platform for Automated Enterprise Analytics and Insight Generation
published: 2026-08-19T09:49:58Z
authors: Manoj N M, Vijayakrishna S, Manjunath Srinivas, Rohit Pahan
url: http://arxiv.org/abs/2608.18740v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Multi-Agent Platform for Automated Enterprise Analytics and Insight Generation

## Abstract
This paper proposes a multi-agent framework built on CrewAI [1] for conversational business intelligence. Five specialized AI agents operate in a sequential pipeline to process natural language queries, retrieve and analyze data, generate visualizations via the Model Context Protocol (MCP) [2], and deliver actionable insights. The platform features a defense-in-depth security architecture for multi-tenant data isolation and a query parameterization mechanism for transforming conversational insights into reusable dashboard components. Evaluation across 300 end-to-end test cases spanning synthetic and production enterprise datasets demonstrates 95.3% functional accuracy, a mean response latency of 24 seconds, and a response quality score of 4.52/5.0 as assessed by an LLM-as-a-Judge framework, with a 93.0% hallucination-free rate, representing a 22.6 percentage point accuracy improvement and 20.2% quality gain over a single-agent baseline. Cross-model evaluation across four LLM backends and human expert validation confirm architectural generalizability and evaluator reliability. An ablation study confirms that the Data Analysis and Report Aggregation agents are the primary drivers of output quality.

## Metadata
- **Published**: 2026-08-19T09:49:58Z
- **Authors**: Manoj N M, Vijayakrishna S, Manjunath Srinivas, Rohit Pahan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18740v1)