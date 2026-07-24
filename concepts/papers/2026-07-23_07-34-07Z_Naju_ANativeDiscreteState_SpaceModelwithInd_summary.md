# Summary: 2026-07-23_07-34-07Z_Naju_ANativeDiscreteState_SpaceModelwithIndependen.md
Saved: 2026-07-24 02:33
Source: 2026-07-23_07-34-07Z_Naju_ANativeDiscreteState_SpaceModelwithIndependen.md
Model: None

---

## Summary  
The paper introduces Naju, a native discrete state‑space model that simultaneously achieves near‑lossless retention of long‑sequence bindings and effective overwriting of stale ones. It argues that the common practice of discretizing continuous‑time SSMs via zero‑order‑hold is unnecessary for memory tracking and instead proposes a direct parameterization of the discrete transition. By factoring the recurrence into an explicit forget gate \(f_n\), an independent write gain \(i_n\), and input‑dependent read/write maps, Naju removes stability constraints that couple retention and writing in coupled designs. Empirically, Naju outperforms Mamba at four times the training length while preserving linear‑time, linear‑memory scaling.

## Key Contributions  
- [Finding 1] Direct parameterization of the discrete SSM transition eliminates the need for continuous‑time zero‑order‑hold discretization and yields a theoretically grounded fading‑memory/BIBO bound.  
- [Finding 2] Decoupling the forget gate \(f_n\) from the write gain \(i_n\) removes the coupling constraint \(|r|+w\le 1\), enabling strong retention and writing simultaneously.  
- [Finding 3] Naju achieves superior performance on long‑sequence tasks, outperforming Mamba in principal comparisons while remaining competitive with Transformers.

## Methodology  
The authors model the state update as \(x_n = f_n \odot x_{n-1} + i_n \odot (B_n u_n)\), where \(f_n\) is a sigmoid‑bounded forget gate (0 < \(f_n\) < 1) providing exponential decay of frozen coordinates, \(i_n\) is an independent write gain that controls how new information overwrites old content, and \(B_n\) are read/write matrices that depend on the input at time n. This factorization yields a discrete transition that can be trained end‑to‑end without any stability regularizer.

## Results  
Theoretically, under uniform boundedness assumptions the model satisfies a fading‑memory/BIBO bound with no additional constraints. Experimentally, Naju maintains strong recall and overwriting capabilities at 4× the training length, outperforming Mamba in the evaluation suite while matching Transformer performance. Crucially, it retains linear‑time computation and linear memory usage.

## Significance  
Naju provides a theoretically sound alternative to continuous‑time SSMs for long‑range memory tasks, decoupling retention and writing to avoid the trade‑off inherent in coupled designs. This enables more efficient long‑sequence models that can be deployed without extra hardware or stability tricks, advancing both theory and practice in sequence modeling.

## Related Concepts  
fading memory, BIBO bound, Schur stability, zero‑order‑hold discretization, state‑space models, Mamba, Transformer, linear scaling.
