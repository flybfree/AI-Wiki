# Summary: 2026-07-23_17-11-34Z_LearningWhatMatters_SupervisingSparseAttentionRout.md
Saved: 2026-07-26 21:28
Source: 2026-07-23_17-11-34Z_LearningWhatMatters_SupervisingSparseAttentionRout.md
Model: None

---

## Summary  
The paper investigates whether sparse attention selectors trained on teacher attention patterns correctly capture the causal evidence that drives model answers, and proposes using masked context to generate causal evidence sets without annotation. It demonstrates that attention often misaligns with true dependencies, leading to poor selector performance. In a two‑step retrieval task, selectors trained on causal evidence achieve near‑perfect accuracy while those trained on attention fail dramatically. The method also applies to pretrained models such as Qwen2.5‑3B and Gemma‑2‑9B.  

## Key Contributions  
- Attention patterns do not always reflect the actual causal dependencies that drive model answers.  
- Causal evidence sets derived solely from masking can train sparse selectors with high accuracy, matching teacher performance.  
- The approach reveals systematic mismatches in pretrained models across conflicting‑fact examples.  

## Methodology  
The authors construct a two‑step retrieval task where each answer is supported by a known evidence set. By randomly masking portions of the context and observing whether the answer changes, they infer causal evidence sets without labeling. These evidence sets are used to fine‑tune sparse attention selectors instead of using teacher attention patterns.  

## Results  
In the controlled task, selector accuracy jumps from 41 % (attention‑trained) to 99 % (causal‑evidence trained). On pretrained models, Qwen2.5‑3B shows 58 % attention on outdated facts despite correct answers; restricting to two relevant sentences improves Gemma‑2‑9B accuracy from 56 % to 99 %. The causal evidence outperforms attention as a training target across regimes.  

## Significance  
This work decouples observation (attention) from computation (causal dependence), offering a principled way to design efficient sparse models that attend only where needed, reducing cost and improving performance without costly annotation.  

## Related Concepts  
Sparse attention, causal evidence sets, teacher‑student distillation, masked context analysis, pretrained model alignment, retrieval tasks.
