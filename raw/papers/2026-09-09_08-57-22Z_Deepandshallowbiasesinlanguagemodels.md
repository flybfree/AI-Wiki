---
title: Deep and shallow biases in language models
published: 2026-09-09T08:57:22Z
authors: An Vo, Vy Tuong Dang, Khai-Nguyen Nguyen, Emilio Villa-Cueva, Thamar Solorio, Anh Totti Nguyen, Daeyoung Kim
url: http://arxiv.org/abs/2609.09901v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Deep and shallow biases in language models

## Abstract
Large language models often repeatedly select the same answer even when many alternatives are plausible. Prior work treats this concentration as bias, but it does not distinguish stable model preferences from responses that depend on a particular prompt wording. We introduce a bias depth score that measures both how strongly a model prefers its top answer under direct prompting and whether that answer survives scenario reframing. Across 4,442 opinion prompts and four large language models, only about a quarter of the concentrated preferences survive reframing. We call these persistent cases Deep biases, and the remaining prompt-dependent cases Shallow biases. Our results show that Deep biases are more often inherited from pretraining and preserved through SFT. Under both continued fine-tuning and prompt-based debiasing for diversity, Deep biases are consistently harder to remove than Shallow biases. Bias depth therefore separates stable learned biases from prompt-wording artifacts that single-prompt metrics conflate. Code, models, and data are available at deepbias.github.io.

## Metadata
- **Published**: 2026-09-09T08:57:22Z
- **Authors**: An Vo, Vy Tuong Dang, Khai-Nguyen Nguyen, Emilio Villa-Cueva, Thamar Solorio, Anh Totti Nguyen, Daeyoung Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.09901v1)