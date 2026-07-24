# Summary: 2026-07-18_04-28-47Z_CLOSER_Bench_EvaluatingBudgetedCross_StageDesignCl.md
Saved: 2026-07-24 00:01
Source: 2026-07-18_04-28-47Z_CLOSER_Bench_EvaluatingBudgetedCross_StageDesignCl.md
Model: None

---

## Summary  
The paper introduces CLOSER‑Bench, a controlled evaluation protocol designed to assess budgeted cross‑stage design closure for hardware agents. It pairs three complementary tasks—spec‑to‑RTL, RTL‑to‑GDS, and spec‑to‑GDS—to capture the full flow from specification through physical implementation while accounting for tool feedback delays and heterogeneous oracles. The benchmark records every simulator, synthesis, STA, and place‑and‑route invocation, measuring final quality, anytime progress, tool cost, and cross‑stage recovery. By exposing a sharp completion‑closure gap across these stages, the study demonstrates that hardware closure is better viewed as a budgeted sequential decision problem rather than a collection of independent code generation tasks.

## Key Contributions  
- [Finding 1] CLOSER‑Bench reveals a pronounced completion‑closure gap: agents can solve localized AXI repair tasks but often fail to achieve full RTL‑to‑GDS closure, especially when verification is required.  
- [Finding 2] The benchmark validates a complete RTL‑to‑GDS flow using open‑source tools (Verilator, Yosys, OpenROAD, KLayout, Sky130) and constructs a macro‑based AXI/DMA streaming accelerator to enable stage‑paired evaluation.  
- [Finding 3] The results motivate treating hardware design closure as a budgeted sequential decision problem that must balance quality, progress, cost, and recovery across abstraction boundaries.

## Methodology  
CLOSER‑Bench adopts a controlled experimental protocol that pairs spec‑to‑RTL, RTL‑to‑GDS, and spec‑to‑GDS tasks for a single hidden objective. The authors record every invocation of simulators, synthesis, STA, and place‑and‑route tools, measuring final quality, anytime progress, tool cost, and cross‑stage recovery. A ten‑task pilot—including RTL repair, mutation‑based verification, coverage, PPA optimization, design‑space exploration, cross‑model debugging, and security—establishes the executable harness built on Verilator, Yosys, OpenROAD, KLayout, Sky130, and the Harbor agent harness. The macro‑based AXI/DMA streaming accelerator is used to pair stages for reproducible evaluation.

## Results  
The benchmark demonstrates a sharp completion‑closure gap: three agents successfully solve the localized AXI repair task, yet the matched verification‑closure task separates one frontier agent from two otherwise successful baselines. Full RTL‑to‑GDS flow validation confirms that the integrated tools can produce functional GDS files, and the macro accelerator enables efficient stage‑paired execution. These results quantify tool cost and recovery time while highlighting where agents excel or falter across abstraction layers.

## Significance  
Treating hardware closure as a budgeted sequential decision problem rather than independent tasks clarifies why certain failures persist (e.g., verification‑closure) and provides a common metric for evaluating progress, quality, and cost. CLOSER‑Bench offers a reproducible framework that bridges the gap between early‑stage code generation and final physical implementation, guiding research toward more robust, end‑to‑end hardware agents.

## Related Concepts  
budgeted cross-stage design closure, completion‑closure gap, RTL generation, verification, physical implementation, simulation, synthesis, STA, place‑and‑route, sequential decision problems, hardware agents.
