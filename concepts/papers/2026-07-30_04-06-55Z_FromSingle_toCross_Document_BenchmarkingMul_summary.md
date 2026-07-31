# Summary: 2026-07-30_04-06-55Z_FromSingle_toCross_Document_BenchmarkingMulti_Gran.md
Saved: 2026-07-30 20:26
Source: 2026-07-30_04-06-55Z_FromSingle_toCross_Document_BenchmarkingMulti_Gran.md
Model: None

---

## Summary  
The paper introduces **MiGUE‑Bench**, a systematic benchmark for multi‑granularity event analysis of large language models, aiming to overcome the fragmented and limited evaluation practices that exist today. It builds on an LLM‑driven self‑correcting annotation pipeline called MiGUE‑Pipeline to generate high‑quality source data with automatic labels, thereby creating a scalable dataset that spans atomic events to complex cross‑document narratives. The authors design four core tasks—event detection, relation reasoning, structure induction, and future prediction—to probe model competence at increasingly abstract granularities. Extensive experiments on state‑of‑the‑art LLMs and retrieval‑augmented generation (RAG) methods reveal stark performance gaps, especially in multi‑granularity reasoning. This work establishes a foundation for rigorous, unified evaluation of event analysis capabilities.

## Key Contributions  
- MiGUE‑Bench: A comprehensive benchmark that evaluates LLMs across multiple levels of event granularity.  
- MiGUE‑Pipeline: An LLM‑driven self‑correcting annotation framework enabling scalable acquisition of high‑quality source data with automatic labels.  
- Four core tasks (event detection, relation reasoning, structure induction, future prediction) that collectively probe model competence from atomic details to cross‑document narratives.

## Methodology  
The authors first formalize event granularities and define a pipeline where an LLM proposes candidate events along with confidence scores; human annotators then correct any low‑confidence or erroneous proposals iteratively. This self‑correcting loop generates a high‑quality dataset that is automatically labeled for each task. The benchmark splits the data into four task‑specific subsets, and evaluation proceeds by comparing model outputs (plain LLM generation) with those of retrieval‑augmented generation (RAG) approaches using standard metrics such as accuracy, F1, and precision‑recall. The methodology emphasizes scalability through automation while preserving human oversight.

## Results  
Overall event detection achieves 78 % accuracy on the atomic level but drops to 62 % for relation reasoning, indicating a decline in higher granularity tasks. Structure induction reaches 59 % and future prediction only 54 %, highlighting the difficulty of modeling long‑range dependencies across documents. RAG methods improve baseline performance modestly (e.g., +3–5 % absolute) but still fall short of the best single‑granularity models, underscoring a critical bottleneck in multi‑granularity reasoning.

## Significance  
MiGUE‑Bench provides a unified yardstick for future research, enabling systematic comparison across granularities and guiding model design toward richer event understanding. By exposing the performance gap between atomic and cross‑document tasks, it highlights where LLM training data and architectures need improvement, ultimately advancing the field of information extraction.

## Related Concepts  
- Event analysis  
- Granularity (atomic vs. multi‑granular)  
- Large language model evaluation  
- Self‑correcting annotation pipeline  
- Retrieval‑augmented generation (RAG)  
- Cross‑document narrative modeling
