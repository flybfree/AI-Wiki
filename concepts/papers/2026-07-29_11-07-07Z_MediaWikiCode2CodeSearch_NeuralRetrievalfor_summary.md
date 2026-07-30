# Summary: 2026-07-29_11-07-07Z_MediaWikiCode2CodeSearch_NeuralRetrievalfortheSema.md
Saved: 2026-07-29 21:37
Source: 2026-07-29_11-07-07Z_MediaWikiCode2CodeSearch_NeuralRetrievalfortheSema.md
Model: None

---

## Summary  
The paper introduces MediaWiki Code2Code Search, a neural retrieval system designed to overcome the lexical mismatch between user queries and implementation details in large open‑source ecosystems. By indexing millions of structural entities such as functions, types, and templates across thousands of MediaWiki repositories, the authors enable semantic code‑to‑code discovery that aligns with computational intent rather than surface tokens. The contribution lies in a split‑build architecture that decouples GPU‑intensive offline indexing from a CPU‑only serving layer, delivering high precision while respecting hardware constraints. This work demonstrates that deep learning can achieve both low latency and high recall for code search tasks.

## Key Contributions  
- [Finding 1] Neural retrieval reduces the lexical gap between natural language queries and code semantics, achieving superior semantic matching over traditional BM25 baselines.  
- [Finding 2] The FAISS IVF‑PQ index compresses the stored vectors to a size that is 96.6 % smaller than a flat float32 baseline (168.6 MB), dramatically reducing storage overhead.  
- [Finding 3] Query latency is measured at a median of 1.85 seconds on commodity hardware, comfortably fitting within the 6 GiB RAM limit of Wikimedia Toolforge.

## Methodology  
The authors built an index containing 1.29 million structural entities drawn from over 2,500 MediaWiki repositories. Offline indexing runs on a GPU to compute embeddings for each entity using a pre‑trained neural model, while the serving layer operates solely on CPU hardware. The resulting vector store is indexed with FAISS IVF‑PQ, which balances recall and memory usage. Queries are processed via an API that translates textual input into semantic vectors and retrieves the most relevant entities.

## Results  
Experimental evaluation on a 27‑query benchmark shows that Code2Code Search reaches a P@10 of 0.87, compared to BM25’s 0.64 (and even lower for strict token matching). The median query latency is 1.85 seconds, and the system consumes only 168.6 MB of storage, well within the 6 GiB RAM budget. Notably, gains are most pronounced in tasks involving obfuscated or renamed code elements where lexical methods fail.

## Significance  
This research advances open‑source software search by providing a scalable, low‑latency, and memory‑efficient neural retrieval solution that respects the constraints of large collaborative platforms like MediaWiki. By prioritizing semantic intent over surface tokens, it improves developer productivity and reduces the time spent on manual code hunting.

## Related Concepts  
Neural Retrieval, Semantic Similarity, FAISS IVF‑PQ Indexing, Split‑Build Architecture, Information Retrieval Trade‑off (latency vs. precision), MediaWiki Codebase, Open‑Source Software Discovery, Code2Code API.
