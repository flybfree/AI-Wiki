---
title: Fewer Assumptions by Design: A Reusable Skill for LLM-Assisted Verus Verification
url: http://arxiv.org/abs/2609.34886v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_10-58-41Z_FewerAssumptionsbyDesign_AReusableSkillforLLM_Assi.md
generated_at: 2026-09-28 23:08
model: qwen3.6-35b-a3b
---

## Summary
This paper investigates the application of Large Language Model agents to assist in formal verification for Rust using Verus, specifically targeting the complexities of doubly linked lists which are difficult to specify formally. The authors demonstrate that by implementing a reusable skill encoding domain knowledge and task decomposition, LLMs can synthesize strong specifications while minimizing reliance on unproven assumptions or axiomatic lemmas. The results indicate that a carefully designed verification skill enables agents to generate low-trust, robust formalizations for self-referential data structures effectively.

## Key Takeaways
- Formal verification of self-referential structures like doubly linked lists is prone to specification weaknesses when LLMs rely on unproven assumptions or `assume` statements, which expands the trusted base and weakens verification guarantees; this work highlights the necessity of mitigating such dependencies to ensure rigorous correctness.
- The study introduces a reusable skill that combines domain-specific knowledge with a task-decomposition strategy, allowing LLM agents to systematically construct specifications rather than generating them randomly, thereby enhancing the consistency and quality of the resulting formal artifacts.
- Comparative evaluation against manual verification and property-specific approaches shows that an LLM agent equipped with this tailored skill successfully produces strong specifications for doubly linked lists while significantly reducing assumptions, proving that structured prompting can yield low-trust results comparable to expert efforts.

## Context
As the Rust ecosystem gains traction in safety-critical domains, formal verification tools like Verus are becoming essential for guaranteeing memory and thread safety, yet the manual effort required remains a significant bottleneck for adoption. Integrating LLMs into this workflow offers potential efficiency gains, but concerns persist regarding the

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34886v1)
