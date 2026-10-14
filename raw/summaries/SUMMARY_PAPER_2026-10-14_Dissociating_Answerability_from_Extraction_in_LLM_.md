---
title: Dissociating Answerability from Extraction in LLM Question Answering over Radiology Reports
url: http://arxiv.org/abs/2610.17576v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_01-55-59Z_DissociatingAnswerabilityfromExtractioninLLMQuesti.md
generated_at: 2026-10-14 01:06
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper proposes a methodological framework for evaluating LLM-based question answering over radiology reports by separating two distinct decisions: whether a report contains an answer (answerability) and which text span provides that answer (extraction). The authors demonstrate that traditional single-metric F1 scoring conflates these decisions, masking critical differences in model behavior, and show that models with similar F1 scores can differ more than twofold in their false-answer rates. Their experiments across 13 LLMs reveal that adding an unanswerable example to demonstrations primarily shifts when models choose to answer rather than how well they extract, and that a simple ensemble-based abstention rule can reduce false-answer rates without degrading extraction quality.

## Key Takeaways
- Models with nearly identical F1 scores exhibited false-answer rate differences exceeding a factor of two, demonstrating that F1 alone is insufficient to characterize the safety profile of a radiology QA system. A false answer presents an unsupported claim as clinical fact, while over-abstention hides information the report actually contains; collapsing both into one number obscures which failure mode dominates.
- Adding a single unanswerable example to demonstration sets caused 12 of 13 models to abstain more frequently, and roughly three-quarters of the answers they withdrew had F1 scores of 0.5 or higher. This shows the unanswerable example primarily altered the answerability decision rather than extraction quality, confirming the two decisions are operationally independent.
- Within individual models, false answers showed no clear statistical association with extraction quality, but a post-hoc ensemble rule—keeping an answer only when a sufficient number of other models also answered—reduced the zero-shot false-answer rate by 4 percentage points without any detectable change in F1, suggesting that answerability can be improved through decision-level interventions rather than better extraction.

## Context
In clinical NLP and medical AI, radiology question answering systems are increasingly proposed as decision-support tools, yet evaluation practices inherited from general-domain QA benchmarks treat all errors through a single F1 metric. This paper sits at the intersection of evaluation methodology, clinical safety, and LLM reliability research, addressing a gap where benchmark scores fail to distinguish between confidently wrong answers and appropriately cautious abstentions. As LLMs are deployed in healthcare settings where a fabricated finding can influence patient care, the ability to audit and control answerability independently from extraction becomes a prerequisite for safe deployment.

## Implications
For radiology QA researchers and benchmark designers, the paper argues that evaluation suites should report false-answer rates, over-abstention rates, and decomposed F1 changes as separate metrics rather than relying on a single aggregate score. For clinical practitioners and AI safety teams, the findings suggest that ensemble-based abstention policies offer a low-cost, model-agnostic safeguard against unsupported claims without requiring retraining or architectural changes. More broadly, the dissociation between answerability and extraction highlights that improving a model's ability to say "I don't know" is a distinct engineering problem from improving its ability to locate correct spans, and progress on one does not guarantee progress on the other.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.17576v1)
