---
title: Identically Trained Language Models Break on Different Jailbreaks
url: http://arxiv.org/abs/2610.34074v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-25_05-30-02Z_IdenticallyTrainedLanguageModelsBreakonDifferentJa.md
generated_at: 2026-10-26 23:27
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates whether jailbreak vulnerability patterns in language models are determined by pretraining data or by the specific pretraining run (seed). By training 150 models across 25 data recipes, 3 pretraining seeds, and 2 post-training seeds at 1B parameters, the authors demonstrate that which jailbreaks break a checkpoint depends far more on the specific pretraining run than on the training data itself. Two copies of the same pretraining run correlate at 0.984 in per-prompt non-refusal rates, while changing only the pretraining seed drops correlation to 0.811, and changing the data recipe drops it only marginally further to 0.779.

## Key Takeaways
- Pretraining run identity dominates over data recipe: changing the pretraining seed (same data, different random initialization) causes a much larger drop in jailbreak vulnerability correlation (0.984 → 0.811) than switching to an entirely different data recipe (0.811 → 0.779), indicating that stochastic training dynamics, not data composition, primarily determine which jailbreaks succeed.
- Best-of-91 attack templates transfer poorly across pretraining seeds but well across post-training seeds: the optimal jailbreak attack found on one checkpoint remains optimal after a new pretraining seed in only 27% of model pairs, versus 67% after a new post-training seed, meaning safety evaluation results are not reproducible across independent pretraining runs.
- Each pretraining run leaves a measurable fingerprint: across 3,211 prompts, a model's per-prompt non-refusal rates can identify its exact pretraining run among all 75 runs with 100% accuracy, and even a random subset of just 50 prompts achieves 98% identification accuracy, confirming that pretraining runs imprint a persistent, detectable signature on model behavior.

## Context
This work challenges a foundational assumption in AI safety evaluation: that jailbreak benchmarks measure properties of a model's training data and safety fine-tuning. The broader field treats a single checkpoint's jailbreak vulnerabilities as representative of its data recipe, but this paper shows that the specific random seed and training trajectory of pretraining introduce idiosyncratic behavioral signatures that dominate over data-level differences. The finding holds across 25 diverse data recipes and at multiple model scales (150M, 300M, 1B parameters), suggesting it is a general phenomenon rather than an artifact of a particular setup.

## Implications
For practitioners building and evaluating safety guardrails, this means that jailbreak attack templates optimized on one checkpoint cannot be assumed to transfer to another model trained on the same data but with a different seed, undermining the reproducibility of safety evaluations and the reliability of red-teaming pipelines. For the industry, it implies that safety certification processes must account for pretraining-run variance rather than treating data recipes as the sole determinant of vulnerability, and that fingerprinting techniques could serve as a tool for auditing which specific training run produced a given model. Researchers designing jailbreak benchmarks should consider multi-seed evaluation protocols to avoid drawing conclusions about data-level safety properties from single-run artifacts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.34074v1)
