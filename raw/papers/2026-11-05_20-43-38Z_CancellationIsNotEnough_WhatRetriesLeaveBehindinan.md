---
title: Cancellation Is Not Enough: What Retries Leave Behind in an Overloaded LLM Engine
published: 2026-11-05T20:43:38Z
authors: Xindan Zhang, Fei Wang
url: http://arxiv.org/abs/2611.08684v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cancellation Is Not Enough: What Retries Leave Behind in an Overloaded LLM Engine

## Abstract
Clients and proxies in front of an LLM engine retry calls that time out. After a transient overload, these retries can keep the engine from recovering even when calls arrive below its capacity. Since the engine may keep computing for clients that have left, propagating cancellation looks like the natural remedy. In this paper, we test it on vLLM with overload experiments on three open models, and with scheduler traces of one that follow each client attempt to the execution it creates in the engine. We find that with retries on, cancellation alone did not restore service in any run, and only 12-38% of the calls that arrived after the overload were delivered. The traces suggest why: retries that vLLM ran typically started prefill less than half a second before they timed out. Executions that vLLM later aborted took 79-85% of the prompt tokens it computed, and vLLM's prompt-token counter missed a third to half of all computed prompt tokens. A retry budget restored service by shedding retries but left many of the overload's calls undelivered. Request coalescing delivered every call from the overload onward, some late, unless cancellation had already aborted the running execution. Overload controls should thus be judged by the executions that retries add and the calls that clients receive.

## Metadata
- **Published**: 2026-11-05T20:43:38Z
- **Authors**: Xindan Zhang, Fei Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.08684v1)