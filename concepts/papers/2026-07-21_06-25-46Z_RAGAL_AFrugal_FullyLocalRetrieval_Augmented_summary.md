# Summary: 2026-07-21_06-25-46Z_RAGAL_AFrugal_FullyLocalRetrieval_AugmentedAssista.md
Saved: 2026-07-24 00:32
Source: 2026-07-21_06-25-46Z_RAGAL_AFrugal_FullyLocalRetrieval_AugmentedAssista.md
Model: None

---

## Summary  
The authors present RAGAL, a retrieval‑augmented assistant designed to support technical‑support staff at a Romanian government agency while respecting three hard constraints: no data egress, read‑only operation, and deployment on a single 8 GB laptop. By leveraging a hybrid dense‑sparse retriever with intent routing and fine‑tuning the bge‑m3 embedder on real ticket data, RAGAL achieves markedly higher performance than baseline models. The work also documents pitfalls such as single‑domain fine‑tuning degradation and introduces counter‑intuitive fixes like PII masking and anchor distillation to prevent SQL hallucination.  

## Key Contributions  
- [Finding 1] Hybrid dense‑sparse retrieval with intent routing lifted internal evaluation from 62 % to 81 %.  
- [Finding 2] Fine‑tuning the bge‑m3 embedder on actual ticket data raised recall@10 from 0.663 to 0.850 and MRR from 0.489 to 0.684 within 72 minutes of training.  
- [Finding 3] Single‑domain fine‑tuning silently lowered retrieval quality on untouched documents; a per‑domain evaluation set and locally generated queries (GenQ) restored performance.  

## Methodology  
RAGAL was built under the constraints that no external API calls are allowed, only drafts are produced by the assistant while humans execute actions, and all training occurs on an 8 GB consumer laptop. The pipeline combines a dense‑vector store with a sparse inverted index for hybrid retrieval, routes queries to domain‑specific modules, fine‑tunes the bge‑m3 embedder using real ticket data, and generates synthetic queries (GenQ) to evaluate untouched domains. A CPU‑only 744B model serves as an offline second opinion, whose limitations are quantified.  

## Results  
The internal evaluation metric improved from 62 % to 81 %, and recall@10 increased to 0.850 with MRR of 0.684 after a brief 72‑minute fine‑tuning run. PII masking was found to enhance generation quality, while an “anchor distillation” scheme made SQL hallucinations impossible by construction. Without per‑domain evaluation, single‑domain fine‑tuning dropped retrieval below the stock baseline, demonstrating the pitfall identified in Finding 3.  

## Significance  
RAGAL provides a frugal, fully local solution for public institutions that cannot export sensitive data or rely on cloud services, offering high‑quality support without incurring egress costs. The techniques—hybrid retrieval, embedder fine‑tuning, and domain‑aware evaluation—can be adapted to other resource‑constrained settings where privacy and latency are paramount.  

## Related Concepts  
RAG (retrieval‑augmented generation), dense‑vector storage, sparse inverted index, intent routing, bge‑m3 embedder fine‑tuning, PII masking, anchor distillation, SQL hallucination prevention, GenQ synthetic queries, CPU‑only large model evaluation.
