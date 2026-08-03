---
title: On the Generalization of Steering Vectors for Chain-of-Thought Faithfulness
published: 2026-07-31T06:30:45Z
authors: Matthew Nguyen, Kyle Cox, Austin Meek, Iván Arcuschin
url: http://arxiv.org/abs/2607.29062v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On the Generalization of Steering Vectors for Chain-of-Thought Faithfulness

## Abstract
Model capabilities have improved in large part due to scaling chain of thought. This has been a promising development for AI safety--where models verbalize their reasoning, it is possible to monitor it. However, in some cases, models do not verbalize important steps in their reasoning process. For example, models prompted with a cue suggesting the incorrect answer may fail to acknowledge that cue, even when it appears instrumental to their conclusion. When chain of thought (CoT) fails to disclose instrumental reasoning steps, we describe it as unfaithful. Prior work has shown that activation steering can be a useful method to improve faithfulness in CoT. We extend this line of work by studying how well steering for faithfulness generalizes across cue types, datasets, and methods of constructing the steering vector for three models (Gemma-3 4B, Qwen-3.5 9B, Gemma-3 12B) in a cued question-answering setting. While steering reliably increases cue acknowledgment for only the largest model (Gemma-3 12B), we find that when steering is effective, its effect generalizes broadly across cue types and datasets--in cross-cue and cross-dataset analyses, effect size is determined primarily by the evaluation setting, rather than the vector's train setting. How the vector is built also matters little--four construction methods, including one whose optimization target mentions no specific cue, yield similar effect sizes. Finally, we consider the possibility that steering promotes the salience of the cue and causes greater cue use, rather than targeting verbalization behaviors. However, we find no evidence for this--steering leaves the rate of cue use roughly unchanged while reducing hidden cue use, i.e., cue use that is not acknowledged.

## Metadata
- **Published**: 2026-07-31T06:30:45Z
- **Authors**: Matthew Nguyen, Kyle Cox, Austin Meek, Iván Arcuschin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29062v1)