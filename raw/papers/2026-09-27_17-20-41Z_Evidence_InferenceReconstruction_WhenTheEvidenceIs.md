---
title: Evidence-Inference Reconstruction: When The Evidence Is Recalled But The Reasoning Goes Wrong
published: 2026-09-27T17:20:41Z
authors: Megan Diehl, Ser-Nam Lim
url: http://arxiv.org/abs/2609.33778v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evidence-Inference Reconstruction: When The Evidence Is Recalled But The Reasoning Goes Wrong

## Abstract
Modern multi-hop LLM agents are equipped with built-in mechanisms to detect errors in intermediate reasoning steps. Such errors trigger corrective actions from these agents, which mostly follow the paradigm of retrying the steps or the reasoning trajectories. Not only are these retries expensive, we present in this paper that they are also potentially unnecessary. To this end, we introduce Evidence-Inference Reconstruction (EIR), which uses structured state to guide one retrieval trajectory, accumulating source evidence in the process. We show that as long as the relevant evidence has been collected, EIR is capable of generating the correct answer in a single final model call even if erroneous evidence has been mixed in due to incorrect intermediate reasoning steps. In one evaluation, using Haiku 4.5 and GPT-4.1 Mini, we evaluate EIR on matched 1,000-question subsets of HotpotQA, 2WikiMultiHopQA, and MuSiQue, showing that EIR improves Answer F1, the overlap between the model's and the correct answer, over the baseline by 8.3--32.8 points, Agentic SSR by 10.6--29.1 points, and Reflexion by 1.1--15.9 points. Additionally, we show that EIR averages 4.85 total model calls per question, compared with 35.29 for Agentic SSR and 12.41 for Reflexion. Together, these results corroborate EIR's central premise: separating evidence retrieval from the final answer model call can improve answer accuracy while utilizing substantially less computation.

## Metadata
- **Published**: 2026-09-27T17:20:41Z
- **Authors**: Megan Diehl, Ser-Nam Lim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.33778v1)