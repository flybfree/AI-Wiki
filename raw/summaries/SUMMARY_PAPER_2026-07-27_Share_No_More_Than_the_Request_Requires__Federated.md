---
title: Share No More Than the Request Requires: Federated Disclosure for Perspective-Aware AI
url: http://arxiv.org/abs/2607.22953v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-24_23-37-38Z_ShareNoMoreThantheRequestRequires_FederatedDisclos.md
generated_at: 2026-07-27 23:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a federated protocol called Provenance Preserving Chronicles (PPC) that enables users to securely share only the minimal context needed for a query, preserving data sovereignty and compliance. It introduces a Chronicle as a temporal knowledge graph and an authorized evidence subgraph that limits disclosure to what a requester’s relationship, purpose, and task require.

## Key Takeaways
- PPC creates a compact authorized evidence subgraph derived from each holder’s Chronicle so only the necessary information is exposed.
- The system enforces “share no more than the request requires” by projecting relationship‑aware views over domain experts’ ontologies without centralizing raw data.
- A two‑phase flow first returns provenance‑linked text, then releases raw artifacts only after explicit holder approval.

## Context
Modern AI systems often rely on centralized data collection which raises privacy and governance concerns. Federated approaches aim to keep data local while allowing useful sharing across networks. This work addresses the gap between user sovereignty and efficient cross‑domain query responses.

## Implications
For practitioners, PPC offers a framework that aligns with regulatory demands for provenance and minimal disclosure. It can be integrated into AI pipelines to reduce risk of over‑sharing and build trust in decentralized systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22953v1)
