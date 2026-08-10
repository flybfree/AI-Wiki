---
title: CreativeInstruct: Scalably Teaching LLMs to Balance Quality, Creativity, and Diversity
published: 2026-08-07T17:55:48Z
authors: Ananya Sahu, Mohit Bansal, Elias Stengel-Eskin
url: http://arxiv.org/abs/2608.07460v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CreativeInstruct: Scalably Teaching LLMs to Balance Quality, Creativity, and Diversity

## Abstract
While post-training improves the capabilities of large language models (LLMs), it generally lowers their output diversity and creativity, negatively impacting tasks that explicitly require creativity (e.g., story generation) as well as those that require it implicitly, e.g., reinforcement learning (RL). We instead propose CreativeInstruct, a scalable instruction-tuning method that teaches LLMs to balance creative, base-model-like generations with the quality of post-trained models, by learning to inject special [StartCreativity] spans that bias generation toward creativity. Furthermore, we introduce a structural diversity metric based on graph edit distance, which captures narrative level variation missed by purely lexical and semantic metrics. On narrative generation, CreativeInstruct matches or exceeds the diversity of both multi-model baselines and distilled variants of their outputs, without sacrificing quality or requiring multiple models at inference time. These results are mirrored in our human evaluation, where we find that annotators rate CreativeInstruct generations as more creative than the post-trained LLMs' generations in 70.3% of cases. We also show the benefits of creative models as a substrate for RL: GRPO applied to a CreativeInstruct checkpoint improves by ~4% on AMC and ~5% points on MATH over the same training applied to the post-trained checkpoint.

## Metadata
- **Published**: 2026-08-07T17:55:48Z
- **Authors**: Ananya Sahu, Mohit Bansal, Elias Stengel-Eskin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07460v1)