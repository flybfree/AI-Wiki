# Summary: 2026-08-03_17-03-19Z_SWE_Touch_BenchmarkingCodingAgentsWhenUsersTouchth.md
Saved: 2026-08-04 01:07
Source: 2026-08-03_17-03-19Z_SWE_Touch_BenchmarkingCodingAgentsWhenUsersTouchth.md
Model: None

---

## Summary  
The paper SWE‑Touch investigates how coding agents behave when users can inspect and modify code in a shared workspace, a scenario that most existing benchmarks ignore. By introducing Counter‑Edits—plausible edits to task‑relevant code that conflict with the original goal—the authors create a realistic stress test for collaborative development. The framework mines multiple repair trajectories from SWE‑bench Verified, DeepSWE, and SWE‑bench Pro, generates user patches, and injects them together with contextual messages at the moment agents encounter the changed region. This enables a direct measurement of how well models understand evolving code and reconcile conflicting edits.

## Key Contributions  
- **Finding 1:** Counter‑Edit reduces the average resolve rate on SWE‑bench Verified by 7.7 percentage points, demonstrating that autonomous performance degrades when workspace changes are introduced.  
- **Finding 2:** The degradation persists across longer‑horizon benchmarks (DeepSWE and SWE‑bench Pro), indicating a broader limitation in state awareness beyond short tasks.  
- **Finding 3:** Trajectory analysis reveals that agents often retain conflicting code or replace it without re‑inspection, highlighting a failure to validate revised behavior.

## Methodology  
The authors built the SWE‑Touch framework by extracting task‑critical regions from diverse repair trajectories and using a separate User Patch Generator to produce plausible edits. These edits are inserted into the repository at the precise moment agents reach the affected code, accompanied by user‑generated messages that reflect typical collaborative interactions. The system then measures how each coding model resolves the task after these modifications, comparing outcomes against baseline scores on SWE‑bench Verified and longer‑horizon datasets.

## Results  
Empirical results show a consistent 7.7 pp drop in resolve rates across all nine evaluated models, with similar drops observed on DeepSWE (average 6.2 pp) and SWE‑bench Pro (average 5.9 pp). Visualization of repair trajectories confirms that many agents either ignore the new code or overwrite it without re‑testing, leading to persistent errors.

## Significance  
These findings underscore a critical gap: strong autonomous coding does not guarantee awareness of shared‑workspace changes. The study identifies three core capabilities—detecting workspace modifications, reconciling conflicting edits with task goals, and verifying revised behavior—as essential for future collaborative agents.

## Related Concepts  
- Autonomous code generation  
- Shared‑workspace editing  
- Counter‑Edit methodology  
- Repair trajectory analysis  
- State awareness in AI systems
