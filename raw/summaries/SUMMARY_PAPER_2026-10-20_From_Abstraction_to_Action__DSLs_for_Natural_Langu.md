---
title: From Abstraction to Action: DSLs for Natural Language Abstraction Interpretation and Execution
url: http://arxiv.org/abs/2610.28311v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-20_14-51-44Z_FromAbstractiontoAction_DSLsforNaturalLanguageAbst.md
generated_at: 2026-10-20 22:24
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper proposes using domain-specific languages (DSLs) as an explicit intermediate representation layer to bridge the gap between high-level natural language abstractions (e.g., "stack blocks in a pyramid") and the concrete actions needed to execute them. The authors demonstrate that generating code over a human-curated DSL dramatically improves language model performance on abstraction-heavy instruction-following tasks, achieving up to 10 absolute F1 point gains and matching human-level performance, while model-induced DSLs only partially recover these benefits and remain inconsistent across runs.

## Key Takeaways
- Language models consistently degrade in performance as the level of abstraction in an instruction increases, because they must simultaneously identify the intended abstraction and unroll it into many concrete actions. The paper shows that introducing a documented DSL whose primitives name recurring abstractions and expand into concrete actions effectively closes this gap, with gains concentrated specifically at higher abstraction levels.
- On the Hexagons visually-grounded instruction-following benchmark and the Text2CAD benchmark, code generation over a human-curated DSL yields dramatic improvements over direct inference, reaching the human performance ceiling. This confirms that the right representational layer is the critical factor, not merely prompting strategies or model scale.
- Models attempting to induce DSLs automatically from domain data recover only a partial fraction of the human-curated gains, produce inconsistent DSLs across runs, and fall short of their human-designed counterparts. This identifies automatic induction of representation layers as a significant open problem and a strong opportunity for future research.

## Context
This work sits at the intersection of natural language understanding, program synthesis, and embodied instruction following, addressing a well-documented failure mode in large language models: their inability to handle compositional, abstract instructions that require multi-step planning. By borrowing the DSL concept from software engineering, the authors reframe abstraction interpretation as a code-generation problem with a constrained, documented vocabulary, which aligns with broader efforts to give models structured intermediate representations rather than relying on end-to-end generation.

## Implications
For practitioners building agentic systems, robotics pipelines, or CAD-assist tools, the findings suggest that investing in curated, domain-specific representation layers is far more effective than scaling models or improving prompts for abstraction-heavy tasks. For the research community, the gap between human-curated and model-induced DSLs highlights a concrete open challenge: automatically discovering and inducing the right representational abstractions from data, which could unlock more general and scalable instruction-following systems without requiring hand-engineered vocabularies for every new domain.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.28311v1)
