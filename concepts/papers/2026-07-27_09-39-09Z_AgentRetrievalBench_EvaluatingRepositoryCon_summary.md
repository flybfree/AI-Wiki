# Summary: 2026-07-27_09-39-09Z_AgentRetrievalBench_EvaluatingRepositoryContextRet.md
Saved: 2026-07-28 22:21
Source: 2026-07-27_09-39-09Z_AgentRetrievalBench_EvaluatingRepositoryContextRet.md
Model: None

---

## Summary  
[The paper introduces Agent Retrieval Bench, a file‑level benchmark to evaluate how coding agents retrieve repository files needed for their tasks. It defines four positive‑retrieval tasks and evaluates retrieval methods against frozen base‑commit repositories using relevance defined by downstream task needs rather than direct semantic similarity. The benchmark includes 427 samples from 25 repositories with diverse data, and explores both gold‑standard and natural no‑gold cases.]  

## Semantic links
- [[concepts/papers/2026-07-23_21-59-56Z_QwenAgentWorld_LanguageWorldModelsforGeneralAgents_summary.md|Summary: Qwen-AgentWorld: Language World Models for General Agents]] — 3 title terms overlap; 29 backlinks; 8 summary/topic terms overlap

## Key Contributions  
- [Finding 1: Qwen3‑Embedding‑4B achieves the best sample‑weighted MRR on positive samples, while Qwen3‑Embedding‑8B leads in Recall@20; RepoMap excels at budgeted context yield at 8K tokens.]  
- [Finding 2: Selective retrieval thresholds calibrated with counterfactual controls do not improve selective success on natural no‑gold cases, revealing a calibration gap.]  
- [Finding 3: Logged agent trajectories miss gold files on 27–35 % of samples; oracle gold context provides substantial remaining headroom compared to random non‑gold contexts.]  

## Methodology  
[The authors built Agent Retrieval Bench by constructing file‑level retrieval tasks from real coding workflows, using base‑commit snapshots and chunked file data. They evaluate lexical retrieval, RepoMap, open‑source embeddings, selective abstention, and logged agent context selection across positive, natural no‑gold, and counterfactual control sets.]  

## Results  
[Sample‑weighted MRR, Recall@20, and token‑budget yield metrics are reported for each method. Selective threshold calibration outcomes show no improvement on natural cases. Trajectory analysis shows 27–35 % gold‑file misses; oracle gold context yields higher file F1 than random non‑gold contexts.]  

## Significance  
[This work highlights retrieval as a critical bottleneck in coding agents, demonstrates trade‑offs among retrieval families, uncovers calibration issues between controlled and natural scenarios, and suggests that better initial context can reduce post‑seed exploration effort.]  

## Related Concepts  
[Retrieval‑augmented generation, code repositories, base‑commit snapshots, token budgeting, MRR, Recall@20, counterfactual control, selective retrieval, file chunks, embedding‑based retrieval, agent trajectories, oracle gold.]
