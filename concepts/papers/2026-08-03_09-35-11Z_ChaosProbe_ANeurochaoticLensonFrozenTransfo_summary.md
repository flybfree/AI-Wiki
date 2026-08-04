# Summary: 2026-08-03_09-35-11Z_ChaosProbe_ANeurochaoticLensonFrozenTransformerInp.md
Saved: 2026-08-03 23:50
Source: 2026-08-03_09-35-11Z_ChaosProbe_ANeurochaoticLensonFrozenTransformerInp.md
Model: None

---

## Summary  
The paper proposes **ChaosProbe**, a deterministic neurochaotic method for constructing fingerprints of frozen transformer input‑embedding spaces using chaotic trajectory transformations. It measures firing rates and entropy responses to generate fixed‑length signatures for each prompt level, thereby providing a stable representation of the embedding space. A proof‑of‑concept study on neutral prompts across four models shows that these signatures reliably distinguish model families. The approach offers a cohort‑dependent, deterministic probe that reveals hidden structure without task‑specific adaptation.  

## Key Contributions  
- **Finding 1:** ChaosProbe constructs response‑based fingerprints that capture chaotic dynamics in frozen embeddings.  
- **Finding 2:** Pearson and Spearman correlations recover all same‑family nearest‑neighbor assignments across models.  
- **Finding 3:** Euclidean distance recovers three of four assignments, demonstrating moderate similarity between families.  

## Methodology  
The authors treat each prompt’s embedding matrix as a vector space and apply a deterministic chaotic transformation (e.g., Lorenz attractor) to generate a trajectory. They record firing rates and entropy at each step, then summarize these signals into fixed‑length metrics: Firing Rate, Entropy, and their statistical correlations. The signatures are computed per model and compared across prompts.  

## Results  
Experimental results on 80 neutral prompts show that Pearson and Spearman correlation perfectly align nearest‑neighbor assignments within each family (GPT‑2 vs DistilGPT‑2, BERT vs RoBERTa). Cosine similarity also recovers same‑family pairs. Euclidean distance matches three of four assignments and one mutual pair. Bootstrap resampling confirms stability; signature‑validity tests rule out constant or collapsed responses.  

## Significance  
ChaosProbe offers a non‑task‑dependent, deterministic probe that reveals latent structure in frozen embeddings, enabling model comparison without fine‑tuning. It highlights how chaotic dynamics can serve as reliable fingerprints for embedding space similarity across architectures.  

## Related Concepts  
- Neurochaos: deterministic yet sensitive trajectories.  
- Firing rate and entropy: measures of activation dynamics.  
- Frozen transformer embeddings: static input representations before contextual processing.  
- Nearest‑neighbor assignments: grouping models by semantic similarity.  
- Correlation metrics (Pearson, Spearman) for quantitative comparison.
