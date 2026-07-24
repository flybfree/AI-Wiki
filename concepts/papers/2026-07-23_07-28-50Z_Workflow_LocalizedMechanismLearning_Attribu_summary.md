# Summary: 2026-07-23_07-28-50Z_Workflow_LocalizedMechanismLearning_Attribution_Gu.md
Saved: 2026-07-24 02:33
Source: 2026-07-23_07-28-50Z_Workflow_LocalizedMechanismLearning_Attribution_Gu.md
Model: None

---

## Summary  
The paper proposes Workflow‑Localized Mechanism Learning (WML), a framework that enables frozen language‑model agents to repair and reuse third‑party Skills by precisely locating where failures occur within a workflow, which mechanisms are responsible, and how to apply relevant knowledge locally. It introduces two core components: Node–Mechanism Attribution, which pinpoints the failed node, implicated mechanisms, and the minimal edit target, and Workflow‑Guided Skill Optimization (WGSO), an iterative loop that selects provenance‑aware third‑party knowledge, applies bounded patches, evaluates candidates, and stores verified outcomes in optimizer‑side memory. The approach avoids global optimization of entire Skills, instead focusing on single‑mechanism defects or relational issues across mechanisms. By integrating attribution with a structured repair cycle, WML improves the transferability and performance of Skills to downstream tasks.

## Key Contributions  
- [Finding 1] Node–Mechanism Attribution isolates the exact workflow node, responsible mechanism(s), and smallest valid edit target within each failure instance.  
- [Finding 2] Workflow‑Guided Skill Optimization (WGSO) selects third‑party knowledge that is both provenance‑aware and scope‑restricted, then applies bounded patches to produce candidate repairs.  
- [Finding 3] The WML loop stores verified outcomes in optimizer‑side memory, enabling future reuse without recomputing the same fixes.

## Methodology  
WML treats a Skills package as a structured workflow composed of nodes and mechanisms that generate outputs. When an agent fails, the system first runs Node–Mechanism Attribution to generate a diagnostic report: (i) the failing node ID, (ii) which mechanism(s) produced the incorrect output, and (iii) the minimal edit target on the input or output that would restore correctness. Based on this attribution, WGSO distinguishes between single‑mechanism defects—handled by routing to L3 resources—and relational defects across mechanisms—addressed via L2 composition protocols. The optimization loop then queries a repository of third‑party Skills, filters candidates for relevance and scope, applies bounded edits, evaluates the patched workflow on validation data, and if successful, records the repair in optimizer‑side memory as a reusable artifact. This iterative process repeats until convergence or a predefined budget is reached.

## Results  
On SpreadsheetBench, WML achieves 90.33 ± 1.53 hard accuracy with DeepSeek and 74.67 ± 3.51 hard accuracy with Qwen3.6‑Flash, compared to baseline SkillAgent performance of ~80–82. Without additional optimization, the learned Skills transfer to WikiTableQuestions with denotation accuracies of 84.00 ± 2.00 (DeepSeek) and 83.00 ± 2.00 (Qwen3.6‑Flash). On Compiler‑Supported50 benchmark, WML attains the highest hard‑PASS rate and the lowest cost per successful task; compiled execution reduces token usage by ~40 % and call count by ~30 % relative to a direct SkillAgent while preserving most successful tasks.

## Significance  
WML demonstrates that structured skill reuse can be guided by precise failure analysis, leading to more efficient, low‑cost optimization of frozen language models. By separating attribution from repair and storing verified outcomes in memory, the framework reduces redundant computation and improves downstream task performance across multiple benchmarks. This work advances the field of modular AI skills by providing a principled mechanism for localized knowledge reuse.

## Related Concepts  
- Node–Mechanism Attribution  
- Workflow‑Guided Skill Optimization (WGSO)  
- L2/L3 composition protocols  
- Provenance‑aware knowledge selection  
- Bounded patch application  
- Optimizer‑side memory storage
