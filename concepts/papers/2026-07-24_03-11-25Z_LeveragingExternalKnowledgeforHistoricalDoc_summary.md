# Summary: 2026-07-24_03-11-25Z_LeveragingExternalKnowledgeforHistoricalDocumentRe.md
Saved: 2026-07-26 21:33
Source: 2026-07-24_03-11-25Z_LeveragingExternalKnowledgeforHistoricalDocumentRe.md
Model: None

---

## Summary  
The paper proposes ARI, a retrieval‑augmented large language model framework for restoring illegible Korean historical documents by integrating external knowledge to resolve proper nouns and other named entities. It builds on masked language modeling while adding explicit retrieval of scholarly sources to improve restoration accuracy. Experiments show ARI outperforms baselines in both character and entity restoration. The approach is validated through expert assessments, indicating practical utility.

## Key Contributions  
- Introduces Retrieval‑Augmented Large Language Model (ARI) framework for historical document restoration.  
- Demonstrates superior performance on Korean historical documents, achieving significant gains in restoring both general characters and named entities.  
- Validates the method through expert assessments, confirming its practicality as a tool for domain experts.

## Methodology  
The authors combine pre‑trained LLMs with a retrieval system that fetches relevant external knowledge (e.g., scholarly articles) to supplement the model’s implicit knowledge. During restoration, ARI first retrieves contextually appropriate passages and then generates text conditioned on both local masked tokens and retrieved information, effectively guiding the model to infer proper nouns and historically accurate content.

## Results  
Experiments compare ARI against baseline models using standard metrics such as BLEU and exact match for character restoration, showing up to 25 % improvement in entity accuracy. Human expert evaluations also report higher perceived quality and confidence in ARI‑generated text compared to baselines.

## Significance  
By bridging the gap between local language modeling and external historical knowledge, ARI enables more accurate restoration of culturally specific proper nouns that are critical for scholarly analysis. This accelerates research and preserves fragile documents by providing reliable digital copies faster than manual correction.

## Related Concepts  
- Retrieval‑Augmented Generation (RAG)  
- Masked language modeling  
- Large language models  
- Named entity recognition  
- Historical document preservation  
- Domain expert evaluation
