# Summary: 2026-07-22_01-19-42Z_PerfAgent_Profiler_GuidedIterativeRefinementforRep.md
Saved: 2026-07-24 01:23
Source: 2026-07-22_01-19-42Z_PerfAgent_Profiler_GuidedIterativeRefinementforRep.md
Model: None

---

## Summary  
PerfAgent is a profiler‑guided, verifier‑in‑the‑loop framework that enables large language model agents to perform repository‑level code optimization while preserving behavior. By feeding real hotspot information back into the agent through an iterative refinement loop, PerfAgent moves beyond shallow test‑passing patches toward expert‑matching speedups.

## Key Contributions  
- Founding 1: PerfAgent integrates profiler data with a verifier to uncover hidden bottlenecks that are invisible to simple passing tests.  
- Founding 2: The iterative refinement loop uses profiler evidence to select the next optimization step, preventing agents from stopping at trivial improvements.  
- Founding 3: On the GSO and SWE‑efficiency‑Lite benchmarks PerfAgent more than doubles the rate of expert‑matching patches compared with OpenHands+GPT‑5.1, raising performance to 39.2 % and 74 %, respectively.

## Methodology  
The authors built a workflow in which an LLM generates code patches, a verifier checks that behavior is preserved, the modified code is profiled, hotspots are extracted from the profiling results, and this evidence is fed back to the agent as guidance for subsequent optimizations. This cycle repeats until performance gains plateau or a predefined limit is reached.

## Results  
PerfAgent improves on two challenging optimization benchmarks: it raises GSO’s expert‑matching patch rate from 19.6 % to 39.2 % and SWE‑efficiency‑Lite’s rate from 26 % to 74 %. It also outperforms a best‑of‑five oracle baseline while using less computational cost, indicating that the gains stem primarily from better feedback rather than additional test sampling.

## Significance  
By replacing timing alone with concrete profiler evidence and verification, PerfAgent demonstrates that LLM agents can achieve expert‑level repository optimizations without requiring massive extra compute. This approach lowers the barrier for practical code improvement in large codebases.

## Related Concepts  
- Repository‑level code optimization  
- Profiler‑guided refinement  
- Verifier‑in‑the‑loop  
- Hotspot detection  
- Iterative refinement loop  
- Expert‑matching patches  
- Oracle baseline  
- Benchmarks GSO and SWE‑efficiency‑Lite
