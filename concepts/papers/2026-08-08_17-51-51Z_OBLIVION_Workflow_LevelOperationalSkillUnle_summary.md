# Summary: 2026-08-08_17-51-51Z_OBLIVION_Workflow_LevelOperationalSkillUnlearningf.md
Saved: 2026-08-10 23:05
Source: 2026-08-08_17-51-51Z_OBLIVION_Workflow_LevelOperationalSkillUnlearningf.md
Model: None

---

## Summary  
The paper addresses the problem of operational skill unlearning for deployed language model agents, where revoked skills can be reconstructed from residual carriers such as archives or transcripts. It introduces OBLIVION as a benchmark and defense harness that treats each episode as a source‑to‑sink workflow and applies Cross‑Surface Coherent Erasure to eliminate these carriers. The contribution is both the framework for evaluating skill revocation beyond explicit registries and the empirical results showing dramatic reductions in attack success.

## Key Contributions  
- [Finding 1] OBLIVION demonstrates that operational skill unlearning can be evaluated as a workflow‑level problem rather than relying solely on parameter forgetting.  
- [Finding 2] The Cross‑Surface Coherent Erasure technique reduces residual carriers, lowering the formal attack success rate from 1.0 to 0.114 and impact‑weighted exposure to 0.115 while preserving utility.  
- [Finding 3] In a separate sandbox evaluation, OBLIVION cuts attack success from 1.0 to 0.2 and impact‑weighted exposure to 0.213 without affecting benign block rates or locked utility.

## Methodology  
The authors model each episode as a workflow where skills flow from source modules (e.g., file access) through intermediate carriers (archives, transcripts, schemas) to sink actions (tool usage). They apply Cross‑Surface Coherent Erasure, which systematically removes or neutralizes these residual carriers at the workflow level. The defense harness freezes remediation near dangerous sinks to prevent skill resurrection, while maintaining locked utility for authorized tasks.

## Results  
Experiments on 88 attack episodes show that without any defense (no‑defense arm) the formal attack success rate is 1.0 and impact‑weighted exposure is also 1.0. With OBLIVION applied, these metrics drop to 0.114 and 0.115 respectively, indicating a 90 % reduction in successful revocation attempts. In a separate sandbox scenario, the same techniques reduce attack success from 1.0 to 0.2 and impact‑weighted exposure to 0.213, with benign block rates remaining at zero.

## Significance  
This work highlights that skill revocation is not merely about deleting parameters but ensuring that operational pathways are blocked, which is crucial for secure AI agents interacting with external systems. By providing a benchmark (OBLIVION) and measurable defenses, the paper advances both security research and practical deployment practices in AI.

## Related Concepts  
- Operational Skill Unlearning  
- Cross‑Surface Coherent Erasure  
- Workflow Evaluation  
- Formal Attack Success Rate  
- Impact‑Weighted Exposure
