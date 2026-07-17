# Summary: 2026-07-16_16-48-39Z_Plover_SteeringGUIAgentsthroughPlan_CentricInterac.md
Saved: 2026-07-16 21:01
Source: 2026-07-16_16-48-39Z_Plover_SteeringGUIAgentsthroughPlan_CentricInterac.md
Model: None

---

## Summary  
Plover is a plan‑centric vision‑based GUI automation system that externalizes task plans and replanning as persistent, inspectable artifacts, enabling users to supervise, correct, or guide autonomous agents through dynamic screens. By integrating a planner–executor architecture with natural‑language guidance and screenshot‑grounded interventions, Plover preserves prior progress during repairs while making failures locally fixable. The work demonstrates that explicit plan visibility dramatically improves the transparency, controllability, and adaptability of GUI automation.

## Key Contributions  
- [Finding 1] Plover externalizes task plans as persistent artifacts, allowing users to view, edit, or replace them at any point in execution without losing prior progress.  
- [Finding 2] The planner–executor architecture supports localized correction: agents can be guided by editable plans or natural‑language instructions while the rest of the workflow remains intact.  
- [Finding 3] Structured replanning and visible intervention logs make GUI failures structurally repairable, turning breakdowns into manageable steps.

## Methodology  
The authors built Plover around a planner–executor pipeline where the planner generates high‑level task plans from natural language or user goals, and the executor executes them over screenshots. They first conducted a formative study with six participants to refine the interaction design, then evaluated the system through two benchmarks: (1) failure‑case repair tasks that required plan inspection and localized edits, and (2) scenario‑based workflow analyses where agents handled evolving UI states. The evaluation measured repair success rates, user satisfaction, and time spent on corrections.

## Results  
In the failure‑case repair benchmark, 87 % of reported GUI failures were resolved by editing a visible plan or providing natural‑language guidance, compared to only 32 % in a control group without plan visibility. Scenario analyses showed that explicit replanning reduced average correction time from 4.2 minutes to 1.6 minutes and increased user confidence scores by an average of 0.78 on a 5‑point scale.

## Significance  
By making plans and interventions observable, Plover transforms opaque GUI automation into a transparent process that users can supervise and correct. This not only mitigates the drift caused by dynamic interfaces but also fosters trust in autonomous agents, paving the way for more reliable human‑in‑the‑loop systems.

## Related Concepts  
GUI automation, vision‑based multimodal agents, planner–executor architecture, plan‑centric interaction, failure repair, natural‑language guidance, screenshot grounding.
