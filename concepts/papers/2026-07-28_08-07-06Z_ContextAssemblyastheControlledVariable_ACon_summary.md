# Summary: 2026-07-28_08-07-06Z_ContextAssemblyastheControlledVariable_AControl_Th.md
Saved: 2026-07-28 20:21
Source: 2026-07-28_08-07-06Z_ContextAssemblyastheControlledVariable_AControl_Th.md
Model: None

---

## Summary  
The paper proposes treating context assembly as the controlled variable in frozen LLM agents, using a control‑theoretic framework to study harness policies that select prompt templates, few‑shot demonstrations, retrieval depth, and planning passes. It formalizes an inner frozen policy πθ (task execution) and an outer online controller πφ (context assembly), arguing that stability is measured via non‑decreasing expected reward under bounded changes of the controller’s parameters. The work also provides an uncertainty‑calibration analysis linking the controller’s confidence estimates to realized task outcomes. Experiments across three domains and two model providers validate this decomposition.

## Key Contributions  
- [Finding 1] Formal decomposition of frozen LLM agent into inner policy πθ (task execution) and outer context policy πφ (context assembly), establishing a control‑theoretic view where context assembly is the controlled variable.  
- [Finding 2] Stability proof that the online controller πφ yields non‑decreasing expected reward when its parameters change within bounded sets, using Zhang et al.’s definition of stability.  
- [Finding 3] Uncertainty‑calibration analysis showing the controller’s confidence estimates align with realized task success rates, providing a metric for trustworthy harness policies.

## Methodology  
The authors adopt a control‑theoretic decomposition where the frozen LLM model πθ operates as an inner policy generating actions from prompts and retrieved context. The outer controller πφ selects prompt templates, few‑shot demonstrations, retrieval depth, and planning/verification passes via reinforcement learning (REINFORCE) or contextual bandit. Experiments instantiate this setup across three domains (code generation, medical diagnosis, legal summarization) using two different LLM providers (GPT‑4o, Claude 3). The outer policy is trained offline on trajectory logs to maximize task reward while minimizing uncertainty.

## Results  
Theoretically, the stability proof holds under bounded parameter changes, guaranteeing monotonic reward growth. Experimentally, πφ improves average task success by 12.7% over baseline policies and reduces confidence‑error variance from 0.45 to 0.18 across domains. The uncertainty calibration metric shows a Pearson correlation of r = 0.63 between controller confidence and actual success.

## Significance  
This work bridges LLM safety with control theory, offering a principled way to monitor harness policies without retraining the model. By treating context assembly as controllable, it enables systematic tuning of retrieval depth and demonstration selection, which are often opaque in current pipelines. The released dataset and deployment recipe support reproducibility, encouraging broader adoption of control‑theoretic approaches in AI safety research.

## Related Concepts  
- Frozen LLM agents: models whose weights are fixed during inference.  
- Control theory: principles of stability and optimal control.  
- Contextual bandit / REINFORCE policy: online learning methods for selecting context assembly strategies.  
- Uncertainty calibration: aligning model confidence with empirical outcomes.
