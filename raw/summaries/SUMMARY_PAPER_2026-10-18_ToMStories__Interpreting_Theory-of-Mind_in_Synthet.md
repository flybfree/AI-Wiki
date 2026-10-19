---
title: ToMStories: Interpreting Theory-of-Mind in Synthetic Narratives
url: http://arxiv.org/abs/2610.22632v1
type: paper-summary
date: 2026-10-18
source_paper: 2026-10-15_20-38-58Z_ToMStories_InterpretingTheory_of_MindinSyntheticNa.md
generated_at: 2026-10-18 22:03
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces ToMStories, a synthetic evaluation dataset of approximately 6,000 short narrative vignettes designed to test whether language models can infer characters' implicit psychological states—emotions, fears, motivations, and emotional wounds—from behavioral cues rather than explicit statements. Evaluating thirteen open-weight models ranging from 1B to 72B parameters, the authors find that while the largest models can match human performance on multiple-choice questions, they fall short on open-ended interpretation tasks, revealing systematic simplifications in how models both interpret and generate implicit psychological states.

## Key Takeaways
- The dataset encodes psychological states through three distinct conveyance modes: implicit "showing" through behavior and context, explicit "telling" through direct description, and conflicting signals between dialogue and narrative description. This tripartite design allows researchers to isolate exactly where models struggle—particularly when cues are indirect or contradictory—rather than conflating comprehension failures with simple reading comprehension gaps.
- A critical performance gap emerges between multiple-choice and open-ended evaluation formats. The largest models (up to 72B parameters) achieve human-level accuracy on constrained multiple-choice questions but underperform on open-ended questions requiring free-form inference. This suggests that models may pattern-match toward plausible answer options rather than genuinely constructing nuanced psychological interpretations, a distinction that multiple-choice benchmarks would obscure.
- The authors caution that synthetic narratives, while useful for controlled experimentation, likely overestimate how well models interpret real human psychology. Models make simplifications in both interpreting and generating implicit states, meaning performance on synthetic vignettes does not straightforwardly transfer to understanding complex, ambiguous real-world social situations.

## Context
Theory-of-Mind evaluation has become a central concern in AI safety and alignment research, as understanding human intentions and emotions is foundational for safe deployment of language models in social, clinical, and collaborative settings. Prior benchmarks have largely relied on explicit statements or simple false-belief tasks, leaving a gap in evaluating whether models can perform the kind of indirect, inferential reasoning that characterizes everyday human social cognition. ToMStories addresses this gap by systematically varying how psychological information is encoded, enabling more granular diagnosis of model reasoning failures.

## Implications
For practitioners building AI systems intended for social interaction—chatbots, therapeutic assistants, negotiation agents, or collaborative tools—these findings suggest that current models may appear socially competent in structured evaluation settings while remaining brittle in open-ended, ambiguous human contexts. The paper also highlights a methodological caution for the broader research community: synthetic evaluation data, while valuable for controlled analysis, can create an inflated sense of model capability that does not hold when models encounter the messiness of real human communication. Designers of future benchmarks should consider open-ended evaluation formats and real-world narrative complexity to avoid overestimating model social understanding.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22632v1)
