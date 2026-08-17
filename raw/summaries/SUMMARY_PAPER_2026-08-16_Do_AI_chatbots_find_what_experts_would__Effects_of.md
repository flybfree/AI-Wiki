---
title: Do AI chatbots find what experts would? Effects of model, user role, and sample size on study retrieval for medical questions
url: http://arxiv.org/abs/2608.13786v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-13_21-38-01Z_DoAIchatbotsfindwhatexpertswould_Effectsofmodel_us.md
generated_at: 2026-08-16 21:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This study compares three large language model chatbots on their ability to retrieve primary clinical studies from the Cochrane Database of Systematic Reviews when answering medical questions. The results show that retrieval rates vary by model and user role, with ChatGPT performing best but still missing many included studies and citing some excluded ones.

## Key Takeaways
- Retrieval recall for included studies ranged widely: ChatGPT achieved 63.1 % while Claude Sonnet 5 reached only 37.0 % and Gemini 3.1 Pro 17.3 %, indicating strong model‑dependent performance differences.
- The researcher role produced higher recall than clinician or patient roles, suggesting that the expertise of the prompting user influences which studies are selected.
- Sample size was the sole independent predictor of retrieval success, with each unit increase in log sample size raising odds of correct citation by 1.80 times.

## Context
The rapid adoption of AI chatbots for clinical information retrieval raises questions about their reliability compared to human experts who curate systematic reviews. This work provides empirical evidence that current models can retrieve a subset of expert‑identified studies but are not yet consistent or unbiased in their selection process.

## Implications
For clinicians and researchers, reliance on AI‑generated citations may lead to incomplete evidence bases if the model’s recall is low. Practitioners should verify retrieved studies and consider human oversight, especially when sample size influences retrieval quality.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13786v1)
