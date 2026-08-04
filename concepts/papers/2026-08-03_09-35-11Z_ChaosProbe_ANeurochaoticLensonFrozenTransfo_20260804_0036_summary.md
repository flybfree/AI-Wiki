# Summary: 2026-08-03_09-35-11Z_ChaosProbe_ANeurochaoticLensonFrozenTransformerInp.md
Saved: 2026-08-04 00:36
Source: 2026-08-03_09-35-11Z_ChaosProbe_ANeurochaoticLensonFrozenTransformerInp.md
Model: None

---

## Summary  
The paper introduces **ChaosProbe**, a deterministic neurochaotic probe that generates response signatures for frozen transformer input‑embedding spaces without any fine‑tuning or downstream adaptation. It treats each prompt’s embedding matrix as a point in a latent space and applies chaotic trajectory transformations to compute firing‑rate and entropy channel responses, which are then summarized into fixed‑length fingerprints. These fingerprints capture the manifold structure of the frozen embeddings and can be compared using standard similarity metrics. The authors demonstrate that these signatures reliably recover nearest‑neighbor relationships among four models (GPT‑2, DistilGPT‑2, BERT‑base, RoBERTa‑base). This work shows that chaos‑based fingerprints expose cohort‑dependent structure in frozen embeddings, offering a new analytical lens beyond performance metrics.  

## Key Contributions  
- [Finding 1] ChaosProbe constructs deterministic neurochaotic response signatures for frozen transformer input‑embedding spaces.  
- [Finding 2] The signatures recover all same‑family nearest‑neighbor assignments and both mutual family pairs across the four models.  
- [Finding 3] Bootstrap resampling validates the stability of Pearson and Spearman correlations, confirming robustness against prompt noise.  

## Methodology  
The authors approached the problem by first selecting a set of neutral prompts (80 in total) that produce stable embedding vectors for each model. For every prompt‑level embedding matrix they applied a logistic‑map based chaotic trajectory to generate firing‑rate and entropy channel trajectories. The response curves were summarized into two scalar measures—Firing Rate and Entropy Channel—that were then encoded as a fixed‑length vector (the signature). Similarity between signatures was evaluated using Pearson correlation, Spearman rank correlation, cosine similarity, and Euclidean distance. Nearest‑neighbor assignments among the four models were recovered by comparing these distances and correlations. To assess reliability, paired bootstrap resampling was performed on the observed prompts, and constant or collapsed responses were checked to ensure they did not dominate the fingerprints.  

## Results  
Across 80 neutral prompts the Euclidean distance recovered three of the four same‑family nearest‑neighbor assignments and one of the two mutual family pairs. Pearson correlation and Spearman rank correlation each recovered all same‑family assignments as well as both mutual family pairs, indicating strong alignment between similarity measures and true relationships. Bootstrap resampling (10 000 iterations) confirmed that these pairings are stable with high confidence. Signature‑validity checks showed no dominance of constant or collapsed responses, proving the fingerprints reflect genuine chaotic dynamics rather than degenerate cases.  

## Significance  
ChaosProbe demonstrates that deterministic neurochaotic signatures can expose hidden structure in frozen transformer input‑embedding spaces, providing a method to compare models without any downstream task. This insight is valuable for model similarity analysis, debugging latent space issues, and understanding how different architectures share or diverge from each other at a representation level. By leveraging chaos theory, the work bridges representation learning with dynamical systems, opening avenues for more interpretable probing of frozen embeddings.  

## Related Concepts  
Neurochaos, Frozen transformer input‑embedding spaces, Firing rate, Entropy channel, Response‑based fingerprints, Nearest neighbor assignment, Mutual family pairs, Pearson correlation, Spearman rank correlation, Cosine similarity, Euclidean distance, Bootstrap resampling, Logistic map trajectory.
