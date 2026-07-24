# Summary: 2026-07-21_06-25-46Z_RAGAL_AFrugal_FullyLocalRetrieval_AugmentedAssista.md
Saved: 2026-07-24 00:49
Source: 2026-07-21_06-25-46Z_RAGAL_AFrugal_FullyLocalRetrieval_AugmentedAssista.md
Model: None

---

## Summary  
RAGAL is a retrieval‑augmented assistant built for the technical‑support team of a Romanian government agency, operating under three hard constraints: zero data egress, read‑only operation (the model drafts only, humans execute), and a single 8 GB consumer laptop as the only development and training machine. The system processes a Romanian‑language corpus of ~25 000 chunks—15 073 resolved support tickets and internal normative documents—and uses hybrid dense‑sparse retrieval with intent routing to boost performance. Fine‑tuning the bge‑m3 embedder locally for 72 minutes raises recall@10 from 0.663 to 0.850 (MRR 0.489 → 0.684). The work also documents a pitfall of single‑domain fine‑tuning and provides a reproducible pipeline for fully local LLM assistance.

## Key Contributions  
- [Finding 1] Hybrid dense‑sparse retrieval with intent routing raised internal evaluation from 62 % to 81 %, showing that retrieval engineering is more impactful than model size.  
- [Finding 2] Fine‑tuning the bge‑m3 embedder on real ticket data improved recall@10 and MRR, demonstrating that modest local training yields substantial gains.  
- [Finding 3] PII masking enhanced generation quality and a structural anchor distillation scheme made SQL hallucination impossible by construction.

## Methodology  
The authors constructed RAGAL as a fully local system using only an 8 GB consumer laptop. They assembled a 25 000‑chunk corpus of resolved support tickets and normative documents, implemented hybrid retrieval (dense + sparse) with intent routing, fine‑tuned the bge‑m3 embedder locally for 72 minutes, generated queries via GenQ to repair domain drift, and employed a CPU‑only 744B model as an overnight batch second opinion. The entire pipeline is documented in sanitized scripts for institutions facing similar data‑locality constraints.

## Results  
Internal evaluation improved from 62 % to 81 %. Recall@10 rose from 0.663 to 0.850 (MRR 0.489 → 0.684). PII masking boosted generation quality, and anchor distillation eliminated SQL hallucinations. Single‑domain fine‑tuning initially degraded retrieval but was corrected with GenQ.

## Significance  
RAGAL proves that high‑quality local LLMs can be deployed under strict data‑locality constraints, offering a cost‑effective alternative to cloud services for sensitive government workloads. It also supplies lessons on fine‑tuning pitfalls and mitigation strategies such as PII masking and anchor distillation.

## Related Concepts  
Retrieval‑augmented generation (RAG), hybrid dense‑sparse retrieval, intent routing, local fine‑tuning of embedder models, PII masking, anchor distillation, GenQ, CPU‑only model serving, data‑egress constraints.
