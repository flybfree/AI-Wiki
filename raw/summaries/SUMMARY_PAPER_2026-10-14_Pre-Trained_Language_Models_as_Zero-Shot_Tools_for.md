---
title: Pre-Trained Language Models as Zero-Shot Tools for Social Science Research
url: http://arxiv.org/abs/2610.19048v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-13_18-43-04Z_Pre_TrainedLanguageModelsasZero_ShotToolsforSocial.md
generated_at: 2026-10-14 20:57
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper demonstrates that pre-trained language models can perform record linkage and demographic inference from names with high accuracy without any task-specific training data. The author introduces EnsembleLink, a hybrid algorithm combining pre-trained embeddings with string-based scorers for record linkage, and shows that large language models outperform traditional name-based ethnicity classifiers like BISG on U.S. voter files while extending to religious, caste-based, and non-U.S. ethnic categories. The central finding is that the world knowledge already encoded in pre-training is sufficient for these tasks, making labeled training data largely unnecessary.

## Key Takeaways
- EnsembleLink combines pre-trained embeddings with string-based scorers to retrieve candidate matches and identify likeliest pairs, matching or exceeding prior record-linkage methods while generalizing across scripts and formats that traditional approaches cannot handle, eliminating the need for labeled training data.
- Large language models achieve up to 83.8% accuracy on ethnicity inference from names in U.S. voter files, surpassing the 78.0% accuracy of the widely used name-supplemented BISG classifier, and open-weight models provide reproducible implementations that approach this performance.
- LLMs extend demographic inference beyond binary racial categories to religious, caste-based, and other ethnic group memberships outside the United States, and their use reduces bias in downstream estimates of geographic racial gaps, suggesting that pre-trained world knowledge encodes the information these tasks require while task-specific labels add comparatively little additional signal.

## Context
Social science research has long relied on supervised classifiers trained on labeled datasets for tasks like record linkage and name-based demographic classification, approaches that are costly to build, brittle across scripts and regions, and often limited to narrow demographic categories. This paper sits within the broader trend of leveraging large-scale pre-trained models as general-purpose tools, showing that the vast multilingual and multicultural knowledge absorbed during pre-training can substitute for domain-specific annotation pipelines. It challenges the assumption that social science tasks inherently require bespoke labeled training data.

## Implications
For social scientists, demographers, and public-health researchers, this work lowers the barrier to conducting cross-national and multi-ethnic demographic analyses without investing in expensive annotation efforts, potentially democratizing access to tools that were previously limited to well-funded institutions. For practitioners in record linkage and identity resolution, EnsembleLink offers a script-agnostic, format-agnostic approach that could reduce error rates in administrative data matching. The finding that pre-training encodes sufficient world knowledge also raises important questions about model bias, reproducibility, and governance when LLMs are deployed as default tools in sensitive demographic research.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.19048v1)
