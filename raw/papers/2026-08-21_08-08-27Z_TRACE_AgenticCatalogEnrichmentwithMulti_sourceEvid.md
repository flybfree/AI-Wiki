---
title: TRACE: Agentic Catalog Enrichment with Multi-source Evidence Grounding
published: 2026-08-21T08:08:27Z
authors: Rohan Kumar, Steven Xu, Kyle MacDonald, Matthew Long, Bernice Chow, Mac VanRenterghem, Sudeep Das
url: http://arxiv.org/abs/2608.20844v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TRACE: Agentic Catalog Enrichment with Multi-source Evidence Grounding

## Abstract
Product catalogs underpin search, discovery, and recommendation in e-commerce, yet they are often attribute-sparse: the attributes shoppers and downstream systems rely on are either buried in unstructured content such as titles and images or missing from the catalog altogether. Manually enriching e-commerce catalogs is impractical given their scale and rapid growth. This paper introduces TRACE, a novel framework for automated catalog attribute enrichment using agentic Large Language Models (LLMs). A ScoutAgent triangulates multimodal evidence across merchant catalogs, syndicated feeds, and identity-matched web search to propose candidate attribute values with supporting evidence, while a JudgeAgent verifies the proposed value for each attribute value against its supporting evidence and decides whether to publish it or route it to human review. On an offline human evaluation dataset, TRACE's proposed attribute values were 98.2% accurate at 74.7% attribute coverage. Deployed in production on an industry-scale catalog, TRACE increased impression-weighted enrichment coverage across four business verticals by 90.4%. An online experiment subsequently showed that surfacing the enriched attributes on the product detail page increased checkout conversion by 0.48%.

## Metadata
- **Published**: 2026-08-21T08:08:27Z
- **Authors**: Rohan Kumar, Steven Xu, Kyle MacDonald, Matthew Long, Bernice Chow, Mac VanRenterghem, Sudeep Das
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20844v1)