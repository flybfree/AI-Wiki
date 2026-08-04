# Summary: 2026-08-02_04-41-20Z_SCHEDBench_ABenchmarkforEvaluatingLLMConstraintFai.md
Saved: 2026-08-03 20:37
Source: 2026-08-02_04-41-20Z_SCHEDBench_ABenchmarkforEvaluatingLLMConstraintFai.md
Model: None

---

## Summary  
The paper introduces SCHEDBench, a benchmark designed to evaluate how large language models (LLMs) preserve constraint‑feasibility and optimality when natural‑language formulations of combinatorial scheduling problems are varied. It creates 1,132 instances from job‑shop, resource‑constrained project scheduling, nurse rostering, and curriculum timetabling domains, templating each instance into multiple surface forms while maintaining a verified reference solution. The study tests thirteen frontier LLMs to determine whether generated schedules remain feasible under semantically equivalent renderings, focusing on constraint reordering as the most sensitive axis. This work contributes both the benchmark itself and empirical evidence of non‑invariance in LLM behavior.

## Key Contributions  
- [Finding 1] SCHEDBench provides a comprehensive natural‑language benchmark for scheduling constraint faithfulness across surface‑form variations.  
- [Finding 2] Empirical results show that LLMs are not invariant to semantically equivalent NL renderings, with feasibility degradation and hard‑constraint violations increasing under certain reorderings.  
- [Finding 3] Constraint reordering is identified as the most pronounced source of sensitivity among tested axes.

## Methodology  
The authors constructed instances by applying domain‑specific templates to canonical scheduling problems, then varied surface forms via lexical synonyms, syntactic restructuring, and constraint ordering. Each instance was paired with a reference solution verified for feasibility and optimality. They fed model prompts containing these NL formulations and compared generated schedules to the reference using feasibility checks and objective scores.

## Results  
Across thirteen LLMs, average hard‑constraint violation rates rose by 12–18 % when constraints were reordered, while other variations caused smaller but consistent shifts. Feasibility dropped from near‑perfect in most cases to moderate violations under reordering. The study also measured per‑instance objective deviation, showing up to a 30 % increase.

## Significance  
This work demonstrates that natural‑language formulations can introduce hidden constraints that break LLM reasoning, highlighting the need for robust evaluation of scheduling LLMs and informing design of more reliable prompt engineering or post‑processing pipelines. It underscores that surface‑form variation is not merely cosmetic but can materially affect computational outcomes.

## Related Concepts  
Constraint faithfulness, surface‑form variation, combinatorial optimization, large language models, feasibility checking, objective optimality, natural‑language templating, job‑shop scheduling, resource‑constrained project scheduling, nurse rostering, curriculum timetabling.
