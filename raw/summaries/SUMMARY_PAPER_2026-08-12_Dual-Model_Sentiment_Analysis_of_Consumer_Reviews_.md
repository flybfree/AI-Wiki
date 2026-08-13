---
title: Dual-Model Sentiment Analysis of Consumer Reviews in the Retail Coffee Sector Using Machine Learning and Deep Learning Approaches
url: http://arxiv.org/abs/2608.12007v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_12-44-27Z_Dual_ModelSentimentAnalysisofConsumerReviewsintheR.md
generated_at: 2026-08-12 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper compares classical machine learning and deep learning methods for sentiment analysis of Starbucks customer reviews collected from ConsumerAffairs. The study finds that Bidirectional LSTM outperforms other models in accuracy and generalization, while class imbalance reduces positive recall across classifiers.

## Key Takeaways
- SVM achieved the highest accuracy at 91 percent among machine‑learning classifiers, indicating its effectiveness for this binary sentiment task.
- Deep learning’s Bidirectional LSTM delivered the strongest performance overall, showing robust handling of sequential review text and better unseen data generalization.
- The inherent class imbalance toward negative sentiment negatively impacted positive recall across several models, highlighting a preprocessing challenge.

## Context
Sentiment analysis remains central to consumer experience analytics, especially in service sectors where brand perception drives decisions. This work contributes to the growing body of research comparing traditional ML with deep learning for real‑world review data, offering insights into model suitability and performance trade‑offs.

## Implications
Practitioners can leverage SVM or Bidirectional LSTM based on their resource constraints and data characteristics. The study underscores that effective preprocessing is essential to mitigate class imbalance, ensuring reliable sentiment scores for retail coffee analytics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12007v1)
