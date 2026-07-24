# Summary: 2026-07-23_02-39-11Z_CSPF_AConstrainedShared_PrivateFusionMethodforNon_.md
Saved: 2026-07-24 02:36
Source: 2026-07-23_02-39-11Z_CSPF_AConstrainedShared_PrivateFusionMethodforNon_.md
Model: None

---

## Summary  
The paper addresses the challenge of reliably evaluating non‑verifiable tasks where human preferences cannot be directly observed, and existing fusion methods often ignore the complementary nature of heterogeneous reward models. CSPF proposes a constrained shared‑private fusion framework that learns to integrate hidden‑state representations from multiple frozen experts under pairwise human‑preference supervision. By separating each expert’s signal into a shared component and an expert‑specific private component, CSPF encourages alignment while preserving distinct viewpoints. The method is evaluated on LM‑Arena target‑domain adaptation and PPE out‑of‑distribution preference tasks.

## Key Contributions  
- [Finding 1] CSPF treats heterogeneous frozen reward models as complementary evaluators rather than a single aggregate signal.  
- [Finding 2] It decomposes each expert’s representation into shared and private parts, enabling cross‑expert alignment while preserving complementary viewpoints.  
- [Finding 3] Empirically, CSPF outperforms baseline approaches including single‑expert reward models, scalar‑score multi‑expert fusion, and rubric‑judge methods on the primary evaluation metrics.

## Methodology  
The authors model each expert’s frozen reward function as a neural network that outputs hidden‑state vectors. Human preference judgments are used to supervise pairwise comparisons of these states, guiding the learning process to align the shared component across experts while allowing private components to capture task‑specific nuances. The fusion step combines the shared part via averaging or learned aggregation and merges it with each expert’s private part, producing a unified representation that respects the constraints imposed by human preferences.

## Results  
Across both LM‑Arena target‑domain adaptation and PPE out‑of‑distribution preference evaluation, CSPF achieves the highest scores among all tested methods. It surpasses single‑expert reward‑model baselines, scalar‑score multi‑expert fusion, and rubric‑judge approaches on the primary metrics such as preference consistency and task performance.

## Significance  
CSPF demonstrates that integrating hidden‑state representations from multiple frozen models can yield a more expressive and reliable evaluative signal for non‑verifiable tasks. This provides a practical route toward integrated evaluative signals, potentially improving robustness and fairness in preference‑based systems where direct human feedback is unavailable.

## Related Concepts  
Hidden‑state representations, shared‑private fusion, constrained fusion, non‑verifiable preferences, LM‑Arena target‑domain adaptation, PPE out‑of‑distribution preference evaluation, reward models, human preference supervision.
