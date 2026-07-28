# Summary: 2026-07-25_09-16-40Z_KAYROS_AnAnytimeandExactOpen_SourceSolverforDurati.md
Saved: 2026-07-27 22:33
Source: 2026-07-25_09-16-40Z_KAYROS_AnAnytimeandExactOpen_SourceSolverforDurati.md
Model: None

---

## Summary  
This paper introduces KAYROS, an open‑source solver that solves duration‑minimization time‑dependent vehicle routing problems (TDVRPTW and TDVRP) with exact optimality guarantees. It is the first tool to provide anytime streaming solutions together with publicly verifiable certificates for piecewise‑linear travel‑time functions, eliminating the need for costly discretisation. The authors also present Poryos2026, a benchmark family generated from real OpenStreetMap road networks that includes checker‑validated best‑known solutions and five instances where KAYROS improves on published references.

## Key Contributions  
- **First anytime exact solver** – KAYROS delivers streaming improving solutions from the first seconds while guaranteeing optimality with certificates, a capability not previously available in open source.  
- **Open‑source, single‑command installation** – The tool has no proprietary dependencies; it can be installed and run with one command, making it accessible to researchers worldwide.  
- **Poryos2026 benchmark family** – A rigorously generated set of 1,080 paired CVRP, VRPTW, TDVRP, and TDVRPTW instances with checker‑validated best‑known solutions and five instances where KAYROS yields strictly better results than existing references.

## Methodology  
KAYROS builds on the branch‑price‑and‑cut framework of Lera‑Romero et al. (2020) but replaces its proprietary LP backend with an open‑source one. The solver employs anytime streaming improving solutions, warm‑start behavior, and checker‑exact pricing to handle stepwise travel times exactly. Its certification protocol involves four independent solves that must agree on a solution certificate, providing publicly verifiable optimality proofs.

## Results  
On the MAMUT‑routing benchmark collection, KAYROS generates 468 optimality certificates, each verified by four independent runs. Five of these certificates strictly improve the published reference values, demonstrating both correctness and superiority over existing methods. The Poryos2026 benchmark confirms feasibility guarantees: every instance’s best‑known solution is checker‑validated, and KAYROS outperforms those references in five cases.

## Significance  
The work bridges a long‑standing gap between exactness and accessibility, offering researchers a tool that can be used immediately without costly discretisation. By providing verifiable certificates, it strengthens the scientific record of optimal solutions for time‑dependent routing problems. The human‑AI collaboration model showcases how iterative design, rigorous verification, and open sharing can accelerate progress in operational research.

## Related Concepts  
- Time‑dependent vehicle routing (TDVRPTW/TDVRP)  
- Branch‑price‑and‑cut algorithmic framework  
- Anytime algorithms with streaming improving solutions  
- Exactness via LP solvers and certificates  
- Piecewise‑linear travel‑time functions  
- Open‑source benchmarking and verification (checker‑exact pricing)
