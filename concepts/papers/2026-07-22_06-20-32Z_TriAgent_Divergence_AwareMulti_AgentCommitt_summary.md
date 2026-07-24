# Summary: 2026-07-22_06-20-32Z_TriAgent_Divergence_AwareMulti_AgentCommitteesforC.md
Saved: 2026-07-24 01:27
Source: 2026-07-22_06-20-32Z_TriAgent_Divergence_AwareMulti_AgentCommitteesforC.md
Model: None

---

## Summary  
The paper introduces TriAgent, a multi‑agent committee that reduces cost in LLM‑based financial sentiment analysis by routing queries to the most appropriate sub‑agents. It uses a Semantic Divergence Index (SDI) to measure disagreement across lexical, sentence‑level and cross‑sentence granularities. The central finding is that a critic re‑tasked over smaller agents’ outputs plateaus F1 at ~0.87, outperforming a same‑size vote (F1=0.66), demonstrating the benefit of stratified diversity. At scale, TriAgent saves millions of dollars compared to baseline LLM usage.

## Key Contributions  
- [Finding 1] The three‑way Semantic Divergence Index (SDI) reliably captures granularity‑based disagreement and routes queries optimally.  
- [Finding 2] A critic re‑tasked over smaller agents’ outputs plateaus F1 at ~0.87, outperforming a same‑size vote (F1=0.66), demonstrating the benefit of stratified diversity.  
- [Finding 3] The SDI also serves as a hallucination detector with AUC 0.90 and drives superior risk‑adjusted returns (Sharpe 3.5) in back‑testing.

## Methodology  
TriAgent decomposes sentiment analysis into three agents: VADER for word‑level lexicon, FinBERT for sentence‑level domain embeddings, and a lightweight LLM (Qwen2.5 0.5B‑14B‑4bit) for cross‑sentence reasoning. Queries are first classified by VADER; if ambiguous, FinBERT scores them; the SDI compares the three outputs and decides which agent’s answer to trust. The critic is a smaller LLM that evaluates the consensus, providing a final decision.

## Results  
Experiments on 20‑ticker data show TriAgent achieves F1=0.87 with the critic, versus 0.66 for vote, and 0.99 shared consensus for Chinese queries using English cache. The SDI detector reaches AUC 0.90. Back‑testing yields Sharpe ratios of 3.50 vs. 1.36 (always FinBERT) and 0.11 (always LLM). At 10 M users, TriAgent saves $9.3 M annually versus GPT‑4o‑mini.

## Significance  
The work resolves the cost trap in production sentiment analysis by leveraging cheap, granular agents and a unified SDI metric, enabling massive savings without sacrificing accuracy. It also provides an interpretable hallucination detector and a principled way to combine heterogeneous models for high‑risk financial decisions.

## Related Concepts  
- Multi‑agent committee  
- Semantic Divergence Index (SDI)  
- Cost‑efficient routing  
- LLM critic  
- Hallucination detection via disagreement  
- Sharpe ratio back‑testing
