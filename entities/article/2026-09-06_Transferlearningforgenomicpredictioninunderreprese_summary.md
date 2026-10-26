# Summary: Transfer learning for genomic prediction in underrepresented populations
Saved: 2026-10-25
Source: 2026-09-06_Transferlearningforgenomicpredictioninunderreprese.md
Model: qwen3.8-flash-next-iq3_xxs
[Original article](https://research.google/blog/transfer-learning-for-genomic-prediction-in-underrepresented-populations/)

---

## Summary
This article from Google Research details a study evaluating the efficacy of transfer learning in improving polygenic risk score (PRS) predictions for underrepresented populations, specifically Japanese individuals, using data from European cohorts. The researchers found that while leveraging large-scale European GWAS data initially enhances prediction accuracy for small target cohorts, this benefit diminishes and can even degrade performance as the sample size of the target population increases. This decline is particularly pronounced for traits with distinct genetic architectures between populations, highlighting the limitations of directly transferring models across diverse ancestries without careful consideration of cohort size and trait specificity.

## Key Takeaways
- Transfer learning from large European-centric GWAS datasets (such as the UK Biobank) can significantly improve PRS accuracy in small underrepresented target cohorts (like Biobank Japan), offering a cost-effective alternative to conducting de novo genome-wide association studies.
- The effectiveness of transfer learning is highly dependent on the sample size of the target population; as the number of individuals in the target cohort grows, the predictive advantage provided by European data decreases and may lead to reduced accuracy compared to using target-specific data alone.
- Genetic architecture differences, including variant allele frequencies and population structure, cause significant performance degradation when transferring models for traits with population-specific genetic mechanisms, indicating that a one-size-fits-all approach is insufficient for cross-population genomic prediction.

## Context
The broader context of this research addresses a critical disparity in genomic medicine: the overwhelming bias toward European cohorts in historical genome-wide association studies (GWAS). This bias results in poor clinical utility for non-European populations, limiting the adoption of polygenic risk scores in global healthcare systems. By investigating transfer learning as a method to bridge this gap, the study contributes to the field of AI-driven genomics by proposing practical guidelines for model training and data integration. It highlights the intersection of machine learning techniques, such as elastic net regularization, with biological constraints, emphasizing that algorithmic improvements must account for underlying biological heterogeneity across populations.

## Implications
This research has significant implications for the future of precision medicine and genomic prediction models. It suggests that healthcare systems cannot simply rely on existing large-scale European datasets to predict disease risk in diverse populations; instead, they must adopt nuanced strategies that balance external data with local cohort information. For AI developers and geneticists, this underscores the need for adaptive modeling techniques that dynamically adjust based on target population size and trait characteristics. Ultimately, these findings support the development of more equitable and accurate diagnostic tools, potentially accelerating the integration of genomic data into clinical decision-making for underrepresented groups while avoiding the prohibitive costs of large-scale de novo studies.
