# Summary: 2026-07-30_12-07-56Z_FromExpertReductiontoBehavioralDivergence_TracingN.md
Saved: 2026-07-30 21:49
Source: 2026-07-30_12-07-56Z_FromExpertReductiontoBehavioralDivergence_TracingN.md
Model: None

---

## Summary  
The paper investigates why mathematically equivalent expert‑reduction orders can lead to different sparse‑MoE execution outcomes, focusing on DeepSeek‑V4‑Flash. It isolates the effect by freezing MoE state and varying aggregation semantics across four operand‑accumulator precision schemes. The study reveals that B‑mode reduction yields multiple continuation basins and downstream token‑level divergences, while C‑mode preserves native routes. This work establishes a numerical compatibility contract for sparse‑MoE runtimes.  

## Key Contributions  
- [Finding 1] The observation that identical expert‑reduction orders produce distinct MoE execution paths due to operand representation and accumulator precision differences.  
- [Finding 2] Identification of 720 A‑mode orders yielding 10 basins versus 720 B‑mode orders forming 360 structural classes and 11 basins, with prompt‑specific splits into layoffs/hiring/other continuations.  
- [Finding 3] Demonstration that post‑mHC state is an intra‑token boundary while full persistent state spans token boundaries, enabling exact reconstruction of downstream trajectories.  

## Methodology  
The authors freeze the local MoE state at layer‑5 for each scheme and vary only aggregation semantics (A, B, C). They generate a fixed Chinese prompt and track continuation basins across 192 trajectories per scheme. They compare native MoE, post‑mHC, next‑router, LM states bitwise to verify persistence. For one controlled B branch they reconstruct the exact post‑mHC endpoint and decode‑boundary outcomes.  

## Results  
Across all schemes, P32, A, and B change every native‑reference route trajectory, while C preserves routes, token sequences, and texts. Post‑mHC checkpoint reconstruction matches 301 downstream states, checkpoints, routes, predictions, and text over seven steps when the same natural next input is used. These controls confirm that identical tokens do not guarantee identical autoregressive state.  

## Significance  
This work shows that numerical compatibility—operand conversion, accumulator precision, reduction order—is a contract required by sparse‑MoE runtimes and hardware backends. It provides controlled causal evidence of divergence rather than deployment incidents, limiting C’s invariance to six‑term states only.  

## Related Concepts  
Expert reduction orders, MoE state persistence, post‑mHC boundary, accumulator precision, continuation basins, numerical compatibility contract, sparse‑MoE runtime semantics.
