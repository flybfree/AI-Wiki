# Summary: 2026-08-02_04-03-59Z_One_SidedQuantileCouplingforFlowMatching.md
Saved: 2026-08-03 21:30
Source: 2026-08-02_04-03-59Z_One_SidedQuantileCouplingforFlowMatching.md
Model: None

---

## Summary  
Flow Matching aims to train continuous‑time generative models by learning a velocity field that connects source and target distributions, but existing couplings require costly batch transport. This paper proposes Quantile Coupling Flow Matching (QC-FM), a lightweight one‑sided coupling that samples only the data batch and constructs paired sources directly without pairwise cost matrices. The method projects ranks onto random orthogonal directions, maps them to Gaussian quantiles, and fills remaining dimensions with conditional Gaussians, eliminating regression variance on selected slices. By preserving projected rank structure while keeping the prior unchanged, QC-FM injects geometric bias at low computational cost.  

## Key Contributions  
- [Finding 1] The one‑sided quantile coupling eliminates pairwise assignment costs by constructing source samples directly from data ranks.  
- [Finding 2] QC-FM removes irreducible regression variance on each selected slice, making the ideal flow linear there while preserving prior sampling.  
- [Finding 3] Experimental results show up to a 12.9 % FID reduction over Baseline coupling and superior performance to OT‑CFM across CIFAR‑10, CelebA, FFHQ, and ImageNet‑64.  

## Methodology  
The authors treat each frame of the video as a slice where data points are projected onto a small number of random orthogonal directions. These projections are converted into Gaussian quantiles that define the rank ordering of source samples. The latent code is then completed in the orthogonal complement by sampling from conditional Gaussians, ensuring that only the projected dimensions carry bias while the rest remain standard normal. This construction requires no cost matrix or assignment step and scales linearly with batch size.  

## Results  
Across four benchmark datasets (CIFAR‑10, CelebA, FFHQ, ImageNet‑64), QC-FM consistently outperforms Baseline flow matching under matched training budgets, achieving FID reductions up to 12.9 % relative to the baseline. It also surpasses OT‑CFM on all tests, demonstrating that preserving rank structure yields a scalable and effective bias injection for flow matching.  

## Significance  
This work highlights that geometric biases can be introduced into continuous‑time generative models without solving expensive batch transport problems, offering a practical path toward faster training and higher‑quality samples. By focusing on one‑dimensional slice coupling, QC-FM reduces computational overhead while preserving the essential information needed for accurate flow estimation.  

## Related Concepts  
One‑sided coupling, quantile coupling, flow matching, copula, Gaussian slices, rank projection, orthogonal complement sampling, transport cost bound, minimal batch size scaling.
