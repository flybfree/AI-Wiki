# Summary: 2026-08-10_06-53-24Z_AgenticRouter_AnExecution_GroundedContinualLearnin.md
Saved: 2026-08-10 23:39
Source: 2026-08-10_06-53-24Z_AgenticRouter_AnExecution_GroundedContinualLearnin.md
Model: None

---

## Summary  
The paper aims to improve the reliability of command‑line based SONiC operations by incorporating execution‑grounded continual learning with memory. It proposes a dual‑path framework that jointly generates multiple actions, predicts their consequences, and selects the best one via utility‑risk reranking. The proposal side abstracts reusable operational lessons into retrieval guidance, while the selection side adapts the consequence predictor using session‑level LoRA updates. Together these components enhance feasible‑action coverage and top‑1 execution success without modifying the underlying LLM.  

## Key Contributions  
- Execution‑grounded dual‑path framework that generates multiple actions and predicts their consequences for CLI SONiC operations.  
- Proposal side abstracts reusable operational lessons into retrievable guidance to improve feasible‑action coverage.  
- Selection side adapts the consequence predictor through session‑level LoRA updates using real SSH feedback.  

## Methodology  
The authors address the problem by first generating several complete CLI actions from a proposal LLM, then predicting each action’s execution consequences with a separate predictor model. A utility‑risk based reranking selects the final action to maximize feasibility and minimize risk. The proposal side treats operational lessons as static retrieval items that can be accessed without altering the LLM itself; the selection side continuously updates the consequence predictor using LoRA fine‑tuning on real SSH feedback from each session, allowing the model to adapt to new contexts while preserving prior knowledge.  

## Results  
Experiments over multi‑turn SONiC operation sessions with different Qwen3 proposal models demonstrate that the framework improves feasible‑action coverage and top‑1 execution success compared to baseline interaction‑only methods. The two adaptation paths provide complementary gains, with the proposal side boosting coverage by an average of 12 % and the selection side raising execution success from 78 % to 89 %.  

## Significance  
This work enables continual learning for LLM agents without retraining or fine‑tuning the base model, reducing operational risk in command‑line workflows. By grounding adaptation in real execution feedback, it makes CLI agents more robust and reliable over time, which is crucial for automated system administration.  

## Related Concepts  
- Continual Learning  
- Execution‑Grounded RL  
- LoRA (Low‑Rank Adaptation) fine‑tuning  
- Retrieval‑Augmented Generation  
- SONiC (System Operations via Natural Language Interface for Computerized Tasks)  
- Dual‑path architecture  
- Utility‑Risk reranking
