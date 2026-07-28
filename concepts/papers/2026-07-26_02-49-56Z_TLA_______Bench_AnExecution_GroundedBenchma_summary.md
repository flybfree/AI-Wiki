# Summary: 2026-07-26_02-49-56Z_TLA_______Bench_AnExecution_GroundedBenchmarkandDa.md
Saved: 2026-07-27 20:14
Source: 2026-07-26_02-49-56Z_TLA_______Bench_AnExecution_GroundedBenchmarkandDa.md
Model: None

---

## Summary  
The paper introduces **TLA$^{+}$‑Bench**, a new dataset and benchmark that evaluates natural‑language to TLA$^{+}$ specification generation by measuring whether the generated formalism actually holds its intended properties when run on a model checker. By grounding grading in execution rather than mere parseability or textual similarity, the authors demonstrate that correctness can be quantified as a range of rates across different evaluation settings. The study also reveals that many existing benchmarks rely on unstated assumptions about how to grade outputs, leading to misleading performance numbers.  

## Key Contributions  
- **Finding 1:** An exact execution‑grounded oracle produces not a single correctness number but a *correctness envelope* – a range of correct rates that depends on evaluation choices such as whether the model is given configuration names or interface supplies.  
- **Finding 2:** Varying only the grading choice (e.g., reference comparison vs. execution) changes the observed correct‑rate sixfold, moving from ~10 % to ~1.7 %, showing that prior benchmarks are highly sensitive to their evaluation methodology.  
- **Finding 3:** Adding the interface‑supply choice widens the envelope elevenfold (from 18.7 % down to 1.7 %), and models write valid TLA$^{+}$ far more often than correct ones; default performance is only 16 % correct, rising to 26 % when configuration names are supplied, while open‑model cases reach ≤1 %.  

## Methodology  
The authors assembled **TLA$^{+}$‑Bench** from 403 gold specifications and 897 parse‑only silver specifications drawn from 13 public repositories, thereby subsuming earlier TLA$^{+}$ generation data. Each gold specification ships a configuration that the TLA$^{+}$ model checker executes over its full reachable state space, producing deterministic results for every property name. The dataset also contains four model‑written natural‑language descriptions in two styles from two providers, each tagged with difficulty and category labels. Grading is performed by running the generated specification through the model checker and counting how many of the configuration names are satisfied, which yields an execution‑grounded correctness score rather than a parse check or textual similarity metric.  

## Results  
The main experimental results show that the *correctness envelope* spans from 1.7 % (lowest) to 26 % (highest). When models are evaluated without additional information, correct rates hover around 16 %; supplying configuration names lifts this to 26 %. Providing open model specifications reduces correctness to ≤1 %, and performance drops sharply with increasing difficulty. These numbers illustrate that many prior benchmarks—relying on parseability or resemblance—would have reported much higher (or lower) scores, highlighting the instability of such metrics.  

## Significance  
Grounding evaluation in execution rather than superficial checks makes TLA$^{+}$‑Bench a reliable reference for measuring natural‑language to formal specification generation. It also exposes how arbitrary grading choices can dramatically alter perceived performance, prompting researchers to adopt more consistent and interpretable benchmarks. The work advances the field by providing an objective, executable yardstick that aligns with the goal of producing truly correct specifications.  

## Related Concepts  
- **TLA$^{+}$**: A modern extension of TLA (temporal logic for analysis) used to describe concurrent systems and their properties.  
- **Model checking**: An automated technique that exhaustively explores a system’s state space to verify whether it satisfies given specifications.  
- **Correctness envelope**: The range of correct‑rate outcomes observed under different evaluation configurations, indicating the impact of grading assumptions.  
- **Benchmarking**: Systematic testing of algorithms or systems using standardized datasets and metrics.
