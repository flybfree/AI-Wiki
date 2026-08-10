# Summary: 2026-08-07_08-44-20Z_Samephysicalstate_differentcollectivedynamics_stat.md
Saved: 2026-08-09 22:51
Source: 2026-08-07_08-44-20Z_Samephysicalstate_differentcollectivedynamics_stat.md
Model: None

---

## Summary  
This paper investigates how the way language‑model agents encode their environment’s state influences collective synchronization outcomes, even when the underlying physical system remains unchanged. By swapping between two different encodings—low‑order circular moments versus a full histogram—the authors show that the same physical configuration can produce opposite synchronization patterns depending on which encoding is used by the model. The experiments reveal that the choice of encoding effectively rewrites the interaction law governing each agent’s advance, stay, or retard decisions. This work demonstrates that state encodings are not neutral interfaces but are integral to the emergent dynamics of language‑model agents.

## Key Contributions  
- [Finding 1] Low‑order circular moment encodings synchronize all six GPT seeds (6/6), whereas histogram encodings fail to synchronize any seed (0/6).  
- [Finding 2] When the same physical field is replayed, the advance/stay/retard probabilities shift far beyond the variation observed within‑encoding repeats for GPT, Claude, and Gemini.  
- [Finding 3] In Claude, the histogram encoding produces synchronization in the opposite direction compared to GPT’s moment encoding.

## Methodology  
The authors built circular‑synchronization agents that operate on a fixed set of neighbour phases. Each agent receives either a summary of its neighbours’ relative phases encoded as low‑order moments (e.g., mean phase, variance) or as a full histogram of those phases. The agents then decide to advance, stay, or retard based solely on this encoding. The experiment is repeated across six random initializations for GPT and Claude, with the same physical field replayed to observe how probabilities evolve beyond within‑encoding variation.

## Results  
GPT’s moment encoding achieved perfect synchronization in every seed (6/6), while its histogram counterpart never synchronized (0/6). Claude exhibited the reverse pattern: moment encoding produced no synchronization (0/6) and histogram encoding succeeded in all seeds (6/6). Replaying identical fields caused each agent’s advance/stay/retard probabilities to drift significantly beyond the within‑encoding repeat variance, indicating that the encoding choice itself alters the effective interaction law.

## Significance  
These findings show that state encodings are not passive representations but active components of model‑dependent dynamics. By altering how information is packaged, language models can steer collective behavior in opposite directions without changing the underlying physical setup. This challenges the assumption that encodings serve as neutral interfaces and highlights the importance of encoding design for predictable agent interactions.

## Related Concepts  
- Language‑model agents  
- State encodings (circular moments vs. histograms)  
- Synchronization dynamics  
- Collective behavior in distributed systems  
- Model‑dependent effective interaction laws
