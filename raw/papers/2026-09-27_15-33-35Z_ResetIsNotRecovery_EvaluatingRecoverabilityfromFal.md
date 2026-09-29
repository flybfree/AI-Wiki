---
title: Reset Is Not Recovery: Evaluating Recoverability from False Conversational Context via Sycophancy Hysteresis
published: 2026-09-27T15:33:35Z
authors: Adi Shnaidman
url: http://arxiv.org/abs/2609.33672v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reset Is Not Recovery: Evaluating Recoverability from False Conversational Context via Sycophancy Hysteresis

## Abstract
Grounded language models are usually evaluated by adding relevant context, but multiturn dialogue also contains unsupported user claims that may contaminate later factual answers. We study post-pressure recoverability: whether a model returns to clean-context behavior after a user repeatedly advocates a wrong answer and then withdraws that pressure. We introduce a recovery-after-pressure protocol for multiple-choice factual dialogue and measure sycophancy hysteresis, the residual probability assigned to the user-advocated wrong answer relative to a clean-context counterfactual. Across seven instruction-tuned open-weight models and two factual benchmarks, ordinary reset often reduces but does not erase pressure-induced bias. History preserving repairs such as user retraction, system reset, and self-verification recover only 2-3/14 model-dataset pairs under the strict clean-restoration diagnostic, whereas operations that change the effective context are substantially more reliable; the two conditions that remove the pressure-bearing history entirely, fresh-context deletion and context truncation, recover 14/14. In an oracle trusted-evidence condition across fourteen model-dataset pairs, preserving the pressure-bearing history while adding benchmark-derived trusted evidence increases accuracy from 0.368 to 0.929, while wrong-answer following falls from 41.2% to 4.3%. Controls show that the effect is not explained by dialogue length, repeated confidence, plausible distractors, mere false-answer mention, or option-label inertia. These results suggest that faithful grounded dialogue requires evaluating which prior context should be treated as evidence and which should be removed or quarantined before answering.

## Metadata
- **Published**: 2026-09-27T15:33:35Z
- **Authors**: Adi Shnaidman
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33672v1)