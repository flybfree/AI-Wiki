# Summary: 2026-07-27_16-05-23Z_LoopingIsNotReliability_State_BoundEvidenceandType.md
Saved: 2026-07-28 00:15
Source: 2026-07-27_16-05-23Z_LoopingIsNotReliability_State_BoundEvidenceandType.md
Model: None

---

## Summary  
The paper investigates why looping‑based repairs in coding agents can degrade reliability despite producing correct patches, and it proposes a formal, state‑bound approach to guarantee that revisions are both admissible and verifiable. By separating the stages of admission, preservation, certification, competence, and liveness, the authors derive an evidence‑bound typed loop contract that mechanically enforces these guarantees. The work demonstrates empirically that stale traces cause substantial correctness loss in real repair trajectories, while a well‑specified implementation preserves verified checkpoints without implying improved agentic competence.  

## Key Contributions  
- [Finding 1] Repeating a correct patch does not guarantee reliability; the overall correctness of an agent after multiple revisions drops sharply when stale traces are used.  
- [Finding 2] A formal, typed loop contract can be derived from evidence‑bound verification to separate admission (accepting patches) from preservation (maintaining verified states).  
- [Finding 3] Experimental results show a 22.2‑point increase in correct‑start harm when stale traces replace current traces, highlighting the need for state‑bound contracts.  

## Methodology  
The authors conducted a sealed five‑seed study on 30 HumanEval repairs, generating 900 three‑revision trajectories under forced revision to isolate the impact of trace fidelity. They employed two common‑state studies using 2,430 branches from frozen programs to control for post‑treatment bias. A prospective 540‑rollout policy was evaluated on a 14B replication, and repository experiments over 24 bugs across four coder stacks were performed to assess floor effects and component heterogeneity. All analyses used Holm‑significance testing with exact confidence intervals.  

## Results  
Current correctness fell from 0.820 after one revision to 0.673 after two revisions, while ever‑correct rose to 0.847. Stale traces harmed 34/135 correct starts versus only 4/135 with current traces (95 % CI [8.9, 37.0]), a Holm‑significant p = 0.0337. The reference implementation of the typed loop contract preserves verified checkpoints and emits auditable admission receipts without improving repair competence or calibrated verifier dependence. Repository experiments revealed floor effects but no Holm‑significant component heterogeneity.  

## Significance  
The findings reveal that looping repairs are vulnerable to trace decay, undermining reliability in agentic code repair systems. By providing a state‑bound, typed contract and an executable specification, the work offers a concrete mechanism for guaranteeing that revisions are both admitted and verified, which is essential for trustworthy automated maintenance. The empirical evidence underscores the importance of preserving current traces to avoid correctness loss, guiding future research on robust verification‑driven repair pipelines.  

## Related Concepts  
- Agentic code repair  
- Looping repairs  
- Trace fidelity (current vs. stale traces)  
- Typed loop contracts  
- Evidence‑bound verification  
- Holm‑significance testing  
- Common‑state studies  
- Floor effects in repository experiments
