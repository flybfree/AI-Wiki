# Summary: 2026-07-23_07-34-07Z_Naju_ANativeDiscreteState_SpaceModelwithIndependen.md
Saved: 2026-07-24 02:43
Source: 2026-07-23_07-34-07Z_Naju_ANativeDiscreteState_SpaceModelwithIndependen.md
Model: None

---

## Summary  
The paper introduces **Naju**, a native discrete state‑space model that explicitly separates long‑sequence retention from active overwriting, arguing that existing continuous‑time SSMs such as Mamba rely on an unnecessary zero‑order‑hold discretization. By factoring the recurrence into an explicit forget gate \(f_n\), an independent write gain \(i_n\), and input‑dependent read/write maps, Naju achieves strong retention and overwriting at four times the training length while retaining linear‑time, linear‑memory scaling. Theoretical analysis shows that this decoupling removes stability constraints, providing a BIBO bound without extra regularizers.

## Key Contributions  
- [Finding 1] Naju decouples the effective retention \(r\) from the write gain \(w\), eliminating the constraint \(|r|+w\le 1\).  
- [Finding 2] The model maintains linear‑time, linear‑memory complexity and outperforms Mamba on long‑sequence benchmarks.  
- [Finding 3] Uniform boundedness guarantees a fading‑memory/BIBO bound under no additional stability regularizer.

## Methodology  
The authors propose a discrete state‑space update \(x_n = f_n \odot x_{n-1} + i_n \odot (B_n u_n)\). The forget gate \(f_n\) is learned as a sigmoid, the write gain \(i_n\) as a scalar multiplier, and \(B_n\) as read/write matrices. This formulation avoids continuous‑time discretization entirely, yielding a native discrete recurrence that directly models retention and writing.

## Results  
Experiments on WikiText‑103 language modeling, Long Range Arena, and multi‑query associative recall demonstrate that Naju consistently matches or exceeds Mamba performance while staying competitive with Transformers. Theoretical analysis confirms the model satisfies a fading‑memory/BIBO bound under uniform boundedness assumptions, preserving linear scaling.

## Significance  
By removing the coupling between retention and writing, Naju offers a principled alternative to continuous‑time SSMs that can achieve both long‑range memory and efficient overwriting without sacrificing stability. This opens pathways for more scalable and reliable long‑sequence models in AI research.

## Related Concepts  
- State‑space models (SSMs)  
- Forgetting gates  
- Write gains  
- BIBO stability  
- Schur‑stability  
- Mamba (continuous‑time SSM)  
- Transformers  
- Linear scaling  

The paper thus advances the field by providing a theoretically grounded, native discrete architecture that balances retention and writing while preserving computational efficiency.
