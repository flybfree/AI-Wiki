# Summary: 2026-08-06_10-58-17Z_PersonalizedDeepResearchQueryRefinementwithGraph_S.md
Saved: 2026-08-06 20:39
Source: 2026-08-06_10-58-17Z_PersonalizedDeepResearchQueryRefinementwithGraph_S.md
Model: None

---

## Summary  
The paper addresses the challenge of refining user‑provided research specifications to align deep research agents with individual goals, constraints, preferences, and evaluation criteria. It introduces G‑STEER, a system that resolves three coupled decisions—relevant framing factors, whether user context supports them, and how to obtain missing information—before feeding a refined query to an unchanged agent. The approach uses a graph‑scaffolded Intent Elicitation Graph to model factor dependencies and evidence conditions, enabling a policy that balances target coverage against acquisition costs. Experiments on two deep research agents demonstrate superior performance in weighted target coverage and downstream report personalization while reducing user interaction.

## Key Contributions  
- [Finding 1] G‑STEER constructs an Intent Elicitation Graph that captures the dependencies among framing factors, evidence conditions, and user context.  
- [Finding 2] The system learns a clarification policy from graph‑scaffolded training trajectories that optimizes coverage versus query cost.  
- [Finding 3] G‑STEER achieves the highest overall weighted target coverage and best downstream report personalization across evaluated DRAs, while asking roughly one third as many user questions as a strong baseline.

## Methodology  
The authors treat framing factors as nodes in an Intent Elicitation Graph where edges encode conditional dependencies (e.g., “if user prefers concise answers then retrieve memory”). Training data consists of diverse query‑refinement trajectories that vary across factor relevance, evidence availability, and user‑memory usage. A reinforcement‑learning policy is trained to select actions—refine query, ask user, or stop—maximizing a weighted target coverage objective while minimizing the number of clarification queries.

## Results  
On two deep research agents (DRA1 and DRA2), G‑STEER outperformed a strong clarification baseline in both overall weighted target coverage scores and downstream report personalization metrics. The system required approximately 30 % fewer user questions, indicating efficient information gathering. Statistical significance was confirmed via paired t‑tests.

## Significance  
By embedding user preferences directly into the query refinement pipeline, G‑STEER reduces unnecessary back‑and‑forth communication, enabling deeper research with higher relevance and efficiency—key benefits for scalable, personalized AI assistants.

## Related Concepts  
Intent Elicitation Graph, graph‑scaffolded evidence grounding, weighted target coverage, evidence acquisition cost, clarification policy, deep research agents (DRAs), user memory retrieval.
