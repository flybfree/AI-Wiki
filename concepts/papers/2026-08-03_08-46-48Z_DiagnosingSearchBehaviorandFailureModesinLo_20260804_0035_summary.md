# Summary: 2026-08-03_08-46-48Z_DiagnosingSearchBehaviorandFailureModesinLong_Hori.md
Saved: 2026-08-04 00:35
Source: 2026-08-03_08-46-48Z_DiagnosingSearchBehaviorandFailureModesinLong_Hori.md
Model: None

---

## Summary  
This paper investigates how deep search agents allocate effort across long‑horizon information‑seeking tasks and whether that effort translates into higher answer quality. By analysing trajectory‑level evidence retrieval and usage, the authors separate failures into “retrieval gaps” (missing necessary evidence) and “utilization gaps” (evidence retrieved but not used correctly). Their systematic diagnosis reveals a weak correlation between search effort and accuracy, with answer performance driven more by cumulative recall of useful evidence than by raw query count. The study also shows that early retrievals often contain the most valuable information yet agents continue searching, generating low‑yield steps.

## Key Contributions  
- **Finding 1:** Search effort and answer quality are only weakly aligned; accuracy correlates strongly with the quality of retrieved evidence, especially cumulative recall, rather than the number of searches or context size.  
- **Finding 2:** Useful evidence typically appears early in a trajectory, yet agents persist in low‑yield retrieval steps, indicating inefficient continuation after sufficient support has been gathered.  
- **Finding 3:** Exploratory reformulations remain beneficial at the query level, but top‑performing agents issue far fewer redundant queries, suggesting better query planning.

## Methodology  
The authors employ a diagnostic framework that treats each search trajectory as a sequence of document‑level relevance judgments. They first separate two behavioral stages: (1) evidence retrieval and (2) evidence utilization within the context. Using human‑annotated judgments on BrowseComp‑Plus, they evaluate which queries retrieve relevant documents at each step and how effectively those documents are incorporated into the final answer. The retrieval model and evaluation harness remain fixed while six agents are compared; results are also validated on BrowseComp via an open‑web search API to ensure robustness.

## Results  
Across all settings, cumulative recall of high‑quality evidence predicts answer accuracy better than total query count or context length. Experiments show that the best agents stop after retrieving a sufficient set of relevant documents, whereas weaker agents continue searching, producing diminishing returns. At the query level, exploratory reformulations improve performance modestly, but the most effective agents limit redundancy, reducing unnecessary queries.

## Significance  
Understanding these failure modes equips researchers with actionable insights for designing deeper research systems: stronger query formulation, smarter evidence selection, and context management that stop when sufficient support is gathered. This work moves beyond empirical correlation to a diagnostic taxonomy that can guide engineering improvements in long‑horizon search agents.

## Related Concepts  
- Deep search agents  
- Trajectory analysis  
- Retrieval vs. utilization gap  
- Cumulative recall  
- Evidence quality  
- Query redundancy  
- Stopping criteria
