# Summary: 2026-08-06_07-52-45Z_RA_CAD_LearningPost_ExecutionCritiqueforState_Awar.md
Saved: 2026-08-06 20:34
Source: 2026-08-06_07-52-45Z_RA_CAD_LearningPost_ExecutionCritiqueforState_Awar.md
Model: None

---

## Summary  
The paper introduces RA‑CAD (ReAct Agent for CAD), a state‑aware agent that learns to generate post‑execution critiques during the text‑to‑CAD generation pipeline. By integrating a Generate–Execute–Critique–Rewrite loop, the agent treats critique as an explicit policy action rather than a side output, enabling it to interpret feedback and steer subsequent rewrites toward valid parametric CAD code. The contribution is twofold: (1) a novel learning framework that optimizes both generated code and critique sequences using trajectory‑level optimization, and (2) empirical evidence that this approach surpasses existing text‑to‑CAD methods in execution validity and geometric quality.  

## Key Contributions  
- **State‑aware post‑execution critique as learnable policy action** – RA‑CAD explicitly generates critiques conditioned on the design intent, current code, and execution feedback, turning critique into a learned decision rather than an auxiliary output.  
- **Trajectory‑level optimization with Group Relative Policy Optimization (GRPO)** – The framework jointly optimizes code trajectories and critique sequences, assigning terminal rewards based on F1 score for validity and Chamfer Distance for geometric quality.  
- **Empirical state‑of‑the‑art results** – RA‑CAD achieves the highest execution validity and geometric scores among all surveyed text‑to‑CAD baselines, including proprietary language models, on CADFusion and Text2CAD benchmarks.  

## Methodology  
RA‑CAD builds on two prior components: **CAD Code Bootstrapping (CCB)**, which first trains a model to produce basic parametric CAD code via supervised fine‑tuning; and **Feedback‑Driven Agent Optimization (FAO)**, which applies GRPO to the full interaction trajectory. During training, the agent repeatedly executes generated code in a simulated CAD environment, records the outcome, and then produces an explicit critique that either terminates the process or guides the next rewrite. The combined loss from CCB’s code quality and FAO’s trajectory reward drives the learning of both generation and critique policies.  

## Results  
Experimental evaluations on CADFusion and Text2CAD demonstrate that RA‑CAD reaches state‑of‑the‑art performance: execution validity (measured by F1 score) exceeds 0.94, while Chamfer Distance for geometric fidelity improves to 0.032, surpassing all competing methods including strong proprietary language models. The improvement is consistent across diverse design intents and code complexities, confirming the robustness of the state‑aware critique loop.  

## Significance  
By treating post‑execution critique as a learnable policy decision, RA‑CAD bridges the gap between feedback generation and its effective utilization in text‑to‑CAD pipelines. This reduces reliance on static, externally supplied critiques and enables continuous self‑improvement throughout code generation, which is crucial for scalable, expert‑level CAD automation.  

## Related Concepts  
- ReAct agent (reactive reinforcement learning)  
- Post‑execution critique as a policy action  
- State‑aware conditioning in generative models  
- Group Relative Policy Optimization (GRPO)  
- F1 score for execution validity  
- Chamfer Distance for geometric quality  
- CAD Code Bootstrapping (CCB)  
- Text‑to‑CAD generation pipeline
