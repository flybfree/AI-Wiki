# Summary: 2026-08-03_02-22-02Z_Post_TrainingonOfficeWorkImprovesSoftwareEngineeri.md
Saved: 2026-08-04 00:24
Source: 2026-08-03_02-22-02Z_Post_TrainingonOfficeWorkImprovesSoftwareEngineeri.md
Model: None

---

## Summary  
The paper investigates whether post‑training on office work tasks can enhance a language model's performance in software engineering, proposing that long‑horizon tasks require goal‑directed execution (GDE). By applying the GDE framework to Qwen3.5-122B-A10B after training it on 363 office workflow tasks, the authors aim to demonstrate cross‑domain transfer of four core behaviors: goal selection, state construction, fidelity maintenance, and verification. Their contribution is a behavioral interpretation showing that these behaviors improve across both office and software domains.  

## Key Contributions  
- The post‑training model achieves a 5.8‑point increase in SWE‑Bench Pro pass@1 despite having no software‑engineering tasks in its training set.  
- Trajectory analysis reveals gains in all four GDE behaviors (goal selection, state construction, fidelity maintenance, verification) both in office workflows and in code repositories.  
- Aggregate statistics show related changes in information gathering, implementation, and verification processes when the model operates on software‑engineering tasks.  

## Methodology  
The authors employed a post‑training fine‑tuning procedure where Qwen3.5-122B-A10B was further trained on a curated collection of Long‑Horizon Multi‑Tool Agent (LHMTA) tasks extracted from typical office workflows, none of which involve software engineering. They then compared the model’s behavior across these tasks using trajectory analysis to quantify changes in the four GDE components and evaluated its performance on SWE‑Bench Pro.  

## Results  
The main experimental result is a 5.8‑point improvement in pass@1 on SWE‑Bench Pro, indicating that the model can now solve software engineering problems more reliably after only office‑work post‑training. The trajectory analysis confirms that each of the four GDE behaviors improves: goal selection becomes more precise, state construction aligns better with higher‑level objectives, fidelity maintenance is stronger, and verification succeeds at a higher rate.  

## Significance  
These findings demonstrate that long‑horizon cross‑domain transfer can be achieved through post‑training on seemingly unrelated domains, challenging the assumption that domain‑specific fine‑tuning is necessary. By showing measurable gains in both office and software tasks, the study opens avenues for building versatile agents that maintain coherent goals across nested workstreams.  

## Related Concepts  
Goal‑Directed Execution (GDE), long‑horizon tasks, cross‑domain transfer, post‑training fine‑tuning, SWE‑Bench Pro, LHMTA, information gathering, implementation, verification.
