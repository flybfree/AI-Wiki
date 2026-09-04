# Summary: 2026-09-01_18-07-09Z_HarnessEngineeringinLLMToolUseviaAgent_NativeReusa.md
Saved: 2026-09-02 20:37
Source: 2026-09-01_18-07-09Z_HarnessEngineeringinLLMToolUseviaAgent_NativeReusa.md
Model: None

---

## Summary  
The paper proposes **Tool Primitives**, a design that replaces rigid API‑schema based tool calling with natural language interfaces, allowing LLMs to invoke tools seamlessly across multiple steps and turns. Building on this, it introduces **ToolFace**, a centralized repository of 25 519 functions that are resolved dynamically at inference time, eliminating the need to embed raw schemas in context. The authors then create **HEART** (Harness‑Engineering for Agent‑Native Reusable Tool Primitives), a three‑component framework—Planner, Router and Verifier—that orchestrates dynamic tool usage, feedback‑driven recovery and multi‑step reasoning. Experiments on five benchmarks show HEART outperforms prior SFT models by 10 % and beats several state‑of‑the‑art LLMs while cutting API costs up to 85 %.  

## Key Contributions
- Tool Primitives decouple tool invocation from raw API schemas using natural language.  
- ToolFace provides a dynamic, centrally hosted function catalog for zero‑shot retrieval.  
- HEART’s Planner‑Router‑Verifier architecture enables reliable multi‑step execution and recovery.  

## Methodology  
The authors first identified two bottlenecks in existing LLM‑tool pipelines: (1) brittle reasoning due to mismatched output types and API schemas, and (2) inefficiency caused by enumerating large tool catalogs. To solve these, they designed Tool Primitives where each tool is wrapped with an LLM‑mediated interface that resolves its schema and executes it internally, allowing natural inter‑tool communication. Next, they built ToolFace as a repository of 25 519 functions; at inference time the system queries only the relevant subset without exposing all schemas to the model. Finally, HEART integrates Planner (generates step‑wise tool calls), Router (selects appropriate tools from ToolFace based on context) and Verifier (monitors execution outcomes and triggers recovery if needed). This layered approach is evaluated end‑to‑end across diverse tasks.  

## Results  
On five benchmark suites, HEART achieves an average gain of 10 % over SFT‑based models and outperforms GPT‑5.4, Claude‑4.6‑Sonnet and Gemini‑3.1‑Pro by roughly 6 %. It also reduces API call costs up to 85 % compared with traditional implementations. In 50 real‑world tasks, HEART completes 84 % of them, which is three times the average success rate (22 %) of three leading commercial models.  

## Significance  
HEART demonstrates that engineering‑level abstractions—specifically reusable tool primitives and a harness framework—can dramatically improve LLM tool use efficiency and reliability, offering a path toward lower cost and higher accuracy in real‑world deployment. By abstracting away schema complexity, the method paves the way for more scalable and maintainable AI agents.  

## Related Concepts  
- Tool Primitives  
- Natural language interface  
- Dynamic tool retrieval  
- Planner‑Router‑Verifier architecture  
- API cost reduction
