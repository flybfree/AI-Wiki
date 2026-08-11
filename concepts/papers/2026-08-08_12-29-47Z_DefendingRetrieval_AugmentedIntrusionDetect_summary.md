# Summary: 2026-08-08_12-29-47Z_DefendingRetrieval_AugmentedIntrusionDetectionAgai.md
Saved: 2026-08-10 22:54
Source: 2026-08-08_12-29-47Z_DefendingRetrieval_AugmentedIntrusionDetectionAgai.md
Model: None

---

## Summary  
Retrieval‑Augmented Intrusion Detection (RAG‑IDS) suffers from two critical vulnerabilities: knowledge poisoning, where an attacker corrupts the vector knowledge base, and prompt injection, which manipulates retrieved documents to flip labels. This paper introduces a three‑tier multi‑agent framework that adds a retrieval‑boundary defense composed of soft trust scoring, label‑embedding consistency checking (LECC), and prompt sanitization. Experiments on CIC‑UNSW‑NB15 demonstrate that the defended system recovers classification quality with minimal overhead, while single‑document attacks are mitigated to low success rates.  

## Key Contributions  
- Retrieval layers in RAG‑IDS are vulnerable to knowledge poisoning and prompt injection, exposing downstream classifiers.  
- The proposed three‑tier architecture (high‑throughput classifier + retrieval agent + defense layer) recovers relative performance from 1.0 at 1 % poisoning down to 0.57 at 30 %, with negligible clean‑performance loss.  
- Label‑embedding consistency checking (LECC) is the primary contributor to robustness, and soft trust‑based demotion outperforms hard filtering in both poisoning and injection scenarios.  

## Methodology  
The authors construct a multi‑agent intrusion detection pipeline: a high‑throughput classifier generates network flow features, a retrieval agent queries a dense vector knowledge base for semantically similar historical traffic, and the defense layer evaluates each retrieved document using soft trust scores to weight relevance, applies LECC to detect embedding mismatches between labels and embeddings, and sanitizes any malicious prompt strings before feeding them to the classifier. This layered approach isolates the retrieval component from the core decision logic.  

## Results  
Under 1 % knowledge poisoning the defended RAG‑IDS maintains a recovery ratio (R) of 1.0 relative to clean performance; at 30 % poisoning it drops to R = 0.57, indicating substantial degradation but still far better than unprotected retrieval. Prompt injection attacks succeed only 0.6–2.4 % when using multi‑document retrieval, compared with 35–55 % for single‑document retrieval. Ablation studies confirm that LECC provides the greatest resilience, while soft trust‑based demotion yields higher detection rates than hard filtering.  

## Significance  
This work delivers an explainable, attack‑resilient foundation for RAG‑based intrusion detection, enabling hybrid deployment alongside high‑throughput classifiers without sacrificing performance. By mitigating both knowledge poisoning and prompt injection at the retrieval boundary, the framework safeguards critical security decisions in real‑time network monitoring.  

## Related Concepts  
Retrieval‑Augmented Generation (RAG), vector knowledge base, soft trust scoring, label‑embedding consistency checking (LECC), prompt sanitization, multi‑document retrieval, label‑flip, hybrid deployment, intrusion detection.
