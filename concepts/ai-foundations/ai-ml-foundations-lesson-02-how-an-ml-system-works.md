---
title: AI/ML Foundations Lesson 02 - How an ML System Works
date: 2026-05-06
status: draft
tags: [lesson, machine-learning, architecture, pipeline, foundations]
source_pages:
  - ai-ml-foundations-syllabus.md
  - raw/articles/2026-05-06_MachineLearningArchitecture_WhatItIs_Components_Ty.md
  - raw/articles/2026-04-25_Architectures_for_Machine_Learning___Springer_Natu.md
  - raw/articles/2026-04-29_Top_Machine_Learning_Architectures_Explained_-_BMC.md
---

## Summary

Placeholder summary — please add a concise summary.


# Lesson 2: How an ML System Works



**Source**: [Original Article](https://example.com/placeholder)
## Navigation
- Previous: [[ai-ml-foundations-lesson-01-ai-machine-learning-and-deep-learning.md|Lesson 1: AI, Machine Learning, and Deep Learning]]
- Landing page: [[ai-ml-foundations-landing-page.md|AI/ML Foundations Landing Page]]
- Next: [[ai-ml-foundations-lesson-03-data-as-the-foundation-of-learning.md|Lesson 3: Data as the Foundation of Learning]]


Time budget: 90 to 120 minutes

## Lesson overview

A machine learning system is bigger than the model inside it. The model is the part that makes predictions, but the system also needs data ingestion, storage, versioning, preparation, training, evaluation, deployment, and monitoring. If any one of those pieces is weak, the whole application can fail even when the model itself looks good in a notebook.

Modern AI systems often add orchestration, memory, tool access, and policy checks around the model.

To keep the lesson grounded, we will use one running example: a company that wants to predict customer churn, which means predicting which customers are likely to leave. That same example will show up in each stage, from data collection to monitoring after launch.

That is why many machine learning problems are really system problems. A churn model can be technically accurate and still fail in production if the input data is stale, the evaluation was too narrow, the deployment is brittle, or no one is watching for drift after launch.

This is also the home of MLOps, or machine learning operations: the set of practices that keeps training, deployment, monitoring, and retraining working together. A/B testing, which means comparing two versions on live traffic, is one common way to see whether a change actually helps.

This lesson gives you a practical map of that full lifecycle so the later lessons on data, training, and deployment fit together as one story.

## Learning goals

By the end of this lesson, you should be able to:

- describe the main stages in an ML pipeline
- explain why an ML model is only one part of the system
- identify the purpose of data ingestion, storage, versioning, preparation, evaluation, deployment, and monitoring
- distinguish offline evaluation from production monitoring
- explain why ML architecture matters for reliability, scale, and maintainability
- name a few common ML architecture families and what they are good for

## 1) An ML system is a pipeline

A useful way to think about machine learning is as a pipeline:

data → storage → preparation → training → evaluation → deployment → monitoring

The pipeline is not just a teaching diagram. It reflects how real ML products are built. Data arrives from one or more sources. It is stored and versioned so the team can reproduce experiments. It is cleaned and transformed into a form the model can use. The model is trained, checked, and then deployed into a real application. After launch, the system is monitored to make sure it still works as the world changes.

In our churn example, the company starts with customer billing, product usage, and support data. Those inputs are collected, stored, prepared, and turned into training examples. The model learns from them, gets evaluated, and then is deployed so the product team can identify customers who may leave.

## 2) Data ingestion starts the process

Data ingestion is the step where the system brings data into the ML workflow. In practice, that data may come from databases, application programming interfaces (APIs), sensors, log files, external datasets, or data lakes. Once the data arrives, it has to be ready for downstream work.

This matters because machine learning cannot fix bad input at the end of the pipeline. If the wrong data enters the system, the model may learn the wrong pattern and confidently repeat that mistake later.

For the churn system, ingestion might pull nightly billing records, daily product-usage logs, and weekly support tickets into the pipeline. The team may not need every update instantly, but they do need the data to arrive reliably and in a form that can be joined later.

Teams use several ingestion patterns. Batch ingestion moves data in chunks on a schedule. Streaming ingestion handles data as it arrives. Real-time ingestion is similar in spirit when the system needs very fresh data. Change data capture, or CDC, tracks only what changed in a source system, which makes it easier to keep downstream data in sync without copying everything again.

For churn prediction, batch ingestion is often enough because customer behavior usually changes over hours or days, not seconds. The right ingestion style depends on the job.

## 3) Storage and versioning make experiments manageable

Once data enters the system, it needs somewhere to live. In ML, storage is not only about saving files. It also has to support access, scale, security, performance, and reproducibility.

Versioning is what makes experimentation manageable. A team may create many dataset versions, feature versions, and model versions while they test ideas. If they do not keep track of which data produced which model, it becomes very hard to explain why a result changed later.

In the churn system, versioning lets the team answer a practical question: if the model performance changed, what changed with it? Did the customer data change? Did the feature definitions change? Did the evaluation setup change? Without versioning, the team has to guess.

This is where data version control becomes useful. Version control lets the team trace a model back to the dataset and configuration used to build it. A feature store also helps here. A feature store is a shared system for storing and serving features, which are the input variables a model uses. It helps keep the same feature definitions consistent between training and live prediction.

That consistency matters because the churn model should see the same meaning for a feature in both places. If “recent usage” is calculated one way during training and another way in production, the model may behave differently even though the code looks correct.

## 4) Preparation turns raw data into usable input

Before training, data usually has to be cleaned, transformed, integrated, sampled, and split.

For the churn system, the team may clean missing billing fields, transform raw timestamps into customer-activity windows, integrate product and support data, and sample a smaller set if the full history is too large to use efficiently. Then they split the data into training, validation, and test sets.

Those three splits serve different purposes. Training data teaches the model. Validation data helps the team tune choices while the model is still being developed. Test data stays hidden until the end so the team can estimate how well the model handles new, unseen examples.

That separation is what keeps evaluation honest. If you train a spam filter and then score it on the same emails it already saw, you are not testing whether it can generalize. You are only checking whether it can remember. The split helps the team measure real performance rather than accidental memorization.

In the churn example, the split also matters because customer behavior changes over time. A model that looks good on old data may not work on newer customer patterns unless the evaluation is set up carefully.

## 5) Training builds the model

Training is the part where the model learns patterns from data. At a high level, the algorithm adjusts internal parameters until its predictions improve.

You do not need the math to understand the workflow. The practical idea is simple: training turns a general-purpose algorithm into a task-specific model. A churn model learns one job: given the customer history it sees, estimate who is likely to leave.

Training also depends on compute. More data and more complex models usually need more memory, more storage throughput, and more processing power. That is one reason machine learning architecture matters: the way the system is built affects what kinds of models it can train efficiently.

In the churn system, training might use past customer actions, billing history, and support interactions. The result is a model that can score current customers, but only if the training pipeline can reliably gather and prepare those signals in the first place.

## 6) Evaluation checks whether the model is useful

Evaluation asks a straightforward question: how well does the model work?

There are two broad kinds of evaluation. Offline evaluation happens during development, after training, on held-out data. Online evaluation happens after deployment, when the model is exposed to real users and real conditions. In practice, online evaluation often means production monitoring, A/B testing, or both.

For the churn system, the team may start with offline evaluation to see whether the model can separate likely churners from stable customers. If the offline result looks promising, they can move to production monitoring after launch to see whether the model still performs well on live data.

The metrics depend on the task. Classification tasks often use accuracy, precision, recall, and F1 score. Accuracy measures how often the model is right overall. Precision measures how often its positive predictions are correct. Recall measures how many of the real positives it found. F1 score balances precision and recall when both matter.

Regression tasks often use mean absolute error, or MAE, and root mean squared error, or RMSE. MAE measures the average size of the mistakes. RMSE penalizes larger errors more strongly. Unsupervised methods may use cohesion, separation, or silhouette-style measures to see whether the groups or patterns make sense.

A technical metric is not always the same as a business goal. That is why teams also care about key performance indicators, or KPIs, which are the business measures that show whether the system is actually helping. A model can look strong on paper and still be the wrong tool if it optimizes the wrong metric.

In the churn example, the team may care more about recall than raw accuracy if missing a customer who is about to leave is more expensive than reviewing a few extra false alarms.

## 7) Deployment puts the model into a real system

Deployment is the step where a trained model becomes part of a live application.

At this stage, the model is no longer just a file on disk or a notebook output. It becomes a service or component that receives input and returns predictions for real users or internal workflows. That change sounds simple, but it is a major shift in responsibility. The model now has to work reliably under real traffic, real latency limits, and real operational constraints.

In the churn system, deployment might mean the model runs inside the product so the customer-success team can see which accounts deserve attention. If the deployment is poorly integrated, the prediction may exist technically but never reach the people who need it.

Deployment is also a team activity. Data scientists, software engineers, IT teams, and domain experts often need to work together. A model can be technically good and still fail operationally if the integration is clumsy or the surrounding application does not fit the workflow.

## 8) Monitoring keeps the system honest after launch

Monitoring is what happens after deployment. It checks whether the model is still working as expected in the real world.

This matters because production data changes. User behavior changes. The outside world changes. Hardware and integration problems can also appear. A model that worked during testing may drift over time even if nobody changed the code.

In the churn system, monitoring may show that recent customer behavior looks different from the training data. Maybe a new pricing plan changed usage patterns, or a new product feature changed how customers interact with the service. The model may still run correctly, but its assumptions may no longer match reality.

Monitoring looks for problems such as failing data feeds, latency spikes, missing inputs, resource shortages, or declining performance. It is the system’s way of asking a simple question: does the live pipeline still match the assumptions we made during training and evaluation?

## 9) What machine learning architecture includes

In the wiki, machine learning architecture means the structure and organization of the whole system, not just the model itself. It includes data flow, storage, preprocessing, training, evaluation, deployment, monitoring, and the retraining loop that keeps the system useful after launch.

That is why architecture choices matter so much. A good architecture makes it easier to keep experiments reproducible, feed data efficiently to training jobs, deploy models into products, and notice when performance starts drifting.

When people talk about ML architecture families, they usually mean different ways of organizing the learning problem itself. Some systems learn from labeled examples. Others look for patterns without labels. Some learn by trial and error. Some are especially good for images, sequences, or generating new data.

For the churn system, the most natural starting point is supervised learning. It uses labeled examples, which means each training example includes the input and the correct answer. If the model predicts a category, the task is classification. If it predicts a number, the task is regression. Churn prediction is usually a classification problem because the output is often a yes-or-no decision: will the customer leave or not?

Unsupervised learning uses data without labels. The model is not told the correct answer. Instead, it looks for structure, similarity, or hidden patterns. In a churn workflow, the team might use unsupervised learning to group customers with similar behavior before they build the supervised model. Clustering groups similar items together, while anomaly detection looks for unusual items that do not fit the normal pattern.

Reinforcement learning is different again. An agent, which is the decision-maker, takes actions in an environment and receives rewards or penalties. Over time, it learns which actions lead to better outcomes. That approach is useful when the right answer is not known in advance and the system has to learn by trying things.

Some architecture families are defined by the type of data they work with. Convolutional neural networks, or CNNs, are designed for images because they can detect local visual patterns such as edges, textures, and shapes. Recurrent neural networks, or RNNs, are designed for sequence data, where order matters. Long short-term memory networks, or LSTMs, are a type of RNN that handles longer context better by deciding what to keep and what to forget.

Transformers are the modern sequence architecture most people hear about today. They use attention, which is a way for the model to focus on the most relevant words, tokens, or positions in the input. A token is a piece of text, such as a word or word fragment. Transformers are especially good at long-range relationships and are the foundation of modern large language models.

Generative models aim to create new data that looks like the data they were trained on. Generative adversarial networks, or GANs, use a generator and a discriminator that compete with each other. A variational autoencoder, or VAE, learns a compressed internal representation and uses it to generate new examples. In a VAE, latent structure means the hidden shape of the data in that compressed representation.

These families matter because different jobs need different strengths. A churn system may begin with supervised learning, may borrow ideas from unsupervised clustering, and may later use a richer model family if the data and business need change. The important point is that architecture should match the problem instead of being chosen by habit.

Good architecture is not just about speed. It is about reliability, maintainability, security, reproducibility, and the ability to adapt when the world changes.

## Key takeaways

- ML is a full system, not only a trained model.
- The main lifecycle is data ingestion, storage, preparation, training, evaluation, deployment, and monitoring.
- Data versioning and feature consistency matter before training even starts.
- Offline evaluation and production monitoring solve different problems.
- Good architecture improves reliability, reproducibility, and maintainability.
- Different ML architecture families fit different jobs, such as images, sequences, unlabeled data, and generation.

## Quick self-check

Answer these in your own words:

1. Why is an ML model only one part of an ML system?
2. What is the difference between training, validation, and test data?
3. Why is data versioning useful?
4. How is offline evaluation different from production monitoring?
5. Why can a technically strong model still fail in production?

## Suggested follow-up reading

- /home/rich/wiki/ai-research/raw/articles/2026-05-06_MachineLearningArchitecture_WhatItIs_Components_Ty.md
- /home/rich/wiki/ai-research/raw/articles/2026-04-25_Architectures_for_Machine_Learning___Springer_Natu.md
- /home/rich/wiki/ai-research/raw/articles/2026-04-29_Top_Machine_Learning_Architectures_Explained_-_BMC.md
- /home/rich/wiki/ai-research/ai-ml-foundations-syllabus.md
