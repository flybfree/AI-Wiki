# Summary: 2026-08-09_22-43-27Z_WhatWouldFixThisRAGFailure_AuditingCounterfactualR.md
Saved: 2026-08-10 23:30
Source: 2026-08-09_22-43-27Z_WhatWouldFixThisRAGFailure_AuditingCounterfactualR.md
Model: None

---

## Summary  
The paper tackles the problem of RAG failures by investigating whether a single incorrect response can be explained by multiple unseen evidence‑repair strategies. It proposes **Pair‑ID**, an offline audit that isolates query, retrieval state and reader while varying the addition or deletion of missing versus verified nonsupport to generate counterfactual responses. By applying this method across 19 981 benchmark queries it discovers a large pool of eligible failures, selects a subset via SHA‑256 ordering, and evaluates how repair interventions affect answer quality.

## Key Contributions  
- [Finding 1] Pair‑ID creates a systematic set of counterfactual response vectors that share the same failure but differ only in evidence addition or deletion.  
- [Finding 2] Support‑addition repairs roughly one third of JOINT cases (0.328 ± 0.075) while deletion repairs about one tenth (0.136 ± 0.019), indicating that adding missing support is more effective than removing nonsupport.  
- [Finding 3] The observed evidence sensitivity is reader‑dependent and only partially predictable from the original failure, with pooled exact‑vector agreement ranging from 0.675 to 0.765.

## Methodology  
Pair‑ID holds a query, its retrieval state and the reader constant, then performs two operations: (i) adds missing support that is not present in the retrieved set, or (ii) deletes verified nonsupport that was included. The resulting pairs are ordered by SHA‑256 of their evidence sets to select 1 200 failures before any sampled answer is generated. For each selected failure the system regenerates a response using only the altered evidence and compares it to the original output.

## Results  
Among 1 190 regenerated‑valid failures, support addition repairs 197 of 600 JOINT cases (0.328, 95 % CI [0.292, 0.367]) and deletion repairs 162 of 1 190 cases (0.136, 95 % CI [0.117, 0.155]). Length‑ and position‑matched shams retain semantic contrasts of 0.223 and 0.101 respectively. The original view shows a macro AUROC of 0.678 and Brier score of 0.152 versus a marginal baseline (Brier = 0.160). Exact‑vector accuracy is 0.637, which does not exceed the 0.646 majority‑vector baseline; vector macro‑F1 is 0.170. Across four readers pooled exact‑vector agreement is 0.675–0.765 while JOINT‑only agreement drops to 0.538–0.691.

## Significance  
These results demonstrate that evidence sensitivity occurs at meaningful rates in the hash‑selected failure sample, confirming that RAG failures are not an information‑theoretic impossibility but a domain‑specific phenomenon. The reader‑dependent nature of these effects suggests that offline audits like Pair‑ID can guide targeted repair policies rather than universal fixes.

## Related Concepts  
RAG failure, counterfactual response, paired evidence interventions, off‑line audit, SHA‑256 ordering, JOINT cases, semantic contrast shams, AUROC, Brier score, exact‑vector accuracy, vector macro‑F1, reader sensitivity.
