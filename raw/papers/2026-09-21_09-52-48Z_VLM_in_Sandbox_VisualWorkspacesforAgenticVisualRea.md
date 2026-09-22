---
title: VLM-in-Sandbox: Visual Workspaces for Agentic Visual Reasoning
published: 2026-09-21T09:52:48Z
authors: Hexiong Yang, Mingrui Chen, Jie Cao, Ran He
url: http://arxiv.org/abs/2609.24362v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VLM-in-Sandbox: Visual Workspaces for Agentic Visual Reasoning

## Abstract
Sandboxed computer environments support multi-step reasoning with tools, executable programs, and persistent files, yet their extension from language models to vision-language models (VLMs) introduces a distinct state-management problem. Visual reasoning produces intermediate image-valued evidence---crops, masks, overlays, zoomed regions, and analytic renderings---that must remain addressable without accumulating unboundedly in multimodal context. We introduce VLM-in-Sandbox, a training-free framework for agentic multimodal reasoning in controlled computer environments. Its Visual Workspace registers generated artifacts in an image ledger, maintains a bounded active visual context, and lets the model explicitly promote selected evidence for subsequent inspection. This separates visual evidence generation, performed by sandbox tools, from visual evidence management. Across seven benchmarks and four base VLMs, VLM-in-Sandbox achieves the highest sample-weighted average accuracy among Vanilla VLM, Append-only Sandbox, and the proposed method. A compiler-matched $2\times2$ study on 1,260 examples further separates model-directed visibility from bounded retention: VLM-in-Sandbox reaches 66.27% accuracy with 18.6% fewer total tokens than the automatic, retain-all control. Over all 6,350 submitted GPT-4.1-mini examples, it produces 302 rescues and 142 regressions relative to Original Append-only. A local vLLM study with prefix caching confirms that the smaller request workload also reduces uncached tokens, time to first token, and end-to-end latency. These results identify explicit visual evidence state as a central abstraction for sandboxed VLM agents.

## Metadata
- **Published**: 2026-09-21T09:52:48Z
- **Authors**: Hexiong Yang, Mingrui Chen, Jie Cao, Ran He
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.24362v1)