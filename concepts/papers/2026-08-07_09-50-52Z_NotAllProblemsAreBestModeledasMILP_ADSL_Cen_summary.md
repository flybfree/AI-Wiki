# Summary: 2026-08-07_09-50-52Z_NotAllProblemsAreBestModeledasMILP_ADSL_CentricFra.md
Saved: 2026-08-09 22:53
Source: 2026-08-07_09-50-52Z_NotAllProblemsAreBestModeledasMILP_ADSL_CentricFra.md
Model: None

---

## Summary  
The paper argues that many combinatorial optimization problems cannot be efficiently or accurately captured by mixed‑integer linear programming (MILP) due to modeling complexity. It proposes OptiDSL, a domain‑specific language framework that leverages large language models to translate natural‑language descriptions into standardized structures, decoupling formulation from execution. By integrating diverse solvers—from heuristics to learning‑based methods—the approach offers flexibility and higher accuracy than rigid MILP pipelines. Experimental evaluation on 44 COP types demonstrates substantial gains in formulation accuracy (51.66% improvement) and modeling time reduction (91.71%). The framework also outperforms MILP pipelines, achieving a 23.09% higher accuracy.

## Key Contributions  
- OptiDSL provides a DSL‑centric optimization modeling paradigm that maps natural language to domain‑accepted structures.  
- The framework decouples problem formulation from solver execution, enabling seamless integration with heterogeneous solvers.  
- Empirically, OptiDSL yields 51.66% higher formulation accuracy and 91.71% faster modeling compared to MILP pipelines.

## Methodology  
The authors built OptiDSL by first defining a set of domain‑specific syntax that captures problem semantics without linear constraints. They then trained an LLM to translate user‑provided natural language specifications into this DSL, producing standardized model files. The generated models are fed to a solver library that includes both traditional MILP solvers and alternative algorithms (e.g., heuristic, metaheuristic, neural). This pipeline allows automatic generation of appropriate formulation and execution.

## Results  
On the benchmark of 44 combinatorial optimization problem types, OptiDSL achieved an average formulation accuracy increase of 51.66% relative to MILP baselines and reduced modeling time by 91.71%. Additionally, it outperformed MILP pipelines on the same tasks, gaining a further 23.09% higher accuracy. The code is publicly available at https://anonymous.4open.science/r/OptiDSL.

## Significance  
This work shifts optimization modeling from a monolithic MILP‑centric view to a flexible DSL‑driven approach, reducing the barrier for domain experts and enabling rapid prototyping. By automating translation with LLMs and supporting multiple solvers, OptiDSL can handle problems where linear constraints are infeasible or inefficient, thus broadening the applicability of optimization tools.

## Related Concepts  
- Mixed-integer linear programming (MILP)  
- Domain‑specific language (DSL)  
- Large language model (LLM) translation  
- Solver library integration  
- Combinatorial optimization problem types
