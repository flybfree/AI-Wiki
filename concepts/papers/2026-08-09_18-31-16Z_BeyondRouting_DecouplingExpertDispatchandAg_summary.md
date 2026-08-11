# Summary: 2026-08-09_18-31-16Z_BeyondRouting_DecouplingExpertDispatchandAggregati.md
Saved: 2026-08-10 23:27
Source: 2026-08-09_18-31-16Z_BeyondRouting_DecouplingExpertDispatchandAggregati.md
Model: None

---

## Summary  
The paper investigates whether the two functions in sparse Mixture‑of‑Experts—dispatch of expert selection and aggregation of their outputs—can be treated independently, proposing a decoupled approach via a post‑compute head that adapts weights while keeping dispatch fixed. It experiments on OLMoE‑1B‑7B and DeepSeek‑V2‑Lite, showing that fixing the dispatched experts but allowing adaptive aggregation yields measurable improvements in language modeling and audit metrics. The core contribution is the Fixed‑Dispatch Adaptive Aggregation (FDAA) framework and empirical evidence of its benefits.

## Key Contributions  
- [Finding 1] Decoupling dispatch and aggregation improves model performance on multiple benchmarks.  
- [Finding 2] The top‑scored expert is rarely truly optimal, indicating misalignment between routing and commitment.  
- [Finding 3] FDAA provides a lightweight post‑compute head that adapts aggregation without retraining the backbone.

## Methodology  
The authors keep router mass, selected expert set, and dispatch fixed; they replace the static aggregation weights with a small neural head (FDAA) trained end‑to‑end on the language‑modeling loss while freezing the rest of the system. They evaluate via cross‑entropy gains, test‑set delta CE, and audit experiments measuring vertex identification accuracy.

## Results  
FDAA reduces fresh WikiText‑103 CE by 0.1523 ± 0.0031 across three seeds; mixed‑domain training yields robust gains on WikiText‑103, C4, and PTB under frozen evaluation. The best‑vertex headroom remains significant, but router Top1 identifies the correct expert only 12.5% (WikiText) and 16.7% (C4). One‑seed mixed‑domain replication shows FDAA improves WikiText and PTB while C4 is statistically neutral.

## Significance  
The work reveals that expert selection and commitment are distinct processes; separating them can boost efficiency, especially in large sparse MoE systems where routing overhead dominates. It also provides a practical method (FDAA) to fine‑tune aggregation without full retraining.

## Related Concepts  
Mixture‑of‑Experts, router dispatch, cross‑entropy loss, mixed‑domain training, post‑compute adaptation, vertex identification accuracy, speaker rank correlation.
