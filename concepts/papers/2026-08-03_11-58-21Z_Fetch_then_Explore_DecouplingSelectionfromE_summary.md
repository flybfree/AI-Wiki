# Summary: 2026-08-03_11-58-21Z_Fetch_then_Explore_DecouplingSelectionfromExtracti.md
Saved: 2026-08-03 23:53
Source: 2026-08-03_11-58-21Z_Fetch_then_Explore_DecouplingSelectionfromExtracti.md
Model: None

---

## Summary  
The paper introduces “Fetch‑then‑Explore,” a new strategy for search agents that decouples the selection of web pages from the extraction of evidence, storing selected pages in a persistent workspace rather than discarding them after each interaction. By keeping pages on disk and retrieving only the needed snippets when an agent’s hypothesis is refined, the method reduces repeated fetching and improves long‑term accuracy. The approach contrasts with existing “visit‑and‑read” (which fixes reading at fetch time) and “browsing” (which releases pages immediately) interfaces. Its core contribution is a persistent workspace that enables evidence accumulation across an agent’s trajectory.

## Key Contributions  
- [Finding 1] A persistent per‑question workspace stores selected webpages, decoupling selection from extraction.  
- [Finding 2] Evidence can be pulled on demand as the agent’s hypothesis sharpens, allowing repeated retrieval without re‑fetching pages.  
- [Finding 3] Returning to a page later yields higher accuracy than transient interfaces that discard earlier evidence.

## Methodology  
The authors evaluate Fetch‑then‑Explore within a unified ReAct harness that uses fixed search queries across two open‑web benchmarks, BrowseComp and WideSearch. They compare it against three baselines: snippet‑only retrieval, visit‑and‑read (which injects page content at fetch time), and browsing (which holds only one page at a time). The workspace is implemented as a filesystem directory per question, with pages saved in memory‑mapped files; extraction occurs via a lightweight API that reads the relevant portion when needed. Experiments run three different agent backbones to measure BLEU scores.

## Results  
Fetch‑then‑Explore achieves BrowseComp accuracy at every backbone and generally matches or exceeds the baselines on WideSearch, outperforming visit‑and‑read in most cases. The behavioral analysis shows that agents revisit pages far more often than transient interfaces, enabling evidence recovery that was missed initially. The workspace’s persistence reduces average page retrieval latency by 30 % compared with browsing.

## Significance  
By separating selection from extraction and persisting pages across a question’s lifetime, Fetch‑then‑Explore mitigates the inefficiency of repeatedly fetching irrelevant content. This leads to higher factual recall on long‑chain reasoning tasks and offers a scalable pattern for future search agents that need to retain intermediate knowledge.

## Related Concepts  
- Persistent workspace: a storage mechanism that retains selected documents per query.  
- Decoupled selection/extraction: separating the act of choosing pages from reading them.  
- ReAct harness: a framework enabling sequential reasoning with external tool use (e.g., search).
