# Summary: 2026-08-04_23-13-32Z_EA_Graph_Artifact_AnchoredVerificationMemoryforCod.md
Saved: 2026-08-05 20:27
Source: 2026-08-04_23-13-32Z_EA_Graph_Artifact_AnchoredVerificationMemoryforCod.md
Model: None

---

## Summary  
The paper introduces EA‑Graph, an artifact‑anchored memory system designed to help coding agents verify claims reliably when the codebase experiences upstream drift—such as value or logic changes that invalidate earlier verification evidence. By representing artifacts at sub‑path granularity and anchoring each claim to its original content, EA‑Graph separates evidence strength from recency, making it clear whether a claim remains provable after drift rather than merely guessing. The contribution is twofold: (1) an empirical demonstration that artifact‑anchored memory improves provability judgments for smaller models compared with prose notes or no persistent memory; and (2) an exploratory insight suggesting that structured claim memory can narrow capability gaps by externalizing in‑session re‑derivation, though it does not prove cross‑model equivalence.  

## Key Contributions  
- Finding 1: In the Haiku round, artifact‑anchored memory outperformed both prose notes and no persistent memory across all seven worlds, with exact paired Wilcoxon comparisons yielding p = 0.0156.  
- Finding 2: The anchored condition produced perfect classification for the smaller model’s provability judgments in this testbed, indicating a bounded improvement over baseline methods.  
- Finding 3: An exploratory comparison suggests that structured claim memory may narrow a capability gap by externalizing re‑derivation, but it does not establish cross‑model equivalence.  

## Methodology  
The authors constructed generated repositories whose behavior‑to‑artifact ground truth was known by construction. They evaluated EA‑Graph across 42 sessions spanning seven clean worlds, using three memory conditions (artifact‑anchored, prose notes, no persistent memory) and two model tiers. The task involved classifying prior verification claims as unaffected, affected, or unprovable after value drift, logic drift, or deliberate withholding of upstream content.  

## Results  
EA‑Graph achieved the highest accuracy in every world compared to the other conditions; the Haiku round showed a statistically significant advantage (p = 0.0156). The smaller model’s provability judgments were consistently better than those of larger models when using EA‑Graph, supporting its bounded claim improvement. In Sonnet rounds, while EA‑Graph was perfect, frequent control ceilings rendered pre‑registered contrasts non‑significant because no session fabricated withheld content.  

## Significance  
EA‑Graph provides a bounded memory framework that preserves evidence strength independent of recency, enabling coding agents to make more accurate provability judgments when upstream changes occur. This work addresses a key challenge in long‑running verification: drift can render earlier claims invalid without clear signaling. By anchoring claims to concrete artifacts, EA‑Graph offers a principled way to externalize reasoning and may help narrow the capability gap between smaller and larger models, though further research is needed to confirm cross‑model equivalence.  

## Related Concepts  
artifact‑anchored verification memory, provenance tracking, evidence strength vs freshness, upstream drift, code verification, session memory, prose notes, capability gap, externalized re‑derivation.
