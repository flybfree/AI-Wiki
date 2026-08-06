# Summary: 2026-08-05_12-23-24Z_PURPOSE_PoisoningConflictResolutioninRAGviaProxy_F.md
Saved: 2026-08-05 20:34
Source: 2026-08-05_12-23-24Z_PURPOSE_PoisoningConflictResolutioninRAGviaProxy_F.md
Model: None

---

## Summary  
Retrieval‑Augmented Generation (RAG) mitigates noisy or contradictory retrieved passages through post‑retrieval conflict resolution, but its robustness to knowledge poisoning remains unexamined. This paper introduces PURPOSE, a strict black‑box poisoning attack that does not rely on frontal contradictions but instead reframes the injection as an update that minimizes conflict with the resolver’s possible reference. By extracting query‑related facts and grounding a pivot event in them, PURPOSE steers the generator toward a target answer while keeping the injected passage consistent with what the resolver might verify. The approach demonstrates that non‑contradicting injection can be a practical mode to enhance poisoning effectiveness.

## Key Contributions  
- [Finding 1] PURPOSE reframes a black‑box poisoning attack as a conflict‑minimizing update rather than a direct contradiction of the resolver’s output, enabling it to exploit the resolver’s own conflict‑resolution logic.  
- [Finding 2] The method extracts query‑relevant facts that approximate the resolver’s possible reference and grounds a pivot event within those facts, ensuring the injection is consistent with what the resolver might verify.  
- [Finding 3] Across three QA benchmarks, five generators, and three conflict‑resolution methods, PURPOSE achieves the highest attack success rate (ASR) in 35 of 45 settings and exceeds the strongest prior attack by +9.7 mean ASR points.

## Methodology  
The authors first analyze a query to identify facts that could serve as plausible references for the resolver. These facts are then used to construct a pivot event—a passage that aligns with the resolver’s likely view—through fact grounding. The conflict‑resolution mechanism remains unchanged; only the generator is guided by PURPOSE to produce an answer that matches the target while preserving consistency with the grounded pivot. This two‑step process—fact extraction and grounding—creates a non‑contradicting injection that can be inserted into RAG without triggering immediate detection.

## Results  
Experiments were conducted on three QA benchmarks, employing five different generator architectures and three conflict‑resolution strategies (e.g., simple majority voting, hierarchical resolution). In 35 out of 45 experimental settings, PURPOSE achieved the highest ASR, surpassing all prior attacks. The mean ASR improvement over the strongest baseline is +9.7 points, indicating a substantial advantage in poisoning effectiveness.

## Significance  
These findings reveal that knowledge poisoning can be effectively leveraged against conflict resolution in RAG by exploiting its own conflict‑minimizing mechanisms rather than relying on overt contradictions. By demonstrating that non‑contradicting injection is both feasible and highly successful, the work highlights a new attack paradigm that could degrade RAG systems without being easily flagged as malicious.

## Related Concepts  
Retrieval‑Augmented Generation (RAG), knowledge poisoning, black‑box attacks, conflict resolution, fact grounding, proxy‑fact‑grounded updates.
