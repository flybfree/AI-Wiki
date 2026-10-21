---
title: Forty Questions: Identifying a Language Model from One-Word Answers
url: http://arxiv.org/abs/2610.28281v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-20_14-33-56Z_FortyQuestions_IdentifyingaLanguageModelfromOne_Wo.md
generated_at: 2026-10-20 22:40
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces a method for identifying the specific language model behind an API endpoint by analyzing its one-word answers to simple everyday questions such as "Name a sound" or "Name a poet." By building statistical profiles of model responses across 40 questions, the author demonstrates that a model can be identified with 92.5% accuracy on a panel of 94 models, far exceeding the 1.1% chance baseline. The method also reveals practical discrepancies in model serving, including mislabeled models and hidden billing practices across commercial API providers.

## Key Takeaways
- The core technique constructs a "profile" for each model recording the frequency with which it produces each possible answer to each question, then attributes new answers to the model most likely to have generated them. Across 94 models, 40 carefully chosen questions achieve 92.5% exact identification accuracy, compared to only 1.1% expected by random chance, demonstrating that even trivial one-word responses carry a strong statistical fingerprint unique to each model.
- Applying the method to 96 real-world API endpoints on OpenRouter covering 13 open-source models, 92 correctly identified as the model they claim to be. However, the investigation uncovered concrete serving anomalies: one model serves Gemma 4 under the name "Llama 4 Maverick," confirmed by the model self-identifying as Gemma 4 and being billed at Gemma 4's token counts. A system prompt applied to an endpoint reduces identification accuracy by 6 to 16 percentage points, showing that prompt engineering can partially mask a model's behavioral signature.
- Billing records expose hidden context injection practices. Grok 4.7 is billed 1,247 input tokens for a one-line question that costs GPT-4o only 12 tokens, and five models state the current date without being billed for the injected context. These findings reveal that API providers add undisclosed system context that inflates costs and alters model behavior in ways invisible to the end user.

## Context
As the AI ecosystem proliferates with hundreds of models served through aggregators like OpenRouter, DeepInfra, and proprietary APIs, users increasingly lack transparency about which model actually powers their requests. This paper addresses a gap in model auditing and provenance verification, offering a low-cost behavioral fingerprinting technique that complements traditional metadata-based identification. It sits at the intersection of model forensics, API transparency, and the growing concern over model mislabeling in commercial serving pipelines.

## Implications
For practitioners and developers relying on API aggregators, this method provides a practical, cents-per-endpoint tool to verify model identity, detect mislabeled endpoints, and uncover hidden billing practices such as undisclosed context injection. For the broader field, it underscores the need for independent auditing mechanisms as model-serving infrastructure becomes more opaque, and it highlights that even the most trivial outputs—single-word answers—encode statistically rich signatures that can serve as a lightweight integrity check across the rapidly expanding landscape of commercial and open-source model deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.28281v1)
