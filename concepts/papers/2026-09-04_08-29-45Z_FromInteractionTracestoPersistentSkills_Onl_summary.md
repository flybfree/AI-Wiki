# Summary: 2026-09-04_08-29-45Z_FromInteractionTracestoPersistentSkills_OnlineEvol.md
Saved: 2026-09-06 21:44
Source: 2026-09-04_08-29-45Z_FromInteractionTracestoPersistentSkills_OnlineEvol.md
Model: None

---

## Summary  
Computer‑use agents can perform complex GUI tasks but their procedural knowledge is usually transient, never retained across rollouts. The authors introduce an online skill‑evolution framework that turns interaction traces and evaluator feedback into a persistent, versioned library of reusable procedures. By freezing the library snapshot between iterations and updating it only with evidence‑driven changes, they create a shared procedural memory that can be audited and reused without altering model parameters. This approach demonstrates that incremental skill updates can meaningfully improve performance on fixed computer‑use stacks.

## Key Contributions  
- [Finding 1] An online skill‑evolution framework converts interaction traces and evaluator feedback into a persistent, versioned library of reusable procedures, with each iteration operating against a frozen snapshot.  
- [Finding 2] The evolving‑library system outperforms an empty‑library control across four OSWorld domains, achieving mean score improvements ranging from 5.7 to 18.6 percentage points after a five‑iteration warm‑up.  
- [Finding 3] Provenance‑aware analysis shows that while retrieval can cross task boundaries, repeated revision leads to churn and loss of original tasks, indicating that benefits are conditional and not guaranteed.

## Methodology  
The authors built an evolving library where every iteration executes against a frozen snapshot of previously stored procedures. Interaction traces from the agent’s GUI actions together with evaluator feedback are encoded into this snapshot, and evidence‑guided updates are applied only when they improve task performance. The same fixed action‑generation and GUI‑grounding stack is used for all four OSWorld application domains, with identical task sets and iteration horizons. A control experiment runs the full system with an empty library to isolate the effect of skill evolution.

## Results  
After a five‑iteration warm‑up period, the Full system consistently yields higher post‑warm‑up evaluator scores in every domain compared with the empty‑library baseline. The mean differences are substantial: 5.7 pp in one domain and up to 18.6 pp in another, reflecting domain‑specific temporal stability of skill reuse. Provenance analysis reveals that revisions can be retrieved across task boundaries, but repeated accepted edits sometimes fail to recover the originating task, highlighting the fragility of persistent knowledge.

## Significance  
The work shows that evolving skill libraries act as an auditable, shared procedural memory that can boost a fixed computer‑use stack without retraining models. However, the conditional nature of these gains—evidenced by revision churn and loss of provenance—means that long‑term reliability is not assured. This research bridges human‑like skill acquisition with automated agents, offering a template for continual learning in interactive environments.

## Related Concepts  
- Interaction traces  
- Persistent skills  
- Procedural knowledge  
- Versioned library  
- Evidence‑guided updates  
- Provenance  
- Revision churn  
- Computer‑use agents  
- OSWorld application domains
