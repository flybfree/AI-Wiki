# Summary: 2026-08-04_06-59-29Z_SAKI_Score_AwareLow_RankKeyIndexingwithRandom_Matr.md
Saved: 2026-08-06 21:39
Source: 2026-08-04_06-59-29Z_SAKI_Score_AwareLow_RankKeyIndexingwithRandom_Matr.md
Model: None

---

## Summary  
The paper introduces SAKI, a training‑free key indexing scheme that directly preserves the attention scores generated during inference rather than merely compressing keys or preserving weight variance. By analyzing how low‑rank compression distorts these scores, the authors derive a covariance‑weighted loss that better reflects the true signal. They show that an optimal rank can be obtained analytically via SVD of this weighted operator, leading to a closed‑form asymmetric factorization. SAKI replaces conventional PCA‑style key indexing with a method that corrects random‑matrix noise and matches PCA’s calibration cost while delivering superior recall.

## Key Contributions  
- [Finding 1] The expected distortion caused by rank‑r key compression is modeled as a covariance‑weighted objective, which directly ties the index to the attention scores rather than reconstruction quality.  
- [Finding 2] An asymmetric SVD factorization of this weighted operator yields an optimal low‑rank solution that can be computed without retraining the model.  
- [Finding 3] Random‑matrix theory is used to separate genuine covariance signal from autocorrelated sampling noise, allowing SAKI to achieve gains where PCA finds no reliable information.

## Methodology  
The authors first compute the covariance matrix of query‑key pairs across a calibration set and define a low‑rank approximation that minimizes the expected score error. This leads to a loss function that is weighted by the covariance of each key, producing a “score‑aware” objective. By performing SVD on the covariance‑weighted query‑key operator, they obtain an asymmetric factorization that directly preserves the most informative components of the attention scores. Random‑matrix analysis then isolates genuine signal from noise, enabling SAKI to correct the index without additional calibration beyond 512 tokens.

## Results  
Across LLaMA 3.1 8B, Qwen 2.5 7B, Mistral 7B v0.1, and Llama 3.2 3B, SAKI consistently outperforms key PCA at every rank tested. At rank 32 it reduces the top‑64 recall error by 13–30 percent (e.g., LLaMA 3.1 8B improves from 0.748 to 0.799). It boosts attention‑head coverage by 68–89 percent, with the largest gains in deeper layers. Predicted score MSE reductions correlate strongly with empirical measurements (Pearson r = 0.997), confirming that the improvement stems from optimizing the attention‑score objective rather than covariance weighting alone.

## Significance  
SAKI demonstrates that a training‑free indexing method can directly preserve the most relevant information—attention scores—leading to measurable gains in generation quality without retraining or additional calibration data. By leveraging covariance‑weighted loss and random‑matrix theory, it outperforms established low‑rank techniques like PCA, especially where PCA’s signal is weak.

## Related Concepts  
- Low‑rank key indexing (e.g., PCA)  
- Covariance weighting of attention scores  
- Random‑matrix theory for noise correction  
- SVD factorization and asymmetric decomposition  
- KV cache compression in transformer inference
