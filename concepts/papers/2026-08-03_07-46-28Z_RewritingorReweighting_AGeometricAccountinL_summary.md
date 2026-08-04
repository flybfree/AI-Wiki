# Summary: 2026-08-03_07-46-28Z_RewritingorReweighting_AGeometricAccountinLanguage.md
Saved: 2026-08-03 23:44
Source: 2026-08-03_07-46-28Z_RewritingorReweighting_AGeometricAccountinLanguage.md
Model: None

---

## Summary  
The paper investigates whether post‑training changes in language models stem from rewriting or merely reweighting existing mechanisms, focusing on two distinct failure modes: repetition (a decoding‑attractor pathology) and sycophancy (a preference‑related alignment issue). By treating model behavior as geometric data, the authors develop a “behavioral manifold” that isolates geometry‑specific coordinates and projects them into low‑dimensional local charts across two complementary spaces. This approach reveals how supervised fine‑tuning (SFT) fundamentally alters these charts while reward optimization mainly adjusts their weights. The unified framework provides a clear mechanistic distinction between the two training objectives.

## Key Contributions  
- [Finding 1] Behavioral manifold analysis isolates behavior‑specific geometry by selecting sparse coordinates and lifting them into low‑dimensional local charts, enabling systematic comparison across model families.  
- [Finding 2] Two chart types—ACT (runtime activation) and NOC (functional information flow)—compress similarly across architectures; contribution‑space charts expose a more architecture‑robust core, whereas activation‑space charts retain stronger family‑specific structure.  
- [Finding 3] Supervised fine‑tuning rewrites the behavioral geometry, while reward optimization changes behavior but largely preserves the underlying chart.

## Methodology  
The authors study two mechanistically distinct failures—repetition and sycophancy—to understand how post‑training alters model behavior. They introduce “behavioral manifold analysis,” which extracts sparse coordinates that are strongly associated with each failure, then projects these into low‑dimensional local charts in both ACT space (capturing runtime activation states) and NOC space (quantifying functional information flow). The resulting charts are compared across multiple model families to reveal shared versus architecture‑specific geometry.

## Results  
The charts derived from the manifold analysis are highly compressed, allowing partial alignment across different architectures. Contribution‑space charts show a robust core that persists despite architectural differences, while activation‑space charts retain more family‑specific details. Experiments demonstrate that supervised fine‑tuning produces a consistent asymmetry in these charts, indicating geometry rewrites, whereas reward optimization alters behavior but leaves the chart largely unchanged.

## Significance  
This geometric perspective offers a unified framework for distinguishing between two common post‑training objectives: SFT, which rewrites behavioral geometry, and reward optimization, which reweights it. By quantifying how each objective reshapes model behavior through distinct geometric transformations, the work clarifies why certain failures persist or are mitigated under different training regimes.

## Related Concepts  
- Behavioral manifold analysis  
- ACT space (runtime activation states)  
- NOC space (functional information flow)  
- Contribution‑space charts  
- Activation‑space charts
