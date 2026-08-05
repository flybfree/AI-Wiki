# Summary: 2026-07-29_20-00-42Z_ComparisonofaParametricPhysics_InformedNeuralNetwo.md
Saved: 2026-07-30 23:13
Source: 2026-07-29_20-00-42Z_ComparisonofaParametricPhysics_InformedNeuralNetwo.md
Model: None

---

## Summary  
This paper presents a comparative study between two data-driven reduced-order modeling techniques—parametric physics-informed neural networks (PINNs) and tensorial reduced-order models (TROMs)—applied to the one-dimensional shallow-water dam-break problem, a classic benchmark in fluid dynamics. The authors develop both models to learn direct solution maps from space, time, and dam-break parameters without requiring numerical integration or calibration, enabling rapid prediction of system behavior. A key innovation is the use of shock-aware collocation in PINNs to enhance robustness when handling discontinuities inherent in dam-break flows.

## Semantic links
- [[concepts/math-physics/math-physics-hub.md|Math and Physics AI Hub]] — 2 title terms overlap; 55 backlinks; 4 summary/topic terms overlap
- [[concepts/papers/2026-07-28_09-38-42Z_At_the_RooflineSparseTensorContractionsonVe_summary.md|Summary: 2026-07-28_09-38-42Z_At_the_RooflineSparseTensorContractionsonVectorPro.md]] — 4 title terms overlap; 9 summary/topic terms overlap; semantic match 0.04
- [[concepts/papers/2026-08-02_00-27-01Z_LearningNottoOptimize_Physics_InformedActio_summary.md|Summary: 2026-08-02_00-27-01Z_LearningNottoOptimize_Physics_InformedAction_Space.md]] — 4 title terms overlap; 7 summary/topic terms overlap; semantic match 0.03

## Key Contributions  
- [Finding 1] The authors successfully develop a parametric PINN that learns a direct solution map for the dam-break problem, achieving high accuracy and enabling out-of-sample predictions.  
- [Finding 2] They introduce shock-aware collocation as a critical enhancement to PINNs, significantly improving their performance in capturing sharp transients like shocks.  
- [Finding 3] The tensorial reduced-order model (TROM) is shown to offer comparable accuracy with the advantage of being non-intrusive and requiring no training data or calibration.

## Methodology  
The methodology centers on constructing two parametric models that bypass traditional time integration by directly mapping input parameters—such as dam height, water level, and boundary conditions—to output states like velocity and pressure. The PINN is trained using collocation points along the solution manifold, with shock-aware formulations to handle discontinuities. The TROM employs a tensorial basis function expansion to represent the state space efficiently, minimizing computational cost while preserving accuracy.

## Results  
Both models demonstrate strong performance in reproducing dam-break solutions for both nominal and extrapolated parameter values. The PINN, particularly when enhanced with shock-aware collocation, achieves high fidelity across a wide range of conditions. The TROM provides consistent results with lower computational overhead. Out-of-sample predictions are validated against analytical solutions, confirming the robustness of both approaches.

## Significance  
This work advances data-driven modeling in fluid dynamics by demonstrating that PINNs and TROMs can be applied effectively to physically complex problems like dam-break flows. The integration of shock-aware techniques into PINNs is a significant contribution, addressing a long-standing challenge in their practical use. These models offer faster, more accurate predictions than traditional numerical methods, with potential applications in engineering design and real-time monitoring.

## Related Concepts  
parametric modeling, physics-informed neural networks (PINNs), reduced-order modeling (ROM), tensorial basis functions, shock-aware collocation, dam-break problem, data-driven simulation, one-dimensional shallow water equations.
