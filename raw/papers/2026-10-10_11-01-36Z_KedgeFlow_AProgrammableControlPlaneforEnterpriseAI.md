---
title: KedgeFlow: A Programmable Control Plane for Enterprise AI Agents
published: 2026-10-10T11:01:36Z
authors: Jun He, Deying Yu
url: http://arxiv.org/abs/2610.14810v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# KedgeFlow: A Programmable Control Plane for Enterprise AI Agents

## Abstract
Enterprise AI agents can execute altered versions of approved actions, concurrently reuse the same permission, or retry operations whose responses were lost. These failures arise when approval and resource execution lack a shared contract. KedgeFlow specifies language-independent contracts for trusted controllers to authorize state-changing operations and privileged gateways to enforce that authority independently of agent reasoning. Inspired by OpenFlow, it connects policy checks supported by evidence, signed permission for an exact action, a shared allowance that can be consumed only once, target-side conditions for applying the change, and retained outcome records. Under trusted issuance of exact-action authority, two conditional properties establish at most one successful claim per allowance and link every governed dispatch to a matching grant, claim, and subsequent dispatch authorization, even when the agent is compromised. A reference implementation exposes this execution path to agent systems through the Model Context Protocol (MCP). In the single-resource evaluation, 6,560 concurrent ledger claim attempts yielded exactly one successful claim for each of 82 allowances. Boundary tests rejected unauthorized and altered requests before consumption. A 32-call gateway race produced one committed mock effect, and a retry after a lost response produced no additional dispatch. Deliberately permissive policy nevertheless authorized an undesirable effect, exposing the limits of execution authorization. Evaluation uses three members of the etcd coordinated key-value store on one host, synthetic authentication and authorization inputs, and a mock target that rejects stale requests. Distributed reservations, enforcement of every production access route, native crash recovery, exactly-once effects at real targets, and interoperability between independent implementations remain untested.

## Metadata
- **Published**: 2026-10-10T11:01:36Z
- **Authors**: Jun He, Deying Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.14810v1)