# Summary: 2026-07-23_07-28-50Z_Workflow_LocalizedMechanismLearning_Attribution_Gu.md
Saved: 2026-07-24 02:43
Source: 2026-07-23_07-28-50Z_Workflow_LocalizedMechanismLearning_Attribution_Gu.md
Model: None

---

## Summary  
The paper proposes Workflow‑Localized Mechanism Learning (WML), a framework that jointly identifies where a failure occurs in a workflow, which specific mechanism caused it, and the minimal edit needed to fix it. By attaching provenance‑aware third‑party Skills to frozen language‑model agents, WML enables localized repair and reuse of knowledge without retraining the whole model. The authors introduce a six‑module Workflow‑Guided Skill Optimization (WGSO) loop that selects appropriate patches, evaluates them locally, and stores verified outcomes in an optimizer memory. On benchmark suites, this approach yields markedly higher hard accuracy than baseline agents.

## Key Contributions  
- **Finding 1:** WML introduces a Node–Mechanism Attribution mechanism that pinpoints the failed workflow node, the implicated mechanisms, and the smallest valid edit target, routing single‑mechanism defects to L3 resources and relational defects across mechanisms to L2 composition protocols.  
- **Finding 2:** The six‑module Workflow‑Guided Skill Optimization (WGSO) loop selects provenance‑ and scope‑aware third‑party knowledge, applies bounded patches, evaluates candidates locally, and stores verified outcomes in optimizer‑side memory for future reuse.  
- **Finding 3:** On SpreadsheetBench, WML achieves 90.33 ± 1.53 hard accuracy with DeepSeek and 74.67 ± 3.51 hard accuracy with Qwen3.6‑Flash; without optimization the learned Skills transfer to WikiTableQuestions at 84.00 ± 2.00 denotation accuracy, while on Compiler‑Supported50 it attains the highest hard‑PASS rate and lowest cost per successful task.

## Methodology  
The authors first model each workflow as a sequence of nodes linked by mechanisms that execute actions or retrieve knowledge. When an agent’s output deviates from the expected result, Node–Mechanism Attribution runs a diagnostic to locate the exact node where the failure originates, the mechanism(s) responsible, and the minimal edit (e.g., patching a single instruction). The WGSO loop then queries the Skill repository for provenance‑compatible knowledge that can be applied locally without violating scope constraints. Candidate patches are generated, evaluated by replaying the affected workflow segment, and only those that restore correctness are stored in an optimizer memory indexed by node and mechanism. This closed‑loop process repeats across tasks to continuously improve the agent’s skill set.

## Results  
Experimental evaluation on SpreadsheetBench shows a 90.33 ± 1.53 hard accuracy with DeepSeek and 74.67 ± 3.51 hard accuracy with Qwen3.6‑Flash, both significantly higher than baseline agents that lack optimization. Transfer to WikiTableQuestions yields denotation accuracies of 84.00 ± 2.00 (DeepSeek) and 83.00 ± 2.00 (Qwen3.6‑Flash), demonstrating robust skill reuse. On Compiler‑Supported50, WML reaches the highest hard‑PASS rate while minimizing cost per successful task; compiled execution reduces token usage and call count compared with a direct SkillAgent, preserving most of its successful tasks.

## Significance  
WML bridges the gap between external reusable Skills and frozen language models by providing a systematic, locally grounded repair mechanism. By isolating failures to specific workflow nodes and mechanisms, it avoids costly global retraining. The WGSO loop ensures that only relevant, provenance‑compatible knowledge is applied, preserving model integrity while maximizing efficiency. These advances lower computational cost, improve accuracy, and enable scalable skill reuse across diverse tasks.

## Related Concepts  
- Mechanism attribution  
- Workflow localization  
- Skill optimization (WGSO)  
- Provenance‑aware knowledge reuse  
- L2/L3 resource routing in composition protocols  
- Structured agent skills
