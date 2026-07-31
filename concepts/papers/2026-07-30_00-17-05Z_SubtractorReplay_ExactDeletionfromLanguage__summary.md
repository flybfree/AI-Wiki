# Summary: 2026-07-30_00-17-05Z_SubtractorReplay_ExactDeletionfromLanguage_ModelMe.md
Saved: 2026-07-30 20:24
Source: 2026-07-30_00-17-05Z_SubtractorReplay_ExactDeletionfromLanguage_ModelMe.md
Model: None

---

## Summary  
The paper investigates whether exact deletion can be performed on a persistent language‑model memory by either subtracting an addressable record or replaying later overwritten information. It demonstrates that the feasibility of exact deletion depends entirely on how the model stores its history, showing that algebraic decrement works for clean records while entangled writes require full replay. Experiments compare these strategies across several pretrained models and report quantitative trade‑offs in performance and utility cost. The work establishes exact deletion as a property of memory representation rather than an algorithmic shortcut.

## Key Contributions  
- [Finding 1] Algebraic decrement yields exact next‑token predictions with median KL ≈ 5.4×10⁻¹⁵ over 31 support‑token deletions, achieving only +2 % perplexity relative to a matched fine‑tune.  
- [Finding 2] Replay is necessary for records that are overwritten later; without replay the model’s output deviates noticeably (certificate ordering persists but utility cost rises).  
- [Finding 3] Utility cost of exact deletion scales with model size and representation complexity, reaching 11.2 % at 4B parameters and 44.3 % at 12B.

## Methodology  
The authors replace the global‑attention layers of Gemma 3 with a support‑vector memory that stores each token as an addressable record. They perform low‑rank recovery to 1 billion parameters, then compare two deletion strategies: (i) decrementing stored vectors and (ii) replaying overwritten entries via checkpointed rewind‑and‑replay. A masked‑refit proxy is evaluated for indistinguishability from a never‑ingested floor under elicitation, sampling, and LiRA attacks. Experiments are repeated on larger models (4B, 12B) and on the 48B Kimi linear hybrid to assess additive writes versus delta‑rule behavior.

## Results  
At 1 billion parameters, both decrement and retained‑key refit agree on next‑token output with negligible error; perplexity is only slightly higher than fine‑tuning. With larger models, certificate ordering remains but utility cost climbs sharply (11.2 % at 4B, 44.3 %). In the Kimi hybrid, additive writes admit a fixed decrement, whereas delta‑rule contributions are suffix‑dependent, causing 12–49 % of a record’s influence to be lost. Checkpointed rewind‑and‑replay deletes real clinical records up to 18,842 tokens, reproducing never‑ingested logits and all recurrent states bit for bit within an MLX implementation.

## Significance  
Understanding exact deletion clarifies the limits of memory‑efficient editing in LLMs. It shows that subtraction works only when influence is addressable, while replay is essential for entangled histories. The findings guide safer model editing by quantifying utility loss and informing architectures that support reversible writes without catastrophic degradation.

## Related Concepts  
addressable influence; algebraic decrement; replay; recurrent state rebuilding; support‑vector memory; KL divergence; perplexity; certificate ordering; delta rule; suffix dependency; MLX implementation; clinical records.
