---
title: MutMem-V2: Cryptographically Authorized Mutation in Persistent Agent Memory Portable Verification and Reproducible Evidence
published: 2026-09-01T13:34:44Z
authors: Walid Saidi
url: http://arxiv.org/abs/2609.01235v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MutMem-V2: Cryptographically Authorized Mutation in Persistent Agent Memory Portable Verification and Reproducible Evidence

## Abstract
MutMem V1 introduced retention-preserving, cryptographically authorized mutation for persistent agent memory but did not provide a complete portable verification contract or clean-install reproduction path. MutMem V2 closes that publication gap without introducing a second memory engine. It specifies exact canonical bytes, domain-separated object and bundle commitments, mandatory recall-evidence membership and ordering, external trust anchors, identity epochs, revocation, authorization, request receipts, ordered disclosure, and three mutation terminal types. The released protocol contains 18 versioned object schemas, 39 recall vectors, 15 mutation vectors, and 37 closed recall failure reasons. Independent Node and Python implementations agree on verdict and primary reason for all 72 structural and cryptographic terminals; a production-conformance corpus agrees on 42/42 cases across 28 required classes. A clean Node v26.8.1 installation reaches first-boot, restart, and scheduler readiness with no experimental memories. A separately scoped 120-unit Canary experiment supports only explicit-marker traversal. Every public table regenerates from a self-hashed aggregate, and an independent verifier reconstructs the statistics and claim boundaries. Historical V1 empirical results remain historical. MutMem V2 supports claims about portable integrity, authorization, traceability, conformance, and reproducibility under stated assumptions; it does not establish semantic truth, universal robustness, or independent replication.

## Metadata
- **Published**: 2026-09-01T13:34:44Z
- **Authors**: Walid Saidi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01235v1)