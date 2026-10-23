---
title: Who Is Sycophantic to Whom? Confident LLMs, Human Deference, and the Collapse of Trust Calibration
url: http://arxiv.org/abs/2610.31579v1
type: paper-summary
date: 2026-10-22
source_paper: 2026-10-22_17-15-59Z_WhoIsSycophantictoWhom_ConfidentLLMs_HumanDeferenc.md
generated_at: 2026-10-22 22:37
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates the reverse of the well-studied LLM sycophancy problem: rather than asking whether language models bend to user preferences, the authors ask whether humans bend to confidently stated but incorrect information from LLMs. Through a controlled within-subjects experiment with 32 participants interacting with five GPT-5-mini-based assistants containing varying levels of planted falsehoods (0–100%), the study demonstrates that humans overwhelmingly defer to confident AI output, absorbing falsehoods at roughly 65% regardless of the falsification rate, while their confidence calibration collapses to chance-level discrimination.

## Key Takeaways
- Human deference to confident AI is near-absolute: across 104 quizzes and 1,040 answers, participants chose the planted falsehood 60% of the time on falsified items versus only 11% on correctly taught items (odds ratio 12.5), and absorbed falsehoods were held with a confidence rating of 8.4 out of 10, mirroring the confidence the assistant projected.
- Trust calibration collapses entirely: the discrimination of confidence for correctness fell from an AUROC of 0.70 to pure chance, meaning participants could no longer distinguish between facts they had verified independently and facts they had merely absorbed from the assistant, yet their post-task trust ratings barely moved, indicating a dangerous disconnect between actual reliability and perceived reliability.
- The interaction loop is self-reinforcing and asymmetric: participants returned to the chat more often when the assistant was worse, but returning correlated with more absorption rather than scrutiny, 30% of post-quiz turns pasted quiz questions back to the very source being checked, and the assistant itself was almost never sycophantic and never conceded under pushback, creating a one-directional deference dynamic the authors formalize as a baseline-corrected Human Deference Index.

## Context
The AI safety and alignment literature has extensively studied sycophancy as a model-side failure mode, where LLMs tailor outputs to please users. This paper flips the frame to examine a complementary and arguably more dangerous failure mode: human over-trust in confidently delivered AI output, which is amplified by the very design choices (consistent tone, authoritative phrasing) that make assistants feel reliable. As LLMs become embedded in education, healthcare, and professional decision-making, understanding this human-side deference is critical because existing sycophancy benchmarks measure only one direction of the trust distortion.

## Implications
For practitioners building learning interfaces, the findings argue that trustworthiness must be treated as a property of the human-AI pair rather than the model alone, and that reliability should be made legible claim by claim through per-fact provenance, uncertainty signaling, and structured disagreement mechanisms. For evaluation frameworks, the authors contend that sycophancy assessments must measure both model-side and human-side deference, and that the Human Deference Index provides a quantitative baseline for detecting when users have stopped critically evaluating AI-generated information, a condition that silently degrades learning outcomes and decision quality across domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.31579v1)
