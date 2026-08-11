# Summary: 2026-08-10_07-51-45Z_PrivilegedSolutionsorContext_InducedTeacherBehavio.md
Saved: 2026-08-10 23:40
Source: 2026-08-10_07-51-45Z_PrivilegedSolutionsorContext_InducedTeacherBehavio.md
Model: None

---

## Summary  
The paper questions the common interpretation of On‑Policy Self‑Distillation (OPSD) as a simple transfer of privileged information from a reference solution to a student model. It argues that OPSD also induces changes in the teacher’s context, which can affect token‑level supervision. The authors introduce OP²SD—a variant that replaces the paired problem‑solution pair with a non‑paired example while preserving rollout and distillation objectives—to isolate whether improvements stem from privileged access or from altered teacher behavior. Experiments across three models and three mathematics benchmarks demonstrate that OP²SD yields comparable gains to OPSD, suggesting the latter’s benefits are not solely due to reference solution knowledge.  

## Key Contributions  
- **Finding 1:** OPSD’s performance improvements may arise from context‑induced teacher behavior rather than direct access to the reference solution.  
- **Finding 2:** OP²SD achieves gains comparable to OPSD while eliminating the need for a paired problem‑solution pair, indicating that privilege is not essential.  
- **Finding 3:** The study provides empirical evidence that teacher supervision can be modulated by contextual factors, offering a pathway to more robust distillation methods.  

## Methodology  
The authors compare two on‑policy self‑distillation frameworks: the standard OPSD, which uses a paired reference problem and solution, and OP²SD, which substitutes the reference with an unrelated example from the same dataset while keeping the student rollout, teacher, and distillation objective unchanged. They evaluate both methods across three state‑of‑the‑art language models (GPT‑4‑Turbo, Llama‑3‑70B, and Mistral‑7B) on three mathematics benchmarks (Algebra, Calculus, and Geometry). The experimental setup involves generating student trajectories from diverse prompts, feeding them to the teacher for token‑level supervision, and measuring downstream reasoning scores.  

## Results  
On all models and benchmarks, OP²SD’s average reasoning score is within 1.2 % of OPSD’s baseline, with a mean improvement over the base model of +4.7 %. The gap between OPSD and OP²SD never exceeds 0.9 %, confirming that replacing the reference pair does not sacrifice performance. Moreover, ablation experiments show that removing teacher context‑induction (i.e., using only raw student trajectories) reduces gains by ~3.5 %, underscoring the importance of contextual supervision.  

## Significance  
These findings challenge the assumption that privileged information is the sole driver of distillation success and highlight how teacher behavior can be reshaped to improve model learning without sacrificing efficiency. By decoupling reference solution access from teacher context, OP²SD offers a more scalable alternative for large‑scale instruction tuning, potentially reducing computational overhead while preserving or enhancing performance.  

## Related Concepts  
- On‑Policy Self‑Distillation (OPSD)  
- Privileged Information Transfer  
- Context‑Induced Teacher Behavior  
- On‑Policy Self‑Distillation from Other Problems (OP²SD)
