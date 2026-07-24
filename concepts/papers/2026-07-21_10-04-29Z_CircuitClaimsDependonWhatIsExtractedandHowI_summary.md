# Summary: 2026-07-21_10-04-29Z_CircuitClaimsDependonWhatIsExtractedandHowItIsComp.md
Saved: 2026-07-24 00:42
Source: 2026-07-21_10-04-29Z_CircuitClaimsDependonWhatIsExtractedandHowItIsComp.md
Model: None

---

## Summary  
The paper argues that the meaning of a circuit extracted from a neural network is not intrinsic; it depends on which subgraph is chosen and how that subgraph is compared to alternatives. By constructing a synthetic Lean proof‑prediction benchmark, the authors demonstrate that differences between reported circuits can be traced to random choices in surface form or checkpoint initialization rather than to genuine task‑specific mechanisms. Their experiments show that circuit‑level claims are only well defined once the extraction criteria—such as pruning threshold and comparison level—are explicitly stated. This work introduces a reporting practice that makes these dependencies transparent for future studies.

## Key Contributions  
- [Finding 1] The claim that a circuit “preserves behavior” is under‑determined: multiple distinct circuits can achieve the same effect, so attributing causality to any one of them is arbitrary.  
- [Finding 2] In their benchmark, component‑to‑component edge overlap between extracted circuits is low and highly sensitive to how attention heads are represented (joint vs. separate) and which checkpoint initializes reinforcement learning.  
- [Finding 3] Only two coarse summaries remain stable across experiments: the set of selected attention heads and a ranking of circuit sizes based on supervised checkpoint initialization.

## Methodology  
The authors built a synthetic Lean tactic‑prediction task where proof rules are fixed but their surface forms vary randomly, allowing the network to learn only the logical structure. They trained two transformer models at dense checkpoints (all weights present) and sparse checkpoints (most weights zero). For each checkpoint they extracted three possible circuits: a compact prediction‑preserving subgraph, a broader graph that retains surrounding read/write/routing structure, and the smallest subgraph above a loss threshold. Attention heads could be represented jointly or separately in the circuit. The experiments varied these extraction choices and compared the resulting circuits to assess their stability.

## Results  
Exact edge overlap between the three extracted circuits dropped to near‑random levels when attention heads were split, indicating that the reported circuit is not uniquely identifiable. However, the set of selected attention heads remained consistent across conditions, and a ranking of circuit sizes based on which supervised checkpoint initialized reinforcement learning was stable. The largest accuracy improvements from RL occurred only when the circuit included more structural information beyond atomic rules, suggesting that richer summaries better capture genuine task mechanisms.

## Significance  
By exposing how arbitrary choices in circuit extraction can masquerade as mechanistic insight, this work clarifies a long‑standing ambiguity in AI interpretability research. It provides a concrete framework for reporting extraction criteria, which will help researchers avoid misleading claims about neural network behavior and guide more rigorous evaluation of learned mechanisms.

## Related Concepts  
- Circuit extraction  
- Ablation studies  
- Attention head representation (joint vs. separate)  
- Reinforcement learning initialization  
- Component‑to‑component edge overlap  
- Synthetic benchmarking for mechanistic analysis
