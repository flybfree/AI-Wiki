# Summary: 2026-07-29_10-14-02Z_UrbanDS_AGraph_GuidedLLMMulti_AgentSystemforData_I.md
Saved: 2026-07-29 20:32
Source: 2026-07-29_10-14-02Z_UrbanDS_AGraph_GuidedLLMMulti_AgentSystemforData_I.md
Model: None

---

## Summary  
The paper introduces UrbanDS, a graph‑guided large language model multi‑agent system designed to automate data‑intensive urban tasks that involve massive, heterogeneous datasets with complex spatial and temporal relationships. By constructing a unified dataset graph and orchestrating several specialized agents, UrbanDS enables automated discovery, processing, analysis, and reporting of urban data without relying on pre‑curated task sets. The approach bridges the gap between generic LLM agents and real‑world city operations by leveraging relational knowledge among datasets.

## Key Contributions  
- [Finding 1]  
- [Finding 2]  
- [Finding 3]  

## Methodology  
UrbanDS tackles data‑intensive urban tasks through a four‑stage pipeline. First, the Data Profiling Agent scans each dataset to generate a concise skill profile and creates a node in a unified dataset graph. Second, the Relation Agent examines these profiles for semantic or structural links, adding directed edges that encode how one dataset can be used with another. Third, at runtime the Planner Agent queries this relational graph to select task‑relevant datasets and constructs an execution plan that orders the specialized Execution Agents. Finally, a Report Agent aggregates logs from all agents into a coherent report, which can be iteratively refined by user feedback. This modular design lets each agent focus on its core operation while sharing intermediate results via a common memory.

## Results  
Experiments on both general data‑science benchmarks and the newly created UrbanDS‑Bench show that UrbanDS consistently outperforms existing LLM agents on tasks requiring large, multi‑source urban datasets. The system reduces manual preprocessing time by up to 45 % and achieves higher model accuracy on spatial analysis problems compared with baselines. Moreover, a pilot deployment in Dongxihu District’s operations platform demonstrated real‑time data ingestion and insight generation for city planners.

## Significance  
UrbanDS demonstrates that graph‑guided multi‑agent LLMs can handle the scale, diversity, and relational complexity of urban data, offering a scalable framework for automated urban analytics. Its integration into municipal platforms underscores the practical value of such systems in delivering actionable insights to public services.

## Related Concepts  
graph‑guided LLM multi‑agent system; dataset graph; Data Profiling Agent; Relation Agent; Planner Agent; Execution Agents; Report Agent; UrbanDS‑Bench.
