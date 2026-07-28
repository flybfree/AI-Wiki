# Summary: 2026-07-24_23-37-38Z_ShareNoMoreThantheRequestRequires_FederatedDisclos.md
Saved: 2026-07-27 23:29
Source: 2026-07-24_23-37-38Z_ShareNoMoreThantheRequestRequires_FederatedDisclos.md
Model: None

---

## Summary  
The paper addresses the need for federated AI systems to disclose only the minimal context required by a request, preserving user privacy and sovereignty while maintaining compliance across domains. It proposes Provenance Preserving Chronicles (PPC) as a protocol that compiles personal data into authorized evidence subgraphs with the rule “share no more than the request requires.” The approach enables secure, queryable views without centralizing raw data.

## Key Contributions  
- Introduces PPC, a federated protocol for minimum‑necessary disclosure using Chronicle and authorized evidence subgraphs.  
- Defines a two‑phase flow that returns provenance‑linked text first and releases raw artifacts only after holder approval.  
- Provides an explicit threat model mapping gaps in blockchain, peer‑to‑peer, and holder‑sovereign designs.

## Methodology  
The authors map the problem of constrained disclosure across federated networks, evaluate existing solutions (blockchain, P2P, and holder‑sovereign models), define core constructs such as Chronicle, evidence subgraph, and access controller, and design a protocol flow. They also propose an explicit threat model to guide security analysis.

## Results  
Theoretically, PPC guarantees that only the request’s relationship, purpose, and task are disclosed; it prevents over‑disclosure while preserving provenance. Practically, simulations show reduced data exposure compared to baseline federated models, with latency comparable to existing protocols.

## Significance  
By enforcing “share no more than the request requires,” PPC advances privacy‑preserving AI, aligns with regulatory demands for provenance and interpretability, and supports user sovereignty in decentralized ecosystems.

## Related Concepts  
Chronicle (temporal knowledge graph), authorized evidence subgraph, federated disclosure, minimum‑necessary principle, provenance linking, access controller, threat model.
