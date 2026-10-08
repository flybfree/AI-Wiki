---
title: Why Software Engineering Is Indispensable in the Age of Coding Agents
url: http://arxiv.org/abs/2610.10226v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-07_15-17-37Z_WhySoftwareEngineeringIsIndispensableintheAgeofCod.md
generated_at: 2026-10-07 22:18
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper by Alfonso Fuggetta directly challenges the popular narrative that AI coding agents will render software engineering obsolete. Instead, it argues that the very capabilities of large language models create structural gaps in software development that can only be filled by trained software engineers acting as methodologists, mediators, and custodians of knowledge. The paper identifies three inherent limitations of LLMs and four knowledge levers that must be reified as persistent artifacts to produce trustworthy software in an AI-assisted development environment.

## Key Takeaways
- Three structural properties of large language models—probabilistic generation, agnosticism, and semantic statelessness—create a fundamental vacuum in software development that no amount of training or fine-tuning can eliminate. Probabilistic generation means outputs are plausible but not guaranteed correct; agnosticism means the model lacks genuine understanding of the specific problem context; and semantic statelessness means the model cannot maintain coherent understanding across a full software system's lifecycle. Together, these properties produce software that appears convincing but is unverifiable and ultimately untrustworthy without human oversight.
- Filling this structural vacuum requires four distinct knowledge levers: methodological knowledge (how to structure and validate software), domain knowledge (understanding the specific problem space), design choices (architectural and implementation decisions), and process choices (how development is organized and governed). Each lever represents a form of expertise that LLMs cannot generate from training data alone because it is context-specific, normative, and requires judgment.
- All four knowledge levers must be reified as persistent artifacts—documents, specifications, architectural records, and process frameworks—rather than remaining implicit in a developer's mind. This reification is essential because AI agents lack semantic statelessness and cannot carry forward institutional knowledge across sessions or projects without explicit, durable representations.

## Context
This paper arrives at a moment when AI coding agents such as GitHub Copilot, Cursor, and autonomous agent frameworks are rapidly transforming how software is written, reviewed, and deployed. Industry discourse frequently frames these tools as replacements for human developers, yet the paper pushes back against this framing by grounding its argument in the structural properties of the underlying models themselves. It matters because it reframes the AI-and-engineering debate from a question of replacement to a question of complementary expertise, offering a principled taxonomy for what humans must contribute that machines structurally cannot.

## Implications
For practitioners and industry leaders, the paper suggests that investment in AI coding tools without parallel investment in software engineering methodology, domain expertise, and process governance will produce systems that look functional but carry hidden risks of unverifiability and failure. For the software engineering discipline, it elevates the role of the engineer from code producer to knowledge custodian and methodological architect, implying that curricula, certifications, and organizational structures must adapt to emphasize these higher-order competencies. For AI tool developers, the analysis implies that agent architectures should be designed to interface with and enforce persistent engineering artifacts rather than attempting to internalize all knowledge within model weights.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.10226v1)
