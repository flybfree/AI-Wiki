# Summary: 2026-06-18_15-32-14Z_CATCH_MEifyouRAG_adatasetofContextuallyAnnotatedmu.md
Saved: 2026-06-18 21:01
Source: 2026-06-18_15-32-14Z_CATCH_MEifyouRAG_adatasetofContextuallyAnnotatedmu.md
Model: None

---


## Summary  
[The paper introduces CATCH-ME if you RAG, a large‑scale, expert‑curated multilingual dataset that tackles the intersection of hate speech and misinformation in multi‑turn dialogues. It bridges a gap between existing single‑turn English datasets and real‑world interactions across five languages. The dataset is anchored to verified fact‑checking sources and includes both document‑level and chunk‑level span annotations for RAG systems. By covering seven marginalized groups, it enables training of factually grounded counterspeech models.]  

## Key Contributions  
- [The authors create the first large‑scale, multilingual dataset of multi‑turn dialogues that simultaneously address hate speech and misinformation, expanding beyond existing single‑turn English resources.]  
- [All dialogues are factually anchored to verified external knowledge such as fact‑checking articles and NGO reports, providing document‑level and chunk‑level span annotations suitable for RAG pipelines.]  
- [The resource spans five languages and targets hate directed at seven marginalized groups, offering a comprehensive benchmark for evaluating counterspeech generation across diverse social contexts.]  

## Methodology  
[Our methodology involved expert curation of real‑world exchanges where hateful or misleading statements overlapped with misinformation. We collected dialogues in five languages, ensured each exchange was factually verified using external fact‑checking sources, and annotated the dialogue at both document and chunk levels with span references to the source material.]  

## Results  
[The dataset comprises over 10,000 multi‑turn exchanges across five languages, covering seven target groups. It is directly usable for RAG by providing clear source spans, enabling downstream models to generate counterspeech that are both persuasive and factually correct.]  

## Significance  
[This work matters because it addresses the critical overlap of hate speech and misinformation—a gap previously ignored in NLP research—by delivering a high‑quality, multilingual benchmark. By providing annotated data for RAG systems, it can improve the factual accuracy and effectiveness of AI assistants that generate counter‑speech.]  

## Related Concepts  
[counterspeech, hate speech, misinformation, multi‑turn dialogue, fact‑checking, RAG (Retrieval‑Augmented Generation), multilingual, marginalized groups, expert curation, span annotations]
