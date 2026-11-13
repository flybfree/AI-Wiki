---
title: Do Large Language Models Show Racial and Sex Bias in Pain Management? A Counterfactual Audit of GPT, Claude, Gemini, Llama, DeepSeek and Qwen
url: http://arxiv.org/abs/2611.14935v1
type: paper-summary
date: 2026-11-12
source_paper: 2026-11-11_02-35-53Z_DoLargeLanguageModelsShowRacialandSexBiasinPainMan.md
generated_at: 2026-11-12 21:41
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper conducts a comprehensive counterfactual audit examining whether large language models exhibit racial and sex bias when assessing acute pain cases, testing 17 models across 24 configurations including GPT-4.1 mini, Claude Haiku 4.5, Gemini 2.5 Flash, Llama, DeepSeek, and Qwen. The central finding is that no statistically significant differences in pain severity ratings or opioid recommendations survived multiple-comparison correction across any model or identity combination, with all pain-severity differences equivalent to zero within one point on a 0-10 scale. The authors conclude that while LLMs do not reproduce the well-documented racial disparities in human pain treatment, the enormous variability between models and across their own settings represents a far greater source of inconsistency than any identity-based bias.

## Key Takeaways
- Across 1,386 comparisons in Study 2 spanning 17 models with reasoning on and off at two precisions, zero comparisons survived false discovery rate correction, and every pain-severity difference was statistically equivalent to zero within one point on a 0-10 scale, with 237 of 238 Q-Pain comparisons equivalent within a quarter point, indicating no detectable racial or sex bias in pain assessment under these conditions.
- The reference White male patient received the high opioid dose in 6% to 93% of responses depending on the model, demonstrating that inter-model and intra-model variability vastly exceeds any between-patient differences, and that serving software, provider, and prompt format introduce noise that dwarfs any potential identity effect.
- The few differences that survived correction within a single model actually favoured Black patients, and the authors caution that opioid decisions were bounded less precisely than pain severity ratings, with Study 1 unable to exclude differences of about 20 percentage points, meaning the absence of detected differences does not constitute proof of their absence.

## Context
This study addresses a critical gap in AI fairness auditing by testing a far broader set of models, including open-weight and proprietary systems, using both explicit identity statements and name-based cues, and by pairing comparisons on the same sampling seed to isolate signal from stochastic noise. Prior audits typically tested only a handful of proprietary models, stated race explicitly, and failed to measure the models' own response instability, making it impossible to distinguish genuine bias from random variation. By introducing a noise floor and testing each deployed configuration separately, the authors establish a methodological standard that future clinical AI fairness studies should adopt.

## Implications
For healthcare practitioners and AI deployment teams, the findings suggest that current LLMs do not reproduce the racial and sex disparities documented in human clinical pain management, but the extreme inconsistency across models and settings poses its own patient-safety risk that demands configuration-specific auditing before clinical deployment. For the AI research community, the paper argues that fairness audits must use multiple names per demographic group, pair comparisons on identical seeds, report the noise floor explicitly, and test each deployed configuration rather than generalising across model families, since the variability introduced by serving infrastructure and prompt formatting can overwhelm any subtle identity effect.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.14935v1)
