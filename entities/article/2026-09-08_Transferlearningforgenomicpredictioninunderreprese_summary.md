# Summary: Transfer learning for genomic prediction in underrepresented populations
Saved: 2026-10-25
Source: 2026-09-08_Transferlearningforgenomicpredictioninunderreprese.md
Model: qwen3.8-flash-next-iq3_xxs
[Original article](https://research.google/blog/transfer-learning-for-genomic-prediction-in-underrepresented-populations/)

---

## Summary
This article presents a study evaluating the efficacy of transfer learning in improving polygenic risk score (PRS) predictions for underrepresented populations, specifically transferring data from European cohorts to Japanese individuals. The researchers found that while leveraging large-scale European genomic data initially boosts prediction accuracy for small target cohorts, this benefit diminishes as the sample size of the target population increases. Ultimately, the study highlights that transfer learning can degrade predictive performance for traits with distinct genetic architectures in larger local datasets, suggesting a need for nuanced approaches to cross-population model training.

## Key Takeaways
- Transfer learning from European-centric Genome-Wide Association Studies (GWAS) improves PRS accuracy for small underrepresented populations but becomes less effective or even detrimental as the target cohort’s sample size grows.
- The study utilized data from the UK Biobank (UKB) and Biobank Japan (BBJ) to test eight clinical traits, revealing that genetic architectures vary significantly across populations, which impacts the transferability of variant associations.
- Directly transferring variants identified in European cohorts to Japanese populations via methods like elastic net regression shows limited success for complex traits when local data becomes sufficient for independent modeling.

## Context
Polygenic risk scores are critical tools in precision medicine, yet their current clinical adoption is hindered by a historical bias toward European genomic data. This bias results in severe accuracy drops when these models are applied to non-European populations due to differences in population structure and variant allele frequencies. Conducting new, large-scale GWAS for every population is cost-prohibitive for most healthcare systems, making transfer learning from existing large datasets a proposed solution to bridge this equity gap.

## Implications
This research provides empirical guidelines for how cross-population GWAS and PRS model training should be conducted to optimize predictive performance. It suggests that while transfer learning is a valuable tool for bootstrapping predictions in data-poor settings, it is not a universal fix for genomic health disparities. As local datasets grow, healthcare systems must prioritize developing population-specific models rather than relying on transferred European data, particularly for traits with high heritability or complex genetic architectures. This finding underscores the urgent need for diverse genomic datasets to ensure equitable and accurate clinical decision-making across all populations.
