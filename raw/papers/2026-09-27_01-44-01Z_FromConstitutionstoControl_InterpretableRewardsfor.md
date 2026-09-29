---
title: From Constitutions to Control: Interpretable Rewards for Aligning Language Models
published: 2026-09-27T01:44:01Z
authors: Johann D. Gaebler, Calvin Isley, Max Lamparth, Stephen Casper, Sharad Goel
url: http://arxiv.org/abs/2609.33086v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Constitutions to Control: Interpretable Rewards for Aligning Language Models

## Abstract
Current approaches to aligning language models often make it hard to know what behavior is being rewarded or to change that reward in a targeted way. In particular, standard preference-based methods collapse multiple considerations into aggregate human judgments, obscuring what drives the resulting reward, while principle-based methods specify high-level values without fully operationalizing them. To address this gap, we develop a rubric-based framework to transform a general-purpose constitution into an interpretable and tunable reward model, using constitution-guided AI feedback to estimate initial weights for the constituent rubric items. We then reweight those dimensions to construct modified rewards for training. Across experiments on political alignment and safety-helpfulness tradeoffs, reweighting individual dimensions predictably changes targeted behaviors largely independently while navigating tradeoffs between conflicting alignment objectives. We show that the same framework can mitigate label bias encoded in preference judgments -- including sycophancy and demographic bias -- by reducing their influence on the training reward. Our results demonstrate that constitution-derived, interpretable rewards can translate high-level alignment principles into more transparent and controllable model behavior.

## Metadata
- **Published**: 2026-09-27T01:44:01Z
- **Authors**: Johann D. Gaebler, Calvin Isley, Max Lamparth, Stephen Casper, Sharad Goel
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33086v1)