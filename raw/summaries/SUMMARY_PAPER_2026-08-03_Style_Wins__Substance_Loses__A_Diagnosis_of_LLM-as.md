---
title: Style Wins, Substance Loses: A Diagnosis of LLM-as-Judge in Idea Generation
url: http://arxiv.org/abs/2608.01666v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_04-01-02Z_StyleWins_SubstanceLoses_ADiagnosisofLLM_as_Judgei.md
generated_at: 2026-08-03 23:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SciStyleBench, a three‑component benchmark to diagnose stylistic bias in LLM judges of scientific ideas. Experiments show that direct LLM judges are highly sensitive to writing style and perform poorly at distinguishing substance from presentation. The proposed module SciStyleExtractor reduces style bias while improving substance recognition. The study demonstrates that style‑driven bias can degrade both the fairness and accuracy of idea ranking.

## Key Takeaways
- Direct LLM judges remain strongly influenced by stylistic variations, producing a Style Bias Index of 0.566 that indicates high sensitivity to presentation.
- The Substance Recognition Rate improves from 0.504 to 0.759 after using SciStyleExtractor, showing better ability to detect scientific content.
- Adversarial Win Rate rises from 0.554 to 0.899, indicating more robust ranking of ideas despite style changes. These metrics provide quantitative evidence for why current LLM judges are unsuitable for high‑stakes scientific evaluation.

## Context
The rapid deployment of large language models as automated judges threatens the reliability of scientific idea evaluation, where superficial style could outweigh substantive merit. This work offers a systematic way to measure and mitigate such bias, aligning AI tools with rigorous scientific standards. As AI systems increasingly replace human reviewers, ensuring that evaluation criteria reflect true content is essential.

## Implications
For researchers developing LLM‑based assessment systems, this framework ensures that style does not compromise the detection of genuine scientific value. Practitioners can adopt SciStyleExtractor to create fairer evaluations, supporting trustworthy AI in research and industry. Adopting this approach will help maintain the integrity of automated research pipelines and reduce reliance on superficial cues.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01666v1)
