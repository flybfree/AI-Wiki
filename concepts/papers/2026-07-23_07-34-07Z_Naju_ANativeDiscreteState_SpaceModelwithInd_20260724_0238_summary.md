# Summary: 2026-07-23_07-34-07Z_Naju_ANativeDiscreteState_SpaceModelwithIndependen.md
Saved: 2026-07-24 02:38
Source: 2026-07-23_07-34-07Z_Naju_ANativeDiscreteState_SpaceModelwithIndependen.md
Model: None

---

## Summary  
The paper introduces **Naju**, a native discrete state‑space model that explicitly separates the mechanisms of long‑sequence memory: retention and overwriting. By factoring the recurrence into an explicit forget gate \(f_n\) (a sigmoid pole) and an independent write gain \(i_n\), Naju removes the coupling constraint that previously forced strong retention to entail weak writing. Empirically, Naju matches or exceeds the performance of Mamba on long‑range tasks while preserving linear‑time, linear‑memory scaling. The model is evaluated across WikiText‑103 language modeling, Long Range Arena, and multi‑query associative recall, demonstrating robust gains at four times the training length.

## Key Contributions  
- [Finding 1] Naju factorizes the recurrent update as \(x_n = f_n\odot x_{n-1} + i_n\odot(B_n u_n)\), introducing an explicit discrete pole \(f_n\) and a separate write gain \(i_n\).  
- [Finding 2] The decoupling eliminates the theoretical limitation \(|r|+w \le 1\), allowing both high retention \(r\) and high writing \(w\) simultaneously.  
- [Finding 3] Naju satisfies a fading‑memory/BIBO bound under uniform boundedness, providing a stability guarantee without additional regularizers.

## Methodology  
Rather than discretizing continuous‑time SSMs via zero‑order hold (as Mamba does), the authors treat the recurrence directly in discrete time. The forget gate \(f_n\) is parameterized by a sigmoid ensuring \(0< f_n < 1\), guaranteeing Schur‑stability for each frozen local coordinate. The write gain \(i_n\) multiplies an input‑dependent read/write matrix \(B_n u_n\). This factorization yields the update rule  
\[
x_n = f_n \odot x_{n-1} + i_n \odot (B_n u_n),
\]  
where \(\odot\) denotes element‑wise multiplication. The model is trained end‑to‑end on standard language‑model objectives, and its memory capacity is measured by retention over long horizons.

## Results  
Naju consistently outperforms Mamba at 4× the training length while maintaining strong forgetting of stale bindings. On WikiText‑103 it achieves a perplexity comparable to Transformers but with lower variance; on Long Range Arena and multi‑query associative recall, Naju’s accuracy exceeds Mamba by up to 2 % without increasing memory usage. Crucially, the model scales linearly in both time and memory: processing \(T\) tokens requires \(O(T)\) operations and \(O(1)\) additional space per token.

## Significance  
By removing the coupling between retention and writing, Naju offers a theoretically grounded architecture that can store long‑range information efficiently. This enables future work to design models where high‑capacity memory is not sacrificed for fast updates, potentially unlocking new applications in retrieval, planning, and continual learning without sacrificing stability.

## Related Concepts  
- State‑space model (SSM)  
- Discrete recurrence  
- Forget gate / pole  
- Write/read maps  
- BIBO bound  
- Schur‑stability  
- Fading memory  
- Linear‑time, linear‑memory scaling
