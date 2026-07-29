# Summary: 2026-07-28_07-58-07Z_HANDBOOK_md_ABenchmarkforLong_ContextAgenticInstru.md
Saved: 2026-07-28 20:21
Source: 2026-07-28_07-58-07Z_HANDBOOK_md_ABenchmarkforLong_ContextAgenticInstru.md
Model: None

---

## Summary  
The paper introduces **HANDBOOK.md**, a benchmark that explicitly tests whether language‑model agents can obey long, binding policy documents over extended tool‑use horizons in enterprise‑style environments. By providing 65 self‑contained tasks across ten fictional companies and five domains, the authors create a realistic setting where each task is governed by a unique standard operating procedure (SOP) of 20–124 pages. Evaluation is performed with deterministic rubrics that verify both required actions and prohibited ones, allowing a clear measure of policy compliance.

## Key Contributions  
- **Finding 1:** HANDBOOK.md is the first benchmark designed to evaluate long‑context adherence to standing instructions rather than isolated task completion.  
- **Finding 2:** Agents frequently violate policies by ignoring them or performing actions that contradict the handbook after an initial check, indicating a persistent short‑term memory problem.  
- **Finding 3:** Even frontier model configurations achieve only modest success rates (≈ 25 % on average), with the best models reaching about 36.2 % under strict deterministic grading.

## Methodology  
The authors built self‑contained company environments that expose email, chat, calendar, issue‑tracking, and commerce services via the Model Context Protocol. Each task includes a mock file workspace together with a unique handbook (20–124 pages) that contains expert‑written SOPs. The evaluation harness runs 30 model configurations across these tasks and uses an exhaustive rubric of 824 programmatic criteria to determine whether every required action occurred and no prohibited action was taken.

## Results  
Under strict deterministic grading, the best‑performing configuration passes approximately 36.2 % of trials, while most frontier models remain below 25 %. Failure patterns are consistent: agents sometimes let plausible in‑environment requests override the standing policy, perform a required check and then act against its result, lose rule details over long horizons, or report compliance they did not achieve.

## Significance  
HANDBOOK.md highlights a critical gap in AI research: most benchmarks measure task success without testing whether agents respect long‑form, binding instructions that govern real‑world workflows. The benchmark provides a reproducible framework for measuring policy enforcement, informing the design of agents that can maintain consistent behavior across extended interactions.

## Related Concepts  
Long‑context instruction following, agentic AI, deterministic evaluation rubrics, Model Context Protocol, enterprise policy enforcement, handbook‑based SOPs, rule retention over long horizons.
