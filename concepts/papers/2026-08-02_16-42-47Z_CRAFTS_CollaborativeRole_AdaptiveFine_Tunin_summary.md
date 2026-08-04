# Summary: 2026-08-02_16-42-47Z_CRAFTS_CollaborativeRole_AdaptiveFine_TuningofLLMA.md
Saved: 2026-08-03 23:32
Source: 2026-08-02_16-42-47Z_CRAFTS_CollaborativeRole_AdaptiveFine_TuningofLLMA.md
Model: None

---

## Summary  
The paper introduces CRAFTS, a framework that automates the construction of executable chemical‑process models from natural‑language requests and process‑flow diagram evidence. By mirroring the staged workflow of chemical engineers, CRAFTS decomposes model building into seven bounded roles and uses deterministic IDAES/Pyomo gates to enforce engineering correctness. The authors fine‑tune three schema‑critical roles (visual, topology, specification) while keeping the remaining roles untuned Qwen, producing typed intermediate representations that guide unit‑operation selection, stream definition, and solver repair. This approach yields a high‑fidelity BuildPlan and SolveReport that expose all simulation decisions in a single contract.

## Key Contributions  
- **Role specialization with fine‑tuning:** CRAFTS fine‑tunes only the visual, topology, and specification roles to produce accurate typed intermediate representations (VisualGraphIR, TopologyIR, SpecIR), while other roles rely on untuned Qwen, enabling targeted adaptation without overfitting.  
- **Deterministic engineering gates:** The framework employs deterministic IDAES/Pyomo checkpoints between stages, guaranteeing that each step respects chemical‑process constraints and that only semantically valid constructors are attached to the model.  
- **High validation and execution performance:** On a held‑out 82‑case split of OpenIDAES‑450, CRAFTS completes the prescribed validation and execution contract for 91.5 % of cases, achieving unit‑operation F1 = 0.815, stream‑definition F1 = 0.791, and directed‑connection F1 = 0.782.

## Methodology  
CRAFTS follows a LangChain/LangGraph workflow that orchestrates seven bounded roles: Input Understanding (recovering requirements from natural language), Visual Specialist (translating PFD evidence into visual contracts), Topology Specialist (generating topology‑aware scripts), Specification Specialist (encoding spec constraints), Debug/Optimization (bounded repair and optimization), Fine‑tuned Role 1, Fine‑tuned Role 2, Fine‑tuned Role 3, and Untuned Qwen for the remaining tasks. The system iteratively builds a BuildPlan that links unit operations, streams, thermodynamic properties, numerical settings, and solver parameters. All semantic artifacts must pass engineering gates before compatible constructors, property packages, and runners are attached.

## Results  
The complete seven‑role workflow is evaluated on the frozen 82‑case holdout of OpenIDAES‑450. CRAFTS fulfills the validation‑execution contract for 91.5 % of cases. The resulting model scores F1 = 0.815 for unit‑operation selection, F1 = 0.791 for stream definition, and F1 = 0.782 for directed‑connection fidelity. These results quantify the reliability of role specialization and typed IRs in automated process‑model construction.

## Significance  
CRAFTS dramatically reduces the manual effort required to translate engineering specifications into executable simulation models, thereby lowering error rates that can invalidate a model. By automating bounded roles with targeted fine‑tuning and deterministic gates, the framework provides a scalable, auditable pipeline for chemical engineers who must repeatedly construct complex process simulations.

## Related Concepts  
- LLM agents and role adaptation  
- Fine‑tuned vs. untuned language models  
- Intermediate representations (VisualGraphIR, TopologyIR, SpecIR)  
- LangChain/LangGraph orchestration  
- IDAES/Pyomo verification gates  
- Chemical process simulation datasets (OpenIDAES‑450)  
- F1 scoring for task performance
