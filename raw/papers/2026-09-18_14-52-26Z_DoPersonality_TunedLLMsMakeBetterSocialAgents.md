---
title: Do Personality-Tuned LLMs Make Better Social Agents?
published: 2026-09-18T14:52:26Z
authors: Tim Krabbe, Xiaodan Shi
url: http://arxiv.org/abs/2609.21857v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Do Personality-Tuned LLMs Make Better Social Agents?

## Abstract
LLMs are increasingly used in social simulations for socially interactive agents and robots, offering more flexibility than rule-based systems. However, even though they mimic human behaviour very well, there is a persistent alienness to them. This work investigates whether personality-aware fine-tuning can reduce this gap by improving the consistency and controllability of personality-conditioned dialogue generation compared with instruction prompting alone. We fine-tune two small open-weight LLMs, Qwen2.5-7B-Instruct and Ministral-8B-Instruct, using a corpus that combines personality-labelled social media posts and dialogues to create a personality-based dialogue engine for social simulation. The resulting models are evaluated across multiple social interaction scenarios using three independent LLM judges, which assess personality fidelity and provide evidence-based behavioral interpretations. We additionally quantify inter-rater agreement and lexical characteristics of the generated dialogue. Results indicate that fine-tuned models are not better at role-playing different personalities than their respective baseline models. However, low inter-rater agreement limits the confidence with which these results can be interpreted. Concerning the quality of generated texts, fine-tuned models are mostly comparable to the baselines, with fine-tuning improving the linguistic diversity of the Qwen models. While the results appear generally usable and the baseline models offer the best overall performance, future studies should place greater emphasis on the quality and domain alignment of training data for accurate personality role-playing.

## Metadata
- **Published**: 2026-09-18T14:52:26Z
- **Authors**: Tim Krabbe, Xiaodan Shi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.21857v1)