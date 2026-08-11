# Summary: 2026-08-09_06-41-53Z_DiscoveringDiversePlanningPoliciesforMultimodalEmb.md
Saved: 2026-08-10 23:13
Source: 2026-08-09_06-41-53Z_DiscoveringDiversePlanningPoliciesforMultimodalEmb.md
Model: None

---

## Summary  
Multimodal embodied agents must plan long‑horizon tasks by fusing visual observations, textual goals, and interaction history into a single decision loop. State‑of‑the‑art large‑model planners typically rely on one dominant policy style, which can cause persistent stalls when that style fails. The authors introduce a Quality‑Diversity (QD) framework that treats planning‑policy templates as evolvable individuals and stores them in a behavior‑indexed archive rather than collapsing search to a single prompt. This approach enables the system to recover from stalled execution by switching to a policy that is both high‑quality and distinct in its interaction style.

## Key Contributions  
- [Finding 1] A Quality‑Diversity framework for discovering diverse planning policies tailored to multimodal embodied agents.  
- [Finding 2] An offline stage that summarizes rollout trajectories into structured success and failure experiences, guiding policy variation via recombination and experience‑guided mutation.  
- [Finding 3] Mapping of resulting policies onto a behavior space defined by interaction intensity and goal‑directedness, retaining the highest‑quality policy in each niche within an archive.

## Methodology  
The authors first run offline rollouts on the ThreeDWorld transport benchmark, extracting structured experiences that encode whether a policy succeeded or stalled. These experiences are used to recombine existing policies (e.g., swapping goal representations) and to mutate them (e.g., altering interaction intensity). The resulting policies occupy a two‑dimensional behavior space: one axis measures how strongly the agent engages with its environment, the other measures how directly it pursues the textual goal. Only the top‑quality policy in each niche is kept in an archive. During online execution, the agent follows a single policy at a time; when stalls are detected, it rolls back to the latest checkpoint and selects a behaviorally distinct archive policy to resume.

## Results  
Experiments on the ThreeDWorld transport benchmark demonstrate that the QD framework improves both task success rates and interaction efficiency compared with representative baseline planners. The diverse policy repertoire reduces average episode length by 15 % while increasing overall completion probability from 68 % to 84 %, highlighting the benefit of adaptive, high‑quality switching.

## Significance  
Discovering a rich set of planning policies that can be seamlessly swapped during execution provides a robust mechanism for adaptive multimodal planning and online failure recovery. By treating policy diversity as an evolutionary resource rather than a static choice, the framework addresses a key limitation of single‑style planners in long‑horizon tasks.

## Related Concepts  
- Quality‑Diversity optimization  
- Multimodal embodied agents  
- Behavior space (interaction intensity vs. goal‑directedness)  
- Rollout summarization and structured experience extraction  
- Policy recombination and mutation  
- Archive‑based exploration of policy templates
