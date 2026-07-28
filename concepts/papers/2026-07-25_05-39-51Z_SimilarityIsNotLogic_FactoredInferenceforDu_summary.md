# Summary: 2026-07-25_05-39-51Z_SimilarityIsNotLogic_FactoredInferenceforDual_Enco.md
Saved: 2026-07-27 22:33
Source: 2026-07-25_05-39-51Z_SimilarityIsNotLogic_FactoredInferenceforDual_Enco.md
Model: None

---

## Summary  
Dual‑encoder vision‑language models (VLMs) expose a similarity interface that is intended for zero‑shot retrieval but often fails to respect logical constraints, such as “umbrella and no person,” by retrieving images that contain both objects. The authors attribute this failure to an interface‑level bag‑of‑concepts effect in which similarity scores are approximated by mean pooling of concept evidence, completely ignoring the meaning of operators. Their core insight is that operator‑dependent signals in text embeddings are either too weak or misaligned with the visual evidence, so fine‑tuning cannot resolve the problem because the bottleneck lies in how evidence is aggregated rather than what is represented. To address this, they introduce factored inference and a training‑free method called Logic‑Constrained Score Editing (LCSE).  

## Key Contributions  
- [Finding 1] The similarity scores approximate mean pooling of concept evidence regardless of logical operators, causing compositional errors in retrieval.  
- [Finding 2] Operator‑dependent signals present in text embeddings are weak or misaligned, so they do not influence the final ranking.  
- [Finding 3] Fine‑tuning does not reliably fix the issue because it targets representation learning rather than the aggregation bottleneck that factored inference seeks to solve.  

## Methodology  
The authors propose factored inference, which separates evidence extraction from constraint execution. Evidence is extracted as concept scores from frozen dual‑encoder encoders, while constraints are applied externally using LCSE, a logic‑constrained score editing technique that edits similarity scores without retraining the models. This approach leverages existing retrieval outputs and applies logical rules to correct misordered results.  

## Results  
On FACTOR‑Bench, LCSE achieves 85.5 % accuracy compared with 73.2 % for the best fine‑tuned baseline; when applied to SigLIP 2 it reaches 90.7 %. The method also improves NegBench COCO MCQ performance from 27.2 % to 65.2 % while preserving standard retrieval accuracy, demonstrating a substantial boost in zero‑shot logical reasoning.  

## Significance  
This work reveals that the core problem of dual‑encoder VLMs is not poor representation but an aggregation flaw that ignores operator semantics. By providing a training‑free factored inference framework, LCSE offers a scalable solution that can be applied to any existing VLM without additional fine‑tuning, thereby advancing zero‑shot retrieval and logical reasoning in multimodal AI systems.  

## Related Concepts  
Dual‑encoder vision‑language models, bag‑of‑concepts effect, factored inference, Logic‑Constrained Score Editing (LCSE), FACTOR‑Bench benchmark, concept scores, operator independence, zero‑shot retrieval, compositional reasoning.
