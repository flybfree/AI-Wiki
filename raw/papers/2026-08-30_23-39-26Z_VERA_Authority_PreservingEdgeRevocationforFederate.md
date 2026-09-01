---
title: VERA: Authority-Preserving Edge Revocation for Federated AI-Agent Workflows
published: 2026-08-30T23:39:26Z
authors: Lifei Liu, Haoran Yu, Xiaochong Jiang
url: http://arxiv.org/abs/2608.30091v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VERA: Authority-Preserving Edge Revocation for Federated AI-Agent Workflows

## Abstract
Modern agent frameworks compose planners, tool agents, remote services, and shared specialists into runtime delegation graphs, but their revocation APIs still resemble token or subtree invalidation. When one delegation is withdrawn, the runtime must know which agents lose authority while independently authorized agents keep working. We study this authority consistency problem and introduce VERA (Verifiable Edge Revocation for Agents), a verifier-checkable revocation contract and API emitted by agent-runtime adapters as signed evidence. Under disjunctive authority, revoking edge e invalidates exactly T_intent(e,G) = reach(G) \ reach(G \ {e}), the agents whose every authorizing root path used e. Used as a contract, this target exposes two runtime failures: tree cascades over-revoke shared agents, while deployer-scoped cascades under-revoke cross-domain descendants. In a LangGraph framework-replt cells repeated 20 times yield 500compiled-framework traces and 2,000 valid signed delegation decisions; 13/25 cells contain runtime multi-parsharing and 8/25 contain cross-deployer shies 500/500 target proofs, preserves all320 alternate-parent shared-agent cases that tree cascade revokes, and rejects unauthorized signers and omission attacks. Baseline replay over 1,9that holder/node and tree-style targetscannot express this behavior. We further validate schema portability on A2A, AutoGen, and CrewAI artifacts: nine traces, including five executable Cregned delegation events that pass schema and signature checks.

## Metadata
- **Published**: 2026-08-30T23:39:26Z
- **Authors**: Lifei Liu, Haoran Yu, Xiaochong Jiang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30091v1)