# Summary: 2026-08-05_17-43-51Z_CoPlan_ATrustworthyCo_IntelligenceInterfaceforCare.md
Saved: 2026-08-05 23:13
Source: 2026-08-05_17-43-51Z_CoPlan_ATrustworthyCo_IntelligenceInterfaceforCare.md
Model: None

---

## Summary  
The paper proposes CoPlan, a co‑intelligent and contestable interface that enables clinicians, patients, caregivers, and care teams to collaboratively generate and refine complex care plans. By employing role‑based argument graphs, the system lets AI agents produce both supporting and challenging arguments while human planners can inspect, reject, or modify them before final plan creation. This design fuses co‑intelligence—where each party contributes complementary expertise—with contestability, preserving human agency and clinical accountability. The work demonstrates CoPlan in an aging‑in‑place scenario, showing how it supports adaptive team recruitment, role‑specific argument review, and practical follow‑up scheduling.

## Key Contributions  
- [Finding 1] CoPlan introduces a contestable, role‑based argument graph framework that makes AI recommendations open to inspection, revision, and justification.  
- [Finding 2] The multi‑agent architecture enables specialized AI agents to generate both supporting and challenging arguments for each stakeholder’s needs.  
- [Finding 3] Human care planners can accept, reject, modify, or add arguments at any stage, ensuring that final plans reflect human judgment and real‑world feasibility.

## Methodology  
The authors approached the problem by designing a multi‑agent workflow where AI agents are specialized to understand clinical, functional, psychosocial, and environmental dimensions. Each agent produces candidate interventions along with argumentative evidence; these arguments are organized into a graph whose nodes represent stakeholders and edges encode supportive or challenging claims. Human planners interact with this graph via a web interface that allows them to evaluate each claim according to their role (e.g., clinician, patient). The system then iteratively refines the plan until consensus is reached, after which scheduling agents translate the final plan into actionable tasks.

## Results  
In the aging‑in‑place case study, CoPlan successfully recruited adaptive care teams and allowed clinicians to review conflicting arguments before finalizing a care plan. Role‑based argument review reduced decision latency by enabling parallel evaluation of supporting versus challenging claims. The system generated a practical follow‑up schedule that aligned with patient preferences and resource availability, demonstrating end‑to‑end functionality from idea generation to implementation.

## Significance  
CoPlan advances trustworthy human‑AI collaboration in care planning by embedding contestability into the workflow, thereby preventing rigid AI outputs and fostering shared responsibility. By preserving human agency while providing transparent justification for each recommendation, it supports clinical accountability and patient empowerment, which are critical for ethical AI deployment in healthcare.

## Related Concepts  
Co‑Intelligence, Contestability, Argument Graphs, Role‑Based Stakeholder Review, Multi‑Agent Workflow, Care Planning, Human‑AI Collaboration, Trustworthiness, Clinical Decision Support.
