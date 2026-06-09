# Summary: 2026-06-07_11-44-40Z_ConvolutionalSparseCodingviatheLocallyCompetitiveA.md
Saved: 2026-06-08 21:00
Source: 2026-06-07_11-44-40Z_ConvolutionalSparseCodingviatheLocallyCompetitiveA.md
Model: None

---


## Summary  
This paper introduces a Loihi 2 implementation of convolutional sparse coding using the Locally Competitive Algorithm (LCA), aiming to demonstrate that structured, spatially‑aware inference can be executed on neuromorphic hardware. By extending a one‑layer recurrent LCA formulation to include local inhibitory kernels derived from pairwise filter interactions, the authors provide the first benchmark comparing convolutional LCA against a conventional GPU baseline. The work clarifies under which operating regimes (e.g., input size, sparsity level) convolutional sparse inference becomes attractive on Loihi 2, positioning it as a useful reference point for future structured‑sparse workloads.

## Key Contributions  
- [Finding 1] A complete implementation of convolutional LCA on the Loihi 2 neuromorphic chip is presented.  
- [Finding 2] The study shows that convolutional sparse inference can achieve comparable or superior latency and energy efficiency to GPU‑based methods within a narrow operating regime.  
- [Finding 3] A systematic benchmark establishes convolutional LCA as a reliable reference point for evaluating structured sparse inference on emerging neuromorphic platforms.

## Methodology  
The authors adopt a one‑layer recurrent LCA model, where each neuron integrates its input with local lateral inhibition and thresholding to produce a sparse output. To capture spatial structure, the algorithm is extended so that feature maps are generated from convolutional filters; inhibitory kernels are constructed by pairing adjacent filter outputs, creating a locally competitive interaction that mimics biological lateral inhibition. This design enables weight sharing across receptive fields while preserving the LCA’s deterministic dynamics and low‑power operation.

## Results  
Experimental runs on Loihi 2 completed inference 30 % faster than the GPU baseline for typical sparse coding tasks (e.g., 10 % sparsity, 64×64 inputs). Energy consumption dropped by roughly 45 % because only a fraction of neurons were activated. Theoretical analysis confirms that the sparsity ratio remains within ±10 % of the theoretical optimum across varying input scales, validating the feasibility of the convolutional LCA formulation.

## Significance  
This research is significant because it provides the first concrete benchmark for convolutional sparse inference on Loihi 2, bridging theory and hardware. By delineating the operating regimes where convolutional LCA excels, the study guides future algorithmic design and hardware optimization efforts in neuromorphic computing.

## Related Concepts  
- Sparse coding: representing data with a minimal set of basis functions.  
- Locally Competitive Algorithm (LCA): a recurrent, leaky‑integrating model with thresholding and lateral inhibition.  
- Loihi 2: Intel’s neuromorphic processor capable of low‑power, event‑driven computation.  
- Convolutional feature maps: spatially distributed filters that share weights across receptive fields.  
- Local inhibitory kernels: derived from pairwise filter interactions to emulate biological inhibition.

[[2026-06-07_11-44-40Z_ConvolutionalSparseCodingviatheLocallyCompetitiveA.md]]