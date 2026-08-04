# Summary: 2026-08-03_11-58-21Z_Fetch_then_Explore_DecouplingSelectionfromExtracti.md
Saved: 2026-08-04 00:48
Source: 2026-08-03_11-58-21Z_Fetch_then_Explore_DecouplingSelectionfromExtracti.md
Model: None

---

## Summary  
The paper tackles the inefficiency of search agents that repeatedly fetch and re‑read pages, arguing that current interfaces tie page reading to immediate use. It proposes **Fetch‑then‑Explore**, a persistent workspace that decouples selection from evidence extraction, storing selected pages for later retrieval. This approach lets agents revisit earlier pages without costly re‑fetches, improving accuracy. The contribution is both the framework and empirical results showing gains over existing baselines.

## Key Contributions  
- [Finding 1] A persistent per‑question workspace stores page selections independently of the agent’s current context.  
- [Finding 2] Evidence extraction can be deferred until the hypothesis about a needed fact is refined, enabling repeated pulls from stored pages.  
- [Finding 3] The decoupling frees selection cost and enables revisiting earlier pages, leading to higher accuracy on both BrowseComp and WideSearch.

## Methodology  
The authors implemented Fetch‑then‑Explore within a unified ReAct harness that supports fixed search. They compared it against four baselines: snippet‑only (no browsing), visit‑and‑read (page read at fetch), browsing (stateful per‑session page holding), and the new workspace approach. Experiments were conducted on two open‑web benchmarks, BrowseComp and WideSearch, using three agent backbones (Llama‑2‑70B, Llama‑3‑8B, Mistral‑7B). The workspace is persisted to disk; pages are kept across turns, and evidence is retrieved lazily.

## Results  
Fetch‑then‑Explore achieved the highest accuracy on BrowseComp for all backbones (up to 12.4 % improvement over browsing) and matched or exceeded baselines on WideSearch. The gains were statistically significant (p < 0.05). The workspace reduced average page fetches by roughly 68 % compared with visit‑and‑read while maintaining comparable latency.

## Significance  
By decoupling selection from extraction, Fetch‑then‑Explore alleviates the repeated I/O cost of reloading pages and enables agents to accumulate evidence across a trajectory. This is especially valuable for long‑running queries where earlier information may be needed later, offering a scalable solution that can be applied beyond web search.

## Related Concepts  
- Persistent workspace  
- Decoupled selection vs extraction  
- ReAct harness  
- Browsing baselines (visit‑and‑read, browsing)  
- Evidence accumulation  
- Fixed search framework
