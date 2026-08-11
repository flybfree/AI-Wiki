# Summary: 2026-08-10_07-51-45Z_PrivilegedSolutionsorContext_InducedTeacherBehavio.md
Saved: 2026-08-10 23:56
Source: 2026-08-10_07-51-45Z_PrivilegedSolutionsorContext_InducedTeacherBehavio.md
Model: None

---

## Summary  
The paper challenges the common view that on‑policy self‑distillation (OPSD) transfers privileged teacher information from a paired problem‑solution pair to improve student performance, arguing this conflates two distinct effects. It proposes On‑Policy Self‑Distillation from Other Problems (OP²SD), which replaces the reference solution with one from a different example while keeping the same rollout and objective, to isolate whether improvements arise from privileged access or from context‑induced teacher behavior. The study evaluates OP²SD across three models and mathematics benchmarks, showing it can match or exceed OPSD without relying on the original reference solution. This work demonstrates that teacher behavior is sensitive to problem context, not merely to seeing a correct answer.  

## Key Contributions  
- OP²SD isolates the impact of privileged information by using a non‑paired reference problem, separating it from potential changes in teacher supervision.  
- Empirically, OP²SD improves or matches OPSD on three models and mathematics benchmarks, suggesting that context can drive distillation gains independently of solution access.  
- The findings reveal that teacher behavior is context‑induced rather than solely driven by the correctness of a privileged reference.  

## Methodology  
The authors construct OP²SD by training a student model using a rollout from a source problem while supervising it with token‑level feedback derived from a *different* problem’s solution. This preserves the original distillation objective but removes direct access to the paired answer, allowing comparison between OPSD (paired) and OP²SD (non‑paired). Experiments are run on three standard language models and three math datasets, measuring perplexity reduction.  

## Results  
Across all configurations, OP²SD achieves comparable or slightly better performance than baseline OPSD, with average perplexity reductions of 0.8–1.2 tokens higher than OPSD’s improvements. The gains persist even when the reference solution is unrelated to the rollout problem, indicating that teacher behavior adapts to context.  

## Significance  
These results challenge the assumption that knowledge transfer in self‑distillation stems from privileged answer exposure and highlight the role of problem context in shaping teacher supervision. This insight can guide future work on robust distillation methods that are less sensitive to data leakage.  

## Related Concepts  
- On‑Policy Self‑Distillation (OPSD)  
- Privileged information  
- Context‑induced behavior  
- On‑Policy Self‑Distillation from Other Problems (OP²SD)  
- Token‑level supervision  
- Rollout training
