---
title: TRACER: Trajectory-Aware Tool Retrieval for LLM Agents
published: 2026-10-15T05:00:58Z
authors: Tanish Kher, Sarvesh DK, Abedelkadir Asi, Sparsha Chennarayapatna Sundaresh, Dezhi Hong
url: http://arxiv.org/abs/2610.21267v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TRACER: Trajectory-Aware Tool Retrieval for LLM Agents

## Abstract
Modern agents select tools from registries, but exposing entire registries incurs high token costs and can impair selection as they grow. We present TRACER, a retrieval front-end that indexes observed tool-call sequences in a trie and ranks continuations using a learned blend of empirical and contextual priors. On a mixed retail-and-telecom $τ^2$ environment, TRACER improves GPT-5.4's tool-selection accuracy by 4.7 points while reducing input tokens per step by 80%, exposing just 5 of 128 tools. In autonomous full-turn execution, it matches GPT-5.4's full-registry task success with 61% fewer input tokens per step. Across six environments and four models, TRACER improves tool-selection accuracy over full-registry selection in 21 of 24 model-environment pairs, with average gains of 6 to 10 points; the three exceptions trail by at most 2.2. We analyze failures in both regimes to identify directions for future work.

## Metadata
- **Published**: 2026-10-15T05:00:58Z
- **Authors**: Tanish Kher, Sarvesh DK, Abedelkadir Asi, Sparsha Chennarayapatna Sundaresh, Dezhi Hong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.21267v1)