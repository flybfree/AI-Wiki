# Summary: 2026-08-08_05-05-38Z_ZhuLong_Execution_GroundedLLMAgentforEDAScriptingw.md
Saved: 2026-08-10 22:49
Source: 2026-08-08_05-05-38Z_ZhuLong_Execution_GroundedLLMAgentforEDAScriptingw.md
Model: None

---

## Summary  
ZhuLong is an execution‑grounded large language model (LLM) agent designed to write and execute EDA scripts that rely on tool‑specific, often undocumented APIs such as PyAether and SKILL. The system integrates API retrieval, documentation inspection, and sandbox execution through a unified MCP framework while employing an offline self‑exploration mechanism that infers hidden behavior via counterfactual experimentation. By grounding its reasoning in real‑time execution, ZhuLong dramatically improves the success rate of EDA tasks compared with a baseline LLM model. The contribution is both methodological (a hybrid retrieval‑execution pipeline) and empirical (quantified gains on benchmark data).  

## Key Contributions  
- **Execution‑grounded LLM agent** that autonomously writes, executes, and iterates PyAether/SKILL scripts using a unified MCP toolset.  
- **Offline API self‑exploration**: counterfactual experiments to deduce undocumented API behaviors without external calls, reducing per‑task tool usage by 22.1 %.  
- **Quantified performance impact**: sandbox execution is the primary driver of success (41.2 pp drop when removed), while self‑exploration adds a 3.2 pp accuracy boost and improves Pass@1 from 23.6 % to 78.5 % on EDA‑Eval‑PyAether.  

## Methodology  
The authors approached the problem by building a pipeline that first retrieves relevant API documentation, then inspects it for gaps, and finally executes code in isolated sandboxes. The offline self‑exploration component runs counterfactual simulations—e.g., invoking an API with unexpected parameters—to observe outcomes and infer missing functionality. All steps are orchestrated through MCP (Model‑Centric Programming) tools that abstract away the underlying tool calls, allowing the LLM to focus on high‑level reasoning while still grounding its actions in concrete execution results.  

## Results  
On the EDA‑Eval‑PyAether benchmark of 158 real‑world tasks, ZhuLong achieves a Pass@1 rate of 78.5 %, far surpassing a pure LLM baseline at 23.6 %. Ablation analysis shows that removing sandbox execution drops performance by 41.2 percentage points, underscoring its critical role. The self‑exploration mechanism contributes an additional 3.2 pp gain and cuts the average number of tool calls per task by 22.1 %. In interactive settings involving unsaved layouts and schematics, ZhuLong reaches 60.0 % Pass@1 for PyAether and 50.0 % for SKILL.  

## Significance  
ZhuLong addresses a long‑tail bottleneck in EDA workflows where undocumented APIs limit LLM utility. By grounding its agent in sandbox execution and supplementing it with offline self‑exploration, the system delivers measurable accuracy improvements while drastically reducing redundant API calls, making large‑scale automated testing more efficient and reliable.  

## Related Concepts  
- LLM coding agents  
- MCP (Model‑Centric Programming) tools  
- Offline API self‑exploration  
- Counterfactual experimentation  
- Pass@1 metric for task success  
- EDA‑Eval‑PyAether benchmark
