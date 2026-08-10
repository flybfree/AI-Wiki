# Summary: 2026-08-07_17-21-49Z_Post_GrokkingCollapseattheRepresentation_ReadoutIn.md
Saved: 2026-08-09 23:12
Source: 2026-08-07_17-21-49Z_Post_GrokkingCollapseattheRepresentation_ReadoutIn.md
Model: None

---

## Summary  
The paper investigates why Muon‑trained transformers experience a post‑grokking collapse that occurs specifically at the representation‑readout interface, leading to loss of generalization across nine configurations modulo 113. It identifies this failure as an artifact of gradient dynamics and optimizer behavior rather than architectural issues, and shows that freezing certain groups resolves it. The study demonstrates that the task selects a family of solutions (k,k) versus (k,‑k), and that Fourier analysis separates circuit failures from masking effects.

## Key Contributions  
- [Finding 1] Muon‑trained transformers suffer a post‑grokking collapse at the representation‑readout interface, causing loss of generalization across nine configurations modulo 113.  
- [Finding 2] The failure is tied to gradient magnitude dropping to ~10⁻⁶ and optimizer step‑size elasticity differences (Muon –0.03 vs AdamW +1.5), with Muon parameters moving eight times faster per parameter, indicating instability at the readout interface.  
- [Finding 3] Freezing embeddings/readout eliminates collapse in all runs; removing normalization and orthogonalization collapses representation from 326 to 4 effective pairs, showing that these operations are crucial.

## Methodology  
The authors systematically varied nine hyperparameters (a+b mod 113, widths, training fractions, subtraction vs addition, depth) across five seeds, monitoring performance. They performed post‑grokking analysis, freezing groups, and used Fourier filtering to distinguish circuit failures from masking. The task‑aligned family achieved perfect performance on the original set but degraded under adversarial conditions.

## Results  
Across 43 checkpoints over five seeds and three regimes, the task‑aligned family reached exactly 100 % accuracy alone, while the full model dropped to ~45.85 % in the circuit‑failure regime. Post‑grokking evaluations ranged from sub‑threshold (137–321) when arms unfrozen to zero when frozen. Rescaling restored 99.9 % performance; grokking resolves upward.

## Significance  
This work reveals that grokking collapse is not due to model capacity but to unstable gradient dynamics at the readout interface, offering insights into training instability and suggesting fixes like freezing or preserving normalization/orthogonalization.

## Related Concepts  
- Muon (modular addition)  
- Grokking  
- Representation‑readout interface  
- Gradient elasticity  
- Fourier filtering  
- Task‑aligned family  
- Post‑grokking collapse
