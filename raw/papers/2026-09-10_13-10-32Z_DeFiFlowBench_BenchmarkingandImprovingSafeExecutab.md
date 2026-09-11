---
title: DeFiFlowBench: Benchmarking and Improving Safe Executability in Natural-Language DeFi Workflow Synthesis
published: 2026-09-10T13:10:32Z
authors: Abhinav Rajeev Kumar, Harshit Arora, Varun Singh, Manikandan Nanjappan
url: http://arxiv.org/abs/2609.11504v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DeFiFlowBench: Benchmarking and Improving Safe Executability in Natural-Language DeFi Workflow Synthesis

## Abstract
A structurally valid DeFi workflow can still authorize a costly trade. We introduce DeFiFlowBench, a benchmark of 207 team-authored prompts for natural-language DeFi workflow synthesis. It measures graph coverage, configuration completeness, and declared safety predicates, then tests supported trade configurations on a local EVM. Direct, constrained, and few-shot prompting produce 14-19 unsafe held-out executions per configuration under a fixed 5% price-impact cap. A slippage bound derived from a quote does not prevent the price impact of the order itself. We propose Koan-Safe, which combines a prompt-only intent parser, a replaceable generator, and structural repair with default safety parameters. On 75 held-out workflow prompts, its hybrid variant scores 0.67 on the static safety proxy, compared with 0.33 for the best baseline. Koan-Safe records no unsafe executions on the saved benchmark outputs. A matched-candidate ablation produces 14-17 unsafe executions when enforcement is disabled. Additional tests expose the limits of default injection: permissive existing thresholds can still authorize unsafe trades. A separately evaluated policy cap addresses this failure on a 36-case diagnostic grid. These results support explicit trade protections and execution-based evaluation, while distinguishing declared safety from a general guarantee.

## Metadata
- **Published**: 2026-09-10T13:10:32Z
- **Authors**: Abhinav Rajeev Kumar, Harshit Arora, Varun Singh, Manikandan Nanjappan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.11504v1)