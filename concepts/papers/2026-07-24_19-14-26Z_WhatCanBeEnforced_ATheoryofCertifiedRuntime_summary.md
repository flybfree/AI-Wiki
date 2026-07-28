# Summary: 2026-07-24_19-14-26Z_WhatCanBeEnforced_ATheoryofCertifiedRuntimeSafetyf.md
Saved: 2026-07-27 23:24
Source: 2026-07-24_19-14-26Z_WhatCanBeEnforced_ATheoryofCertifiedRuntimeSafetyf.md
Model: None

---

## Summary  
The paper “What Can Be Enforced? A Theory of Certified Runtime Safety for Tool‑Using Agents” investigates how static runtime guardrails can guarantee safety when agents invoke external tools, focusing on the limits of what can be certified as safe. It separates three intertwined questions: (1) which deterministic policies are enforceable by a gate relative to fixed oracle predicates; (2) how false‑block and miss rates behave under an exogenous law with calibrated interventions; and (3) whether static scores or ungated trajectories correctly capture the closed‑loop safety frontier when blocking alters future behavior. The authors develop theoretical bounds, formalize an occupancy program for controlled models, and add robustness via bounded representation attacks, showing that benign calibration alone is insufficient.

## Key Contributions  
- [Finding 1] Deterministic gates enforce exactly those nonempty safety policies whose good prefixes the register model can recognize; policy nontriviality is undecidable with two decrementable counters but lies in PSPACE for a separable monotone fragment.  
- [Finding 2] Under a fixed exogenous law, Neyman‑Pearson provides the exact false‑block/miss frontier, and conformal calibration yields a finite‑sample marginal certificate—potentially realized via block‑all.  
- [Finding 3] Once blocking changes future proposals, static scores and ungated trajectories need not identify the closed‑loop frontier; instead, a specified finite controlled model generates an occupancy program that captures the safety guarantee.

## Methodology  
The authors approach the problem by (i) constructing register models of tool‑using agents to capture observable state transitions, (ii) formulating oracle predicates as deterministic tests on those prefixes, and (iii) applying formal game‑theoretic analysis—Neyman‑Pearson for calibration, occupancy theory for closed‑loop dynamics—to derive theoretical guarantees. Experiments employ static diagnostics to verify which policies are recognized, controlled‑model enumeration to enumerate feasible policy spaces, representation rewrites to test robustness margins, and paired closed‑loop reruns to compare static vs. dynamic safety assessments.

## Results  
Theoretical analysis shows that enforceable policies form a PSPACE‑complete subclass of monotone policies, while the false‑block/miss frontier is exactly characterized by Neyman‑Pearson under exogenous law. Calibration produces finite‑sample certificates via block‑all, and an occupancy program derived from a controlled model yields a bounded representation attack that adds a robustness margin. Experiments confirm that static diagnostics correctly identify enforceable prefixes, that control‑model enumeration matches theoretical counts, and that representation rewrites improve calibration robustness without sacrificing safety.

## Significance  
This work bridges the gap between static tool‑use policies and certified runtime safety, offering concrete tools for engineers to design guardrails that are both provably safe and practically calibrated. By separating theoretical limits from empirical implementation, it enables more reliable deployment of agentic systems where tool calls can have irreversible consequences.

## Related Concepts  
runtime guardrails, oracle predicates, deterministic gates, register models, PSPACE‑complete decision problems, monotone fragment, Neyman‑Pearson theorem, false‑block/miss frontier, conformal calibration, block‑all, occupancy program, bounded representation attacks, static diagnostics, controlled model enumeration.
