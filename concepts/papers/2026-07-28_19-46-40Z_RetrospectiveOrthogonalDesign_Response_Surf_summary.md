# Summary: 2026-07-28_19-46-40Z_RetrospectiveOrthogonalDesign_Response_SurfaceReco.md
Saved: 2026-07-29 22:12
Source: 2026-07-28_19-46-40Z_RetrospectiveOrthogonalDesign_Response_SurfaceReco.md
Model: None

---

## Summary  
Retrospective Orthogonal Design (ROD) addresses the problem that regression estimates and sums of squares are sensitive to multicollinearity and term ordering when only observational data are available. The authors propose a method for reconstructing conditional mean surfaces on a probability‑balanced lattice while preserving observed cell means, completing unsupported cells, and evaluating the reconstruction via piecewise‑affine interpolation over Freudenthal polyhedra. By jointly selecting resolution and completion among rank‑admissible candidates and refitting on an untouched test set, ROD yields specification‑invariant contrast effects and order‑independent sums of squares. The approach also calibrates response‑free projections to a scientific basis and adjusts for finite‑resolution recovery loss.  

## Key Contributions  
- ROD reconstructs conditional mean surfaces on a probability‑balanced lattice, preserving observed cell means and completing unsupported cells.  
- It yields specification‑invariant contrast effects and unique, order‑independent sums of squares within the retained contrast space.  
- A Rao‑based information adjustment provides dependence‑aware sample‑size guidance for ROD planning.  

## Methodology  
The authors begin with a set of observational data and define a probability‑balanced lattice that balances treatment levels across experimental blocks. Using weighted tensor‑product contrasts, they reconstruct the conditional mean surface, completing any cells that were not observed in the original design. The reconstructed surface is evaluated through piecewise‑affine interpolation over Freudenthal polyhedra to ensure smoothness. Resolution and completion are selected jointly by validating rank‑admissible candidates on an untouched test set; after selection, the model is refitted and its performance is assessed on this hold‑out data. A response‑free projection calibration maps the fixed reconstruction onto a declared scientific basis, correcting for finite‑resolution recovery loss. Finally, a Rao information adjustment supplies sample‑size guidance that accounts for variable dependence among factors.  

## Results  
Across 6,480 simulated conditions spanning nine data‑generating processes, ROD matched or exceeded polynomial regression in five processes and performed strongest on threshold, sign‑interaction, and localized surfaces. For the quadratic‑interaction process, mean out‑of‑sample \(R^2\) differed by only 0.0001, while calibrated coefficient bias remained small across prespecified targets. In a weighted Mincer application, ROD produced the highest out‑of‑sample \(R^2\) point estimate, with substantial interval overlap with polynomial regression, and provided exhaustive sums of squares allocations that were invariant to term‑entry order.  

## Significance  
ROD tackles fundamental statistical issues arising from multicollinearity and term ordering in observational designs, offering a robust surface reconstruction that is specification‑invariant and order‑independent. By providing specification‑aware contrast effects and unique sums of squares, the method improves experimental efficiency and reduces bias in coefficient estimates. The Rao information adjustment further guides sample‑size planning, making ROD a practical tool for designing efficient experiments and interpreting complex response surfaces.  

## Related Concepts  
probability‑balanced lattice, Freudenthal polyhedra, tensor‑product contrasts, piecewise‑affine interpolation, Rao information adjustment, response‑free projection calibration, orthogonal design, sums of squares, multicollinearity sensitivity, term ordering invariance
