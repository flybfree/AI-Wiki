# Summary: 2026-06-30_13-16-39Z_Calibration_NotCompilation_DetectingandRepairingMi.md
Saved: 2026-06-30 21:00
Source: 2026-06-30_13-16-39Z_Calibration_NotCompilation_DetectingandRepairingMi.md
Model: None

---


## Summary  
The paper argues that the true test of a probabilistic program is its statistical calibration—not merely whether it compiles and passes unit tests. It introduces a comprehensive “calibration oracle” built from Bayesian workflow diagnostics (posterior predictive checks, simulation‑based calibration, sampler diagnostics such as R̂, divergences, ESS, and held‑out predictive density) to detect misspecification in programs written by large language models (LLMs). The authors then evaluate how this oracle can be used for repair, showing that feedback from the oracle yields far better outcomes than unit‑test feedback or no feedback at all. Finally, they demonstrate on real LLM‑generated code that a substantial fraction of runnable programs are statistically misspecified and that calibration‑guided repair outperforms conventional review methods.

## Key Contributions  
- [Detection: A reference‑free detector using 14 misspecification types across 10 model families achieves AUC 0.97 (88 % at 2 % FPR), far exceeding the unit‑test oracle’s 0 %).]  
- [Repair: Incorporating calibration feedback into an LLM repair loop improves performance dramatically compared with unit‑test feedback, which is itself worse than no feedback.]  
- [Reality: In a benchmark of neutral briefs, 15–47 % of runnable LLM programs are statistically misspecified; calibration‑guided repair beats LLM‑as‑judge review, Bayesian‑workflow checklists, and self‑debug data summaries.]

## Methodology  
The authors constructed a benchmark with 200 instances spanning 14 misspecification categories (e.g., Gaussian vs. heavy‑tailed likelihoods, Poisson vs. over‑dispersed counts) across ten model families. They evaluated detection using both a reference‑based classifier and a fully reference‑free version that relies on an automated search for correct programs. Calibration was assessed via the full Bayesian workflow: posterior predictive checks, simulation‑based calibration, sampler diagnostics (R̂, divergences, ESS), and held‑out predictive density. For repair, they inserted the oracle’s feedback into a loop where LLMs rewrite their own code after receiving either unit‑test results or calibration diagnostics.

## Results  
The detection system achieved an AUC of 0.97 overall (88 % at a 2 % false‑positive rate), while the reference‑free version reached 62–78 % accuracy, compared with 0 % for unit‑test feedback. In repair experiments, GPT‑5.1 improved from 33 % to 92 % and Claude from 75 % to 100 % after calibration‑guided rewrites (paired McNemar test, *n* = 228). When applied to programs generated from scratch for neutral briefs, the system identified that 15–47 % are misspecified; calibration‑guided repair outperformed LLM‑as‑judge review, a Bayesian‑workflow checklist, and data‑summary self‑debug.

## Significance  
The work establishes that correctness in probabilistic programming is defined by statistical calibration rather than syntactic compilation. By providing an objective “calibration oracle,” it bridges the gap between unit tests and true model validation, offering a practical path to improve LLM reliability in scientific computation.

## Related Concepts  
- Posterior predictive checks  
- Simulation‑based calibration  
- Sampler diagnostics (R̂, divergences, ESS)  
- Held‑out predictive density  
- Unit‑test oracle  
- LLM‑as‑judge review  
- Bayesian‑workflow checklist  
- Data‑summary self‑debug
