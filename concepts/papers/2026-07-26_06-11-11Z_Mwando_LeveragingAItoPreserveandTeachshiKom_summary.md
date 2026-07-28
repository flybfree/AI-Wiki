# Summary: 2026-07-26_06-11-11Z_Mwando_LeveragingAItoPreserveandTeachshiKomori.md
Saved: 2026-07-27 23:52
Source: 2026-07-26_06-11-11Z_Mwando_LeveragingAItoPreserveandTeachshiKomori.md
Model: None

---

## Summary  
The paper introduces Mwando, an AI virtual assistant aimed at preserving and teaching the shiKomori language of the Comoros Islands. It covers all four dialectal variants—shiNgazidja, shiMwali, shiNdzuani, and shiMaore—through a comprehensive knowledge base built from phrases, proverbs, dictionaries, and grammar lessons. The system employs a multi‑agent architecture that combines vector search, a knowledge graph, and web‑search fallback to generate accurate, context‑aware responses. Evaluation on 500 queries shows strong performance in vocabulary lookup and grammar explanations.

## Key Contributions  
- Mwando is the first AI‑driven tool dedicated to an endangered language, shiKomori.  
- The multi‑agent architecture integrates vector search, a knowledge graph, and web fallback for context‑aware responses across dialects.  
- Experimental results on 500 queries demonstrate strong performance in vocabulary lookup and grammar explanations.

## Methodology  
To build Mwando, the authors first compiled a knowledge base containing thousands of phrases, proverbs, lexical entries, and grammatical rules from each dialect variant. This data is stored in a structured knowledge graph that links concepts and provides semantic relationships. Vector embeddings are generated for each entry to enable fast similarity search. When a query arrives, the system runs vector search first; if no match is found, it triggers web‑search fallback to retrieve external resources. The multi‑agent setup coordinates these components to produce coherent answers.

## Results  
The evaluation involved 500 user queries covering vocabulary retrieval and grammar explanation tasks. Results show that Mwando correctly answered 89 % of vocabulary lookups and 84 % of grammar questions, outperforming baseline methods. Qualitative case studies illustrate successful interactions but also reveal challenges such as dialectal ambiguity and limited external knowledge.

## Significance  
This work matters because it provides a scalable framework for preserving endangered languages through AI, offering a blueprint that can be adapted to other low‑resource linguistic communities. By combining computational resources with community‑driven content, Mwando demonstrates how technology can support cultural heritage education.

## Related Concepts  
shiKomori (Comorian language), dialectal variants, knowledge graph, vector search, multi‑agent system, low‑resource natural language processing, educational AI, preservation of endangered languages.
