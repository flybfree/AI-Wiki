# Summary: 2026-07-21_09-45-34Z_DocAtlas_Long_DocumentUnderstandingasMutable_State.md
Saved: 2026-08-10 22:37
Source: 2026-07-21_09-45-34Z_DocAtlas_Long_DocumentUnderstandingasMutable_State.md
Model: None

---

## Summary  
DocAtlas proposes treating long‑document understanding as a mutable‑state information‑seeking process, introducing an external harness that dynamically selects, reads, stores, reviews, and presents evidence across pages, tables, figures, and charts. The system maintains a hierarchical tree and note store that act as active working memory while the agent records its findings, all within a fixed context budget. This design enables both inference‑time use with large vision‑language models (VLMs) and end‑to‑end reinforcement learning for compact VLM agents.  

## Key Contributions  
- [Finding 1] Introduces a mutable‑state interaction framework where document information is actively searched, read, stored, reviewed, and shown to the model step‑by‑step.  
- [Finding 2] Implements a hierarchical tree and note store that maintains evidence across pages, enabling selective access and active working memory.  
- [Finding 3] Demonstrates significant performance gains for both large VLMs (GPT‑5.4) and compact VLM agents via end‑to‑end reinforcement learning in the harness.  

## Methodology  
The authors designed DocAtlas as an external “document harness” that exposes four tools: search, reading, note‑taking, and review. As the agent records evidence, the harness updates a hierarchical tree of retrieved items and a parallel note store, creating an active working memory. Retrieval is self‑improving because each new observation can be re‑indexed or prioritized. The same harness can be used with large VLMs that read the stored state at inference time, or it can serve as a training environment for compact VLM agents through reinforcement learning, all constrained by a fixed context budget to keep memory usage manageable.  

## Results  
GPT‑5.4 reaches 71.4 % on MMLongBench‑Doc, surpassing the human‑expert reference of 65.8 %. A Qwen3.5‑4B VLM trained with end‑to‑end RL in the DocAtlas environment scores 63.7 %, compared with a baseline that receives the full document as input and achieves only 54.4 %. These results show that mutable evidence handling can boost both large‑scale and compact agents by a substantial margin.  

## Significance  
DocAtlas bridges retrieval‑augmented generation, multi‑turn tool use, and active working memory into a single mutable‑state paradigm, allowing long‑document tasks to be handled efficiently even with limited context windows. By training compact VLM agents in this environment, the system reduces reliance on massive language models while maintaining high accuracy, opening practical pathways for real‑world document analysis where storage and latency are constraints.  

## Related Concepts  
Retrieval‑Augmented Generation (RAG), Multi‑turn tool use, Active working memory, Hierarchical evidence trees, End‑to‑end reinforcement learning, Context budget constraints, Long‑document understanding, Vector databases, Vision‑Language Models (VLMs).
