---
title: When Skills Meet Safety: Benchmarking and Characterizing the Adaptive Jailbreak Robustness of Skill-Merged LLMs
published: 2026-08-09T07:41:06Z
authors: Yu Ma, Hongli Shi, Jing Li, Xinran Xu, Weiwei Hou
url: http://arxiv.org/abs/2608.08542v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Skills Meet Safety: Benchmarking and Characterizing the Adaptive Jailbreak Robustness of Skill-Merged LLMs

## Abstract
Model merging has become the default way to give an aligned language model new skills without retraining: a practitioner folds task vectors from math, code, or domain specialists into a safety-aligned base using task arithmetic, TIES, or DARE. This convenience is known to carry a safety cost, but almost all of that evidence rests on static refusal tests: fixed harmful prompts scored for compliance. We argue this is misleading. Because safety alignment is "shallow," concentrated in the first few generated tokens, a merged model's static refusal can stay clean while a real adaptive attack still breaks it. We introduce SkillSafe-Bench, a controlled benchmark that scores skill-merged models on static refusal, adaptive jailbreak robustness, and capability retention under a conservative two-judge AND rule. Across six open-weight bases (five families, two scales), static safety does not predict robustness to attack: under a semantic template attack, safe-looking merges on the fragile bases (both Qwen scales and Gemma) are jailbroken 60-76% of the time while others (Llama, Phi-4) stay robust. We further show the static effect of merging is base-conditional, characterize same-recipe abliteration-style safety erosion through a data-free geometric signal (the overlap of a task vector with a safety subspace), and outline SubSafe-Merge, which projects this overlap away to remove that erosion at held capability. Adaptive evaluation is not optional for merged LLMs: the models that most need it look safe under static screening.

## Metadata
- **Published**: 2026-08-09T07:41:06Z
- **Authors**: Yu Ma, Hongli Shi, Jing Li, Xinran Xu, Weiwei Hou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08542v1)