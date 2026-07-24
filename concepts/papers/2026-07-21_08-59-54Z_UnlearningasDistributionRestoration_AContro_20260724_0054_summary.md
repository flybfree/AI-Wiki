# Summary: 2026-07-21_08-59-54Z_UnlearningasDistributionRestoration_AControlledCou.md
Saved: 2026-07-24 00:54
Source: 2026-07-21_08-59-54Z_UnlearningasDistributionRestoration_AControlledCou.md
Model: None

---

## Summary  
The paper proposes unlearning as a problem of restoring the original training distribution, using a controlled counterfactual testbed where each model is paired with a matched retraining reference. By auditing oracle‑free screens and certificate‑style criteria across 45 seeds spanning five architecture families, it demonstrates that many methods retain held‑out knowledge despite passing standard forward tests, exposing the inadequacy of oracle‑free certification as a guarantee. The study also shows that a damage‑relative recalibration anchored to the reference can certify only a small subset of models, while a fixed‑magnitude logit‑suppression attack defeats the full forward battery in many cells.

## Key Contributions  
- [Finding 1] The matched retraining reference reveals that retained knowledge persists at a level ≈ 2.8 nats below the never‑learned baseline (cluster CI [-3.16, −2.48]), indicating that standard unlearning evaluation can be fooled by methods that keep hidden facts.  
- [Finding 2] Oracle‑free certificate criteria fail in most cells: the injected model fails a fixed retain threshold in 41/45 cells and its own round‑trip certification succeeds only once, showing that such certificates are not reliable indicators of true unlearning.  
- [Finding 3] A damage‑relative recalibration anchored to the reference certifies only 15/45 models; where it abstains, its picks lie within retraining noise (0.80 nats), and a logit‑suppression attack defeats forward‑only certification in 12/45 cells.

## Methodology  
The authors built a controlled testbed with a matched retraining reference for each model seed. They evaluated oracle‑free screens and certificate‑style criteria across 45 seeds belonging to five open architecture families, using only forward passes and no external oracle. The study also performed damage‑relative recalibration anchored to the reference’s operating point.

## Results  
Retained knowledge is measured as a loss of –2.82 nats below the never‑learned level (CI [-3.16, −2.48]). The reference fails the fixed retain threshold in 41/45 cells and its own round‑trip certification in 31/45; only one cell fully certifies. A damage‑relative recalibration certifies 15/45 models, while a logit‑suppression attack defeats forward‑only certification in 12/45 cells. The screen rejects the injected model in all 45 cells, accepts the reference in 44, and partially detects entity‑routing suppression (35/45), confirming its necessity but not sufficiency.

## Significance  
The work challenges the assumption that oracle‑free certification can guarantee true unlearning, highlighting the need for selective, empirical tests. It also introduces an identifiability theorem that limits which facts admit a valid forget threshold at all, with TOFU (theoretical output function) as the boundary case.

## Related Concepts  
Unlearning, distribution restoration, oracle‑free certification, selective screening, certificate‑style criteria, damage‑relative recalibration, logit suppression, identifiability theorem, TOFU.
