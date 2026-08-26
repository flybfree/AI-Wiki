---
title: From Gradient-Boosted Trees to Deep Recommenders: Practical Lessons from Migrating a Production Customer Support Recommender
published: 2026-08-25T06:50:39Z
authors: Sonia Sharma, Jeyendran Balakrishnan, Shreya Rajpal, Swapnil Parekh, Nagaraj Janardhana, Andrew Mattarella-Micke
url: http://arxiv.org/abs/2608.24132v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Gradient-Boosted Trees to Deep Recommenders: Practical Lessons from Migrating a Production Customer Support Recommender

## Abstract
Product catalogs in fast-moving service businesses are shifting from static, independently priced SKUs toward dynamically bundled, discount-coupled offerings--a shift that strains the tree-based classifiers traditionally preferred for sparse and highly imbalanced data. These classifiers assume a fixed, slowly changing label space and struggle to incorporate multimodal signals such as tabular data and transcripts. We present the migration of a live, production conversational recommendation system from a gradient-boosted multiclass model to a pairwise-binary deep recommender. Because this system is critical to ecosystem growth initiatives and downstream features like dynamic pitching--surfacing the most relevant pitch text to a support agent in real time during a live customer conversation--maintaining live recommendation quality was a non-negotiable constraint. We detail the techniques that made this migration successful--reformulating recommendation as pairwise binary prediction to learn jointly from user and item features, and enhancing learned representations via negative sampling and noise injection. To efficiently incorporate long, live conversation context, we apply attention pooling over transcript chunks and benchmark it against TF-IDF and sentence-embedding baselines. Finally, we explore multiple architectures (including two-tower models, DeepFM, and their variants) and loss functions such as contrastive loss. Evaluating against a CatBoost baseline across all conversational stages, we demonstrate that our approach achieves parity at conversation beginning and outperforms at later conversational stages.

## Metadata
- **Published**: 2026-08-25T06:50:39Z
- **Authors**: Sonia Sharma, Jeyendran Balakrishnan, Shreya Rajpal, Swapnil Parekh, Nagaraj Janardhana, Andrew Mattarella-Micke
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24132v1)