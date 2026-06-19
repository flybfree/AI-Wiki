---
title: 'AI/ML Foundations Lesson 04 - Supervised Learning: Learning from Labels'
date: 2026-05-06
status: draft
tags: [lesson, supervised-learning, classification, regression, foundations]
source_pages:
  - ai-ml-foundations-syllabus.md
  - raw/articles/2026-05-06_MachineLearningArchitecture_WhatItIs_Components_Ty.md
  - raw/articles/2026-04-25_Architectures_for_Machine_Learning___Springer_Natu.md
  - raw/articles/2026-04-29_Top_Machine_Learning_Architectures_Explained_-_BMC.md
  - raw/articles/2026-05-07_Supervised_Learning_Web_Sources.md
---

## Summary

Placeholder summary — please add a concise summary.


# Lesson 4: Supervised Learning: Learning from Labels



**Source**: [Original Article](https://www.ibm.com/think/topics/supervised-learning)
## Navigation
- Previous: [[ai-ml-foundations-lesson-03-data-as-the-foundation-of-learning.md|Lesson 3: Data as the Foundation of Learning]]
- Landing page: [[ai-ml-foundations-landing-page.md|AI/ML Foundations Landing Page]]
- Next: [[ai-ml-foundations-lesson-05-unsupervised-learning-finding-hidden-structure.md|Lesson 5: Unsupervised Learning: Finding Hidden Structure]]


Time budget: 90 to 120 minutes

## Lesson overview

Supervised learning is a machine learning (ML) approach where each training example comes with the correct answer. The input side of the example is made up of features, which are the measurable details the model can use. The output side is the label, or target, which is what the model is trying to predict.

This style of learning is common because many real-world problems already have known answers. An email can be labeled spam or not spam. A transaction can be labeled fraudulent or normal. A house listing can come with a sale price. In each case, the model is not inventing the task from scratch. It is learning from examples that already include the answer.

In practice, supervised learning usually uses three data splits. The training set teaches the model. The validation set helps the team tune choices during development. The test set is held back until the end so the team can check how well the model generalizes, meaning how well it works on new examples it never saw during training.

The central question in this lesson is simple: how does a model learn from labeled examples, and how do classification and regression solve different versions of that problem?

## Learning goals

By the end of this lesson, you should be able to:

- explain what supervised learning is
- describe the role of labels in training
- distinguish classification from regression
- explain why training examples need both inputs and outputs
- recognize common supervised learning use cases

## 1) Supervised learning uses labeled examples

In supervised learning, the training data includes both the input and the desired output. The input is the feature set, and the output is the label or target. The label tells the model what the correct answer should be.

For example, if the input is an email and the label is “spam” or “not spam,” the model learns to map email features to that category. If the input is a house listing and the label is the sale price, the model learns to predict a number. If the input is an image and the label is “cat,” the model learns which visual patterns tend to belong to that class.

The word “supervised” matters because the labels act like guidance. The model is not discovering the task on its own from raw data. It is being shown the target answer during training, and it keeps adjusting until its predictions are closer to the known answers.

Scenario: imagine teaching a child to sort fruit. If you point to an apple and say “apple,” then point to a banana and say “banana,” you are giving labeled examples. Over time, the child can learn to recognize the difference. Supervised learning works in a similar way: the examples are the lesson, and the labels are the answer key.

## 2) The input-output relationship is the key idea

Supervised learning is about learning a relationship between inputs and outputs. The input might be an image, a customer record, a set of sensor readings, or a block of text. In ML terms, those are features. The output is the label or target value.

During training, the model makes a prediction and compares it with the correct answer in the labeled data. That comparison gives feedback about how far off the model was, which is how learning happens. Over time, the model adjusts its internal settings so its predictions move closer to the truth.

Scenario: if you give a model a photo of an animal and the label says “dog,” the model learns which visual patterns tend to correspond to that label. Later, when it sees a new image, it tries to produce the same kind of label. If the new image is blurry, the learned relationship still helps it make a reasonable guess.

## 3) Classification predicts categories

Classification is the supervised learning task where the output is a category.

Examples include spam versus not spam, fraud versus not fraud, cat versus dog, or approved versus rejected. Sometimes there are only two classes. Sometimes there are many. In image classification, a convolutional neural network, or CNN, is a type of neural network that is especially good at finding patterns in images, such as edges, shapes, and textures.

Classification is useful when the answer belongs to a known set of options. The model is not predicting a continuous number. It is choosing among discrete labels, so the output is usually something like yes/no, class A/class B, or one of several named categories. Classification can be binary, meaning two classes; multiclass, meaning more than two classes; or multilabel, meaning one example can belong to more than one class.

Many classifiers also produce a score or probability before the final label is chosen. A decision threshold turns that score into a class prediction. For example, a spam model may estimate a 0.92 probability that an email is spam, then classify it as spam because that score is above the chosen threshold. Changing the threshold changes the tradeoff between precision and recall. If the team needs fewer false alarms, it can raise the threshold; if it needs to catch more true positives, it can lower the threshold. When the probabilities themselves are poorly calibrated, the team may also need probability calibration before it trusts the scores.

Common classification metrics include accuracy, precision, recall, and F1 score. Accuracy measures overall correctness. Precision asks how often a positive prediction is right. Recall asks how many real positive cases the model found. F1 score balances precision and recall. These metrics matter because a model can look good on accuracy alone while still missing important cases, especially when the classes are imbalanced.

Scenario: a bank might train a classification model to decide whether a transaction is suspicious. The output is not “how suspicious” in a numerical sense. The output is usually a class such as suspicious or normal. That makes the task a decision problem, not a counting problem.

## 4) Regression predicts numbers

Regression is the supervised learning task where the output is a number.

Examples include predicting house price, delivery time, energy usage, or a customer’s lifetime value. The label is still supervised, but instead of a category, it is a numerical target. In a housing example, the model might predict that a home will sell for $420,000 rather than choosing from a list of categories. Google’s Machine Learning Crash Course uses linear regression as the classic example of this setup: the model learns a relationship between features and a numeric label value.

Some regression models predict a continuous quantity directly, while others are used in systems where a number is later turned into a decision. A delivery-time model may output 18.7 minutes, and the business may then decide how that estimate changes routing or customer messaging.

Common regression metrics include mean absolute error, or MAE, and root mean squared error, or RMSE. These metrics show how far the model’s predictions are from the true values. MAE is easy to read as an average absolute miss. RMSE gives extra weight to larger mistakes, so it is useful when big errors matter more than small ones.

Scenario: if a real estate app predicts that a home will sell for $420,000, regression is the family of methods that produced that estimate. If the real sale price turns out to be $435,000, the model’s error is the difference between those two numbers.

## 5) Supervised and unsupervised learning solve different problems

Supervised and unsupervised learning solve different problems. Supervised learning uses labeled data. You already know the correct answer for each training example, and the model learns to predict that answer on new inputs. Unsupervised learning uses unlabeled data. The model is not trying to match a known answer. Instead, it looks for hidden structure such as clusters, patterns, or unusual records.

A simple way to remember the difference is that supervised learning predicts known answers, while unsupervised learning discovers unknown structure.

Scenario: a bank with labeled fraud cases can train a supervised model to predict whether a new transaction is fraud. If the bank does not yet have reliable labels and wants to explore whether suspicious behavior naturally forms groups, it may use unsupervised learning first.

The contrast becomes clearer in a few everyday examples. Email spam detection is supervised because past emails are labeled spam or not spam. House price prediction is supervised because the target is a known sale price. Customer segmentation is unsupervised because the model is asked to discover natural groups from purchase behavior. News article clustering is unsupervised because the system groups similar articles without being told the categories in advance. Anomaly detection can be either, but it often starts with unsupervised methods when labels are incomplete.

An anomaly is something unusual enough to stand out from the rest of the data. In practice, that might mean a strange credit-card transaction, a server log pattern that does not match normal traffic, or a sensor reading that breaks the usual trend. That is useful in fraud detection, cybersecurity, and monitoring systems, especially when labels are missing or incomplete.

The key practical difference is that supervised learning is best when you know what you want to predict, while unsupervised learning is best when you want to explore the data and discover structure before you know the labels. The two approaches often work together: you may explore data with unsupervised methods first, then create labels and switch to supervised learning later.

For a fuller explanation, see Lesson 5: /home/rich/wiki/ai-research/ai-ml-foundations-lesson-05-unsupervised-learning-finding-hidden-structure.md.

## 6) Supervised learning is only as good as the labels

Because supervised learning depends on labels, the labels themselves matter a lot. If the labels are inconsistent, incomplete, or wrong, the model will learn distorted patterns.

That means label quality is part of model quality. The model is not just learning from the input data. It is learning from the pairing between the input and the answer, so a bad label can point the whole model in the wrong direction.

This is why training sets in supervised learning often require careful curation. A mislabeled dataset can create a model that looks good on paper but fails in reality. It is also why teams compare the training, validation, and test sets carefully. If the labels are shaky in one split, evaluation can look better or worse than it should.

Scenario: if a dataset marks many harmful emails as “not spam,” the spam filter will learn from bad guidance and make worse predictions. A small labeling mistake repeated many times can become a large modeling mistake.

## 7) Why supervised learning is so widely used

Supervised learning is popular because it is practical. Many business and technical tasks already have historical outcomes.

If you have past examples of what happened, you can often train a model to predict what will happen next. That makes supervised learning useful for fraud detection, medical diagnosis support, recommendation ranking, forecasting, and image recognition.

Supervised learning includes many familiar methods, such as linear regression, logistic regression, random forests, and neural networks. These algorithms work differently, but they all learn from labeled examples.

A good way to think about this is that the supervised-learning family is broad enough to include both simple statistical models and large neural networks. What they share is not the architecture. What they share is the training signal: each example comes with the right answer.

Scenario: a hospital may use a supervised model to estimate the likelihood of readmission. A retailer may use another supervised model to predict which products a shopper will click. An image app may use a CNN to classify a photo as cat, dog, or something else.

## 8) Supervised learning is still part of a larger system

Even though this lesson focuses on labels, supervised learning still sits inside the larger ML pipeline introduced earlier. It needs cleaned data, a train/validation/test split, proper evaluation, and deployment planning.

After training, the model should be checked on held-out data before it is put into use. Once it is deployed, it should continue to be monitored with real production data. A model can look strong during testing and still fail later if the real-world data changes over time. If the model produces probabilities, the team should also check whether the scores remain well calibrated in production and whether the decision threshold still matches the business goal.

So when you hear “we trained a supervised model,” that does not mean the work is finished. It means one major piece of the system is complete, and the rest of the pipeline still matters.

Scenario: a model that predicts whether a lead will convert still needs to be integrated into the sales workflow, monitored for drift, and retrained when the market changes.

## Closing summary

Supervised learning is one of the most useful ML approaches because it turns labeled examples into a predictive system. The model learns a relationship between features and labels, then applies that relationship to new inputs. Classification handles categories. Regression handles numbers. Both depend heavily on label quality and honest evaluation. In practice, supervised learning is not just about training a model; it is about building a reliable pipeline that can keep working after deployment.

## Quick self-check

Answer these in your own words:

1. What makes a learning problem “supervised”?
2. What is the difference between a label and an input?
3. When would you use classification instead of regression?
4. Why are bad labels a serious problem?
5. Why is supervised learning still only one part of a larger ML system?

## Suggested follow-up reading

- /home/rich/wiki/ai-research/raw/articles/2026-05-07_Supervised_Learning_Web_Sources.md
- https://www.ibm.com/think/topics/supervised-learning
- https://www.ibm.com/think/topics/classification-vs-regression
- https://developers.google.com/machine-learning/crash-course/classification
- https://developers.google.com/machine-learning/crash-course/linear-regression
- https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall
- https://scikit-learn.org/stable/supervised_learning.html
- https://scikit-learn.org/stable/modules/classification_threshold.html
- https://scikit-learn.org/stable/modules/calibration.html
- /home/rich/wiki/ai-research/raw/articles/2026-05-06_MachineLearningArchitecture_WhatItIs_Components_Ty.md
- /home/rich/wiki/ai-research/raw/articles/2026-04-25_Architectures_for_Machine_Learning___Springer_Natu.md
- /home/rich/wiki/ai-research/raw/articles/2026-04-29_Top_Machine_Learning_Architectures_Explained_-_BMC.md
- /home/rich/wiki/ai-research/ai-ml-foundations-syllabus.md
