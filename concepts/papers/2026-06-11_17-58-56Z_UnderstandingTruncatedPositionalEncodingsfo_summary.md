# Summary: 2026-06-11_17-58-56Z_UnderstandingTruncatedPositionalEncodingsforGraphN.md
Saved: 2026-06-11 23:02
Source: 2026-06-11_17-58-56Z_UnderstandingTruncatedPositionalEncodingsforGraphN.md
Model: None

---


## Summary  
The paper investigates the expressive power of truncated positional encodings (PEs) used in graph neural networks (GNNs), which are typically derived from spectral or walk‑based families but limited to a finite number of terms for computational efficiency. While complete PEs are theoretically equivalent across different families, truncation can drastically reduce their capabilities, yet the impact remains largely unexplored. The authors introduce rigorous theoretical analyses and empirical experiments to reveal how these truncated encodings differ in expressive strength compared with full‑scale counterparts. Their work establishes that several popular GNN tricks lose their superiority when limited to a small number of terms.

## Key Contributions  
- [Finding 1] Truncated spectral PEs (e.g., using only the first k eigenspaces) are no longer stronger than the 1‑WL test, indicating a fundamental loss of expressive power under truncation.  
- [Finding 2] The $k$‑harmonic distances family, which is closely related to truncated spectral encodings, exhibits distinct expressive capabilities that differ from both full‑scale and other truncated variants.  
- [Finding 3] A mixed approach combining several truncated PEs outperforms any single truncated family on real‑world datasets, suggesting that diversity in truncation mitigates the drawbacks of each individual choice.

## Methodology  
The authors first formalize the expressive power of full spectral and walk‑based positional encodings using the 1‑WL (one‑Walk Lemma) and 3‑WL (three‑Walk Lemma) tests. They then define truncated versions by limiting the number of terms to k, such as keeping only the top k eigenvectors or powers up to $A^{k}$. To compare these variants, they construct theoretical lower bounds on the expressive power of each truncated family and conduct extensive experiments on benchmark graph datasets (e.g., Cora, PubMed) using state‑of‑the‑art GNN architectures. The mixed‑PE strategy is evaluated by randomly selecting a subset of truncated spectral, walk‑based, and $k$‑harmonic encodings and training them jointly.

## Results  
Theoretical analyses show that the 1‑WL test fails for many truncated spectral encodings when k is small, confirming their weaker expressive power. The $k$‑harmonic distances exhibit a non‑monotonic relationship with k$, sometimes surpassing full spectral PEs but often falling short of walk‑based counterparts. Experiments reveal that ensembles of truncated PEs achieve higher classification accuracy and lower inference time than any single truncated family, especially on heterogeneous graph structures.

## Significance  
Understanding the impact of truncation is crucial because GNNs rely heavily on efficient positional encodings; prematurely limiting them can degrade performance without saving computational cost. The paper provides a theoretical framework for evaluating truncated PEs and practical guidance for designing more robust GNN pipelines, encouraging research into adaptive or hybrid encoding strategies.

## Related Concepts  
- Positional Encodings (PEs) in GNNs  
- Spectral encodings (eigenvectors/effective resistance)  
- Walk‑based encodings (polynomials of adjacency matrix)  
- 1‑WL and 3‑WL expressive power tests  
- Truncated eigenvector or matrix‑power representations  
- $k$‑harmonic distances as a truncated spectral family
