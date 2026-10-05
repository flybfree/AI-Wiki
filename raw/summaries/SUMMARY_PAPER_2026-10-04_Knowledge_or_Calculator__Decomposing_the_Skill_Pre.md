---
title: Knowledge or Calculator? Decomposing the Skill Premium in Verifiable Financial Agent Workflows
url: http://arxiv.org/abs/2610.03564v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-02_16-44-04Z_KnowledgeorCalculator_DecomposingtheSkillPremiumin.md
generated_at: 2026-10-04 21:38
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces FinSkillBench, a 2,603-episode evaluation suite spanning 12 financial subtasks in portfolio construction, risk management, and fundamental analysis, designed to decompose where performance gains in financial AI agents actually come from. Through paired analysis across 9 models and 3 resource conditions, the authors demonstrate that curated skill packages (human-authored procedural documents and executable domain tools) produce a substantial +16.2-point mean score improvement, while self-generated skills within a single episode yield only +0.5 points. Critically, the authors show that the "skill premium" is not a property of the underlying model alone but emerges from the full interaction between model, resource provisioning, and evaluation harness design.

## Key Takeaways
- Curated skill packages dramatically outperform self-generated skills: across 17,820 episodes and 8 models, curated packages raise mean scores from 0.366 to 0.528 (+16.2 points), whereas skills generated within a single episode add only +0.5 points while consuming more tokens and turns, suggesting that in-the-moment skill generation is fundamentally insufficient for reliable financial reasoning.
- Decomposing the premium reveals that executable domain tools contribute +19.5 points while human-authored procedural documents contribute +5.6 points, and their combination is subadditive rather than additive, indicating that tools and documentation serve complementary but partially overlapping roles depending on the task type.
- The skill premium is strongly workflow-dependent: executable tools dominate in numerically intensive workflows, documentation matters more when procedural guidance or output schema compliance is the bottleneck, and interpretive tasks benefit from both resources. These effects are sign-stable across 10 scoring variants and cluster bootstrap analyses, and an independently implemented second harness reproduces the directional pattern while showing that effect magnitudes depend on how tools and data are exposed to the model.

## Context
This work addresses a critical gap in the AI agent evaluation landscape: most benchmarks measure whether a model can retrieve or reason about facts, but financial workflows demand correct quantitative execution, reliable use of procedural resources, and auditable structured outputs. By introducing deterministic verifiers and hidden regenerable ground truth, FinSkillBench moves beyond static answer-checking toward evaluating whether agents can reliably execute multi-step financial procedures. The decomposition methodology—separating documentation from executable tools—provides a methodological template for understanding agent capability gains across any domain where procedural knowledge and computational tools are both required.

## Implications
For practitioners building financial AI agents, the findings argue strongly against relying on models to generate their own procedural skills on the fly and instead advocate for carefully curated, externally provided tool and documentation packages tailored to specific workflow types. For the broader AI research community, the demonstration that the "skill premium" is a property of the full model-resource-harness system rather than the model alone challenges the common practice of attributing capability improvements to model architecture alone, suggesting that evaluation infrastructure and resource provisioning design are equally important levers for agent performance. Industry teams deploying financial agents should treat tool integration and procedural documentation as first-class engineering concerns rather than afterthoughts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.03564v1)
