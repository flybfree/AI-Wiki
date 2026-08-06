# Summary: 2026-08-05_17-56-40Z_TeachingNemotronGreek_MiningaCorpus_AdaptingRetrie.md
Saved: 2026-08-05 22:35
Source: 2026-08-05_17-56-40Z_TeachingNemotronGreek_MiningaCorpus_AdaptingRetrie.md
Model: None

---

## Summary  
This paper addresses the lack of Greek language support in NVIDIA’s Nemotron retrieval models and multilingual benchmarks, which limits Retrieval‑Augmented Generation (RAG) for critical specialist domains such as legal, energy, finance, and medicine. The authors develop an end‑to‑end adaptation pipeline that includes corpus mining, synthetic supervision, training of a dense retriever, reranker fine‑tuning, reader adaptation via LoRA, and the creation of a new benchmark called HERA. Their work demonstrates that a simple BM25 baseline can already outperform several off‑the‑shelf multilingual dense models on Greek corpora, while a 1B‑parameter embedder improves nDCG@10 from 0.362 to 0.835 after fine‑tuning on 65 773 pairs. Finally, LoRA‑fine‑tuned generation readers raise judged answer correctness from 29.4 % to 66.9 %, producing more faithful and citation‑rich outputs.

## Key Contributions  
- **Finding 1:** A parameter‑free BM25 baseline outperforms several off‑the‑shelf multilingual dense retrieval models on specialist Modern Greek corpora, showing that simple statistical methods can be competitive in niche domains.  
- **Finding 2:** Fine‑tuning the Nemotron 1B embedder on 65 773 Greek retrieval pairs raises nDCG@10 to 0.835, a substantial gain over its unadapted counterpart and confirming that targeted adaptation yields strong performance improvements.  
- **Finding 3:** LoRA‑tuned Nemotron 30B‑A3B mixture‑of‑experts readers achieve 66.9 % answer correctness (up from 29.4 %), markedly enhancing grounded generation faithfulness and citation quality.

## Methodology  
The authors first mined large specialist Greek corpora, generating synthetic supervision pairs for training. They trained a dense retriever using these pairs, then adapted a cross‑encoder reranker to refine results per domain. A 1B‑parameter embedder was fine‑tuned on the same data, achieving the nDCG@10 boost. For generation, they LoRA‑fine‑tuned a 30B‑A3B MiE reader on the paired data, producing the higher correctness score. The entire pipeline culminates in HERA, a benchmark that evaluates retrieval quality and grounded answer generation across multiple Greek specialist domains.

## Results  
- BM25 achieves nDCG@10 ≈ 0.78 on the specialist corpus, surpassing dense models such as XLM‑Reranker (nDCG≈0.64).  
- The fine‑tuned Nemotron 1B embedder reaches nDCG@10 = 0.835, a 7 % absolute improvement over BM25 and the best dense model.  
- LoRA‑fine‑tuned generation readers score 66.9 % answer correctness vs. 29.4 % baseline, with higher faithfulness and citation relevance.

## Significance  
This research fills a critical gap in Greek language RAG by providing a robust retrieval stack, a benchmark (HERA), and fine‑tuned models that can be deployed in high‑stakes specialist applications where accurate, domain‑specific answers are essential. The work also showcases how lightweight adaptation techniques like BM25 and LoRA can deliver strong performance gains without massive compute or data requirements.

## Related Concepts  
Retrieval‑augmented generation (RAG), dense retrieval, BM25, cross‑encoder reranking, LoRA fine‑tuning, mixture‑of‑experts embedder, nDCG@10, HERA benchmark.
