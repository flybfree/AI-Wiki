# Summary: 2026-07-22_06-20-32Z_TriAgent_Divergence_AwareMulti_AgentCommitteesforC.md
Saved: 2026-07-24 01:38
Source: 2026-07-22_06-20-32Z_TriAgent_Divergence_AwareMulti_AgentCommitteesforC.md
Model: None

---

## Summary  
TriAgent tackles the cost trap in LLM‑based financial sentiment analysis by deploying a multi‑agent committee that routes queries according to contextual granularity and a Semantic Divergence Index (SDI). The system combines a word‑level lexicon, a sentence‑level transformer, and a cross‑sentence reasoner to minimize unnecessary expensive cloud processing. By leveraging the SDI signal, TriAgent achieves higher accuracy while dramatically reducing compute cost at scale.  

## Key Contributions  
- [Finding 1] The critic plateau demonstrates that re‑tasking the LLM as a critic over smaller agents’ outputs yields an F1 of ~0.87, whereas a simple majority vote drops to F1=0.66, highlighting the value of granularity‑stratified diversity.  
- [Finding 2] The SDI serves as a robust hallucination detector with AUC=0.90 and enables cost‑free cross‑border canonicalization, achieving F1=0.99 for Chinese queries using an English cache.  
- [Finding 3] A single‑stage SDI strategy delivers the best risk‑adjusted return (Sharpe=3.50) on a 20‑ticker back‑test, outperforming always‑FinBERT (1.36) and always‑LLM (0.11).  

## Methodology  
TriAgent structures queries into three granularity layers: VADER for word‑level sentiment, FinBERT for sentence‑level classification, and a 0.5 B Qwen2.5 model with Mistral‑7B/Phi‑3.5‑mini cross‑family checks for cross‑sentence reasoning. The Semantic Divergence Index quantifies pairwise disagreement across these layers, guiding each query to the most appropriate agent tier.  

## Results  
Experiments show that a shared consensus dictionary answers 95 % of Chinese queries from an English cache with F1=0.99 at zero marginal cost. SDI’s detection performance is quantified by AUC=0.90. The single‑stage SDI approach yields a Sharpe ratio of 3.50, while the always‑FinBERT baseline scores 1.36 and the always‑LLM baseline only 0.11. At 10 million users, TriAgent saves $9.3 million annually compared to GPT‑4o‑mini.  

## Significance  
By aligning compute with actual semantic need, TriAgent breaks the linear cost scaling trap of LLM sentiment analysis, delivering higher accuracy and measurable financial savings. The SDI also provides a reliable post‑hoc detection mechanism for hallucinations, improving trust in automated trading signals.  

## Related Concepts  
multi‑agent committee, semantic divergence index (SDI), granularity stratification, cross‑sentence reasoning, F1 score, Sharpe ratio, hallucination detection, cost trap, shared consensus dictionary.
