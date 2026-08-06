# Summary: 2026-08-05_09-24-39Z_AgreementBeforeDiversity_Verification_FirstComplem.md
Saved: 2026-08-05 23:12
Source: 2026-08-05_09-24-39Z_AgreementBeforeDiversity_Verification_FirstComplem.md
Model: None

---

## Summary  
The paper proposes a principled framework for coordinating heterogeneous language‑model ensembles called Agreement‑Before‑Diversity (ABD), which separates the space of candidate responses from the authority to replace them. It introduces a frozen, label‑free decision rule that retains an anchor answer only when two trusted samples corroborate it under a fixed equivalence relation; otherwise the answer is replaced by a diverse synthesis. The method provides exact analytical identities linking the accuracy gap to coverage and anchor advantage, and to recovery versus destruction of answers. Experiments on LiveCodeBench‑v6 and GPQA‑Diamond demonstrate that ABD outperforms baseline ensembles while keeping inference costs low.

## Key Contributions  
- [Finding 1] The first identity shows that the accuracy gap relative to unconditional synthesis is jointly determined by agreement coverage and the anchor’s advantage on the protected subset.  
- [Finding 2] The second identity reveals that the gap relative to never synthesizing reflects a contrast between authorized recovery and authorized destruction of answers.  
- [Finding 3] Neither identity assumes independence or calibrated confidence, and the expected inference cost is approximately eight minus five times the coverage in number of calls.

## Methodology  
ABD decouples candidate headroom from replacement authority by treating the latter as an explicit, auditable object. The decision rule is frozen and label‑free: an anchor answer persists only if two trusted samples satisfy a fixed equivalence relation; otherwise a heterogeneous synthesis replaces it. This gating mechanism creates a “protected stratum” where answers are retained, while diversity supplies potential alternatives.

## Results  
On LiveCodeBench‑v6 ABD achieved 59.43 % accuracy versus Single9 (52.57 %) and HAC (52.00 %), with n = 175; on GPQA‑Diamond it reached 75.00 % versus controls at 72.78 %, with n = 180. The exact identities localize differences: LiveCodeBench shows 3 protected cases where coverage contributes only 1.71 points, GPQA‑Diamond has 13 vs 8 discordant cases among 132 items, and a frozen anchor perturbation yields 12 vs 0 discordant cases among 71.

## Significance  
ABD explains why verification‑first complementarity improves ensemble performance without sacrificing diversity, offering theoretical clarity on how coverage and anchor advantage jointly shape accuracy. The method reduces inference cost predictably (≈ 8 − 5·coverage calls) and provides a transparent audit trail for answer replacement.

## Related Concepts  
heterogeneous language‑model ensembles; agreement‑before‑diversity (ABD); verification‑first complementarity; fixed equivalence relation; protected stratum; frozen anchor; identity linking coverage to accuracy gap; recovery vs. destruction of answers.
