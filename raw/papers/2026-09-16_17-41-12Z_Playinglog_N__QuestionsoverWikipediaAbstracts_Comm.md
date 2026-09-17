---
title: Playing log(N)-Questions over Wikipedia Abstracts: Communication Efficiency Between Paired Frontier Models
published: 2026-09-16T17:41:12Z
authors: Peter Potash
url: http://arxiv.org/abs/2609.19113v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Playing log(N)-Questions over Wikipedia Abstracts: Communication Efficiency Between Paired Frontier Models

## Abstract
We evaluate six frontier language models on the two-agent $\log(N)$-Questions game. A questioner sees $N$ Wikipedia lead paragraphs and must identify a secretly chosen target using exactly $\log_2 N$ yes/no questions. An answerer sees only the target and the question, and replies with one word. Both roles run on the same provider, so the game measures how well a model communicates with itself across an information asymmetry. We run 408 games over document sets of 4 to 1024 paragraphs at a total API cost of \$363. One model finishes well behind the others: Claude Opus 5 wins 28 of 68 games, against 45 to 56 for GLM-5.3, GPT-5.6 Sol, Grok 4.6, Gemini 3.8 Flash and Kimi K3. The leading five are only marginally separable. Pooling those five, win rate declines with set size at $r=-0.973$ and is fit by a single per-round reliability parameter. The form is $\text{win}=p^{\log_2 N}$ with $p=0.928$. Losses divide into answer errors and discrimination failures in roughly equal measure, and models almost never name a document their own evidence excludes. Every unanimous answer error from the weakest model was inspected: 32 of 34 are ``No'' answers, on properties stated in the document's first sentence, under an instruction that explicitly warns against defaulting to ``No''. Information per question, estimated from answer balance, correlates with win rate at $r=+0.88$. The only two models to extract a full bit per question are the only two that partition on document titles, a strategy absent below $N{=}32$ and used in a quarter of questions above it. Reasoning-token expenditure varies $4.5\times$ across models with little relation to success, and the trace grows as the candidate set shrinks without a matching gain in reliability.

## Metadata
- **Published**: 2026-09-16T17:41:12Z
- **Authors**: Peter Potash
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.19113v1)