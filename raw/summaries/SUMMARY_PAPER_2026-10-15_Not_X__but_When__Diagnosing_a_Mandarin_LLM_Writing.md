---
title: Not X, but When: Diagnosing a Mandarin LLM Writing Tic through Contextual Appropriateness
url: http://arxiv.org/abs/2610.22249v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_17-22-11Z_NotX_butWhen_DiagnosingaMandarinLLMWritingTicthrou.md
generated_at: 2026-10-15 23:03
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether recurring linguistic patterns in Mandarin LLM output constitute problematic "tics" or serve legitimate communicative functions, focusing specifically on the corrective construction "bushi X, ershi Y" (not X, but Y). The authors develop a Gricean pragmatics-based decision tree to classify model uses as substantive, optional, or defective, finding that while models use the construction 2.5 to 9.2 times more densely than human writers, the vast majority of uses are grammatically correct but contextually unnecessary, revealing a fundamental gap in appropriateness rather than correctness.

## Key Takeaways
- The paper introduces a novel evaluation framework grounded in Gricean pragmatics and corrective negation theory, classifying uses of "bushi X, ershi Y" by testing whether the context makes X a live alternative and whether rejecting X is genuinely informative. Of 307 annotated model uses, only 1.30% were defective (incorrect), while 52.8% were optional (correct but unneeded), demonstrating that models fail far more often in contextual appropriateness than in grammatical correctness.
- Five commercial LLMs deploy this construction 2.5 to 9.2 times more densely than a human reference corpus, and the problem is reinforced by the training and evaluation pipeline: reward models preferentially score outputs containing the construction even over quality-matched variants, LLM judges favor it even when context does not license it, and both supervised fine-tuning and preference optimization tend to increase its frequency in open-weight models.
- The central insight is that diagnosing a "tic" requires evaluating when an expression is called for, not merely whether it is grammatically valid. This reframes the study of model writing habits from surface-level pattern detection to a deeper assessment of communicative competence and contextual judgment.

## Context
This work sits at the intersection of computational linguistics, pragmatic theory, and LLM evaluation methodology. As the AI community increasingly relies on reward models, LLM-as-judge pipelines, and preference optimization to shape model behavior, understanding how these systems inadvertently amplify stylistic habits is critical. The paper addresses a gap in the literature: while much attention has been paid to detecting machine authorship through recurring phrases, the appropriateness of those phrases in context remains largely unexamined, particularly for non-English languages where discourse conventions differ substantially.

## Implications
For practitioners building and evaluating LLMs, this research suggests that reward models and preference optimization pipelines may be actively reinforcing inappropriate stylistic patterns rather than merely reflecting them, meaning that standard alignment techniques could worsen the very "tics" they are meant to avoid. For the broader field, the paper advocates shifting evaluation criteria from correctness to contextual appropriateness, urging developers to build models that are attentive to when an expression is warranted rather than simply whether it is grammatically permissible. This has practical consequences for content generation, translation, and any application where natural-sounding, contextually sensitive Mandarin output is required.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.22249v1)
