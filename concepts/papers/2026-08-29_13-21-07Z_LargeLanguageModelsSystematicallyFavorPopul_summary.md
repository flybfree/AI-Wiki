# Summary: 2026-08-29_13-21-07Z_LargeLanguageModelsSystematicallyFavorPopularOptio.md
Saved: 2026-08-31 20:43
Source: 2026-08-29_13-21-07Z_LargeLanguageModelsSystematicallyFavorPopularOptio.md
Model: None

---

## Summary  
The paper investigates how large language models exhibit a systematic tendency to favor popular but incorrect multiple‑choice options, even when those answers are wrong, which we term popularity bias and is linked to confidence miscalibration. To isolate this phenomenon the authors introduce PopMCQ, a benchmark that varies option popularity while keeping the correct answer fixed across six controlled strategies. Experiments on 22 open‑source LLMs ranging from 0.5 B to 32 B parameters demonstrate that under strong popularity pressure models choose wrong popular answers about two‑thirds of the time. The study proposes PopDebias, a lightweight inference‑time correction that removes the popularity prior without fine‑tuning or label‑dependent testing.  

## Key Contributions  
- Finding 1: LLMs systematically favor popular answer options even when they are incorrect, leading to confidence miscalibration.  
- Finding 2: PopMCQ benchmark with six controlled strategies isolates popularity bias across diverse model sizes and evaluation settings.  
- Finding 3: PopDebias inference‑time correction removes the popularity prior without fine‑tuning, achieving up to a 54.1 percentage point accuracy gain under strong pressure.  

## Methodology  
The authors designed a benchmark by fixing the correct answer while varying the popularity of distractors using six controlled strategies; they measured model choices and confidence scores across 22 open‑source LLMs ranging from 0.5 B to 32 B parameters, employing PopDebias which fits a small calibration split and applies a simple subtraction at inference time.  

## Results  
Under the most adversarial setting where all distractors are more popular than the correct answer, models choose wrong popular options 66 % of the time; applying PopDebias reduces this to under 20 %, delivering accuracy gains up to 54.1 percentage points across the model range, with consistent improvements measured on a held‑out test set.  

## Significance  
This work reveals a systematic vulnerability in LLM evaluation that could mislead rankings and research, prompting developers to adopt lightweight debiasing methods; by providing an open benchmark (PopMCQ) and a practical correction (PopDebias), the study advances responsible AI deployment and improves fairness of MCQ assessment.  

## Related Concepts  
popularity bias, confidence miscalibration, multiple‑choice question evaluation, inference‑time correction, calibration split, popularity prior removal.
