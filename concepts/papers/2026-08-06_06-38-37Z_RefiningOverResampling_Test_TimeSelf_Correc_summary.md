# Summary: 2026-08-06_06-38-37Z_RefiningOverResampling_Test_TimeSelf_Correctionfor.md
Saved: 2026-08-06 22:05
Source: 2026-08-06_06-38-37Z_RefiningOverResampling_Test_TimeSelf_Correctionfor.md
Model: None

---

## Summary  
The paper addresses the limitation of test‑time scaling where additional inference compute often yields diminishing returns because new rollouts repeat existing answer patterns rather than generating diverse reasoning. It introduces a verifier‑free breadth–depth refinement framework that leverages extra compute to both explore multiple independent reasoning trajectories and iteratively self‑correct each trajectory before aggregating results. The method combines breadth, which preserves diverse initial attempts, with depth, which repairs local errors within those attempts, to produce higher‑quality answers than greedy decoding or simple majority voting.  

## Key Contributions  
- [Finding 1] A verifier‑free breadth–depth refinement framework that uses test‑time compute for both exploration and iterative self‑correction of candidate solutions.  
- [Finding 2] Iterative self‑critique and self‑correction within each rollout, enabling local reasoning errors to be repaired before aggregation.  
- [Finding 3] Majority voting of refined answers yields consistently higher accuracy than greedy decoding, majority voting, verifier‑based best‑of‑N, beam search, and lookahead decoding across multiple benchmarks.  

## Methodology  
The authors sample a set of independent reasoning rollouts from the LLM, then apply an iterative self‑critique loop to each rollout that identifies flawed steps and proposes corrections. After refinement, all corrected answers are aggregated via majority voting, preserving diverse initial attempts (breadth) while improving them locally (depth). The process is fully verifier‑free; it relies only on the model’s own reasoning output for correction.  

## Results  
Across AIME24, AIME25, AMC, OlympiadBench, and MATH500, the breadth–depth refinement consistently outperforms greedy decoding, majority voting, verifier‑based best‑of‑N, beam search, and lookahead decoding on open‑weight models. For Qwen2.5‑1.5B, accuracy rises from 25.0 % to 32.5 % on AMC and climbs from the strongest verifier baseline of 58.0 % to 58.0 % (a modest gain) on MATH500, demonstrating that test‑time compute is more effective when used for refinement rather than merely sampling or verifier selection.  

## Significance  
This work shows that allocating extra inference time to refine sampled reasoning trajectories can substantially boost LLM performance, especially in open‑weight settings where external reward models are unavailable. By integrating breadth and depth, the method mitigates the repetition problem inherent in simple test‑time scaling, offering a more robust path to higher accuracy without relying on costly verification systems.  

## Related Concepts  
- Test‑time scaling  
- Verifier‑based selection  
- Breadth–depth refinement  
- Majority voting aggregation  
- Iterative self‑correction  
- Self‑critique loops  
- Open‑weight models
