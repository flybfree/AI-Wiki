---
title: APIFlow-Bench: Measuring Whether Agents Survive Long, Dependent API Workflows
published: 2026-08-29T08:12:11Z
authors: Zelin Wan, Arash Nourian, Xiaoxiao Li, Nihar Nandan, Kamalakannan Nandagopal
url: http://arxiv.org/abs/2608.29128v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# APIFlow-Bench: Measuring Whether Agents Survive Long, Dependent API Workflows

## Abstract
Tool-using agents are commonly evaluated by a single bit: whether an end-to-end workflow completed. This metric fails to distinguish failures that matter in production, such as expired credentials, malformed payloads, or correct execution followed by incorrect final delivery. We introduce APIFlow-Bench, a fully auditable benchmark for long-horizon, dependent REST-API workflows that decomposes performance into seven engineering capabilities and requires agents to produce answers supported by the actual call path. We generate synthetic API worlds forward, subtask by subtask; each subtask is admitted only after a zero-LLM self-test triad verifies its grader and an oracle establishes solvability, and an adversarial audit identified and fixed six grader exploits. Grading is deterministic and provenance-sensitive: a state check traces a mock-minted canary through the API data flow to the response the answer must originate from, and a typed answer card is verified field by field. We release all answer keys and 44,362 unredacted execution transcripts. Across 19 frontier and open-weight models under one neutral scaffold, we find: (1) longer dependency chains degrade success, from 93% on individual subtasks to 74% on clean 20-subtask chains and 61% when including the 8% of chain trials that a model-consensus screen flags as passed by no model; (2) reliability separates models more than best-case capability, with best-of-five spanning seven points but all-five-of-five reliability spanning 44 points; (3) the independent-error account of compounding failure does not fit the data: pass rates on 20-subtask chains are 33 percentage points above the product of subtask-level rates, and on the clean slice 77% of failing runs reached the correct final state and failed only at delivery.

## Metadata
- **Published**: 2026-08-29T08:12:11Z
- **Authors**: Zelin Wan, Arash Nourian, Xiaoxiao Li, Nihar Nandan, Kamalakannan Nandagopal
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29128v1)