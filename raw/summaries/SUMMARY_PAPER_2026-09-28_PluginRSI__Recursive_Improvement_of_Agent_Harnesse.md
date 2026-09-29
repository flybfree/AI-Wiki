---
title: PluginRSI: Recursive Improvement of Agent Harnesses with Reusable Plugins
url: http://arxiv.org/abs/2609.32423v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-26_09-49-25Z_PluginRSI_RecursiveImprovementofAgentHarnesseswith.md
generated_at: 2026-09-28 20:50
model: qwen3.6-35b-a3b
---

## Summary
PluginRSI introduces a novel framework for optimizing language model agent harnesses by decomposing them into atomized, reusable plugins rather than searching over monolithic programs. The method independently improves individual plugins, accumulates them in a shared library, and recombines them to evolve new harnesses iteratively. This approach demonstrates superior performance across software engineering, command-line interaction, and question-answering tasks while enabling effective transferability to unseen models and accelerated convergence on future optimization runs.

## Key Takeaways
- PluginRSI shifts harness optimization from searching complete programs to composing atomized plugins, allowing individual mechanisms to be isolated, improved independently, and reused across different iterations without the complexity of monolithic search spaces.
- The framework maintains a shared library where evolved plugins are accumulated; this repository enables recombination into new harnesses at each step, fostering continuous improvement and creating a growing asset of proven functional components.
- Empirical results show PluginRSI outperforms existing methods in software engineering, command-line interaction, and question-answering domains, while the evolved plugin library facilitates transferability to other solver models and accelerates convergence speed on unseen tasks during subsequent optimization cycles.

## Context
As autonomous agents become increasingly central to complex workflows, the design of their surrounding harnesses—comprising prompts, tools, and control logic—has emerged as a critical bottleneck for performance. Traditional optimization techniques often treat the entire agent configuration as a single unit, limiting modularity and making it difficult to leverage learned improvements across different tasks or model architectures.

## Implications
Practitioners can leverage PluginRSI to build more robust and adaptable agent systems by maintaining a reusable plugin library that reduces the cost of optimizing new agents or

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.32423v1)
