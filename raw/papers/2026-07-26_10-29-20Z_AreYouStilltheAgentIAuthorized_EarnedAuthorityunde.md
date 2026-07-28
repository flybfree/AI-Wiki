---
title: Are You Still the Agent I Authorized? Earned Authority under a Fixed Ceiling for Evolving Agents
published: 2026-07-26T10:29:20Z
authors: Zhaoxi Zhang, Xiaomei Zhang
url: http://arxiv.org/abs/2607.23586v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Are You Still the Agent I Authorized? Earned Authority under a Fixed Ceiling for Evolving Agents

## Abstract
Long-lived AI agents increasingly evolve after deployment by retaining experience, acquiring skills and tools, revising workflows, delegating work, and moving across task phases. This improves adaptation but creates a distinct authorization problem. Tool-enabled agents can turn model errors and prompt injections into consequential external actions; when evolution occurs under a live grant, the subject exercising that authority or the context in which it acts may no longer match what the user evaluated. Evolution can change both the effects reachable under an old grant and the authority required by the task, which may rise, fall, or become incomparable. Existing tool policies constrain actions but do not determine when a grant survives this change.   We formulate authorization continuity: when does an existing grant remain valid, how may active authority change, and what boundary must never move? Our state-bound model fixes a transition envelope and an immutable effect ceiling at grant time. The envelope determines whether the grant survives a mutation; below the ceiling, authority may contract freely and expand only under specified evidence conditions. We distinguish requested from realized effects and prove that, under complete mediation, sound effect abstraction, attenuating delegation, and monitor integrity, mutation cannot amplify protected effects beyond the user-issued ceiling. Agent-produced evidence may allocate authority below the ceiling but cannot raise it. Finally, we map six mutation classes to their authorization consequences.

## Metadata
- **Published**: 2026-07-26T10:29:20Z
- **Authors**: Zhaoxi Zhang, Xiaomei Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23586v1)