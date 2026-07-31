# Summary: 2026-07-30_06-05-45Z_Baikal_StructuredSearchforDeepResearchoverDataLake.md
Saved: 2026-07-30 20:27
Source: 2026-07-30_06-05-45Z_Baikal_StructuredSearchforDeepResearchoverDataLake.md
Model: None

---

## Summary  
Deep research over heterogeneous data lakes demands an LLM agent that can efficiently synthesize high‑quality reports by investigating evidence across thousands of tables and passages while respecting a fixed subquestion budget. The Baikal framework treats this task as a budgeted search problem, clustering the evidence into semantically coherent regions to guide both exploration and exploitation. By generating region‑grounded subquestions and using reward‑based policies for region selection, Baikal balances local promise with global coverage. Experiments on two data lakes demonstrate that structured semantic exploration can markedly improve report quality compared with existing baselines.

## Key Contributions  
- **Budgeted Search Formulation:** The authors cast deep research over data lakes as a budgeted search problem and introduce the Baikal framework, which systematically explores evidence under a limited subquestion budget.  
- **Semantic Region Clustering:** Evidence from heterogeneous tables and passages is clustered into semantic regions, enabling balanced exploration‑exploitation decisions that avoid overexposure to locally promising but narrow evidence.  
- **Performance Gains on Real Benchmarks:** Baikal’s best configuration improves report scores by 28 % on HybridQA and 36 % on TAT‑QA relative to strong baselines such as DeepSearcher and OpenCode agents, validated against a rubric that measures groundedness, relevance, diversity, and utility.

## Methodology  
Baikal treats each data lake as a knowledge graph composed of tables, Wikipedia passages, and financial report excerpts. First, the system clusters all evidence into semantic regions using a combination of topic modeling and LLM embeddings, producing a set of distinct “knowledge zones.” The agent then selects which region to investigate next according to a policy (e.g., Bayesian ε‑greedy or UCB) that balances exploitation of high‑value regions with exploration of under‑explored ones. Within the chosen region, Baikal formulates subquestions grounded in the region’s content and iteratively generates answers, using finding quality as a reward signal to update region‑level value estimates. The search continues until the budgeted number of subquestion generations is exhausted.

## Results  
Across 15 queries spanning HybridQA (10,993 tables) and TAT‑QA (2,757 tables), Baikal’s top configuration yields report scores that are 28 % higher on HybridQA and 36 % higher on TAT‑QA than the strongest baselines. The improvement is attributed to better coverage of diverse semantic regions, which enhances both groundedness and diversity while preserving utility under the fixed subquestion budget. Evaluation also includes a new rubric that scores reports on four dimensions; Baikal consistently outperforms DeepSearcher and OpenCode agents in all dimensions.

## Significance  
The work shows that systematic, structured exploration of heterogeneous data can produce noticeably better research outputs without increasing computational effort, addressing a key limitation of existing iterative retrieval‑generation pipelines. By organizing evidence into semantic regions, Baikal mitigates the risk of local overfitting and ensures broader coverage, which is crucial for real‑world applications where reports must be both accurate and comprehensive.

## Related Concepts  
- LLM agent  
- Data lake search  
- Budgeted search problem  
- Semantic region clustering  
- Exploration–exploitation balance (UCB, Bayesian ε‑greedy)  
- Retrieval‑grounded generation  
- Groundedness, relevance, diversity, utility scoring rubric
