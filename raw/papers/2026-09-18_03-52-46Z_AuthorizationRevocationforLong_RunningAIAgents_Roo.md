---
title: Authorization Revocation for Long-Running AI Agents: Root-Scoped Quiescence under Delegation and Asynchronous Execution
published: 2026-09-18T03:52:46Z
authors: Genliang Zhu, Chu Wang
url: http://arxiv.org/abs/2609.21284v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Authorization Revocation for Long-Running AI Agents: Root-Scoped Quiescence under Delegation and Asynchronous Execution

## Abstract
Long-running AI agents outlive initiating processes through credentials, delegated tasks, queues, callbacks, reservations, and provider-side operations. Cancellation, process exit, and credential revocation neither close every pre-cut carrier nor distinguish independently authorized shared work. We define root-scoped authorization quiescence: for each manifested sink, a certificate accounts for every cut-relevant acceptance under the retired root-epoch atom that precedes its local fence and excludes protected acceptance under that atom after the fence, while permitting exact rebind to a current, independently sufficient support.   The root-scoped quiescence protocol linearizes a root cut, fences old-root expansion and protected sinks, represents alternative and conjunctive authority as antichains of minimal sufficient root sets, and composes provider-frontier certificates into a cutset over registered old-root paths. Exact channel-token accounting reconciles transfers; missing or conflicting evidence remains indeterminate. Under stated assumptions, we prove post-cut issuer non-expansion, support-sound projection, compositional soundness under exact channel conservation, independent-support preservation, merge-order independence, and crash/replay stability.   A provider-free late-effect test suite matches 17/17 registered outcomes. Two cancellation-only and one cut-only execution accept the same class of already scheduled late effect; two cut-plus-fence executions, one restart, and one stale-process execution reject it. A separately implemented checker verifies 17/17 traces and rejects 44/44 consistently rehashed semantic regressions. The certificate establishes root-relative authorization quiescence within its bound manifest and configuration, not global idleness, rollback, or business completion.

## Metadata
- **Published**: 2026-09-18T03:52:46Z
- **Authors**: Genliang Zhu, Chu Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.21284v1)