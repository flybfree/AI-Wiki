---
title: Do Language Models Consistently Encode the Current Year?
published: 2026-08-16T03:22:24Z
authors: Suze van Adrichem, Aditi Bhaskar, Diyi Yang, Christopher Potts, Jing Huang
url: http://arxiv.org/abs/2608.15507v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Do Language Models Consistently Encode the Current Year?

## Abstract
A consistent concept of the current time is important for temporal reasoning, yet how language models represent the current time is not well understood. We contribute two tasks that probe the current year in conceptually distinct ways: an associative task, which infers the current year from verb tense, and a declarative task, which directly queries for the current year. Both tasks estimate current years within one year of the post-training data cutoff of instruction-tuned language models. For base models, predictions on the associative task serve as a strong proxy for the pre-training data cutoff, with an average error of only 10 months across 13 models. However, their internal mechanisms diverge: the associative task uses mechanisms similar to factual recall, while the declarative task lacks consistent causal pathways. This divergence poses a challenge for updating the current year in language models. None of prompting, SFT, or weight editing succeed in shifting the associative and declarative years simultaneously. Prompting updates the declarative year (94.6% success across 351 target years) but leaves the associative year nearly unchanged (1.7% success). Year-shifted SFT also fails to shift the associative year, matching the target year in only one of eight models. Weight editing, while effective for both tasks individually, does not generalize across both. Overall, our results show that the current year is not consistently encoded in language models: The associative notion, deeply ingrained in linguistic structures learned in pre-training, uses different causal mechanisms and resists the same modifications that easily shift the declarative notion learned in post-training.

## Metadata
- **Published**: 2026-08-16T03:22:24Z
- **Authors**: Suze van Adrichem, Aditi Bhaskar, Diyi Yang, Christopher Potts, Jing Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15507v1)