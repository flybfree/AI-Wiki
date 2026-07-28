---
title: AlloBench: Measuring Online Tool Allocation Capability in LLM Agents
published: 2026-07-25T19:05:29Z
authors: Daniel Wang, Andrew Xu
url: http://arxiv.org/abs/2607.23332v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AlloBench: Measuring Online Tool Allocation Capability in LLM Agents

## Abstract
Creating a reusable tool is an investment: an agent pays a fixed cost now in exchange for the potential of future reuse. Therefore, a user should prefer an agent that creates a small number of highly reusable tools, rather than many one-offs. We introduce a paired benchmark that tests whether LLM agents exhibit conscious allocation behavior under a fixed budget in two contexts: an abstract text-based formulation and a code-construction task. We find that every frontier model we test---Claude Haiku, Claude Opus, GPT-5.4-mini, and GPT-5.6 Sol---acts near-optimally in the abstract framing but fails to transfer this ability to script-writing. Through further experiments, we identify the particular failure modes for each model. Notably, the first three models fail even when the scripts are not evaluated, while GPT-5.6 Sol stays selective under that weaker manipulation and collapses only at full construction. Furthermore, an open-source Qwen model policy-trained for abstract allocation generalizes this ability across held-out lexical variations, but sees no improvement at script allocation. Together, these results establish online tool allocation as a significant capability boundary, even for modern frontier models.

## Metadata
- **Published**: 2026-07-25T19:05:29Z
- **Authors**: Daniel Wang, Andrew Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23332v1)