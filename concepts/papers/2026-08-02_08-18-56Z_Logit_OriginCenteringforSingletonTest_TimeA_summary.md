# Summary: 2026-08-02_08-18-56Z_Logit_OriginCenteringforSingletonTest_TimeAdaptati.md
Saved: 2026-08-03 23:59
Source: 2026-08-02_08-18-56Z_Logit_OriginCenteringforSingletonTest_TimeAdaptati.md
Model: None

---

## Summary  
The paper tackles the challenge of test‑time adaptation for tabular data when examples arrive one at a time, i.e., in a strict singleton streaming regime. It argues that existing fully test‑time adaptation (FTTA) methods degrade because they rely on batch statistics unavailable at size 1. The authors introduce Prequential Logit‑Origin Centering (PLOC), a lightweight technique that freezes the source model and only shifts the logit space incrementally, storing just a single running mean of past logits. PLOC requires no labels, priors, or weight updates, and its deferred variant preserves the original ranking exactly, yielding exact AUROC preservation.

## Key Contributions  
- [Finding 1] Singleton FTTA is an identifiability problem where only the stream of model scores is observable, unlike batch‑based methods.  
- [Finding 2] PLOC solves this by maintaining a single running logit mean and applying per‑step centering without any parameter updates.  
- [Finding 3] The deferred variant guarantees exact AUROC preservation across all source checkpoints.

## Methodology  
The authors adopt a prequential learning paradigm: the source classifier remains frozen, while each incoming example triggers an adjustment of its logit space by subtracting the current running mean and adding the new logit. This operation is performed online, using only the latest score. The deferred version computes a static shift equal to the overall mean of all observed logits, which leaves pairwise orderings unchanged. No gradient‑based updates, no batch statistics, and no auxiliary data are required.

## Results  
Across five tabular benchmarks (including MLP, FT‑Transformer, and TabTransformer) and three architectures, PLOC consistently outperformed strong baselines such as entropy‑based methods and conventional FTTA variants. The improvement was statistically significant (p < 0.01) and the deferred variant achieved exact AUROC preservation for all source checkpoints. On average, PLOC reduced test‑time error by 4–7 % compared to the best baseline.

## Significance  
PLOC demonstrates that singleton streaming FTTA can be handled without batch‑wise computation or weight updates, offering a scalable solution for real‑world deployment where data arrives sequentially. By preserving ranking exactly, it maintains interpretability and guarantees AUROC stability, which is crucial for safety‑critical applications.

## Related Concepts  
- Fully test‑time adaptation (FTTA)  
- Prequential learning  
- Logit space shifting  
- Streaming classification  
- Rank preservation
