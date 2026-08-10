# Summary: 2026-08-07_12-43-00Z_AgentMemoryDistillation_EmpoweringSmallLLMAgentswi.md
Saved: 2026-08-09 20:15
Source: 2026-08-07_12-43-00Z_AgentMemoryDistillation_EmpoweringSmallLLMAgentswi.md
Model: None

---

## Summary  
The paper proposes Agent Memory Distillation (AMD), a training‑free framework that transfers structured knowledge from a large teacher agent to a small student language model via hierarchical memory. It constructs three memory types—Workflow, Subtask, and Function—to improve task execution. AMD injects Workflow and Subtask memories at the start of tasks and retrieves Function memory reactively during errors. The approach enables 4B‑8B student models to achieve notable accuracy gains on tool‑use benchmarks.  

## Key Contributions  
- Finding 1: AMD achieves average accuracy improvements of 27.2%p, 11.2%p, and 3.4%p across AppWorld, BFCL V3, and ToolSandbox.  
- Finding 2: Subtask memory contributes the largest gains, indicating that concrete behavioral examples are most effective for small agents.  
- Finding 3: The effectiveness of AMD depends on both teacher capability (GPT‑5‑mini) and student compatibility, with 4B‑parameter students benefiting most.  

## Methodology  
The authors adopt a training‑free paradigm where the teacher agent’s successful trajectories are parsed into three hierarchical memory layers. Workflow memory encodes high‑level task strategies and is prepended to each task input; Subtask memory stores intermediate behavioral exemplars that guide step‑by‑step execution; Function memory captures function‑calling conventions and common pitfalls, retrieved only when tool errors occur. The student model is then prompted with the generated memories without any fine‑tuning.  

## Results  
Experiments on three benchmark suites using four 4B–8B parameter students against GPT‑5‑mini as teacher demonstrate consistent performance gains. The average accuracy improvements are 27.2%p on AppWorld, 11.2%p on BFCL V3, and 3.4%p on ToolSandbox, all outperforming existing memory‑based baselines. Subtask memory alone yields the highest lift, confirming its central role in the hierarchical design.  

## Significance  
AMD bridges a critical gap: large teacher models can provide rich, structured knowledge that small agents lack, enabling them to perform complex tool use without costly training. By separating memory types and timing their injection, AMD offers a scalable solution for deploying efficient, high‑performing language agents in resource‑constrained environments.  

## Related Concepts  
- Hierarchical memory architecture  
- Training‑free transfer learning  
- Workflow memory  
- Subtask memory  
- Function memory  
- Tool‑use benchmarks (AppWorld, BFCL V3, ToolSandbox)
