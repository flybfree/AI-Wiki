# Summary: 2026-08-05_06-47-46Z_CARGO_VL_CounterfactualArbitrationwithRisk_Constra.md
Saved: 2026-08-05 23:12
Source: 2026-08-05_06-47-46Z_CARGO_VL_CounterfactualArbitrationwithRisk_Constra.md
Model: None

---

## Summary  
Vision‑language systems often encounter disagreements between the visual and textual evidence retrieved for a query, which can lead to unreliable answers or unnecessary abstention. This paper proposes **CARGO‑VL**, a group‑relative optimization framework that jointly handles four evidence states—aligned (A), image‑correct only (I), text‑correct only (T), and both‑wrong (N)—as a single bundle while enforcing answer invariance, source equivariance, and the ability to switch between answering and abstaining. The method couples condition‑wise correctness with transition rewards and uses a primal‑dual controller to balance unsafe answers against excessive deferral, thereby achieving counterfactual consistency in multimodal evidence arbitration.

## Key Contributions  
- [Finding 1] CARGO‑VL introduces a group‑relative optimization that treats the four evidence states (A/I/T/N) as one bundle rather than optimizing them independently.  
- [Finding 2] It couples condition‑wise correctness with transition rewards to enforce answer invariance, source equivariance, and seamless switching between answering and abstention.  
- [Finding 3] The XMC (eXtended Modal Conflict) resource systematically generates conflict instances across modalities for training.

## Methodology  
The authors formulate the arbitration problem as a risk‑constrained group optimization where each evidence state is represented by a conditional policy. A dual formulation with primal and dual variables enforces constraints that guarantee consistency under counterfactual evidence changes. Relational transition rewards guide the model from one evidence state to another while preserving answer content, source selection, or abstention as appropriate. An adaptive risk‑control module dynamically adjusts the trade‑off between unsafe answers and excessive deferral, ensuring safe and efficient decision making.

## Results  
Experiments on CMC‑Bench and Modality‑Bias demonstrate that CARGO‑VL improves conflict handling by an average of 12 % over pointwise baselines. The unsupported‑answer rate drops by roughly 8 %, and modality usage becomes more balanced, with a variance reduction of 0.4 compared to baseline models. Ablation studies confirm complementary gains: relational transition signals add about 3 % improvement, while adaptive risk control yields the largest benefit (≈5 %). Across multiple seeds, CARGO‑VL consistently outperforms prior approaches.

## Significance  
By treating evidence arbitration as a joint optimization problem with explicit risk constraints, CARGO‑VL provides a principled, scalable way to achieve reliable multimodal reasoning. This is crucial for real‑world deployment where visual and textual sources may be equally or unequally trustworthy, and where the model must decide when to answer versus when to abstain.

## Related Concepts  
vision‑language models, counterfactual consistency, group‑relative optimization, primal‑dual control, abstention, modality bias, conflict resolution.
