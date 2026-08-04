# Summary: 2026-08-03_11-08-58Z_Geometry_GuidedLayerwiseFFNWidthAllocationinTransf.md
Saved: 2026-08-04 00:46
Source: 2026-08-03_11-08-58Z_Geometry_GuidedLayerwiseFFNWidthAllocationinTransf.md
Model: None

---

## Summary  
The paper proposes a geometry‑guided method for allocating the hidden width of feed‑forward networks (FFNs) inside Transformers based on how token representations are transported through each layer. By measuring geometric changes with Gromov‑Wasserstein distortion and degree‑one persistent homology, the authors create a layerwise approximation that yields an exact fixed‑budget optimizer, allowing capacity to be placed where it is most needed. Their experiments show that this allocation can outperform uniform width schedules and conventional cosine tapers, especially in large models. The work bridges topology‑based analysis with practical training efficiency.

## Key Contributions  
- [Finding 1] Raw Euclidean Gromov‑Wasserstein work tracks residual‑norm growth across layers.  
- [Finding 2] Normalized Gromov‑Wasserstein and persistent homology are front‑loaded, reflecting early layer sensitivity.  
- [Finding 3] Geometry‑based width allocations improve validation loss relative to uniform and cosine taper schedules, with the largest gains at 440 M parameters.

## Methodology  
The authors model each FFN as a transport of a cloud of token representations, quantifying the induced geometric distortion using both raw Euclidean Gromov‑Wasserstein distance and its scale‑normalized version. They also compute degree‑one persistent homology under these metrics to capture topological changes. A layerwise approximation surrogate is derived from this geometric information, which is then used as an exact fixed‑budget optimizer that allocates FFN width per layer.

## Results  
Across seven pretrained language models, raw Euclidean Gromov‑Wasserstein work correlates strongly with residual‑norm growth, while normalized versions show front‑loaded allocation. The geometry‑based schedules reduce mean validation loss compared to uniform and a hand‑designed cosine taper in paired 128 M/256 M training runs. At the 440 M scale, geometry allocations improve over uniform by substantially more than the cosine taper, whereas anti‑topological raw control performs worse than uniform.

## Significance  
This research demonstrates that geometric analysis of token representation transport can guide efficient capacity allocation in Transformers, leading to better performance and training efficiency. By replacing heuristic width schedules with topology‑informed optimizers, practitioners can achieve higher accuracy without increasing parameter count or computational cost.

## Related Concepts  
- Feed‑forward networks (FFNs) within Transformer architectures  
- Gromov‑Wasserstein distance for measuring geometric similarity  
- Persistent homology and degree‑one persistence to capture topological changes  
- Token representation transport as a capacity model  
- Fixed‑budget optimization based on layerwise approximations
