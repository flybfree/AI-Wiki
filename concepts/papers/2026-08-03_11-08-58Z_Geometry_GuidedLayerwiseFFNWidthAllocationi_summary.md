# Summary: 2026-08-03_11-08-58Z_Geometry_GuidedLayerwiseFFNWidthAllocationinTransf.md
Saved: 2026-08-04 00:30
Source: 2026-08-03_11-08-58Z_Geometry_GuidedLayerwiseFFNWidthAllocationinTransf.md
Model: None

---

## Summary  
The paper investigates whether the hidden width of feed‑forward networks in Transformers can be optimized based on geometric measurements taken during forward passes, rather than using a fixed constant width. It proposes to model each FFN as moving token representations and quantify this movement with correspondence‑preserving shift metrics such as Gromov‑Wasserstein distortion and persistent homology. By deriving a layerwise approximation surrogate, the authors obtain an exact optimizer that respects a fixed budget of parameters. Experiments across several pretrained language models demonstrate that geometry‑guided allocations outperform uniform width and cosine taper schedules.  

## Semantic links
- [[concepts/papers/2026-07-22_12-20-58Z_Foundation_model_guidedradiogenomicdiscover_summary.md|Summary: 2026-07-22_12-20-58Z_Foundation_model_guidedradiogenomicdiscoverylinkin.md]] — 4 title terms overlap; 9 summary/topic terms overlap; semantic match 0.03
- [[concepts/papers/2026-08-03_11-15-31Z_Feed_ForwardSteeringinTransformerResidualDy_summary.md|Summary: 2026-08-03_11-15-31Z_Feed_ForwardSteeringinTransformerResidualDynamics.md]] — 3 title terms overlap; 13 summary/topic terms overlap; semantic match 0.14
- [[concepts/papers/2026-08-03_11-15-31Z_Feed_ForwardSteeringinTransformerResidualDy_20260804_0047_summary.md|Summary: 2026-08-03_11-15-31Z_Feed_ForwardSteeringinTransformerResidualDynamics.md]] — 3 title terms overlap; 12 summary/topic terms overlap; semantic match 0.13

## Key Contributions  
- [Finding 1] A geometric framework using Gromov‑Wasserstein distortion and persistent homology to measure token‑representation transport in FFNs.  
- [Finding 2] An exact fixed‑budget optimizer that approximates layerwise width allocation from forward‑pass geometry.  
- [Finding 3] Empirical evidence that normalized‑work schedules reduce validation loss more than uniform or cosine taper allocations, especially at larger model sizes.  

## Methodology  
The authors treat each feed‑forward network as a geometric channel transporting a cloud of token embeddings. They compute the induced geometric change by evaluating Gromov‑Wasserstein distortion between successive layers under raw and scale‑normalized metrics, and they also estimate degree‑one persistent homology to capture topological invariants. These measurements are approximated with a layerwise surrogate that respects a total parameter budget, yielding an optimizer that allocates width per layer based on the measured geometry rather than a predetermined schedule.  

## Results  
Across seven pretrained language models, raw Euclidean work correlates strongly with residual norm growth, while normalized work is front‑loaded across early layers. Gromov‑Wasserstein metrics align better with sensitivity to perturbations than finite‑sample topological estimates. In paired 128M and 256M training runs, several normalized‑work schedules achieve lower mean validation loss compared to both uniform width and a cosine taper schedule. At the 440M scale, geometry‑based allocations improve over uniform by a larger margin than the cosine taper, whereas anti‑topological raw control performs worse than uniform.  

## Significance  
By replacing arbitrary width policies with data‑driven geometric measurements, this work enables more efficient parameter allocation in Transformers, potentially reducing memory and compute costs while improving generalization. The approach bridges deep learning optimization theory with persistent homology, offering a novel tool for scalable model design.  

## Related Concepts  
- Feed‑forward network (FFN) width allocation  
- Gromov‑Wasserstein distortion  
- Persistent homology (degree‑one)  
- Topological data analysis  
- Parameter budgeting in deep networks
