# Summary: 2026-08-01_10-52-56Z_VerificationWithoutSufficiency_Per_ChunkFilteringF.md
Saved: 2026-08-03 21:27
Source: 2026-08-01_10-52-56Z_VerificationWithoutSufficiency_Per_ChunkFilteringF.md
Model: None

---

## Summary  
The paper investigates why per‑chunk verification fails on multi‑hop retrieval‑augmented generation tasks and proposes a decomposition‑based repair that conditions verification on sub‑questions rather than the original query. It demonstrates that standard entailment scoring yields low performance (AUC ≈ 0.5) while conditioning on decompositions restores high scores, especially when combined with retrieval. The authors show empirically that per‑chunk gating is detrimental across multiple datasets and generator sizes.

## Key Contributions  
- Finding 1: Per‑chunk verification assumes each retrieved chunk is a sufficient premise for the answer, which breaks down on multi‑hop questions where the relevant paragraph is not named in any sub‑question.  
- Finding 2: Conditioning verification on decomposed sub‑questions (instead of the original query) restores high entailment scores and lifts performance by ~0.35 AUC points.  
- Finding 3: Off‑the‑shelf decomposers can capture a substantial portion of this improvement, especially when retrieval is used to select the top paragraph.

## Methodology  
The authors systematically evaluate per‑chunk filtering across HotpotQA, 2WikiMultihopQA, and MuSiQue using three generator sizes (Qwen2.5‑7B) and two prompt variants. They compare four regimes: no filtering, per‑chunk gating based on original entailment, per‑chunk gating based on decomposition‑derived sub‑question entailment, and full retrieval‑augmented generation with decomposition. Controls include model capacity, premise length, hypothesis template, decision threshold, retriever choice, answer‑matching criterion, and prompt design.

## Results  
Entailment AUCs: original query 0.643/0.523/0.560; per‑chunk gating (original) drops to ~0.48/0.49/0.51; decomposition‑conditioned gating recovers 0.840 on MuSiQue (+0.355 lift). Off‑the‑shelf decomposer with retrieval reaches 0.637, while without retrieval only 0.533. Across all cells, per‑chunk gating is worse than no filtering; penalty grows with generator capability.

## Significance  
This work reveals a fundamental flaw in naïve verification that misaligns premise‑answer relationships on multi‑hop tasks and offers a low‑cost repair that can be integrated into existing retrieval pipelines without retraining large models. It also highlights the value of decomposition for aligning generated answers to sub‑question premises.

## Related Concepts  
- Retrieval‑augmented generation (RAG)  
- Multi‑hop question answering  
- Entailment scoring / verification  
- Decomposition of questions and answers  
- Per‑chunk gating in generative pipelines
