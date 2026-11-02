# Summary: 2026-10-01_14-34-32Z_NotAllExperienceBelongsintheWeights_ComponentRouti.md
Saved: 2026-10-01 22:35
Source: 2026-10-01_14-34-32Z_NotAllExperienceBelongsintheWeights_ComponentRouti.md
Model: None

---

## Summary
This paper addresses the ongoing debate regarding how self-improving GUI agents should utilize their past experiences, specifically comparing fine-tuning against retrieval-augmented generation. The authors argue that previous disagreements stem from treating trajectories as monolithic bundles rather than analyzing individual components with distinct properties. To resolve this, they introduce "component routing," a framework that decomposes experience into locators, procedures, state facts, and lessons to determine the optimal storage destination for each part. Their findings demonstrate that separating these components significantly enhances agent performance compared to whole-trajectory approaches.

## Key Contributions
- **Component Routing Framework**: The authors propose splitting trajectories into four distinct semantic components (locators, procedures, state facts, and lessons) and empirically determining which context (weights vs. prompt) is superior for each specific type of information across diverse environments and model families.
- **Predictive Rule for Destination Selection**: They derive a simple rule based on two pre-training properties—recurrence and state-conditionality—that accurately predicts the optimal destination for experience components, achieving perfect recovery rates in held-out settings.
- **Analysis of Value Dynamics**: The study identifies how training dynamics and producer-consumer mismatches influence the utility of weights versus context, revealing that readout decreases when items recur frequently in weights, while context gains are driven by information gaps.

## Methodology
The researchers conducted a comprehensive comparative analysis across three backbone model families, two distinct GUI environments, and multiple random seeds. They first decomposed successful agent trajectories into four atomic components: locators (identifying UI elements), procedures (sequences of actions), state facts (current system status), and lessons (generalizable insights). Each component was then evaluated in two destinations: integrated into the model’s weights via fine-tuning or injected into the prompt context via retrieval. To automate routing, they measured recurrence (how often an item appears) and state-conditionality (dependence on specific states) prior to training, fitting a rule that maps these properties to the optimal destination. This approach allowed them to isolate the impact of each component type without the confounding variables present in whole-trajectory baselines.

## Results
The experimental results show a clear divergence in performance based on component type: locators and lessons perform significantly better when stored in model weights, whereas procedures and state facts yield higher utility when kept in the prompt context. The proposed routing rule, based solely on recurrence and state-conditionality, correctly predicted the optimal destination for 24 out of 24 test cells involving held-out backbone families. Furthermore, agents utilizing component routing outperformed all whole-trajectory baselines and improved upon single-destination strategies by an average of +3.5 points in task success rates. The study also noted that writing recurring items into weights led to decreased readout efficiency, highlighting the diminishing returns of over-fitting repetitive data.

## Significance
This work provides a nuanced understanding of experience utilization in autonomous agents, moving beyond binary choices between fine-tuning and retrieval. By demonstrating that different types of knowledge require different storage mechanisms, it offers a more efficient path for scaling self-improving systems. The findings suggest that future GUI agents should adopt modular memory architectures rather than treating all past interactions as equal data points, potentially leading to more robust and adaptable AI behaviors in complex interactive environments.

## Related Concepts
- Self-improving AI Agents
- Retrieval-Augmented Generation (RAG)
- Continual Learning
- Parameter-Efficient Fine-Tuning
- Experience Replay
- GUI Automation

## Original research paper

[Canonical original paper: http://arxiv.org/abs/2610.01787v1](http://arxiv.org/abs/2610.01787v1)
