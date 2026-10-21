---
title: Cognitive Maps in Large Language Models
url: http://arxiv.org/abs/2610.25596v1
type: paper-summary
date: 2026-10-21
source_paper: 2026-10-19_00-02-30Z_CognitiveMapsinLargeLanguageModels.md
generated_at: 2026-10-21 11:04
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether large language models construct internal representations analogous to the cognitive maps that animals use for flexible spatial reasoning. Through relational reasoning tasks and causal "mosaic experiments" that manipulate internal activations in open-weight language models, the authors demonstrate that models exceeding ten billion parameters form structured internal representations of relational information, binding entities to roles within an abstract relational framework. The findings reveal that LLMs compose pairwise relationship links retrospectively rather than maintaining a global coordinate system, and that entity-role binding is mediated by sparse, distributed key-value pairs whose perturbation can implant predictable "false memories."

## Key Takeaways
- Models beyond the ten-billion-parameter scale successfully inferred unstated relationships between entities and generalized these inferences to entirely synthetic entity names, indicating that the relational reasoning is not memorization-based but reflects a genuine abstract representational structure that transfers across novel entities.
- Across diverse model and task families, LLMs generated abstract representations of relational structure and combined them additively with representations of entity identity, effectively binding entities to roles within a relational framework. Critically, models stored observed relationships as pairwise links that they composed retrospectively when queried, rather than prospectively positioning each entity within a global coordinate system—differing from the continuous spatial maps hypothesized in biological cognition.
- Entity-role binding was mediated by a sparse, distributed set of key-value pairs within the model's internal activations. By causally perturbing these specific pairs through mosaic experiments, the researchers implanted "false memories" that altered model behavior in predictable and interpretable ways, providing direct causal evidence for the representational mechanism underlying relational reasoning.

## Context
The concept of cognitive maps originates in neuroscience, where place cells and grid cells in the hippocampus and entorhinal cortex enable animals to navigate novel environments flexibly. This paper extends that framework to artificial systems by asking whether LLMs develop analogous internal organizational structures when processing relational information. The work sits at the intersection of mechanistic interpretability, cognitive science, and AI safety, providing a causal experimental methodology—mosaic experiments that manipulate internal activations—that moves beyond correlational probing of model internals toward direct causal interrogation of how representations are structured and composed.

## Implications
For AI safety and interpretability practitioners, the identification of sparse, distributed key-value pairs as the binding mechanism offers a concrete target for auditing, editing, and steering model behavior, including the ability to implant or correct "false memories" in a controlled manner. For the broader field, the finding that relational structure is composed retrospectively from pairwise links rather than maintained as a global map suggests that scaling models may not automatically produce more coherent or globally consistent reasoning, raising important questions about how to design architectures or training procedures that encourage more robust relational generalization. Industry applications in knowledge graph reasoning, multi-hop question answering, and agent planning stand to benefit from a mechanistic understanding of how models compose relational information under limited input.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.25596v1)
