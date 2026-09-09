---
title: CIVI: A Framework for Diagnosing Search Agent Failures in Civic Information
url: http://arxiv.org/abs/2609.08094v1
type: paper-summary
date: 2026-09-08
source_paper: 2026-09-08_01-09-40Z_CIVI_AFrameworkforDiagnosingSearchAgentFailuresinC.md
generated_at: 2026-09-08 22:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CIVI, a framework for diagnosing search agent failures in civic information, and evaluates ten frontier agents against human baselines. It finds that none of the agents matches an attentive human baseline across accuracy, invocation rate, selective no-search accuracy, and source citation rates. A key diagnostic tool ARISE decomposes failures into four modes, showing retrieval-bound causes account for most errors.

## Key Takeaways
- CIVI's benchmark spans cross-national, interjurisdictional government contexts covering UN standard functional categories, providing a comprehensive testbed for civic search agents.  
- The evaluation reveals all ten agents underperform human baselines in accuracy and source citation metrics, indicating systemic issues beyond simple knowledge gaps.  
- ARISE attributes 72.1% of observed failures to retrieval-bound causes rather than to gaps in the models' parametric knowledge.

## Context
In AI for public service, deploying search agents carries high stakes because errors can mislead citizens. This paper addresses the need for systematic failure analysis beyond accuracy alone, highlighting that diagnostic tools are essential for trustworthy civic AI.

## Implications
For policymakers and developers, CIVI offers a diagnostic framework to pinpoint where search failures occur in government information systems. It encourages prioritizing retrieval improvements over model fine-tuning when addressing civic AI challenges.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.08094v1)
