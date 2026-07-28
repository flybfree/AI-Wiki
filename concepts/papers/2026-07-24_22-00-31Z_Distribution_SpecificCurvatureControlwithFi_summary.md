# Summary: 2026-07-24_22-00-31Z_Distribution_SpecificCurvatureControlwithFinite_Sa.md
Saved: 2026-07-27 22:32
Source: 2026-07-24_22-00-31Z_Distribution_SpecificCurvatureControlwithFinite_Sa.md
Model: None

---

## Summary  
A short fine‑tuning run can erase the safety guards of an open‑weight model, allowing harmful adaptations such as weapon assistance or hate speech generation. The paper proposes HarmAlign, a method that applies function‑preserving spectral deformation constrained to an estimated contrastive activation subspace, with finite‑sample guarantees to bound harmful curvature. By deriving lower bounds on the local harmful‑distribution curvature and converting them into convergence‑rate control for constant‑step gradient descent, HarmAlign can protect benign tasks while still allowing safe adaptation. Empirically it blocks direct fine‑tuning attacks across a hazardous‑knowledge relearning setting and a harmful assistance fine‑tuning scenario.

## Key Contributions  
- Finite‑sample lower bounds on the estimated subspace energy and resulting local harmful‑distribution curvature.  
- A stability–progress dichotomy that turns certified curvature into conditional convergence‑rate control for constant‑step gradient descent.  
- Empirical demonstration that HarmAlign blocks three distinct fine‑tuning attacks while preserving benign tasks across first‑order optimizers.

## Methodology  
The authors treat safety as a geometric problem: they compute an approximate contrastive activation subspace using a small set of benign data, then apply spectral deformation that preserves function values within this subspace. The deformation is limited to the estimated subspace, yielding a curvature estimate with finite‑sample bounds. This ensures that only harmful directions in the model’s output space incur large curvature while benign directions remain shallow.

## Results  
Theoretically, the method provides O(1/√n) guarantees on the energy of the estimated subspace and O(1/n) lower bounds on harmful curvature for n samples. Experimentally, within a fixed‑architecture, finite‑budget threat model, HarmAlign successfully prevents direct fine‑tuning attacks and three adaptive attacks across both hazardous‑knowledge relearning and assistance fine‑tuning tasks. The protection persists across all tested first‑order optimizers at every checkpoint, even under out‑of‑distribution harmful fine‑tuning.

## Significance  
This work bridges the gap between theoretical safety guarantees and practical model adaptation by offering finite‑sample curvature control that is both stable and progressive. It enables open‑weight models to retain beneficial fine‑tuning capabilities without compromising safety, addressing a critical vulnerability in AI systems where small updates can cause catastrophic misuse.

## Related Concepts  
- Curvature control: limiting how quickly gradients change.  
- Spectral deformation: modifying model weights via eigen‑space transformations.  
- Contrastive activation subspace: a low‑dimensional region of activations that distinguishes benign from harmful data.  
- Finite‑sample guarantees: error bounds that depend on the number of training samples, not infinite limits.  
- First‑order optimizers and constant‑step gradient descent: standard training dynamics used in practice.
