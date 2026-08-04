---
title: When Memory Becomes Authority: Benchmarking Authority Collapse at the Memory Consolidation Boundary
published: 2026-08-03T04:15:40Z
authors: Qiuyang Zhan, Rui Zhang, Sheng Guo, Lepeng Zhao, Zhuotao Liu
url: http://arxiv.org/abs/2608.01679v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Memory Becomes Authority: Benchmarking Authority Collapse at the Memory Consolidation Boundary

## Abstract
Persistent memory allows (self-evolving) LLM agents to adapt across tasks by consolidating heterogeneous interaction histories into reusable facts, preferences, observations, and rules. Yet consolidation also imposes an implicit authorization boundary: it determines whether stored information may later be consumed as a user fact, an attested observation, or a standing instruction. We identify authority collapse, in which consolidation preserves a claim while erasing the source constraints governing its authorized use, causing the stored memory to imply greater authority than its source permits. We introduce AuthMem-Bench, a controlled paired benchmark that holds the focal claim and downstream task fixed while varying only source authority. It evaluates write-time collapse, downstream authorization errors, and automatic authority preservation. Across seven consolidators based on widely used agent-memory systems and seven LLM backbones, we observe authority collapse in 48 of 49 evaluated configurations. In a controlled action-grounded evaluation, collapsed memories without authority metadata yield a mean unauthorized-action rate of 50.3%. In an end-to-end evaluation, automatically predicted and persisted authority labels reduce the observed unauthorized-action rate from 16.9% to 0.0%, while benign task success remains essentially unchanged. These findings show that memory-driven adaptation must preserve not only what was   learned, but also the authority under which it may be reused.

## Metadata
- **Published**: 2026-08-03T04:15:40Z
- **Authors**: Qiuyang Zhan, Rui Zhang, Sheng Guo, Lepeng Zhao, Zhuotao Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01679v1)