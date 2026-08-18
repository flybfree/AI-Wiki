---
title: When AI Rewrites, Classifiers Relax: Uncertainty-Aware Sentiment Analysis on Sarcastic and AI-Paraphrased Social Text
published: 2026-08-15T17:41:45Z
authors: Shresth Shroff
url: http://arxiv.org/abs/2608.15338v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When AI Rewrites, Classifiers Relax: Uncertainty-Aware Sentiment Analysis on Sarcastic and AI-Paraphrased Social Text

## Abstract
Sentiment classifiers are increasingly applied to social media content that is either sarcastic or AI-generated --- two distributional regimes where standard evaluations offer little guidance. We present a three-part empirical study of sentiment classifier behaviour under these conditions. First, we find that confidence scores on sarcastic text are significantly lower than on non-sarcastic text (Mann--Whitney $p = 2 \times 10^{-6}$), confirming that classifiers sense their own uncertainty on ironic content even without explicit uncertainty modelling. Second, and counterintuitively, we show that sentiment classifiers achieve higher accuracy on AI-paraphrased reviews than on the original human-authored text (RoBERTa: $+5.8$ pp for Qwen3.5-4B paraphrases, $+3.7$ pp for Gemma4-E4B), revealing a cross-domain stylistic alignment effect: AI paraphrases remove distributional noise that confounds Twitter-trained classifiers, producing cleaner, more prototypical sentiment text. Third, we demonstrate that a lightweight abstention wrapper --- flagging the $14\%$ of inputs with confidence below $0.6$ --- improves accuracy from 82.2\% to 88.9\% ($+6.7$ pp) on the retained set. We further compare Semantic Entropy and MC-Dropout-style disagreement as uncertainty signals and find near-identical AUROC ($0.650$ vs.\ $0.646$) on sarcastic text, suggesting that for short social media inputs, both methods are interchangeable. Our results motivate a shift from confident single-label prediction to uncertainty-aware abstention in high-stakes sentiment applications such as mental health flagging and content moderation.

## Metadata
- **Published**: 2026-08-15T17:41:45Z
- **Authors**: Shresth Shroff
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15338v1)