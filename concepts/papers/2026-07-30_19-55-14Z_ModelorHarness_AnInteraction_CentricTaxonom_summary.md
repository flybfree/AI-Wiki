# Summary: 2026-07-30_19-55-14Z_ModelorHarness_AnInteraction_CentricTaxonomyforLoc.md
Saved: 2026-08-02 21:04
Source: 2026-07-30_19-55-14Z_ModelorHarness_AnInteraction_CentricTaxonomyforLoc.md
Model: qwen3.8-flash-next-iq3_xxs

---

## Summary
This paper addresses the critical challenge of diagnosing agent failures by introducing an interaction-centric taxonomy that moves beyond system-level outcome evaluations. The authors argue that existing methods obscure the origin of faults, creating a "repair-assignment problem" where it is unclear whether to fix the model, the harness, the environment, or the benchmark. To resolve this, they propose a structured framework that localizes failures to specific interactions between components, such as models, tools, and users. By assigning each failure mode to a specific edge and fault side, the taxonomy provides actionable guidance for targeted interventions, applicable across various agent architectures including coding assistants and multi-agent systems.

## Key Contributions
- **Interaction-Centric Taxonomy**: The authors introduce a novel classification system comprising 41 distinct failure modes. Unlike previous benchmark-specific taxonomies, this framework is generalized and organized by assigning failures to specific edges between system components (e.g., model-tool, model-user) and identifying the "fault side" responsible for the error.
- **Actionable Repair Assignment**: The taxonomy directly links failure categories to specific engineering interventions. Model-side failures indicate targets for post-training or fine-tuning, harness-side failures point to improvements in scaffolding and tool integration, and environment or grader failures highlight the need for redesigning evaluation conditions or benchmarks.
- **Cross-Architecture Applicability**: The framework is designed to be agnostic to specific agent architectures, demonstrating utility across diverse systems such as coding assistants, long-horizon personal assistants, and multi-agent systems, thereby providing a unified diagnostic language for agent development.

## Methodology
The authors developed the taxonomy by analyzing the interactions among core agent components: models, harnesses, users, tools, memory, and environments. They grounded the taxonomy in empirical data, including worked examples from public benchmarks, model system cards, published reports, and logged agent trajectories. To validate the taxonomy's reliability and objectivity, they employed independent reasoning agents as judges to categorize failures. These automated judges were compared against human-generated category labels to assess the consistency and reproducibility of the classification scheme across different frontier models.

## Results
The study evaluated the taxonomy's effectiveness using four frontier models as judges. The results demonstrated high inter-rater reliability, with the strongest automated judge achieving a Cohen’s kappa ($\kappa$) score of 0.76 against human category labels. This high agreement suggests that the taxonomy captures shared structural patterns in agent failures rather than reflecting annotator-specific biases or preferences. The findings indicate that the proposed framework can reliably localize failures to specific components, enabling more precise diagnosis and targeted repair strategies.

## Significance
This work is significant because it transforms agent evaluation from a black-box outcome assessment into a diagnostic tool for system improvement. By clarifying where faults originate, the taxonomy helps developers avoid misdirected efforts, such as fine-tuning a model when the actual issue lies in poor tool integration or flawed benchmark design. It provides a standardized language for the AI community to discuss and fix agent failures, potentially accelerating the development of more robust and reliable agent systems by ensuring that interventions are applied to the correct component.

## Related Concepts
- Agent Failure Localization
- Interaction-Centric Taxonomy
- Repair-Assignment Problem
- Model Post-Training
- Harness Engineering
- Benchmark Design
- Cohen’s Kappa ($\kappa$)
- Multi-Agent Systems
- Agent Scaffolding
