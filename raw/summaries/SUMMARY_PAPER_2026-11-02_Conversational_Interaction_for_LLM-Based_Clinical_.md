---
title: Conversational Interaction for LLM-Based Clinical Text-to-SQL: A User Study with Healthcare Professionals
url: http://arxiv.org/abs/2611.00605v1
type: paper-summary
date: 2026-11-02
source_paper: 2026-10-31_04-01-13Z_ConversationalInteractionforLLM_BasedClinicalText_.md
generated_at: 2026-11-02 21:28
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper presents a within-subjects user study comparing single-turn and conversational multi-turn text-to-SQL interfaces for accessing electronic health record (EHR) data via the MIMIC-IV database, conducted with 14 physicians and supplemented by interaction logs from 21 healthcare professionals. The study demonstrates that conversational interfaces significantly outperform single-turn approaches in usability, user trust, and real-world adoption preference, while revealing that realistic clinical queries frequently require clarification dialogue that benchmark evaluations fail to capture.

## Key Takeaways
- The conversational multi-turn interface achieved a mean System Usability Scale score of 85.9 compared to 68.2 for the single-turn interface (p<0.001), with statistically significant advantages across performance expectancy, effort expectancy, self-efficacy, and behavioral intention constructs. In forced-choice comparisons, 93% of participants reported greater overall satisfaction with the conversational interface, 86% preferred it for real-world adoption, and 71% trusted its results more, with zero participants preferring or trusting the single-turn interface.
- Turn-level analysis of 425 logged user interactions revealed that freely composed clinical queries triggered clarification requests in 24.8% of cases, compared to only 1.8% for predefined, fully specified questions. Critically, 64.3% of these clarification episodes originated from EHR- or clinical-domain knowledge gaps, indicating that ambiguity is inherent to real clinical information-seeking rather than an artifact of poor interface design.
- The authors argue that conversational interaction is a practical prerequisite rather than a convenience for natural-language EHR access, and that benchmark-style evaluation with fully specified questions substantially underrepresents the ambiguity and iterative refinement demands of genuine clinical use.

## Context
Text-to-SQL research has historically been evaluated on curated benchmarks such as Spider or BIRD, where questions are fully specified and single-turn generation is assumed. This paper challenges that evaluation paradigm by placing LLM-based query generation in the hands of actual clinicians working with real EHR data, bridging the gap between benchmark performance and deployed usability. It contributes to the broader conversation in AI about the limitations of static evaluation metrics and the necessity of studying human-AI interaction dynamics in high-stakes domains like healthcare.

## Implications
For healthcare IT practitioners and EHR vendors, these findings suggest that investing in conversational, multi-turn dialogue capabilities is not an optional enhancement but a functional requirement for any natural-language query system intended for clinical deployment. For the AI research community, the study highlights that benchmark evaluations using fully specified questions can mask critical failure modes—particularly the high rate of clarification needs driven by domain-specific ambiguity—meaning that evaluation protocols must incorporate realistic, underspecified user queries. For clinicians and health systems, the results indicate that trust and adoption of AI-assisted data access tools depend heavily on whether the system can handle iterative refinement and domain-specific ambiguity, which single-shot generation cannot address.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.00605v1)
