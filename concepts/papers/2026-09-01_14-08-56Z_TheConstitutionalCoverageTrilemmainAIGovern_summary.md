# Summary: 2026-09-01_14-08-56Z_TheConstitutionalCoverageTrilemmainAIGovernance.md
Saved: 2026-09-01 22:55
Source: 2026-09-01_14-08-56Z_TheConstitutionalCoverageTrilemmainAIGovernance.md
Model: None

---

## Summary  
The paper investigates whether the suite of “constitutional” values encoded by deployed frontier large‑language models (LLMs) can satisfy the diverse preferences of users. By auditing the implicit value rankings in 23 LLM archetypes and measuring how those rankings are traded off among 1,649 U.S. participants, the authors reveal a **demand‑supply trilemma**: user demand spans all five core values (safety, helpfulness, honesty, autonomy, equity), but the current model supply is narrow, drifting away from some values and leaving many users “constitutionally homeless.” Their contribution formalizes this as a **budgeted‑pluralism trilemma**, shows that the empirical data realize its binding regime, and demonstrates that a minimal two‑vertex menu of honesty and autonomy improves welfare far more than deploying all 23 archetypes.  

## Key Contributions  
- [Finding 1] Demand for AI safety is broad but undercovered; only one‑third of users are fully represented by any single model’s value hierarchy, indicating a large “constitutional homelessness” problem.  
- [Finding 2] The supply of frontier LLM archetypes is narrow and systematically drifts: autonomy declines in five out of six families while equity rises, safety improves in four, creating monotone version trends that worsen welfare for the least‑served users.  
- [Finding 3] A two‑vertex menu \(\{e_{\mathrm{HON}}, e_{\mathrm{AUT}}\}\) reduces mean regret by 47 % (95 % CI [43 %, 52 %]) compared with the full 23‑archetype frontier, and adding three vertices can cut mean/worst‑group regret up to 81 %/64 %.  

## Methodology  
The authors combine a **paraphrase‑controlled audit** of the as‑shipped default constitutions across 23 LLM archetypes with a **pairwise trade‑off study** in which 1,649 U.S. participants rank their preferred value configurations on the same instrument. The audit quantifies each model’s implicit ranking of safety, helpfulness, honesty, autonomy, and equity; the trade‑off experiment measures how users would exchange these values across models. This dual approach yields both a snapshot of supply (audit) and a measure of demand (participants), enabling statistical comparison and drift analysis.  

## Results  
Demand is broad: all five values appear in user rankings, yet no single archetype dominates; 37 % of users are constitutionally homeless. Supply occupies only ~2 % of the demand hull under conservative noise‑matched estimation (0.10 % at full precision). Across six model families, autonomy decreases while equity and safety increase, with monotone version trends (\(p = 0.013\)). The drift is directional—moving away from already uncovered values worsens the welfare floor for the least‑served users. A two‑vertex menu of honesty and autonomy outperforms the full set by 47 % in mean regret (CI [43 %, 52 %]), and adding three vertices can reduce mean/worst‑group regret up to 81 %/64 %. These empirical findings are formalized as a budgeted‑pluralism trilemma, confirmed to be binding, and robust to distance‑based welfare measures or degraded routing.  

## Significance  
Understanding the constitutional coverage gap is crucial for designing AI governance that respects human values. The trilemma highlights systemic under‑representation of autonomy and honesty, suggesting targeted interventions (e.g., minimal value menus) can dramatically improve user welfare without costly model proliferation. This work provides a methodological template for evaluating how emerging AI systems align with societal priorities and guides policymakers toward more inclusive, efficient governance architectures.  

## Related Concepts  
- Constitutional institutions in AI  
- Frontier LLM archetypes  
- Value hierarchy (safety, helpfulness, honesty, autonomy, equity)  
- Welfare floor and constitutional homelessness  
- Budgeted‑pluralism trilemma  
- Pareto trade‑off studies with human participants
