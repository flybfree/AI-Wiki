---
title: AI/ML Foundations Lesson 03 - Data as the Foundation of Learning
date: 2026-05-06
status: draft
tags: [lesson, data, machine-learning, foundations, training-data]
source_pages:
  - ai-ml-foundations-syllabus.md
  - raw/articles/2026-05-06_MachineLearningArchitecture_WhatItIs_Components_Ty.md
  - raw/articles/2026-04-25_Architectures_for_Machine_Learning___Springer_Natu.md
  - raw/articles/2026-04-29_Top_Machine_Learning_Architectures_Explained_-_BMC.md
  - raw/articles/2026-05-07_Data_Foundation_Web_Sources.md
---

## Summary

Placeholder summary — please add a concise summary.


# Lesson 3: Data as the Foundation of Learning



**Source**: [Original Article](https://example.com/placeholder)

## Semantic links
- [[concepts/ai-foundations/ai-ml-foundations-lesson-01-ai-machine-learning-and-deep-learning.md|AI/ML Foundations Lesson 01 - AI, Machine Learning, and Deep Learning]] — 3 title terms overlap; shared tags: foundations, lesson, machinelearning; 5 backlinks
- [[concepts/ai-foundations/ai-ml-foundations-lesson-02-how-an-ml-system-works.md|AI/ML Foundations Lesson 02 - How an ML System Works]] — 2 title terms overlap; shared tags: foundations, lesson, machinelearning; 4 backlinks
- [[concepts/ai-foundations/ai-ml-foundations-lesson-04-supervised-learning-learning-from-labels.md|AI/ML Foundations Lesson 04 - Supervised Learning: Learning from Labels]] — 3 title terms overlap; shared tags: foundations, lesson; 5 backlinks

## Navigation
- Previous: [[ai-ml-foundations-lesson-02-how-an-ml-system-works.md|Lesson 2: How an ML System Works]]
- Landing page: [[ai-ml-foundations-landing-page.md|AI/ML Foundations Landing Page]]
- Next: [[ai-ml-foundations-lesson-04-supervised-learning-learning-from-labels.md|Lesson 4: Supervised Learning: Learning from Labels]]


Time budget: 90 to 120 minutes

## Lesson overview

Machine learning is only as good as the data it learns from. A model does not discover truth on its own; it learns patterns from examples, and those examples come from data. If the data is incomplete, biased, noisy, stale, or badly labeled, the model can still learn, but it may learn the wrong thing.

To keep the lesson grounded, we will use one running example: a company building a customer churn model, which predicts which customers are likely to leave. We will follow that data through the full pipeline, from collection to versioning, so each step feels connected to the next.

This matters because people often focus on the model first. In real projects, the more important question is usually: what data are we feeding into the system, where did it come from, how clean is it, how was it transformed, and how was it split?

## Learning goals

By the end of this lesson, you should be able to:

- explain why data quality strongly affects model performance
- describe the steps of data collection, cleaning, transformation, integration, sampling, and splitting
- distinguish training, validation, and test data
- explain why representative data matters
- understand why data versioning supports reproducibility

## 1) Data is what the model learns from

Machine learning is not magic. It is pattern learning. A model learns from examples, and those examples come from data.

For a churn model, that data might include billing history, product usage, support tickets, and past cancellation records. If those records are incomplete or misleading, the model can still find patterns, but the patterns may not reflect reality. A model trained on weak data may look impressive in a notebook and still fail when it meets real customers.

That is why data work is not a side task. It is the starting point of learning itself.

## 2) Collection brings the real world into the system

Data collection is the step where the team gathers information from sources such as databases, application programming interfaces (APIs), sensors, data lakes, or external datasets. A data lake is a large storage area that keeps raw data in its original form until the team is ready to use it.

For the churn model, collection might pull customer billing records from one database, product usage logs from another system, and support interactions from a ticketing tool. The important question is not just whether the data exists. It is whether the collected data reflects the real world well enough for the model to learn from it.

That idea is called representativeness. Representative data looks enough like the future environment that the model will not be surprised when it is used in production. If the training data only captures one kind of customer behavior, the model may work well on that narrow slice and fail everywhere else.

Different jobs also need different ingestion patterns. Batch ingestion moves data in chunks on a schedule. Streaming ingestion and real-time ingestion bring in data continuously or with very low delay. Change data capture, or CDC, means tracking only the changes made to existing records instead of copying the whole dataset again.

For churn prediction, batch ingestion is often enough because customer behavior usually changes over hours or days, not seconds. A live fraud system would need fresher data, but churn is usually a slower-moving problem.

## 3) Cleaning removes obvious problems

Raw data is usually messy. It can contain missing values, typos, duplicates, inconsistent formats, outliers, or broken records. Cleaning is the process of finding and fixing those problems before the model sees them.

This step matters because machine learning systems do not automatically know which values are wrong. If the pipeline does not catch the error, the model will happily learn from it.

In the churn example, one field might contain “NY” in some rows and “New York” in others. Another field might have blank values where the customer never entered their usage history. Cleaning means normalizing those inconsistencies so the model sees one coherent dataset instead of a pile of mixed signals.

Cleaning does not mean making every record perfect. It means removing the kinds of noise that would distort learning or make evaluation less trustworthy.

## 4) Transformation turns raw data into usable input

Transformation reshapes raw data into a format the model can use. That can include encoding categories, scaling values, parsing text, and extracting features. Encoding categories means converting labels such as “small,” “medium,” and “large” into a numerical representation. Scaling values means putting numeric fields onto comparable ranges so one large number does not dominate the learning process. Feature extraction means turning raw data into useful input variables, or features.

For the churn model, transformation might turn timestamps into “days since last login,” convert product plan names into numeric indicators, or summarize support tickets into counts and response times. The model is not learning from raw records directly. It is learning from a representation of those records.

That representation matters. A model can only learn patterns that are visible in the way the data is encoded. If an important signal is lost during transformation, the model may never have a chance to use it.

In natural language processing, or NLP, which means machine learning with text, transformation is often especially important. Raw text may need to be tokenized, which means split into smaller units such as words or subwords, before a model can process it.

One more practical rule matters here: any transformation that learns from data, such as scaling or category encoding, should be fit on the training set and then applied to the validation and test sets. That keeps information from the test set from leaking back into the training process. In practice, this is easiest to enforce when preprocessing steps live inside a single machine learning pipeline, because the pipeline applies the same fitted transformation consistently and helps prevent data leakage. The same idea shows up in production pipelines: the model should see the same transformation logic during training and live use.

## 5) Integration combines information from multiple sources

Many useful ML systems depend on more than one dataset. Integration merges data from several sources into a single dataset suitable for learning.

For a churn model, that might mean combining billing data, product usage data, and support ticket data into one training table. Each source gives a different part of the story. Billing tells you about payment behavior, product usage tells you how engaged the customer is, and support tickets can reveal frustration or unresolved problems.

Integration is powerful, but it also adds risk. The more sources you combine, the more carefully you have to handle timing, duplicate records, and mismatched definitions. If one source is updated daily and another is updated weekly, the team has to decide how to align them before training.

The value of integration is that it lets the model see a fuller picture than any one source could provide alone.

## 6) Sampling keeps the dataset workable and balanced

Sometimes the dataset is too large to use in full, or it contains a severe imbalance between categories. Sampling selects a representative subset of the data so the model can train efficiently.

The goal is not just smaller data. The goal is useful data. If the sample is not representative, the model may learn a distorted version of the real world.

For the churn model, sampling might help if the company has millions of customers and years of history. The team may not need every single row to build a first useful model. Sampling can also help with class imbalance, which means one category is much more common than another. If only a tiny fraction of customers churn, the model may need sampling or weighting so it does not learn to always predict “no churn.” Weighting means giving some examples more influence during training than others.

A churn dataset with extreme imbalance can look deceptively good if you only measure accuracy. A model that always predicts “no churn” may seem accurate while being nearly useless. In that situation, precision-recall curves and balanced accuracy often tell a more honest story than raw accuracy, because they expose how the model behaves on the rare class. That is why sampling and evaluation have to be designed together.

## 7) Splitting creates training, validation, and test sets

Splitting is one of the most important steps in the pipeline. The dataset is divided into separate parts so the model can be trained and evaluated honestly.

Training data is used to fit the model. Validation data is used during development to tune choices and compare versions. Test data is held back until the end so the team can estimate how well the model handles unseen data.

The point of the split is to avoid overfitting, which happens when a model learns the training data too specifically and fails to generalize. Generalize means perform well on new data, not just the examples it memorized during training.

For the churn model, this distinction matters because past customers are not identical to future customers. If the team uses the wrong split, they may overestimate how well the model really works.

Because churn data is time-ordered, the team often needs a chronological split rather than a random shuffle. That means the model is trained on earlier customers and evaluated on later customers. This is the same reason time-series splitting exists in tools such as scikit-learn’s TimeSeriesSplit: future data should not leak into the past. If churn is rare, the team may also use stratified splitting so each split keeps a similar churn/non-churn balance. Both choices help the evaluation stay realistic.

## 8) Versioning supports reproducibility

The source material also emphasizes data version control. This is the practice of tracking changes to datasets, models, and related artifacts over time. Artifacts are the files and outputs produced during the machine learning process, such as datasets, feature files, trained models, and evaluation reports.

Versioning matters because ML experiments are not one-and-done. Teams try many dataset variations, feature sets, and model versions. If results change later, versioning helps answer the question: what changed? Some platform docs also warn that versioning only helps if the underlying data is truly reproducible; if a dataset version points at mutable content, the snapshot can stop matching the original experiment.

In the churn example, versioning lets the team compare last week’s cleaned dataset with this week’s updated one. If a model suddenly performs worse, the team can check whether the problem came from the data, the feature definitions, or the training setup.

For models that use derived features, point-in-time correctness is important. That means the training table should only use feature values that were actually available at the moment each label was recorded. If the team accidentally includes future information, the model can look better in training than it really is. A feature store helps reduce this risk by keeping training and serving definitions aligned and by making feature reuse more consistent across the pipeline.

Without versioning, debugging becomes guesswork. With versioning, the team can reproduce past results and understand why a model changed.

## 9) Data quality is a system issue

It is tempting to treat data quality as a one-time cleanup task. In practice, it is a system issue. Data quality has to be maintained through collection, storage, transformation, splitting, and monitoring.

That is why the course source material links data quality with the larger ML architecture. Good data is not just “nice to have.” It is part of how the whole system stays reliable.

Another way this shows up is training-serving skew, which means the data used to train the model no longer matches the data the live system receives. A feature that was stable during training may drift in production if an upstream pipeline changes. Versioning, feature stores, and monitoring all help reduce that mismatch.

In the churn model, if an upstream service stops populating a field, the model may still run, but its predictions can quietly get worse. The pipeline needs checks that catch that kind of problem before users feel the damage.

## Key takeaways

- ML models learn from data, so data quality matters enormously.
- Good data work includes collection, cleaning, transformation, integration, sampling, and splitting.
- Training, validation, and test data serve different purposes.
- Representative data helps the model generalize.
- Versioning makes experiments reproducible and easier to debug.

## Quick self-check

Answer these in your own words:

1. Why does data quality matter so much in machine learning?
2. What is the difference between data cleaning and data transformation?
3. Why is data integration useful?
4. What is the difference between training, validation, and test data?
5. How does data versioning help when a model changes over time?

## Suggested follow-up reading

- /home/rich/wiki/ai-research/raw/articles/2026-05-06_MachineLearningArchitecture_WhatItIs_Components_Ty.md
- /home/rich/wiki/ai-research/raw/articles/2026-04-25_Architectures_for_Machine_Learning___Springer_Natu.md
- /home/rich/wiki/ai-research/raw/articles/2026-04-29_Top_Machine_Learning_Architectures_Explained_-_BMC.md
- /home/rich/wiki/ai-research/ai-ml-foundations-syllabus.md
