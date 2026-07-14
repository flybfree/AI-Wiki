---

title: "Summary: STRIDE: Training Data Attribution via Sparse Recovery from Subset Perturbations"
url: http://arxiv.org/abs/2606.05165v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-03_17-59-36Z_STRIDE_TrainingDataAttributionviaSparseRecoveryfro.md
generated_at: "2026-06-11 10:52"
model: nvidia/nemotron-3-nano-4b

---
# Summary: 2026-06-03 17-59-36Z Stride Trainingdataattributionviasparserecoveryfro


## Summary
This paper introduces STRIDE, a method for attributing model predictions to specific training examples without costly retraining or gradient tracking. By modeling data influence in the activation space and solving it as a sparse recovery problem, STRIDE recovers individual example contributions efficiently. The approach achieves state‑of‑the‑art performance on LLM pre‑training attribution while being an order of magnitude faster than prior techniques.

## Key Takeaways
- STRIDE treats training data attribution as a compressive sensing task, learning lightweight steering operators that approximate the functional shift caused by subset perturbations.  
- The framework recovers sparse linear decompositions of example influences directly from perturbed test predictions, avoiding per‑parameter gradient computation.  
- Experiments demonstrate that STRIDE is 13× faster than previous state‑of‑the‑art methods while maintaining comparable or better attribution accuracy.

## Context
Attribution in large language models remains a bottleneck because causal interventions require full retraining, which is infeasible for billions of parameters. Existing gradient‑based approaches suffer from computational cost and local approximation errors. This work offers a scalable alternative that operates on the activation level rather than the parameter space.

## Implications
StrIDE enables practitioners to identify data contamination or select high‑impact training samples without retraining, accelerating model development cycles. The method’s efficiency could be adopted across AI pipelines, fostering trustworthy AI by providing transparent attribution insights.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.05165v1)
