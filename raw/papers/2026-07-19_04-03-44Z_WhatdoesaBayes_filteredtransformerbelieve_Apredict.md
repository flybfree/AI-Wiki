---
title: What does a Bayes-filtered transformer believe? A predictive Monte Carlo approach
published: 2026-07-19T04:03:44Z
authors: Afiq Abdillah Effiezal Aswadi, Haotong Ma, Susan Wei
url: http://arxiv.org/abs/2607.17060v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What does a Bayes-filtered transformer believe? A predictive Monte Carlo approach

## Abstract
A Bayes-filtered transformer (BFT) is a transformer trained on sequences that are generated in two steps: first a latent task is drawn from a prior, then observations are drawn conditional on that task. Trained under autoregressive log loss, the BFT's next-token prediction, in the idealized limit, is the Bayesian posterior predictive distribution (PPD) induced by that prior and that conditional law. In practice the trained BFT is only an approximation of this ideal PPD, raising an interpretive question: what prior and posterior over the latent task has the trained BFT actually internalized? Existing work answers this question by comparing the trained BFT's predictions against the predictions of various "reference" posteriors, each standing in for a different candidate algorithm or computation the BFT might be implementing. This prediction-space comparison is fragile: different posteriors can share the same posterior-mean predictions. We use predictive Monte Carlo (PMC) as a general interpretability tool for any BFT: using only next-token generation, PMC returns an approximation to the implicit prior and posterior over the latent task, answering the interpretive question directly in latent space. We apply PMC to three stylized task families spanning 0-Markov and 1-Markov exchangeability. The phenomena previously reported in these settings remain visible in latent space. Code is available at https://github.com/afiq-aswadi/bft-pmc

## Metadata
- **Published**: 2026-07-19T04:03:44Z
- **Authors**: Afiq Abdillah Effiezal Aswadi, Haotong Ma, Susan Wei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.17060v1)