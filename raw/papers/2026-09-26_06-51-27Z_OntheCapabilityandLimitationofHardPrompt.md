---
title: On the Capability and Limitation of Hard Prompt
published: 2026-09-26T06:51:27Z
authors: Lijia Yu, Shuaitong Liu, Gaojie Jin, Xinyu Li, Xiao-Shan Gao
url: http://arxiv.org/abs/2609.32302v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On the Capability and Limitation of Hard Prompt

## Abstract
Prompt engineering has become an indispensable tool for using large language models (LLMs), turning LLMs into task-specific experts without changing their weights. Despite notable theoretical advances in prompt engineering, the theory for the more practical hard or discrete prompts is largely open. In this paper, we try to fill this gap either by providing a complete solution or by making substantial progress on the three core theoretical questions regarding hard prompts. First, we show that determining the existence of a hard prompt for a transformer to solve a downstream task is NP-complete and that finding an optimal hard prompt is NP-hard, which is the first computational complexity result for hard prompting, as far as we know. Second, we show that, unlike soft or continuous prompts, hard prompts have essential limitations: hard prompts are not complete; short hard prompts do not significantly enhance the ability of transformers; and long hard prompts exhibit the "prompt dominating answer phenomenon," meaning that, with high probability, the same answer is given for all queries of the same length. On the other hand, linear hard prompts do not have the limitations of short or long prompts. Third, we provide a tight bound on the size of the task in terms of the prompt length for the performance of prompts on the finite task to generalize to the entire data distribution, leading to a necessary and sufficient condition for generalizability. This is the first result on generalization for prompting, as far as we know. Our findings not only offer the first theoretical insights into hard prompts but also provide provably reliable practical guidance for real-world LLM usage.

## Metadata
- **Published**: 2026-09-26T06:51:27Z
- **Authors**: Lijia Yu, Shuaitong Liu, Gaojie Jin, Xinyu Li, Xiao-Shan Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32302v1)