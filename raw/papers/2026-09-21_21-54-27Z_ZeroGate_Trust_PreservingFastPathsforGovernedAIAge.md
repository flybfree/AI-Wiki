---
title: ZeroGate: Trust-Preserving Fast Paths for Governed AI Agent Runtimes
published: 2026-09-21T21:54:27Z
authors: Zexun Wang
url: http://arxiv.org/abs/2609.25443v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ZeroGate: Trust-Preserving Fast Paths for Governed AI Agent Runtimes

## Abstract
Moving authorization earlier can shorten an agent's dispatch boundary without removing authorization work. It can also admit an action whose payload, authority, or relevant state has changed. ZeroGate separates exact-action approval from durable local admission: an issuer signs a short-lived ActionPass, and a trusted runtime adapter reconstructs the final action before a local gate checks its binding and consumes its nonce. A SQLite transaction couples nonce consumption, applicable quota updates, and an admission receipt. We state a conditional decision-preservation proposition: successful local admission implies that a specified synchronous policy would authorize the same action at the admission point, provided approval is sound, all policy dependencies are represented and current, observations are faithful, and consumption is atomic. The implementation alone establishes neither current-world freshness nor exactly-once remote effects. Evaluation separates authored semantic fixtures, controlled concurrency and crash experiments, and an Azure Blob study comparing synchronous and prepared execution through the same issuer and gate. Both modes mint an exact-action pass; lifecycle latency includes preparation and prepared-batch dwell. Across 4800 cloud attempts, prepared worker-admission-to-dispatch p95 ranges from 9.802 to 11.374 ms, versus 25.018 to 334.000 ms synchronously, across the tested concurrency levels. Prepared mean complete lifecycle is longer at every level: the boundary improvement is not a net speedup. The contribution is an explicit revalidation contract, a durable reference boundary, and an auditable comparison of where authorization cost is paid, not a new cryptographic primitive or a universal performance frontier.

## Metadata
- **Published**: 2026-09-21T21:54:27Z
- **Authors**: Zexun Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.25443v1)