# Summary: 2026-08-05_03-32-08Z_NotEveryDivergenceShouldBeSuppressed_Counterfactua.md
Saved: 2026-08-05 22:23
Source: 2026-08-05_03-32-08Z_NotEveryDivergenceShouldBeSuppressed_Counterfactua.md
Model: None

---

## Summary  
The paper addresses a limitation of divergence‑based supervision in on‑policy distillation (OPD) by proposing the concept of counterfactual recoverability, which asks whether an erroneous prefix can be corrected after the fact. By replaying each error state through budget‑matched teacher‑continuation and rollback branches, the authors classify states as recoverable, irreversible‑but‑avoidable, or ambiguous, thereby providing a decision variable that guides how training should treat those trajectories. The method replaces blind suppression of divergences with a learnable proxy that predicts whether an error is correctable. This outcome‑grounded approach yields measurable gains in both diagnostic accuracy and downstream model performance.

## Key Contributions  
- Finding 1: Counterfactual recoverability distinguishes between errors that can be corrected (recoverable) and those that are merely avoidable but cannot be recovered, unlike simple divergence metrics.  
- Finding 2: A branch‑derived recoverability proxy achieves an AUC of 1.000 on the AIME diagnostic set, while divergence alone scores only 0.392, demonstrating superior discriminative power.  
- Finding 3: Component ablation experiments reveal that retaining teacher‑correctable prefixes contributes the largest single improvement to overall success rates.

## Methodology  
The authors formulate the problem as a decision task: given an error state, they run two budget‑matched simulations—one where the student continues with the teacher’s guidance (teacher‑continuation) and one where it rolls back to the last correct prefix (rollback). The relative performance of these branches informs whether the original trajectory is recoverable. States are then labeled as recoverable, irreversible‑but‑avoidable, or ambiguous, and a binary proxy derived from branch outcomes replaces the raw divergence signal. This proxy is trained jointly with OPD loss to maximize recovery while preserving supervision.

## Results  
The recoverability proxy attains an AUC of 1.000 on AIME diagnostics, far exceeding the 0.392 AUC achieved by divergence alone. In mean continuation‑minus‑rollback effect calculations, recoverable states produce a positive value of 0.185, whereas irreversible‑but‑avoidable states yield –1.000, confirming opposite intervention preferences. Frozen evaluations show that recoverability‑aware control improves AIME2025 success from 0.517 to 0.578 and lifts the average@32 on AIME2024‑2025 from 0.2656 to 0.3125, while GPQA‑Diamond average@32 rises from 0.2702 to 0.3070. Ablation studies confirm that preserving teacher‑correctable prefixes yields the greatest single benefit.

## Significance  
By grounding supervision decisions in whether errors can be recovered rather than merely how large they are, the paper introduces a more nuanced and outcome‑focused strategy for OPD. This shift reduces unnecessary suppression of potentially correctable mistakes and aligns training with actual learning opportunities, leading to higher model robustness and performance across benchmark suites.

## Related Concepts  
- On‑policy distillation (OPD)  
- Counterfactual reasoning in reinforcement learning  
- Branch diagnostics for trajectory analysis  
- Recoverability proxy as a learned decision variable
