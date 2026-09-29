---
title: Action-Space Shaping for LLM Agents: Measuring and Mitigating Tool-Schema Bias
url: http://arxiv.org/abs/2609.34971v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_11-52-43Z_Action_SpaceShapingforLLMAgents_MeasuringandMitiga.md
generated_at: 2026-09-28 22:56
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces "schema bias," revealing that Large Language Model agents often perform inconsistently across functionally equivalent tool schemas even when the underlying executable actions and task states remain identical. The authors present an executable transformation framework employing nine operators to systematically rewrite tool definitions, enabling controlled isolation of interface effects from task complexity. Their evaluation demonstrates severe schema bias with success rates ranging from total failure to 97% based solely on schema representation, and shows that training fails to generalize across variants unless the specific schema is explicitly included in the training data.

## Key Takeaways
- The study develops an executable transformation framework using nine operators, including merging, splitting, and distributing actions, to generate multiple functionally equivalent tool schemas while preserving task semantics; this allows researchers to attribute performance changes strictly to interface variations rather than alterations in reachable states or action logic.
- Evaluation of eleven LLMs uncovers substantial schema bias, where success rates fluctuate dramatically depending on how tools are defined, indicating that current models lack robustness and often fail to recognize functional equivalence across different schema representations.
- Training does not automatically repair schema bias; improvements are only observed for specific schema variants if those exact definitions appear during training, suggesting that agents do not inherently learn action-space agnostic policies and require diverse schema exposure to develop generalizable tool-use capabilities.

## Context
As LLM-based agents increasingly automate complex workflows, the reliability of their interactions with external tools is paramount; however, existing research often treats tool schemas as static inputs, neglecting how representation choices might fundamentally influence model behavior. This work challenges the assumption that functional equivalence guarantees behavioral consistency by demonstrating that superficial changes in interface design can drastically alter agent performance, highlighting a critical vulnerability in current agentic architectures regarding generalization and robustness to input formatting.

## Implications
Practitioners developing agentic systems must treat tool schema design as a significant determinant of reliability rather than a mere formatting choice, necessitating evaluation protocols that assess performance across multiple schema variants to ensure consistent behavior. For the broader field, these findings imply that future training strategies should incorporate schema-agnostic objectives or

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34971v1)
