---
title: Interface-Induced Trajectory Censoring
url: http://arxiv.org/abs/2609.03966v1
type: paper-summary
date: 2026-09-04
source_paper: 2026-09-03_15-00-31Z_Interface_InducedTrajectoryCensoring.md
generated_at: 2026-09-04 15:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates why the tool‑call rate reported by an agent can be zero even when the model emits perfectly valid calls, attributing it to interface censoring rather than model failure. Experiments show that swapping serving components dramatically changes scores and call acceptance rates across a range of model sizes, indicating that the problem lies in the interaction between the parser and adapter.

## Key Takeaways
- The tool‑call rate is zero because the server parses the trajectory before any downstream component sees it, censoring the signal.  
- Changing only the serving adapter or parser yields opposite effects: one side scores 0.00 while the other scores near 1.0, proving the interaction—not a single defect—drives the outcome.  
- Silent failures persist across model scales; at evaluation time the silent fraction stays between 0–2 per 100 calls, and fixing the adapter restores parsing but yields only marginal pass‑rate improvement.

## Context
In AI research on agentic systems, evaluating end‑to‑end tool usage is essential yet often overlooked. This work highlights that performance metrics can be misleading if they ignore how model outputs are filtered by serving infrastructure, a common source of silent failures in real deployments.

## Implications
For practitioners building or deploying agent pipelines, the findings stress the need for robust interface checks to prevent invisible censoring from degrading tool‑use rates. Ignoring this interaction can lead to inflated performance estimates and wasted effort on model fine‑tuning alone.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.03966v1)
