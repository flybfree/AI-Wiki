# Summary: 2026-08-07_19-11-54Z_CODS_IterativeBellman_ResidualDataSelectionforReus.md
Saved: 2026-08-10 22:39
Source: 2026-08-07_19-11-54Z_CODS_IterativeBellman_ResidualDataSelectionforReus.md
Model: None

---

## Summary  
Offline reinforcement learning repeatedly trains policies from a fixed transition pool, making redundant data costly across seeds and hyperparameters, while naive subsampling can remove rare transitions needed for long‑horizon credit assignment. CODS introduces a critic‑guided selector that alternates between fitting an algorithm‑matched critic and acquiring high‑residual transitions before freezing a reusable subset, producing a static artifact that refreshes scores as the critic evolves. Unlike prior methods, CODS yields a reusable offline selection procedure rather than a formal coreset guarantee.

## Key Contributions  
- [Finding 1] The iterative Bellman‑residual selector (CODS) balances fitting and acquisition to retain rare high‑value transitions.  
- [Finding 2] CODS produces a static reusable artifact that can be reused across seeds and hyperparameter settings, unlike one‑shot residual selection.  
- [Finding 3] CODS maintains performance comparable to full pool at only 10 % budget, achieving 96.6 % of eligible‑pool performance on D4RL tasks.

## Methodology  
The authors build a critic that matches the algorithm’s reward shaping and computes residuals; high‑residual transitions are prioritized for inclusion in the reusable set; after each acquisition round the selector freezes the current subset, allowing reuse without recomputation. This alternation between fitting (updating residual scores) and acquisition (selecting data) enables a static artifact that refreshes as the critic changes.

## Results  
In 20 D4RL‑algorithm cells, CODS retains 96.6 % of full‑pool performance on a 10 % budget; it exceeds ReDOR and OPER on 19/20 cells and all six subset advantages remain significant (Holm correction). Five acquisition rounds improve four representative cells by 11.23 points, saturating thereafter. Whole‑trace extension retains 95.4 % of pooled ALFWorld success and 96.5 % exact match on GSM8K.

## Significance  
By enabling a reusable offline selection that reduces data cost while preserving performance, CODS addresses the scalability bottleneck in large‑scale RL research, allowing experiments across seeds and hyperparameters without sacrificing credit assignment fidelity.

## Related Concepts  
Offline reinforcement learning, prioritized replay, coresets, residual selection, Bellman residuals, hierarchical inference, Holm correction, reusable artifacts, whole‑trace evaluation.
