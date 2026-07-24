# Summary: 2026-07-21_15-31-49Z_ATLAS_AFoundationNeuralSamplerforAmorphousMaterial.md
Saved: 2026-07-24 01:19
Source: 2026-07-21_15-31-49Z_ATLAS_AFoundationNeuralSamplerforAmorphousMaterial.md
Model: None

---

## Summary  
The paper introduces ATLAS, a foundation neural sampler that directly generates Boltzmann‑distributed amorphous structures from an energy function without relying on rare barrier‑crossing events or biased reference ensembles. By learning a diffusion process parameterized as an equivariant graph neural network, ATLAS generalizes across system size, temperature, and composition, enabling efficient thermodynamic sampling and steering toward specific observables. The method also incorporates composition‑amortized pretraining to reduce inverse‑design costs dramatically. Coupled with a large language model agent, ATLAS searches high‑entropy metallic glass compositions for an optimal trade‑off between stiffness and ductility.  

## Key Contributions  
- [Finding 1] ATLAS achieves a free energy error below 0.2 % in the low‑temperature glass regime while using over 500× fewer energy evaluations than conventional parallel tempering MCMC.  
- [Finding 2] The sampler generalizes to Cu‑Zr and Cr‑Co‑Ni metallic glasses, reproducing short‑range order trends and allowing steering of structure toward prescribed order parameters and bulk moduli.  
- [Finding 3] Composition‑amortized pretraining cuts inverse‑design costs by several hundred‑fold compared with training from scratch for each composition.  

## Methodology  
ATLAS learns a diffusion process that samples the Boltzmann distribution of amorphous configurations directly from a target energy function. The diffusion dynamics are parameterized by an equivariant graph neural network, which captures local and global structural information. Because the diffusion is reversible, time reversal enables efficient thermodynamic estimation and steering toward desired observables such as order parameters or bulk modulus. A composition‑amortized pretraining phase trains a universal model on multiple compositions before fine‑tuning for a specific target, reducing the need for costly inverse‑design cycles.  

## Results  
In 2D Kob‑Andersen systems, ATLAS reproduces parallel tempering MCMC distributions with negligible error and computes free energies and entropies accurately. For Cu‑Zr and Cr‑Co‑Ni glasses, it recovers experimentally observed short‑range order and can steer structures to target order parameters while optimizing bulk moduli. The composition‑amortized approach outperforms composition‑specific training from scratch, lowering inverse‑design costs by several hundred‑fold. Coupled with a language‑model agent, ATLAS searches an eight‑element space for high‑entropy glasses balancing stiffness and ductility, identifying a converged Pareto frontier within 480 oracle evaluations.  

## Significance  
ATLAS establishes a foundation model for sampling, steering, and designing amorphous materials, bridging data‑driven generative methods with inverse‑design workflows. Its efficiency and generalizability open new pathways for discovering high‑performance glasses without exhaustive experimental screening.  

## Related Concepts  
amorphous materials, Boltzmann distribution, diffusion sampler, graph neural network (equivariant), time reversal, parallel tempering MCMC, order parameters, bulk modulus, Pareto frontier, inverse‑design, high‑entropy metallic glasses, composition‑amortized pretraining, energy function, thermodynamic estimation.
