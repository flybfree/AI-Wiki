# Summary: 2026-08-11_13-27-56Z_ReOrder_OPD_Reliability_AwarePromptOrderingforOn_P.md
Saved: 2026-08-11 23:24
Source: 2026-08-11_13-27-56Z_ReOrder_OPD_Reliability_AwarePromptOrderingforOn_P.md
Model: None

---

## Summary  
The paper proposes ReOrder‑OPD, a reliability‑aware prompt ordering scheme for on‑policy distillation that improves training by sorting prompts based on teacher continuation reliability rather than using unreliable local signals. It defines prompt‑level reliability R as the teacher’s probability of completing a student prefix to a correct answer and uses a proxy (max ROUGE‑5 F1 between student rollout and verifier‑correct same‑prompt teacher trajectories) to rank prompts. The authors show that high‑R prompts yield larger gains, descending‑R ordering outperforms random/ascending orders, and the method complements within‑trajectory supervision across multiple benchmarks. The method leverages teacher feedback without additional inference beyond the existing OPD pipeline, making it computationally efficient.  

## Key Contributions  
- Finding 1: Prompt‑level teacher continuation reliability R is a strong predictor of OPD performance.  
- Finding 2: A simple proxy (max ROUGE‑5 F1) reliably separates coarse reliability levels without requiring many teacher continuations.  
- Finding 3: ReOrder‑OPD’s descending‑R prompt ordering consistently improves aggregate metrics across Qwen3 and Gemma4 mathematics and code tasks.  

## Methodology  
The authors compute R by generating a student prefix, then measuring the maximum ROUGE‑5 F1 between that rollout and a teacher trajectory that produces the correct answer for the same prompt. They bin prompts into ten equal‑frequency bins of this proxy score to obtain actual reliability levels. The proxy is computed per prompt and reused across multiple trajectories, enabling scalable ranking. ReOrder‑OPD sorts prompts in descending order of R, then draws independent on‑policy trajectories for vanilla OPD training.  

## Results  
Experiments on Qwen3 and Gemma4 mathematics and code settings show that ReOrder‑OPD improves every matched aggregate comparison compared with random or ascending ordering. Gains are observed across six FiRe‑OPD and ExOPD settings, indicating that prompt ordering complements within‑trajectory supervision. The improvement persists under varying batch sizes and learning rates.  

## Significance  
This work addresses a fundamental limitation of OPD: reliance on unreliable teacher signals leads to suboptimal training. By introducing a reliability metric R and using it to order prompts, ReOrder‑OPD enables more effective utilization of teacher feedback, leading to higher student performance without extra compute for teacher continuations. Thus, reliability‑aware ordering offers a principled way to harness teacher signals in OPD.  

## Related Concepts  
Prompt ordering, on‑policy distillation (OPD), teacher continuation reliability (R), ROUGE‑5 F1 as a proxy metric, within‑trajectory supervision.
