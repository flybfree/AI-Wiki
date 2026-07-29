---
title: Anti-Backdoor Coreset Selection via Cumulative Entropy
published: 2026-07-28T09:37:11Z
authors: Qi Zhao, Christian Wressnegger
url: http://arxiv.org/abs/2607.25502v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Anti-Backdoor Coreset Selection via Cumulative Entropy

## Abstract
Recent training-time defenses against neural backdoors isolate a benign subset from poisoned training data, to learn a backdoor-free model from it. In this paper, we formulate this defense strategy as a coreset selection problem, giving rise to so-called "Anti-Backdoor Coreset Selection." Since poisonous samples have (a) lower prediction uncertainty and are (b) less frequent than benign samples, coreset selection naturally focuses more on samples associated with benign functionality than the backdoor functionality. We use the Cumulative Entropy as selection criterion to further facilitate this effect. The metric tracks the learning dynamics of training samples and allowing us to select benign samples with high informativeness for the coreset. Additionally, we unlearn the chosen samples in each epoch to facilitate the separability between benign and poisonous samples. Together, this yields an exceptionally effective training-time defense that constructs a benign coreset to train a backdoor-free model. Unlike prior defenses that compromise natural accuracy and fail against certain attacks, our method mitigates backdooring attacks consistently with a negligible impact on natural performance.

## Metadata
- **Published**: 2026-07-28T09:37:11Z
- **Authors**: Qi Zhao, Christian Wressnegger
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25502v1)