# Summary: 2026-08-11_05-31-18Z_MAP_Graph_Provenance_AwareSharedMemoryforMulti_Age.md
Saved: 2026-08-11 23:03
Source: 2026-08-11_05-31-18Z_MAP_Graph_Provenance_AwareSharedMemoryforMulti_Age.md
Model: None

---

## Summary  
The paper introduces MAP‑Graph, a provenance‑aware shared memory layer for multi‑agent workflows that distinguishes hard authorization from graded trust and adapts evidence requirements to action risk. It does so by modeling agents, sources, memories, claims, and actions in a typed execution graph where ancestry is traced, permissions are filtered, path trust is computed multiplicatively, and a risk‑sensitive gate checks before each action while preserving lineage for audit.

## Key Contributions  
- A provenance‑aware memory layer that integrates access control with graded trust based on the risk profile of actions.  
- A typed execution graph representation enabling precise tracing of evidence ancestry and exclusion of ineligible records.  
- A risk‑sensitive gating mechanism that reranks eligible memories by semantic similarity and multiplicative path trust before each action.

## Methodology  
The authors construct a workflow as a typed execution graph whose nodes are agents, sources, memories, claims, and actions; edges encode provenance. For each edge they compute a trust score equal to the product of permissions along the path. Only records with sufficient trust are considered eligible. Eligibility is further refined by ranking candidates according to semantic similarity. A gate evaluates the action’s risk (e.g., high‑stakes) and may reject or modify memory retrieval, while the full lineage is logged for audit.

## Results  
On a benchmark of 2,700 synthetic tasks across three domains, MAP‑Graph achieves 94.96 % overall task success, 72.70 % exact decision accuracy, and 90.22 % in the clean setting where a correct “Allow” is required. Ablations isolate the roles of permission filtering, path trust, and action gating; transfer tests with two additional backbones preserve both the exact‑decision and access‑control advantages.

## Significance  
Provenance becomes an operational control signal within the system rather than merely post‑hoc audit metadata, improving safety, efficiency, and reliability of multi‑agent interactions where evidence provenance matters.

## Related Concepts  
- Shared memory  
- Provenance tracking  
- Permission filtering  
- Path trust (multiplicative)  
- Risk‑sensitive gating  
- Typed execution graphs  
- Semantic retrieval  
- Lineage auditing
