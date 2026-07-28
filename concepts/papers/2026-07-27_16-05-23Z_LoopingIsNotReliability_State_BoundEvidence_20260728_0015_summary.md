# Summary: 2026-07-27_16-05-23Z_LoopingIsNotReliability_State_BoundEvidenceandType.md
Saved: 2026-07-28 00:15
Source: 2026-07-27_16-05-23Z_LoopingIsNotReliability_State_BoundEvidenceandType.md
Model: None

---

## Summary  
The paper investigates why looping in code repair may not guarantee reliability, showing that repeated revisions can degrade correctness despite high initial accuracy. It introduces a state‑bound evidence framework and typed revision contracts to bound what loops can safely repeat. The authors present empirical evidence from HumanEval repairs and theoretical analysis of trace effects. Their contribution is an executable specification for agentic loop repair that separates admission, preservation, certification, competence, and liveness.

## Key Contributions  
- **Finding 1:** Repeated revisions degrade correctness (0.820 → 0.673) while ever‑correct rises to 0.847, indicating looping does not preserve reliability.  
- **Finding 2:** Stale traces cause a 22.2‑point increase in correct‑start harm compared with current traces (p = 0.0337), CI [8.9, 37.0].  
- **Finding 3:** Repository experiments across 24 bugs and four coder stacks reveal floor effects and component heterogeneity without Holm‑significant differences.

## Methodology  
The authors conducted a sealed five‑seed study on 30 HumanEval repairs, generating 900 three‑revision trajectories under forced revision. They employed two common‑state studies with frozen programs to control bias and a prospective rollout policy to test the joint correctness criterion. Repository experiments were performed over 24 bugs using four coder stacks.

## Results  
Correctness dropped from 0.820 after one revision to 0.673 after two, yet ever‑correct improved to 0.847. Stale traces harmed correct starts by 34/135 versus 4/135 (p = 0.0337). The rollout policy eliminated observed harm but failed the joint criterion. Floor effects and heterogeneity were observed across bug types.

## Significance  
This work challenges the assumption that looping equals reliability in code repair, offering a principled contract to limit unsafe repetitions and thereby improving trust in agentic systems that perform iterative revisions.

## Related Concepts  
- State‑bound evidence  
- Typed revision contracts  
- Agentic code repair  
- HumanEval benchmark  
- Rollout policy
