---
title: Isolating a Language Model's Judgment with a Label-Free Subspace
url: http://arxiv.org/abs/2610.21256v1
type: paper-summary
date: 2026-10-15
source_paper: 2026-10-15_04-49-49Z_IsolatingaLanguageModel_sJudgmentwithaLabel_FreeSu.md
generated_at: 2026-10-15 22:22
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether changes in a language model's final output under different instructions reflect a genuine shift in internal judgment or merely a failure to express a stable judgment. The authors discover that instruction-induced differences in hidden-state vectors concentrate in a low-dimensional "expression subspace," which can be identified without any benchmark labels. By projecting this subspace out of a linear predictor, they recover a reliable internal judgment that remains stable across unseen instruction phrasings, even when the model's own final answers degrade.

## Key Takeaways
- The authors demonstrate that when the same input is processed under different instruction formats, the resulting hidden-state vectors differ primarily within a low-dimensional subspace they term the "expression subspace." This subspace can be identified in a fully label-free manner, meaning no ground-truth annotations are required to isolate it, making the method broadly applicable across tasks such as correctness evaluation, entailment, and safety classification.
- After removing the expression subspace's contribution from a linear predictor, the resulting "isolated judgment" generalizes to instructions never used during subspace identification. In negated-judgment experiments, the isolated predictor's AUROC jumps from 0.504 to 0.825 for entailment and from 0.480 to 0.891 for safety, showing that the model's internal assessment was present all along but was being masked by expression-level noise.
- The authors find that the underlying judgment signal is readable in earlier transformer layers, before the expression subspace begins to interfere with the predictor. This layer-wise analysis suggests that judgment formation and expression formatting are separable computational processes within the model, and that earlier-layer representations preserve a cleaner signal than final-layer outputs.

## Context
This work sits at the intersection of mechanistic interpretability and robust evaluation of large language models. A persistent challenge in AI safety and evaluation research is that prompting strategies, instruction templates, and output formatting can dramatically alter a model's reported answers, raising concerns about whether models truly "understand" or merely pattern-match to surface instructions. Prior work on representation engineering and activation steering has attempted to control model behavior through interventions in hidden states, but typically requires labeled data or task-specific supervision. This paper advances the field by showing that a purely unsupervised, geometry-based approach can disentangle judgment from expression, offering a new diagnostic tool for probing model internals without relying on benchmark annotations.

## Implications
For practitioners building evaluation pipelines, this method provides a way to audit whether a model's internal assessment is stable regardless of how the question is phrased, which is critical for safety-critical deployments where instruction sensitivity can silently flip a model's output. For the research community, the finding that judgment is accessible in earlier layers before expression interference suggests that interpretability tools and probing classifiers should target intermediate representations rather than final hidden states. Industry teams deploying LLMs for content moderation, fact-checking, or compliance review could leverage label-free subspace isolation to build more robust internal monitors that do not require retraining or re-annotation when prompt templates change.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.21256v1)
