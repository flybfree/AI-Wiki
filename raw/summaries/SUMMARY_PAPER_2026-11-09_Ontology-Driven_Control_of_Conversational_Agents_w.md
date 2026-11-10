---
title: Ontology-Driven Control of Conversational Agents with a Use-Case for Job Interview Practice
url: http://arxiv.org/abs/2611.09282v1
type: paper-summary
date: 2026-11-09
source_paper: 2026-11-06_10-35-18Z_Ontology_DrivenControlofConversationalAgentswithaU.md
generated_at: 2026-11-09 21:26
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper proposes an ontology-based framework for designing and controlling conversational strategies in Large Language Models, moving away from ad hoc, non-reusable adaptations toward formally defined and transparent conversational characteristics. Using a job interview practice use case, the authors demonstrate that automatically fine-tuning an LLM based on ontologically defined concepts effectively improves the model's compliance with desired conversational traits, including tone, style, and global conversational strategy. The work shows that multiple concurrent conversation aspects can be simultaneously controlled through a single formal ontology structure.

## Key Takeaways
- The authors introduce a systematic ontology-based approach to define conversational strategies at both the micro level (individual response characteristics such as tone and style) and the macro level (global conversational strategy), replacing the common practice of ad hoc, non-reusable, and non-transparent prompt engineering or fine-tuning adjustments that dominate current LLM adaptation workflows.
- Through a job interview practice use case, the paper demonstrates that automatically fine-tuning an LLM using training data generated from formally defined ontological concepts measurably improves the model's alignment with the requested conversational characteristics, providing empirical evidence that structured knowledge representations can guide LLM behavior more reliably than unstructured instructions.
- The approach explicitly handles multiple concurrent conversation aspects simultaneously within a single ontology, enabling transparent and reusable definitions of desired conversational behavior that can be audited, modified, and reapplied across different domains without requiring bespoke development for each new scenario.

## Context
Current LLM-based conversational agents in domain-specific settings typically rely on prompt engineering, system instructions, or ad hoc fine-tuning to steer model behavior, approaches that are opaque, difficult to reuse, and hard to verify. This paper sits at the intersection of knowledge representation, ontology engineering, and LLM alignment research, proposing a structured alternative grounded in formal ontologies. It addresses a recognized gap in the field: the lack of transparent, reusable, and formally verifiable methods for controlling conversational strategy at a global level rather than merely shaping individual responses.

## Implications
For practitioners building domain-specific conversational agents in education, training, and professional coaching applications, this ontology-driven approach offers a reusable and auditable method to enforce complex conversational behaviors without opaque prompt hacks. For the broader AI research community, it demonstrates that formal knowledge structures can serve as effective training signals for LLM alignment, potentially bridging symbolic AI and neural language models. Industry applications in interview training, tutoring systems, and customer service could benefit from transparent, verifiable conversational control that reduces the risk of unpredictable model behavior in high-stakes interactions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.09282v1)
