# Summary: 2026-10-04_15-22-23Z_MESH_Harness_Self_ImprovingAgentHarnessesviaBandit.md
Saved: 2026-10-05 22:24
Source: 2026-10-04_15-22-23Z_MESH_Harness_Self_ImprovingAgentHarnessesviaBandit.md
Model: None

---

## Summary
This paper introduces MESH-Harness, a novel framework for optimizing agent harnesses—the code structures that manage context, state, and tool coordination for language models—without altering the underlying model weights. The core contribution is a method that decomposes harnesses into modular, role-specific components, enabling systematic substitution and recombination of these modules. By employing bandit-guided compositional evolution, specifically using shared module representations and full-covariance LinUCB for scoring, the method efficiently navigates the vast search space of possible harness configurations. This approach allows for self-improving agent systems that significantly outperform existing baselines like Meta-Harness while maintaining lower computational costs for both search and inference.

## Key Contributions
- **Modular Decomposition and Reusability:** The authors establish a framework where agent harnesses are broken down into functional modules with explicit interfaces. This design allows for the substitution and recombination of alternative implementations for specific roles (e.g., context management, tool calling), facilitating design reuse and systematic optimization.
- **Efficient Search via Bandit-Guided Evolution:** The paper introduces a search strategy that combines shared module representations with full-covariance LinUCB (Linear Upper Confidence Bound) to score candidate combinations. This method predicts performance and exploration value, enabling the selection of promising configurations without exhaustively enumerating the combinatorial space.
- **Performance and Cost Efficiency:** MESH-Harness demonstrates superior performance over Meta-Harness across diverse tasks, including mathematical reasoning, code generation, and scientific tasks, achieving improvements of 2.00 to 7.01 points. Additionally, it reduces aggregate test-time costs by 44.2% and total optimization costs by 14.6% compared to the baseline.

## Methodology
The authors approach the problem of harness optimization by treating it as a compositional search problem under a limited evaluation budget. First, they define the agent harness as a collection of functional modules with role-specific interfaces, allowing for modular substitution. To guide the search, they employ a bandit algorithm using full-covariance LinUCB to score candidate combinations based on predicted performance and exploration value. This scoring mechanism is integrated with mixed-start coordinate ascent to select complete configurations for evaluation efficiently. After evaluation, validation traces are used to guide local code edits, refining the modules. These refined candidates are then incorporated into fixed-capacity role-specific pools, which serve as the source for subsequent recombination steps in an iterative optimization loop. This process ensures that the system learns from feedback while keeping the search space manageable.

## Results
Experimental evaluations were conducted on text tasks, retrieval-augmented mathematical reasoning, code generation, and interactive scientific tasks. MESH-Harness consistently outperformed Meta-Harness, with performance gains of 5.70, 7.01, 2.00, and 5.00 points, respectively, under matched candidate-evaluation budgets. Furthermore, iterative optimization cycles improved MESH-Harness performance by an additional 5.63 to 7.79 points over its initial configurations. In terms of efficiency, the reported configurations showed a 44.2% reduction in aggregate test-time cost and a 14.6% reduction in total cost (including search overhead) compared to Meta-Harness. These results validate that the proposed method effectively improves agent performance while controlling optimization costs.

## Significance
This research is significant because it addresses a critical bottleneck in deploying large language models: the inefficiency and rigidity of current agent harnesses. By demonstrating that harnesses can be systematically improved through modular design and efficient search algorithms without retraining the model, the paper offers a practical pathway for enhancing agent capabilities in resource-constrained environments. The reduction in both search and inference costs makes this approach viable for real-world applications where computational budgets are limited. It shifts the focus from model scaling to architectural optimization, providing a scalable method for self-improving agents that can adapt to specific tasks through code-level evolution rather than weight updates.

## Related Concepts
- Agent Harnesses
- Modular Design
- Bandit Algorithms
- LinUCB (Linear Upper Confidence Bound)
- Compositional Evolution
- Coordinate Ascent
- Self-Improving Agents
- Retrieval-Augmented Generation (RAG)
- Code Generation
- Optimization Budgets

## Original Paper
- [arXiv:2610.05300 — MESH-Harness](https://arxiv.org/abs/2610.05300v1)
