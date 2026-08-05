---
title: AI/ML Foundations Lesson 15 - Evaluation, Overfitting, and Limits
date: 2026-05-06
status: draft
tags: [lesson, evaluation, overfitting, monitoring, limits, foundations]
source_pages:
  - ai-ml-foundations-syllabus.md
  - raw/articles/2026-05-06_MachineLearningArchitecture_WhatItIs_Components_Ty.md
  - raw/articles/2026-04-25_Architectures_for_Machine_Learning___Springer_Natu.md
  - raw/articles/2026-04-29_Top_Machine_Learning_Architectures_Explained_-_BMC.md
  - raw/articles/2026-05-05_Machinelearningoperations-AzureArchitectureCenter.md
  - raw/articles/2026-04-25_LLMs___10_Things_That_Matter_in_AI_Right_Now___MIT.md
---

## Summary

Placeholder summary — please add a concise summary.


# Lesson 15: Evaluation, Overfitting, and Limits



**Source**: [Original Article](https://example.com/placeholder)

## Semantic links
- [[concepts/ai-foundations/ai-ml-foundations-lesson-01-ai-machine-learning-and-deep-learning.md|AI/ML Foundations Lesson 01 - AI, Machine Learning, and Deep Learning]] — 3 title terms overlap; shared tags: foundations, lesson; 5 backlinks
- [[concepts/ai-foundations/ai-ml-foundations-lesson-13-agents-and-agentic-workflows.md|AI/ML Foundations Lesson 13 - Agents and Agentic Workflows]] — 3 title terms overlap; shared tags: foundations, lesson; 5 backlinks
- [[concepts/ai-foundations/ai-ml-foundations-lesson-09-attention-and-transformers.md|AI/ML Foundations Lesson 09 - Attention and Transformers]] — 3 title terms overlap; shared tags: foundations, lesson; 6 backlinks

## Navigation
- Previous: [[ai-ml-foundations-lesson-14-choosing-the-right-architecture-for-the-task.md|Lesson 14: Choosing the Right Architecture for the Task]]
- Landing page: [[ai-ml-foundations-landing-page.md|AI/ML Foundations Landing Page]]
- Next: [[ai-ml-foundations-lesson-16-deployment-scaling-and-what-comes-next.md|Lesson 16: Deployment, Scaling, and What Comes Next]]


Time budget: 90 to 120 minutes

## Lesson overview

A model is only useful if it keeps working on new data in the real world. That sounds obvious, but it is one of the most important ideas in machine learning. A system can look excellent during training and still fail when it meets new examples, changing conditions, or messy real users.

This lesson is about how we check whether a model really works. It covers evaluation, overfitting, validation, testing, monitoring, and the limits of modern AI systems. The main idea is simple: learning is not finished when training ends. A good system has to prove itself before deployment and keep proving itself after deployment.

## Learning goals

By the end of this lesson, you should be able to:

- explain why training performance is not the same as real-world performance
- describe overfitting and underfitting in plain language
- explain validation, testing, and monitoring as parts of one evaluation cycle
- recognize common AI limits such as brittleness, hallucination, bias, and domain drift
- understand why technical metrics and business impact both matter

## 1) Training success does not guarantee real-world success

A model can look impressive on the data it already saw and still perform badly on fresh data.

That happens because training data is only a sample of reality. The model is not learning the world itself. It is learning patterns from a particular dataset, with all of that dataset’s gaps, quirks, and noise. If the model leans too hard on those accidental details, it may seem smart in development and then disappoint in production.

The machine learning architecture sources describe evaluation as part of the full system, not an afterthought. That is the right mental model. Training is one stage. Evaluation is what tells you whether the model can generalize, meaning whether it can work on examples it has not seen before.

Scenario: a model trained on studio photos of shoes may do very well in the lab, but fail when a customer uploads a blurry phone picture taken in poor lighting.

## 2) Overfitting means learning too much of the wrong thing

Overfitting happens when a model fits the training data too closely.

Instead of learning the underlying pattern, it learns the noise, exceptions, or tiny details that happened to exist in the training set. A model that overfits can look strong during development because it remembers the examples very well, but that same memory becomes a weakness when the world changes even a little.

A helpful analogy is studying by memorizing one practice exam instead of understanding the subject. You might score perfectly on that exact test, but you have not actually learned the material well enough to handle a new version.

Scenario: if a fraud detector memorizes the exact timing and pattern of one month’s transactions, it may struggle when customer behavior shifts during a holiday season.

## 3) Underfitting means the model never learned enough

The opposite problem is underfitting.

An underfit model is too simple or too poorly trained to capture the real pattern in the data. It does not memorize too much. It learns too little. Where overfitting is “too specific,” underfitting is “too vague.”

This matters because evaluation is not only about catching a model that is too clever. It is also about catching a model that is too weak. A model that cannot learn the pattern is just as useless as one that memorizes the noise.

Scenario: a very simple model may miss the difference between normal seasonal sales changes and a real demand spike because it cannot express the pattern at all.

## 4) Validation and testing help measure generalization

Validation and testing are ways to ask, “Will this model work on data it has not seen yet?”

A validation set is used during development. It helps you compare versions, tune settings, and notice whether changes make the model better or worse. A test set is held back until later so you can do a cleaner final check. Both are meant to estimate generalization, which is the model’s ability to perform well on new data.

The architecture and MLOps sources both emphasize splitting data and checking model candidates before they are promoted. That is important because it prevents you from fooling yourself with training scores alone.

Scenario: if you are building a recommendation system, you should test it on users and items the model did not see during training, so the result is closer to real production behavior.

## 5) Offline evaluation and online evaluation are different

Evaluation does not happen only once.

Offline evaluation happens before deployment, usually with held-out data in a development environment. Online evaluation happens after deployment, when real users and real traffic interact with the system. Offline evaluation is useful because it is controlled. Online evaluation is useful because it is real.

Both matter. A model can win offline and still fail live if the data pipeline changes, the user behavior shifts, or the application environment is different from the lab.

The Azure MLOps source describes staging, testing, production deployment, and monitoring as a single lifecycle. That is a good way to think about it. The model is not “done” when the notebook is finished; it is only ready to enter a larger system.

MLOps, or machine learning operations, is the practice of running that lifecycle reliably. CI/CD, or continuous integration and continuous delivery, helps teams ship updates safely, and the operational loop usually includes data, model, and infrastructure metrics that can trigger retraining or investigation.

Scenario: a customer-support classifier may look excellent in offline tests, but after deployment it may receive different kinds of tickets than it saw in the test set.

## 6) Monitoring keeps the system honest after deployment

Once a model is in production, monitoring tells you whether it is still doing its job.

Monitoring looks for changes in model behavior, data quality, and infrastructure health. In plain language, it answers questions like: Are predictions still accurate? Is the input data still similar to what we trained on? Is the endpoint still fast enough? Did something break in the pipeline?

The Azure MLOps source is very direct about this. It says teams monitor model, data, and infrastructure metrics, and then use those metrics to trigger action. That action might be retraining, investigation, or infrastructure repair.

Scenario: a seasonal forecasting model may work well in summer and then drift in winter because the input data distribution has changed and the old assumptions no longer match reality.

## 7) Domain drift means the world changed

Domain drift happens when the environment that produced the data changes after training.

Maybe customer behavior shifts, a product changes, the language users write in evolves, or the business itself moves in a new direction. The model is still the same model, but the world it was trained for is no longer the same world it is serving.

This is why machine learning is not a “train once and forget forever” process. Real systems live in moving environments.

Scenario: a spam filter trained before a new phishing campaign may start missing messages until it is updated with examples of the new attack style.

## 8) Modern AI systems have practical limits

Modern AI can be powerful and still be unreliable in important ways.

Brittleness means the system can break or behave strangely when the input is slightly different from what it expected. Hallucination means the model can generate confident-sounding output that is wrong or invented. Bias means the system can reproduce unfair patterns from the data it learned from. These are not edge cases to ignore. They are core limitations to understand.

The MIT article on large language models notes that longer context and more complicated tasks can make systems lose track of what they are doing. That is a useful reminder that scaling does not remove limits; it changes the shape of the limits.

Scenario: if you ask a language model to summarize a report and it adds a detail that was never in the report, that is hallucination. If it answers one prompt correctly but fails on a slightly reworded version, that is brittleness.

## 9) Evaluation should include technical and business outcomes

A model can score well on a metric and still fail to create value.

That is why evaluation should look at both technical performance and business impact. Technical metrics tell you whether the model is doing the computational job you asked of it. Business metrics tell you whether the system is helping the organization in a meaningful way.

The architecture sources and MLOps source both point to this broader view. In production, it is not enough for a model to be “accurate.” It also has to be useful, fast enough, safe enough, and maintainable enough.

Scenario: a customer-service classifier may have high accuracy, but if it sends too many urgent tickets into the wrong queue, the support team may actually get slower.

## 10) Evaluation is a lifecycle, not a one-time event

Good evaluation starts before deployment and continues after deployment.

During development, you compare model versions and use validation data to guide decisions. Before release, you use test data for a more honest final check. After release, you monitor the live system and retrain or redesign when the world changes. That is the real rhythm of machine learning work.

This is also why modern ML is often described as an operating system for prediction rather than a single model artifact. The value comes from the whole loop: data, training, evaluation, deployment, monitoring, and feedback.

Scenario: a recommendation engine may need periodic retraining because user tastes, item availability, and seasonal patterns all change over time.

## 11) Evaluate the system, not just the model

For agentic workflows, evaluation has to measure more than accuracy. You also want task completion, tool success, recovery from errors, refusal behavior, long-horizon consistency, and whether the system stays within policy.

Recent research on scaling agent systems (arXiv:2512.08296) reveals that performance scales differently for multi-agent coordination than for single models. Key findings include:
- **Coordination matters more than agent count**: Adding more agents can degrade performance if not aligned with task properties
- **Different scaling laws**: Agent systems have their own scaling principles based on orchestration quality, model capability, and measurable coordination overhead
- **Long-horizon consistency**: Performance over extended interactions depends on harness design as much as model size

Offline tests tell you how the system behaves in a controlled setup. Online evaluation tells you how it behaves with real users and real traffic. Both matter.

Scenario: a model may answer benchmark questions well but still fail if it picks the wrong tool or loses track of a multi-step task. A long-horizon agent might start strong but drift off-task after 45K tokens without proper context compaction and verification layers.

## 12) What to remember without the jargon

A good model is not just one that learned the training set well. It is one that keeps working on new data in the real world.

Evaluation checks that before deployment. Monitoring checks that after deployment. Overfitting, underfitting, drift, brittleness, hallucination, and bias are the common ways ML systems fail.

## Closing summary

Evaluation is how you find out whether a model really works. Overfitting means the model learned the training set too closely. Underfitting means it never learned enough. Validation and testing help you measure generalization before deployment. Monitoring helps you keep the system honest after deployment. Domain drift, brittleness, hallucination, and bias remind us that real-world AI is always limited by data, context, and design.

The big lesson is that machine learning is a living system. If the data changes, the model can age. If the environment changes, the model can drift. If the task is misunderstood, even a good model can fail. Good evaluation is what keeps those failures visible early enough to fix.

## Key takeaways

- Training performance is not enough.
- Overfitting means learning the training data too closely.
- Underfitting means the model is too simple or too weak to capture the pattern.
- Validation and testing estimate generalization.
- Monitoring is needed after deployment.
- Real systems have limits like drift, brittleness, hallucination, and bias.
- Technical metrics and business metrics both matter.

## Quick self-check

Answer these in your own words:

1. Why can a model do well in training and still fail in practice?
2. What is the difference between overfitting and underfitting?
3. Why do we need validation and test sets?
4. What does monitoring check after deployment?
5. What is the difference between hallucination and brittleness?
6. Why should evaluation include business outcomes as well as technical metrics?

## Suggested follow-up reading

- /home/rich/wiki/ai-research/raw/articles/2026-05-06_MachineLearningArchitecture_WhatItIs_Components_Ty.md
- /home/rich/wiki/ai-research/raw/articles/2026-05-05_Machinelearningoperations-AzureArchitectureCenter.md
- /home/rich/wiki/ai-research/raw/articles/2026-04-25_Architectures_for_Machine_Learning___Springer_Natu.md
- /home/rich/wiki/ai-research/raw/articles/2026-04-29_Top_Machine_Learning_Architectures_Explained_-_BMC.md
- /home/rich/wiki/ai-research/raw/articles/2026-04-25_LLMs___10_Things_That_Matter_in_AI_Right_Now___MIT.md
- /home/rich/wiki/ai-research/ai-ml-foundations-syllabus.md
