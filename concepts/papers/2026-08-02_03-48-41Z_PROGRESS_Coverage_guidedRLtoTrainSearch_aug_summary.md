# Summary: 2026-08-02_03-48-41Z_PROGRESS_Coverage_guidedRLtoTrainSearch_augmentedL.md
Saved: 2026-08-03 20:36
Source: 2026-08-02_03-48-41Z_PROGRESS_Coverage_guidedRLtoTrainSearch_augmentedL.md
Model: None

---

## Summary  
The paper proposes PROGRESS, a coverage‑guided reinforcement learning framework that explicitly shapes the search‑augmented LLM agent’s query decomposition process. By leveraging frozen teacher models to generate essential sub‑queries for complex inputs, PROGRESS provides lightweight guidance during RL training without dense supervision. This approach aims to improve both reasoning accuracy and search efficiency of large language model agents. The contribution is a novel reward shaping mechanism that directly influences how the agent breaks down queries.  

## Key Contributions  
- [Finding 1] A coverage‑guided reinforcement learning (RL) objective that rewards correct decomposition of complex user queries into essential sub‑queries, thereby improving task performance.  
- [Finding 2] Integration of teacher‑generated search queries as lightweight guidance signals within an R1‑style training loop, enabling sparse supervision over query generation decisions.  
- [Finding 3] Empirical evidence that coverage‑guided RL yields higher accuracy and lower inference latency compared to baseline search‑augmented LLM agents.  

## Methodology  
The authors adopt a teacher‑student architecture where a frozen teacher model decomposes incoming queries into a set of essential sub‑queries. These sub‑queries are used as coverage rewards that steer the policy network’s query generation during RL training. The reinforcement learning loop follows an R1 framework: the agent selects actions (sub‑query proposals), receives coverage reward, and updates its policy to maximize long‑term task success. Because teacher models remain static, the guidance is sparse yet targeted, avoiding the need for dense process‑level supervision.  

## Results  
Experiments on benchmark datasets show that PROGRESS improves overall task accuracy by up to 6.2% relative to a standard search‑augmented LLM baseline. Additionally, the agent’s inference time decreases by approximately 15% due to more efficient query decomposition. The coverage reward correlates strongly with the quality of sub‑query generation, confirming that explicit supervision yields measurable gains.  

## Significance  
By explicitly supervising search strategies through coverage rewards, PROGRESS addresses a critical gap in current RL training for LLMs: opaque, outcome‑only feedback that does not guide intermediate reasoning steps. This method enables more interpretable and efficient agents, paving the way for scalable, human‑like query handling.  

## Related Concepts  
- Reinforcement Learning (RL)  
- Search‑augmented LLM agents  
- Coverage‑guided RL  
- Teacher‑student model framework  
- R1 training loop  
- Query decomposition
