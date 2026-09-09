---
title: Personalizing LLM Agent Memory Using Biometrics
published: 2026-09-08T10:46:12Z
authors: Yanhong Qian, Qingguo Meng, Shihao Ding, Xingbo Dong, Zhe Jin, Hanrui Wang, Isao Echizen
url: http://arxiv.org/abs/2609.08558v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Personalizing LLM Agent Memory Using Biometrics

## Abstract
Personalized memory helps LLM agents deliver stable, tailored assistance by storing and reusing user-specific data across interactions. In multi-user scenarios, however, retrieval must consider not only semantic similarity but also whether the current requester matches the identity associated with the stored memory. We propose Bio-Memory, a biometric-aware memory architecture that conditions memory retrieval on both semantic similarity and biometric matching. Built on top of A-Mem, Bio-Memory augments each atomic memory note with a biometric embedding and uses biometric matching to form the retrieval candidate pool before semantic ranking. We evaluate Bio-Memory on LoCoMo in a 10-user shared-agent setting over 7 face benchmarks and 10 palmprint protocols. Across datasets, Bio-Memory consistently separates owner and non-owner queries. Under face-based personalization, the largest average gap reaches 27.29% / 21.15% in F1 / BLEU-1 on CALFW; under palmprint-based personalization, the corresponding gap is 25.75% / 19.22% on MS_Blue. These results support biometrics as a practical control signal for personalized memory retrieval in shared environments.

## Metadata
- **Published**: 2026-09-08T10:46:12Z
- **Authors**: Yanhong Qian, Qingguo Meng, Shihao Ding, Xingbo Dong, Zhe Jin, Hanrui Wang, Isao Echizen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.08558v1)