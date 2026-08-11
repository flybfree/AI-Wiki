---
title: Online Conformal Prediction Beyond Feedback
published: 2026-08-07T11:58:48Z
authors: Joar Skalse, Edoardo Pona, Osvaldo Simeone, Nicola Paoletti
url: http://arxiv.org/abs/2608.07139v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Online Conformal Prediction Beyond Feedback

## Abstract
Uncertainty quantification is essential when deploying machine learning models in safety-critical applications. Online conformal prediction (OCP) provides theoretically principled uncertainty quantification for arbitrary black-box classifiers and non-i.i.d. data streams by constructing prediction sets that are guaranteed to contain the true label at a user-specified frequency. OCP usually updates prediction sets using feedback from previously deployed predictions. We instead study an OCP setting beyond feedback: on each round, the learner can either output a prediction set or query the correct label, but not both. Thus, no deployed prediction is ever evaluated directly. We reduce this problem to a partial monitoring game in which prediction actions return no observation and a separate query action reveals the label. The reward function is constructed in a way that encourages the learner to output small prediction sets while ensuring that the correct label is covered with a sufficiently high probability. To solve this game, we develop OCP with queries (OCPQ) by adapting the label efficient forecaster of Cesa-Bianchi, Lugosi, and Stoltz (2004) to our setting. For any black box classifier and any (non-i.i.d.) oblivious data stream of length $T$, OCPQ has $O(T^{2/3})$ expected regret and expected coverage at least $β-O(T^{-1/3})$ for a user-defined $β$, while querying only an expected $T^{-1/3}$ fraction of rounds. This provides coverage comparable to bandit-based OCP methods while requiring no feedback from deployed prediction sets. Experiments on real-world datasets further demonstrate the effectiveness of our approach.

## Metadata
- **Published**: 2026-08-07T11:58:48Z
- **Authors**: Joar Skalse, Edoardo Pona, Osvaldo Simeone, Nicola Paoletti
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07139v1)