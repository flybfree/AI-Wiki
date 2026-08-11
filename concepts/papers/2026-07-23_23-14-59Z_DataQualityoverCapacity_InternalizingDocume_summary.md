# Summary: 2026-07-23_23-14-59Z_DataQualityoverCapacity_InternalizingDocumentsinto.md
Saved: 2026-07-26 21:32
Source: 2026-07-23_23-14-59Z_DataQualityoverCapacity_InternalizingDocumentsinto.md
Model: None

---

## Summary  
The paper proposes a closed‑book question‑answering (QA) system that embeds entire training documents directly into the weights of a 4‑bit Gemma‑4‑e4b model using low‑rank adaptation (LoRA), eliminating reliance on external retrieval or context windows. By systematically varying LoRA rank, learning rate, and architecture while keeping data quality constant, the authors discover that once adapter capacity is sufficient, improvements in training‑data quality drive most gains. The study also reveals a hard gate below which no amount of data intervention improves performance.  

## Semantic links
- [[concepts/papers/2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCo_summary.md|Summary: 2026-07-21_16-31-35Z_PromptDesignatScale_HowFormat_InstructionCount_and.md]] — 3 title terms overlap; 11 backlinks; 10 summary/topic terms overlap

## Key Contributions  
- Finding 1: Data quality becomes the dominant lever for closed‑book accuracy after LoRA capacity reaches a threshold; increasing rank or learning rate yields diminishing returns.  
- Finding 2: A single curation pass—shortening gold answers to canonical 1–6 word spans and discarding trivia—raises closed‑book accuracy from 57.7 % to 85.7 % on a 15‑document corpus, outperforming all architectural tweaks.  
- Finding 3: The internalized LoRA adapter (84.2 % recall) beats a BM25‑RAG pipeline with a base reader (58.9 %) and even a realistic gold‑chunk oracle (65.6 %) at lower latency, demonstrating practical superiority over retrieval baselines.  

## Methodology  
The authors conduct roughly 100 training runs ranging from single documents to a 99‑document corpus, measuring closed‑book accuracy after each experiment. They vary LoRA rank, learning rate, and alternative architectures while holding data quality constant to isolate the effect of capacity versus data quality. A curation step is applied uniformly across runs to quantify its impact. The study also includes latency measurements for the internalized adapter compared with retrieval pipelines.  

## Results  
Closed‑book accuracy improves from 57.7 % (single document) to 85.7 % after the curation pass, a jump larger than any architectural change. Capacity trends show that LoRA rank must grow roughly linearly with corpus size; below this point no data intervention helps. The internalized adapter achieves 84.2 % recall on a 15‑document slice, surpassing BM25‑RAG (58.9 %) and a gold‑chunk oracle (65.6 %). Latency is lower than retrieval baselines because the model’s weights already contain the answer.  

## Significance  
This work shifts focus from sheer capacity to data quality in closed‑book LLM training, offering a cost‑effective path to high accuracy without expanding context windows or adding external components. It also provides empirical evidence of misdiagnosed coupling between rank and learning rate, guiding future debugging practices. The findings are valuable for practitioners seeking efficient, low‑latency QA systems that rely solely on internalized knowledge.  

## Related Concepts  
- LoRA (Low‑Rank Adaptation)  
- Closed‑book QA  
- Adapter capacity threshold  
- Data curation and gold answer simplification  
- Retrieval‑augmented generation (RAG) baselines
