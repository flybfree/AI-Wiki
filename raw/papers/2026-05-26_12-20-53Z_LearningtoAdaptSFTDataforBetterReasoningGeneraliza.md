---

title: Learning to Adapt SFT Data for Better Reasoning Generalization
published: "2026-05-26T12:20:53Z"
authors: Lisong Sun, Li Wang, Chen Zhang, Jinyang Wu, Kui Zhang, Tianhao Peng, Wenjun Wu
url: http://arxiv.org/abs/2605.26924v1
type: paper-summary
tags: [paper-summary, arxiv]

---

## Summary

Placeholder summary — please add a concise summary of this paper's key findings and contributions.



# Learning to Adapt SFT Data for Better Reasoning Generalization



**Source**: [Original Paper](http://arxiv.org/abs/2605.26924v1)
## Abstract
Large language models (LLMs) have achieved remarkable progress, with post-training playing a crucial role in enhancing their reasoning capabilities. Among post-training paradigms, supervised fine-tuning (SFT) is widely used: it leverages external data to provide dense supervision and enables efficient training. However, directly fine-tuning on expert data can hurt generalization when the data distribution is mismatched with the target model's own distribution. In this work, we propose Data Adaptation for Reasoning Tuning (DART), which formulates the use of a fixed, potentially distributionally misaligned SFT dataset as an optimization problem over demonstration transformations. DART trains a mapper model with reinforcement learning to convert original SFT data into model-adapted supervision that better matches the target model's distribution and learning preferences. The transformed data are then used for SFT, allowing the target model to better exploit external supervision. Experiments across multiple models and datasets show that DART improves generalization, achieves higher training efficiency than direct RL, and helps models surpass standard SFT. Our code is available at https://anonymous.4open.science/r/DART525E50D.

## Metadata
- **Published**: 2026-05-26T12:20:53Z
- **Authors**: Lisong Sun, Li Wang, Chen Zhang, Jinyang Wu, Kui Zhang, Tianhao Peng, Wenjun Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.26924v1)