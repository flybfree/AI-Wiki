---
title: Modeling Discourse Profiles in Climate Misinformation Discourse
url: http://arxiv.org/abs/2610.24489v1
type: paper-summary
date: 2026-10-19
source_paper: 2026-10-17_06-15-44Z_ModelingDiscourseProfilesinClimateMisinformationDi.md
generated_at: 2026-10-19 21:43
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces a novel approach to climate misinformation detection by constructing "discourse profiles" from recurring rhetorical patterns found across comments and threads in a large-scale TikTok climate discourse dataset. Rather than classifying individual comments in isolation, the authors cluster comments into shared rhetorical patterns and integrate these profiles into fine-grained misinformation classifiers via a late-fusion architecture, demonstrating significant macro-F1 improvements over text-only baselines for several model representations.

## Key Takeaways
- Discourse profiles, defined as clusters of recurring rhetorical patterns across comments and threads, capture a structural property of online climate misinformation that text-only classifiers miss. By incorporating these profiles into classifiers using a late-fusion architecture, the authors achieve statistically significant macro-F1 improvements over bag-of-words, TF-IDF, and MPNet baselines under video-disjoint evaluation across three training seeds, confirming that rhetorical context materially aids misinformation detection.
- The results are model-dependent: while simpler representations benefit substantially from discourse-profile augmentation, RoBERTa-large shows only a positive mean improvement with substantially greater variability, and the difference fails to reach statistical significance. This suggests that very large pretrained language models may already encode some discourse-level information internally, limiting the marginal benefit of explicit profile features.
- Beyond classification performance, discourse profiles shape how misinformation is received and propagated. Discourse-profile-conditioned language model agents exhibit misinformation acceptance patterns that align with profile-level misinformation prevalence in the ClimateDisc dataset, and the relationship between misinformation prevalence and engagement persistence varies across dominant discourse profiles, revealing that rhetorical framing influences both belief formation and viral spread.

## Context
This work sits at the intersection of misinformation detection, discourse analysis, and computational social science, addressing a well-known limitation in the field: most misinformation classifiers operate on isolated text units and ignore the conversational and rhetorical scaffolding that sustains misinformation in online communities. By leveraging a large-scale TikTok dataset and introducing a clustering-based discourse profile framework, the paper bridges natural language processing methods with communication theory, offering a template for how structural discourse features can be operationalized as machine-learning features.

## Implications
For practitioners building misinformation detection systems on social platforms, this research suggests that incorporating discourse-level features—such as recurring rhetorical patterns and thread-level context—can yield meaningful gains over purely text-based pipelines, particularly for lighter-weight models. For platform moderators and policy researchers, the finding that discourse profiles shape misinformation reception and engagement persistence implies that interventions targeting specific rhetorical framings may be more effective than blanket content moderation, guiding the design of more nuanced platform governance strategies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.24489v1)
