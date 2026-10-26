# Summary: Transfer learning for genomic prediction in underrepresented populations
Saved: 2026-10-25
Source: 2026-09-10_Transferlearningforgenomicpredictioninunderreprese.md
Model: qwen3.8-flash-next-iq3_xxs
[Original article](https://research.google/blog/transfer-learning-for-genomic-prediction-in-underrepresented-populations/)

---

## Summary
This article details a study by Google Research evaluating the efficacy of transfer learning in polygenic risk scores (PRS) for genomic prediction, specifically focusing on transferring models from European cohorts to underrepresented populations like those in Biobank Japan. The researchers found that while transfer learning initially improves prediction accuracy for small target cohorts, this benefit diminishes or reverses as the target population's sample size increases, particularly for traits with distinct genetic architectures. Consequently, the study provides empirical guidelines suggesting that large-scale de novo GWAS in target populations are necessary to achieve optimal predictive performance, rather than relying solely on transferred European-centric models.

## Key Takeaways
- Transfer learning from large European datasets (UK Biobank) to smaller non-European cohorts can initially boost genomic prediction accuracy, offering a cost-effective interim solution for underrepresented populations.
- The effectiveness of transfer learning is highly dependent on the sample size of the target population; as the target cohort grows larger, transferred models degrade in accuracy compared to models trained directly on the target population's data.
- Genetic architecture differences, including variant allele frequencies and population structure, significantly impact cross-population prediction performance, making direct transfer of PRS from European cohorts unreliable for complex traits without local calibration.

## Context
The broader context of this research addresses a critical inequity in AI-driven healthcare: the historical bias of Genome-Wide Association Studies (GWAS) toward European populations. This bias has resulted in Polygenic Risk Scores that perform poorly when applied to non-European individuals, limiting their clinical utility and exacerbating health disparities. As healthcare systems increasingly adopt AI for personalized medicine, the inability to accurately predict disease risk across diverse ancestries represents a significant barrier to equitable care. Conducting de novo GWAS is often cost-prohibitive, making transfer learning a tempting but potentially flawed shortcut that this study critically examines.

## Implications
This research has profound implications for the development of fair and robust AI models in genomics. It suggests that simply scaling up existing European-centric datasets is insufficient for global health applications; instead, diverse data collection must be prioritized to build accurate models for all populations. For industry stakeholders, this highlights the need for strategic investment in large-scale genomic studies within underrepresented groups rather than relying on algorithmic transfer techniques alone. Furthermore, it underscores that AI model performance metrics must be evaluated across diverse demographic slices to prevent systematic biases from embedding themselves into clinical decision-support tools, ensuring that AI advancements do not inadvertently widen existing health gaps.
