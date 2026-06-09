# Summary: 2026-05-05_17-57-19Z_Safetyandaccuracyfollowdifferentscalinglawsinclini.md
Saved: 2026-05-07 22:08
Source: 2026-05-05_17-57-19Z_Safetyandaccuracyfollowdifferentscalinglawsinclini.md
Model: None

---

## Summary
This paper argues that clinical LLM accuracy and safety do not improve in lockstep as systems are scaled. Using a radiology-focused benchmark and a large model sweep, the authors show that evidence quality and retrieval design matter more than raw context or extra inference compute for avoiding dangerous errors.

## Key Takeaways
- Introduces SaFE-Scale and RadSaFE-200 for safety-oriented clinical evaluation.
- Evaluates 34 locally deployed LLMs under six prompting and retrieval conditions.
- Clean evidence substantially improves accuracy and reduces high-risk errors and contradictions.
- Standard RAG, agentic RAG, and max-context prompting do not fully close the safety gap.

## Context
The study examines a medical setting where rare but severe mistakes matter more than average benchmark accuracy. It compares closed-book prompting, evidence-based prompting, and retrieval strategies to assess both correctness and safety.

## Implications
The results imply that safer clinical deployment requires careful evidence construction, not just larger models or longer contexts. This supports treating safety as a deployment property shaped by system design choices and worst-case behavior.

## Original Reference
- Title: Safety and accuracy follow different scaling laws in clinical large language models
- Authors: Sebastian Wind, Tri-Thien Nguyen, Jeta Sopa, Mahshad Lotfinia, Sebastian Bickelhaup, Michael Uder, Harald Köstler, Gerhard Wellein, Sven Nebelung, Daniel Truhn, Andreas Maier, Soroosh Tayebi Arasteh
- URL: http://arxiv.org/abs/2605.04039v1
- Published: 2026-05-05T17:57:19Z