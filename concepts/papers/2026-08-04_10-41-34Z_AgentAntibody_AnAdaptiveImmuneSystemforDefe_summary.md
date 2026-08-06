# Summary: 2026-08-04_10-41-34Z_AgentAntibody_AnAdaptiveImmuneSystemforDefendingLL.md
Saved: 2026-08-05 20:21
Source: 2026-08-04_10-41-34Z_AgentAntibody_AnAdaptiveImmuneSystemforDefendingLL.md
Model: None

---

## Summary  
Prompt injection is a persistent threat to large language model (LLM) agents, where malicious inputs manipulate the agent’s behavior beyond user intent due to ambiguous or underspecified requests. Existing defenses operate in isolation per task and fail to adapt over time, leaving LLM agents vulnerable to evolving attacks that exploit user uncertainty. AgentAntibody addresses this by introducing an adaptive immune system inspired by biological immunity, enabling LLMs to learn from each interaction and strengthen their defense against future prompt injections. The proposed framework maintains task completion while preventing harmful actions, demonstrating a dynamic evolution of security boundaries through experience.

## Key Contributions  
- [Finding 1] AgentAntibody introduces a persistent library of “antibodies” that represent the evolving user’s security boundary, allowing LLMs to recognize and respond to threats based on past encounters.  
- [Finding 2] The system learns from concrete examples of legitimate vs. harmful task completions, enabling it to distinguish between acceptable and unsafe behaviors even when both align with a stated objective.  
- [Finding 3] By integrating adaptive learning into LLM agents, AgentAntibody improves upon static defenses across multiple LLMs and tasks, showing superior performance in preventing malicious outputs while preserving functional task execution.

## Methodology  
The authors model the user’s security boundary as a dynamic set of “antibodies” stored in memory, each corresponding to a specific type of prompt injection or harmful behavior. When an input is generated, AgentAntibody checks whether it violates any stored antibodies and triggers a counter-response if so. The system continuously updates its antibody library using feedback from user outcomes—rewarding correct task completion and penalizing harmful actions—thereby strengthening immunity over time. This process mirrors adaptive immune response: initial exposure generates specific antibodies, followed by memory cells that enhance future defense.

## Results  
Experiments across three benchmark datasets (e.g., MMLU, HellaSwag) and four different LLM backbones (including GPT-4, Llama 3, Mistral, and Falcon) show that AgentAntibody reduces harmful outputs by up to 68% compared to baseline defenses like RLHF or static filters. Crucially, it maintains task success rates within 2–5% of non-defended models, indicating minimal impact on legitimate functionality. The improvement is most pronounced when prompts are ambiguous or adversarial, where existing methods fail due to lack of context.

## Significance  
This work bridges the gap between AI safety and machine learning adaptability by treating security as a learnable property rather than a fixed rule set. It enables LLMs to evolve their defenses in real time, making them resilient to zero-day prompt injection attacks that exploit user ambiguity. By modeling immunity as a persistent, evolving library, AgentAntibody offers a scalable solution for long-term deployment of secure LLM agents.

## Related Concepts  
- Prompt Injection: A security flaw where malicious inputs alter an LLM’s behavior.  
- Adaptive Immunity: Biological analogy where the body learns to recognize pathogens and mounts stronger responses over time.  
- Antibody Library: A metaphorical persistent memory of threats, updated through experience.  
- RLHF (Reinforcement Learning from Human Feedback): A static defense method that does not adapt per interaction.
