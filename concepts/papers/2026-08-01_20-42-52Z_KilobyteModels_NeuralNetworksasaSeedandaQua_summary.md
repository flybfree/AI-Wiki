# Summary: 2026-08-01_20-42-52Z_KilobyteModels_NeuralNetworksasaSeedandaQuantizedL.md
Saved: 2026-08-03 20:32
Source: 2026-08-01_20-42-52Z_KilobyteModels_NeuralNetworksasaSeedandaQuantizedL.md
Model: None

---

## Summary  
The paper proposes an extreme form of neural‑network compression in which the deployable artifact is not a set of weights but a short “recipe” that can regenerate them. By expressing a network’s parameters as a nonlinear function of a compact trainable latent and a fixed random basis, only the latent needs to be stored because the basis and initialization are reproducible from an integer seed. The resulting model becomes a *seed* together with a quantized latent whose size is bounded by its dimension and bit width rather than the original parameter count. This approach yields aggressive compression while preserving accuracy.

## Key Contributions  
- [Finding 1] Only the latent needs to be stored; the random basis and initialization are deterministic from an integer seed, eliminating the need to keep large weight matrices on‑device.  
- [Finding 2] The artifact consists of a seed plus a quantized latent whose storage cost is set by the latent dimension and bit width, not by the number of parameters in the original network.  
- [Finding 3] Aggressive bit widths are achievable only after fine‑tuning the latent with quantization in the loop; a structured block‑wise basis allows weights to be regenerated almost for free even for very large networks.

## Methodology  
The authors build on Mapping Networks, which decompose a network’s weight matrix into a fixed random basis and a trainable latent that encodes the nonlinear mapping. They introduce a *block‑wise* version of this basis that can scale to projections too large to fit in memory. The workflow is: (1) generate a reproducible seed to initialize the basis; (2) train only the latent under quantization constraints; (3) at inference time, reconstruct each block’s weights by applying the fixed basis to the quantized latent values. This method avoids storing the full weight matrix and relies on cheap integer arithmetic for regeneration.

## Results  
Experiments show that a mapped model attains accuracy comparable to an aggressively quantized version of the same network while occupying far fewer bytes—often orders of magnitude less than storing raw weights. The size of the compressed artifact is determined solely by the latent dimension and the chosen bit width, not by parameter count. Moreover, achieving the most aggressive bit widths requires iterative fine‑tuning of the latent with quantization constraints, but a structured basis ensures that weight regeneration is essentially free even for networks whose projection cannot be held in memory.

## Significance  
The cost of storing and transmitting trained neural networks scales linearly with their parameter count, creating bottlenecks for over‑the‑air updates, on‑device libraries, and bandwidth‑limited deployments. By replacing the weights themselves with a tiny seed and a quantized latent, this work dramatically reduces storage and transmission overhead without sacrificing performance, opening new possibilities for real‑time, low‑bandwidth AI services.

## Related Concepts  
Mapping Networks, latent representation, quantization, integer seed reproducibility, block‑wise basis, compressed artifact, over‑the‑air updates.
