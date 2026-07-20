# Summary: 2026-07-17_17-23-22Z_LearningStandardModelstructurefromLHCdatawithRiema.md
Saved: 2026-07-19 21:00
Source: 2026-07-17_17-23-22Z_LearningStandardModelstructurefromLHCdatawithRiema.md
Model: None

---

## Summary  
The paper introduces **ShellFlow**, a transformer‑based generative model that learns the full Standard Model (SM) structure from raw LHC data using Riemannian flow matching. It is trained on roughly one billion ATLAS events without any explicit physics priors except the on‑shell condition and the invariant‑mass formula, allowing it to span five decades of invariant mass—from sub‑GeV up to TeV energies. The model reproduces all SM particle kinematics, resonance positions, lepton angles, quark masses, and inter‑particle correlations in a single training run. This work shows that the SM’s internal structure can be inferred directly from recorded collision data.

## Key Contributions  
- **Finding 1:** A single transformer architecture can generate each particle with correct intra‑particle kinematics across the entire invariant‑mass range.  
- **Finding 2:** The model reproduces the dilepton resonances (J/ψ, Υ, Z) at their PDG positions without any dedicated loss term for those features.  
- **Finding 3:** Inter‑particle correlations that are not part of the training objective are still learned by the flow network.

## Methodology  
The authors employ a Riemannian conditional flow matching model called **ShellFlow**. The on‑shell manifold is defined solely by the particle mass–energy relation and the invariant‑mass formula, which serve as the only physics priors. A transformer encoder processes the recorded event composition, while a reverse‑flow generator samples particles from this manifold. Training uses standard cross‑entropy loss on the generated events; no additional SM constraints are imposed.

## Results  
From one training run on ~10⁹ ATLAS 13 TeV events, ShellFlow learns to reproduce: intra‑particle kinematics, the J/ψ, Υ and Z dilepton resonances at their PDG masses and angles, the leptonic Weinberg angle, the W and top quark masses, and inter‑particle correlations that arise naturally. The model spans five invariant‑mass decades—from sub‑GeV to TeV—covering a range no single Monte Carlo sample can fully capture.

## Significance  
ShellFlow demonstrates that much of the SM’s phenomenology is data‑driven rather than hand‑crafted, reducing reliance on explicit parameterization. By learning structure from raw LHC events, it opens pathways for discovering new physics or refining parameters directly from experimental data, without requiring separate phenomenological models.

## Related Concepts  
- Riemannian flow matching (conditional generative modeling)  
- On‑shell manifold constraints  
- Transformer architecture for sequential data  
- Invariant‑mass formula and particle kinematics  
- Standard Model phenomenology
