---
title: Successive Training Stages and Large Language Model Persuasion: Effects of Misalignment, Supervised Fine-Tuning, and Preference Optimization
url: http://arxiv.org/abs/2610.09964v1
type: paper-summary
date: 2026-10-07
source_paper: 2026-10-07_12-36-18Z_SuccessiveTrainingStagesandLargeLanguageModelPersu.md
generated_at: 2026-10-07 22:21
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This study investigates how three successive post-training stages—misalignment via supervised fine-tuning on conspiracy data, additional persuasive SFT on argumentative data, and Identity Preference Optimization (IPO)—affect the persuasiveness of large language models on human attitudes. Through a randomized experiment with 835 participants exposed to personalized texts on 10 divisive political issues, the authors found that targeted supervised training on persuasive data significantly increases LLM persuasiveness, while preference optimization provides no meaningful additional benefit beyond that supervised training.

## Key Takeaways
- A significant condition-by-baseline-attitude interaction (F(4, 825) = 5.33, p < .001) demonstrated that the effect of training stages on attitude change depends critically on participants' initial attitudes, meaning that persuasion outcomes are not uniform across all individuals but are moderated by where a person already stands on a given issue.
- Persuasive supervised fine-tuning on argumentative data produced a meaningfully greater attitude change than conspiracy training alone (Cohen's d = 0.30), indicating that the content and structure of the training data—specifically argumentative framing rather than mere conspiracy content—play a decisive role in how effectively an LLM shifts reader attitudes.
- Identity Preference Optimization (IPO), a preference-optimization method applied after persuasive SFT, yielded a negligible additional effect (d = 0.03), and GPT-4 did not differ from neutral text (d = -0.01), suggesting that preference-based alignment techniques do not enhance persuasiveness beyond what targeted supervised training already achieves, and that general-purpose frontier models are not inherently more persuasive than baseline text.

## Context
As large language models become increasingly embedded in information ecosystems, understanding how their post-training pipelines shape their capacity to influence human beliefs is essential for AI safety and governance research. This paper addresses a gap in the literature by isolating the contributions of distinct training stages—misalignment, persuasive fine-tuning, and preference optimization—rather than treating model behavior as a monolithic outcome, thereby offering a more granular account of how alignment and misalignment processes interact to produce persuasive outputs.

## Implications
For AI safety practitioners and model developers, these findings suggest that the persuasiveness of a language model is primarily determined by the nature of its supervised fine-tuning data rather than by subsequent preference-optimization steps, which means that auditing and controlling training data composition is a more effective intervention point than tuning alignment objectives. For regulators and platform operators, the results underscore the need to scrutinize not only whether a model has been fine-tuned but what specific argumentative or persuasive content was used during that fine-tuning, since the same model architecture can produce markedly different levels of attitude influence depending on its training pipeline.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.09964v1)
