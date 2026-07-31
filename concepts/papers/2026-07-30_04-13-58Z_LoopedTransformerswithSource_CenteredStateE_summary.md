# Summary: 2026-07-30_04-13-58Z_LoopedTransformerswithSource_CenteredStateEvolutio.md
Saved: 2026-07-30 21:38
Source: 2026-07-30_04-13-58Z_LoopedTransformerswithSource_CenteredStateEvolutio.md
Model: None

---

## Summary  
Looped Transformers reuse a single Transformer block across varying depths to increase effective depth without adding parameters, but the shared recurrence is compromised by input‑conditioned signals that can shift hidden states even when the reference point should remain fixed. This paper introduces Source‑Centered State Evolution (SCSE), a design that preserves exact anchor invariance while still allowing state‑dependent computation through learned deviations. SCSE achieves this by forcing zero deviation to map to no update, using a mask that guarantees the anchor is a one‑step fixed point, and letting nonzero deviations drive recurrent dynamics. The approach reconciles input conditioning with reference preservation in a principled way.

## Key Contributions  
- [Finding 1] SCSE provides exact anchor invariance by enforcing a zero‑deviation forcing bias through a mask that maps any deviation to no state change, making the anchor a true fixed point for all depths.  
- [Finding 2] The primary gains in recurrent quality stem from two learned components: (i) an input‑conditioned anchor that captures the source signal, and (ii) an initial deviation recurrence that propagates state updates only when nonzero.  
- [Finding 3] Training a model reveals observable recurrent motion; the magnitude of deviations correlates with task performance, providing a diagnostic tool for diagnosing loop behavior.

## Methodology  
The authors propose SCSE as a modification to additive‑injection looped Transformers. At each recurrent step they compute an anchor value from the input and an initial deviation that is learned jointly. The zero‑deviation mask ensures that when the deviation equals zero, no hidden state update occurs, preserving the reference point exactly. Nonzero deviations are propagated through a recurrence that depends on both the anchor and the previous state, allowing conditional computation while still respecting the source‑centered design.

## Results  
Empirical evaluation on WikiText‑2, WikiText‑103, direct web‑corpus pretraining, held‑out web‑text transfer, and LAMBADA completion shows that SCSE improves the controlled recurrent quality frontier across all tasks. Ablation studies confirm that removing either the learned anchor or the deviation recurrence reduces performance, indicating these components are essential. Additionally, a trained‑model case study demonstrates that deviations follow expected patterns, supporting the diagnostic claim.

## Significance  
SCSE offers a principled solution to a longstanding tension in looped Transformers: maintaining exact reference points while enabling state‑dependent computation without extra parameters. By eliminating the harmful zero‑deviation bias and grounding updates in a learned anchor, it yields higher performance on downstream tasks with minimal architectural overhead.

## Related Concepts  
- Looped Transformers  
- Source‑Centered State Evolution (SCSE)  
- Zero‑deviation mask  
- Learned anchor  
- Input conditioning  
- Recurrent quality frontier
