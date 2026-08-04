---
title: CRAFTS: Collaborative Role-Adaptive Fine-Tuning of LLM Agents for Chemical Process Simulation
published: 2026-08-02T16:42:47Z
authors: Ziyun Zhang, Yuxin Lin, Eldin Wee Chuan Lim, Xinghao Ding
url: http://arxiv.org/abs/2608.01369v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CRAFTS: Collaborative Role-Adaptive Fine-Tuning of LLM Agents for Chemical Process Simulation

## Abstract
Constructing an executable chemical-process model remains manually intensive. Chemical engineers translate underspecified requests into coupled decisions about unit operations, thermodynamics, streams, specifications, degrees of freedom (DoF), initialization, solver repair, and optimization; one error can invalidate the model. CRAFTS mirrors the staged workflow of chemical engineers by decomposing simulation building into bounded subtasks assigned to seven bounded roles, with deterministic IDAES/Pyomo gates between stages. Given a natural-language request, process flowsheet diagram (PFD) evidence, and curated chemical-engineering knowledge, Input Understanding and Intent recover requirements, constraints, and process semantics; visual, topology, and specification specialists translate them into typed simulator contracts; and Debug and Optimization support bounded repair and eligible optimization. Fine-tuning is applied to the three schema-critical visual, topology, and specification roles, while the remaining roles use untuned Qwen. The resulting VisualGraphIR, TopologyIR, SpecIR, BuildPlan, and SolveReport expose unit, port, thermodynamic, numerical, and execution decisions. Compatible constructors, property packages, and runners are attached only after semantic artifacts pass engineering gates. We introduce OpenIDAES-450, a 450-case IDAES process- simulation dataset, and evaluate the complete seven-role LangChain/LangGraph workflow through solve and eligible optimization on its frozen 82-case held-out split. CRAFTS completes the prescribed validation and execution contract for for 91.5% of cases and achieves unit, stream, and directed-connection F1 scores of 0.815, 0.791, and 0.782. These results demonstrate the effectiveness of role specialization, typed intermediate representations, and deterministic engineering gates for reliable automated process-model construction.

## Metadata
- **Published**: 2026-08-02T16:42:47Z
- **Authors**: Ziyun Zhang, Yuxin Lin, Eldin Wee Chuan Lim, Xinghao Ding
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01369v1)