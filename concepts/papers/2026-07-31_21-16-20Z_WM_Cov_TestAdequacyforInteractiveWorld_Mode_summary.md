# Summary: 2026-07-31_21-16-20Z_WM_Cov_TestAdequacyforInteractiveWorld_Model_Style.md
Saved: 2026-08-03 23:49
Source: 2026-07-31_21-16-20Z_WM_Cov_TestAdequacyforInteractiveWorld_Model_Style.md
Model: None

---

## Summary  
The paper tackles the challenge of evaluating whether interactive world‑model‑style testing in autonomous driving simulations can generate sufficient, valid evidence to support safety‑critical stopping decisions. It introduces WM‑Cov, a provider‑agnostic evaluation layer that translates raw simulation outputs into requested, realized, and valid evidence while reporting multiple adequacy metrics such as coverage growth and failure‑mode diversity. Experiments on TeraSim/SUMO events, mixed trace pools, and the DriveArena TrafficManager–WorldDreamer matrix demonstrate that many “dangerous” rollouts are actually valid ADS failures or partial realizations. The results show convergence of valid interactive evidence under budget constraints rather than relying solely on raw failure counts.

## Key Contributions  
- [Finding 1] WM‑Cov provides a provider‑agnostic evaluation layer that converts raw simulation outputs into requested, realized, and valid evidence.  
- [Finding 2] The adequacy framework includes coverage growth, valid‑failure discovery, failure‑mode diversity, realism, artifact suppression, duplicate accounting, and valid‑evidence precision.  
- [Finding 3] Experiments on TeraSim/SUMO events, mixed trace pools, and the DriveArena matrix show that dangerous‑looking rollouts include valid ADS failures, duplicates, partial realizations, and artifacts; the matrix yields 304 fully realized evidence versus 56 partial attempts, with a disjoint route‑slice check producing 74/6.

## Methodology  
The authors formulate interactive world‑model‑style testing adequacy as a problem of generating enough valid closed‑loop evidence for a specified intent. WM‑Cov is implemented as an evaluation layer that receives provider outputs (e.g., TeraSim/SUMO events) and transforms them into the three dimensions: requested event, realized outcome, and validity flag. The study uses a DriveArena TrafficManager–WorldDreamer matrix to generate 360 ego‑route requests across two planners, six prompt conditions, and two horizons, then measures how many attempts become fully realized evidence versus remaining partial. A disjoint route‑slice subset is also evaluated to assess coverage growth.

## Results  
Out of the 304 executed attempts, 304 become fully realized evidence while 56 remain partial; a separate 80‑request slice yields 74 fully realized and 6 partial attempts. Coverage growth metrics increase as more valid evidence is collected, indicating convergence toward adequacy under budget limits. Valid‑failure discovery uncovers rare but safety‑relevant failures, failure‑mode diversity spans multiple event types, realism scores are high, artifact suppression reduces false positives, duplicate accounting is minimal, and the precision of valid‑evidence is strong.

## Significance  
This work provides a principled method for assessing testing adequacy beyond raw failure counts, enabling budgeted validation that aligns with safety‑critical stopping decisions. By converting provider outputs into valid evidence and reporting comprehensive metrics, WM‑Cov helps autonomous driving planners generate more reliable test scenarios and improves the trustworthiness of simulation‑based evaluation.

## Related Concepts  
World‑model‑style testing, interactive simulation infrastructure, counterfactual rollouts, autonomous driving evaluation, adequacy metrics (coverage growth, valid‑failure discovery), provider‑agnostic evaluation layers, DriveArena matrix, TeraSim/SUMO events, mixed trace pools, ADS failures.
