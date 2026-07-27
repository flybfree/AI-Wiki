# Summary: 2026-07-24_10-01-00Z_LearningontheJob_ContinualLearningfromDeploymentFe.md
Saved: 2026-07-26 21:45
Source: 2026-07-24_10-01-00Z_LearningontheJob_ContinualLearningfromDeploymentFe.md
Model: None

---

## Summary  
The paper proposes a framework that enables frozen‑weights AI agents to learn continuously from the feedback they generate during deployment, such as outcome verdicts and after‑the‑fact corrections. By distilling each episode into concise natural‑language rules stored in an external memory, the system can retrieve relevant guidance when the model is invoked again, thereby avoiding the need for full retraining. Experiments on a banking benchmark demonstrate that this approach dramatically improves single‑trial success rates compared with static retrieval baselines. The method also shows that accumulated memories can be shared between models, further boosting performance without any additional training.

## Key Contributions  
- [Finding 1] Learning from one‑bit outcome verdicts lifts single‑trial success to 1.6× the baseline on the τ‑bench banking domain versus a static‑RAG control.  
- [Finding 2] Learning from after‑the‑fact corrections raises performance to 2.6× and solves 22 of the 84 tasks that the baseline never resolves.  
- [Finding 3] The accumulated memory store transfers between models, allowing each model to outperform its own no‑memory baseline.

## Methodology  
The authors pair a frozen‑weights agent with an external memory that records natural‑language rule distillations derived from deployment feedback. Each episode’s verdict or correction is turned into a concise rule that is stored and later retrieved when the model processes new tasks. The system is evaluated on τ‑bench, where a static RAG retrieves the entire policy corpus as a baseline, while the continual‑learning setup uses the same data but learns from the feedback. Experiments are run on both open‑weights Mistral Large (self‑hostable) and the frontier model Claude Sonnet 5.

## Results  
Single‑trial success improves to 1.6× the static‑RAG baseline when only outcome verdicts are used, and to 2.6× when corrections are incorporated as well. The continual‑learning approach recovers solutions for 22 out of 84 previously unsolvable tasks, whereas the baseline solves none. Moreover, each model’s performance exceeds its own no‑memory baseline by an average of ~15 %, and models that read the memory built by another model achieve further gains.

## Significance  
This work demonstrates that continual learning can be performed entirely from deployment feedback without retraining frozen models, opening a practical path for organisations with data‑sovereignty constraints to self‑host open‑weights agents. By turning everyday operational outcomes into reusable rules, the approach reduces reliance on costly model updates and enables long‑term adaptation in real‑world settings.

## Related Concepts  
- Continual learning  
- Retrieval‑augmented generation (RAG)  
- Frozen‑weights models  
- Memory store / external knowledge base  
- Natural‑language rule distillation  
- Task transfer between models
