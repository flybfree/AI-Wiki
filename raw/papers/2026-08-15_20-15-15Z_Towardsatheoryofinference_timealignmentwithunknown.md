---
title: Towards a theory of inference-time alignment with unknown rewards
published: 2026-08-15T20:15:15Z
authors: Steve Hanneke, Hongao Wang, Mingyue Xu
url: http://arxiv.org/abs/2608.15402v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Towards a theory of inference-time alignment with unknown rewards

## Abstract
Generative model alignment has received broad interest, and significant progress has been made in supervised fine-tuning and inference-time computation. Yet, alignment has remained poorly understood from a statistical learning perspective. We formulate inference-time alignment as a weak-to-strong learning problem, where a reference policy (weak learner) is assumed to be fairly good and the goal is to produce a strong learner that predicts a good response at test time with arbitrarily high probability. Our problem is formulated as learning from scratch --- everything is learned from data rather than assuming access to a good reward estimate, and thus differs from the existing inference-time alignment theory. Our model shares similarity to the recent work of arXiv:2510.15464, where for each prompt, there could be multiple good responses. Our definition of the alignment learnability follows the PAC learning principle. We introduce a novel combinatorial dimension of the reward class which we call the alignment dimension, and show that it completely characterizes the alignment learnability --- a reward class is alignment learnable if and only if its alignment dimension is finite. The core of our learning procedure works by invoking the ordinary one-inclusion graph algorithm to run a tournament over all pairs of label sets satisfying that neither is a subset of the other. We believe our results might shed light on establishing a complete theoretical understanding towards alignment.

## Metadata
- **Published**: 2026-08-15T20:15:15Z
- **Authors**: Steve Hanneke, Hongao Wang, Mingyue Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15402v1)